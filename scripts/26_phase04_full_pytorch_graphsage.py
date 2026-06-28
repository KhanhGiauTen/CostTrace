import json
import math
import random
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

LOCAL_DEPS = Path(".codex_deps/phase04_torch").resolve()
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import torch
import torch.nn.functional as F


SEEDS = [11, 23, 42, 77, 101]
N_FOLDS = 3
PATIENCE = 50
MAX_EPOCHS = 500
LR = 0.01
WEIGHT_DECAY = 5e-4
HIDDEN_DIM = 32
DROPOUT_1 = 0.35
DROPOUT_2 = 0.20

OUT_DIR = Path("results/model")
AUDIT_DIR = Path("results/audit")
MODEL_DIR = Path("models/graphsage")
NODES_PATH = Path("results/metrics/node_scores.csv")
EDGES_PATH = Path("data/processed/sashts/edgelist.csv")
SELECTED_HYPERPARAMETERS_PATH = AUDIT_DIR / "selected_hyperparameters.json"


def final_hyperparameters() -> dict:
    defaults = {
        "hidden_dim": HIDDEN_DIM,
        "dropout_1": DROPOUT_1,
        "dropout_2": DROPOUT_2,
        "lr": LR,
        "weight_decay": WEIGHT_DECAY,
    }
    if not SELECTED_HYPERPARAMETERS_PATH.exists():
        return defaults
    with open(SELECTED_HYPERPARAMETERS_PATH, encoding="utf-8") as f:
        payload = json.load(f)
    selected = payload.get("selected_config", {})
    return {
        "hidden_dim": int(selected.get("hidden_dim", defaults["hidden_dim"])),
        "dropout_1": float(selected.get("dropout_1", defaults["dropout_1"])),
        "dropout_2": float(selected.get("dropout_2", defaults["dropout_2"])),
        "lr": float(selected.get("lr", defaults["lr"])),
        "weight_decay": float(selected.get("weight_decay", defaults["weight_decay"])),
    }


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def sigmoid_np(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35, 35)))


def rank_average(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[order[j + 1]] == values[order[i]]:
            j += 1
        ranks[order[i : j + 1]] = (i + j + 2) / 2.0
        i = j + 1
    return ranks


def roc_auc(y_true: np.ndarray, score: np.ndarray) -> float:
    y = y_true.astype(int)
    pos = y == 1
    neg = y == 0
    n_pos = int(pos.sum())
    n_neg = int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rank_average(score)
    return float((ranks[pos].sum() - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg))


def average_precision(y_true: np.ndarray, score: np.ndarray) -> float:
    y = y_true.astype(int)
    n_pos = int(y.sum())
    if n_pos == 0:
        return float("nan")
    order = np.argsort(-score, kind="mergesort")
    y_sorted = y[order]
    tp = np.cumsum(y_sorted)
    precision = tp / (np.arange(len(y_sorted)) + 1)
    return float((precision * y_sorted).sum() / n_pos)


def best_f1_threshold(y_true: np.ndarray, probs: np.ndarray) -> float:
    best_thr = 0.5
    best_f1 = -1.0
    for thr in np.linspace(0.05, 0.95, 91):
        metrics = metric_dict(y_true, probs, thr)
        if metrics["f1"] > best_f1:
            best_f1 = metrics["f1"]
            best_thr = float(thr)
    return best_thr


def metric_dict(y_true: np.ndarray, probs: np.ndarray, threshold: float) -> dict[str, float]:
    y = y_true.astype(int)
    pred = (probs >= threshold).astype(int)
    tp = int(((pred == 1) & (y == 1)).sum())
    tn = int(((pred == 0) & (y == 0)).sum())
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    precision = tp / max(tp + fp, 1)
    recall = tp / max(tp + fn, 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-12)
    return {
        "auc": roc_auc(y, probs),
        "ap": average_precision(y, probs),
        "accuracy": float((tp + tn) / max(len(y), 1)),
        "f1": float(f1),
        "precision": float(precision),
        "recall": float(recall),
        "brier": float(np.mean((probs - y) ** 2)),
        "positives": int(y.sum()),
        "n": int(len(y)),
    }


def make_group_folds(nodes: pd.DataFrame, seed: int) -> list[tuple[np.ndarray, np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed)
    summary = (
        nodes.groupby("hhid")
        .agg(n=("node_id", "size"), positives=("sars_label", "sum"))
        .reset_index()
    )
    summary["rate"] = summary["positives"] / summary["n"]
    summary["rand"] = rng.random(len(summary))
    summary = summary.sort_values(["rate", "n", "rand"], ascending=[False, False, True], kind="mergesort")
    fold_groups = [[] for _ in range(N_FOLDS)]
    fold_counts = [0 for _ in range(N_FOLDS)]
    for row in summary.itertuples(index=False):
        fold = int(np.argmin(fold_counts))
        fold_groups[fold].append(row.hhid)
        fold_counts[fold] += int(row.n)

    households = nodes["hhid"].to_numpy()
    out = []
    for fold in range(N_FOLDS):
        test_groups = set(fold_groups[fold])
        val_groups = set(fold_groups[(fold + 1) % N_FOLDS])
        train = np.array([h not in test_groups and h not in val_groups for h in households])
        val = np.array([h in val_groups for h in households])
        test = np.array([h in test_groups for h in households])
        out.append((train, val, test))
    return out


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    nodes = pd.read_csv(NODES_PATH).sort_values("node_id").reset_index(drop=True)
    edges = pd.read_csv(EDGES_PATH)
    required = {"node_id", "hhid", "sars_label"}
    missing = required - set(nodes.columns)
    if missing:
        raise ValueError(f"Missing required node columns: {sorted(missing)}")
    return nodes, edges


def build_adjacency(nodes: pd.DataFrame, edges: pd.DataFrame) -> torch.Tensor:
    node_to_idx = {str(node): idx for idx, node in enumerate(nodes["node_id"].astype(str))}
    adj = np.zeros((len(nodes), len(nodes)), dtype=np.float32)
    for row in edges.itertuples(index=False):
        u, v = str(row.source), str(row.target)
        if u not in node_to_idx or v not in node_to_idx:
            continue
        i, j = node_to_idx[u], node_to_idx[v]
        weight = math.log1p(float(getattr(row, "weight", 1.0)))
        adj[i, j] += weight
        adj[j, i] += weight
    row_sum = adj.sum(axis=1, keepdims=True)
    adj = np.divide(adj, np.maximum(row_sum, 1e-12), out=np.zeros_like(adj), where=row_sum > 0)
    return torch.tensor(adj, dtype=torch.float32)


def feature_matrix(nodes: pd.DataFrame, train_mask: np.ndarray) -> tuple[torch.Tensor, list[str]]:
    df = nodes.copy()
    for col in ["sleep_room_enc", "cared_by_enc", "sex_enc", "site_enc", "age_enc"]:
        if col not in df.columns:
            df[col] = 0.0
    if "weighted_degree_sec" not in df.columns:
        df["weighted_degree_sec"] = 0.0
    df["log_weighted_degree_sec"] = np.log1p(pd.to_numeric(df["weighted_degree_sec"], errors="coerce").fillna(0.0))
    df["log_degree"] = np.log1p(pd.to_numeric(df["degree"], errors="coerce").fillna(0.0))
    feature_names = [
        "degree_centrality",
        "betweenness_centrality",
        "closeness_centrality",
        "log_degree",
        "log_weighted_degree_sec",
        "sleep_room_enc",
        "cared_by_enc",
        "age_enc",
        "sex_enc",
        "site_enc",
    ]
    x = df[feature_names].apply(pd.to_numeric, errors="coerce").fillna(0.0).to_numpy(np.float32)
    mins = x[train_mask].min(axis=0)
    maxs = x[train_mask].max(axis=0)
    x = (x - mins) / np.maximum(maxs - mins, 1e-12)
    return torch.tensor(x, dtype=torch.float32), feature_names


class FullGraphSAGE(torch.nn.Module):
    def __init__(
        self,
        in_dim: int,
        hidden_dim: int = HIDDEN_DIM,
        dropout_1: float = DROPOUT_1,
        dropout_2: float = DROPOUT_2,
    ):
        super().__init__()
        self.dropout_1 = dropout_1
        self.dropout_2 = dropout_2
        self.self_1 = torch.nn.Linear(in_dim, hidden_dim)
        self.neigh_1 = torch.nn.Linear(in_dim, hidden_dim, bias=False)
        self.self_2 = torch.nn.Linear(hidden_dim, hidden_dim)
        self.neigh_2 = torch.nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.out = torch.nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        h = F.relu(self.self_1(x) + self.neigh_1(adj @ x))
        h = F.dropout(h, p=self.dropout_1, training=self.training)
        h = F.relu(self.self_2(h) + self.neigh_2(adj @ h))
        h = F.dropout(h, p=self.dropout_2, training=self.training)
        return self.out(h).squeeze(-1)


@torch.no_grad()
def predict(model: torch.nn.Module, x: torch.Tensor, adj: torch.Tensor) -> np.ndarray:
    model.eval()
    return torch.sigmoid(model(x, adj)).cpu().numpy()


def run_one(
    seed: int,
    fold: int,
    nodes: pd.DataFrame,
    edges: pd.DataFrame,
    masks: tuple[np.ndarray, np.ndarray, np.ndarray],
    hidden_dim: int = HIDDEN_DIM,
    dropout_1: float = DROPOUT_1,
    dropout_2: float = DROPOUT_2,
    lr: float = LR,
    weight_decay: float = WEIGHT_DECAY,
    save_checkpoint: bool = True,
    checkpoint_prefix: str = "graphsage",
) -> dict:
    set_seed(seed + fold)
    train_mask_np, val_mask_np, test_mask_np = masks
    x, feature_names = feature_matrix(nodes, train_mask_np)
    y = torch.tensor(nodes["sars_label"].astype(float).to_numpy(), dtype=torch.float32)
    adj = build_adjacency(nodes, edges)
    train_mask = torch.tensor(train_mask_np, dtype=torch.bool)
    val_mask = torch.tensor(val_mask_np, dtype=torch.bool)
    test_mask = torch.tensor(test_mask_np, dtype=torch.bool)

    model = FullGraphSAGE(
        x.shape[1],
        hidden_dim=hidden_dim,
        dropout_1=dropout_1,
        dropout_2=dropout_2,
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    n_pos = float(y[train_mask].sum().item())
    n_neg = float(train_mask.sum().item() - n_pos)
    pos_weight = torch.tensor([n_neg / max(n_pos, 1.0)], dtype=torch.float32)

    best = {"val_ap": -np.inf, "epoch": 0, "state": deepcopy(model.state_dict())}
    wait = 0
    for epoch in range(1, MAX_EPOCHS + 1):
        model.train()
        optimizer.zero_grad()
        logits = model(x, adj)
        loss = F.binary_cross_entropy_with_logits(
            logits[train_mask], y[train_mask], pos_weight=pos_weight
        )
        loss.backward()
        optimizer.step()

        probs = predict(model, x, adj)
        val_ap = average_precision(y[val_mask].numpy().astype(int), probs[val_mask_np])
        if np.nan_to_num(val_ap, nan=-np.inf) > best["val_ap"] + 1e-8:
            best = {"val_ap": float(val_ap), "epoch": epoch, "state": deepcopy(model.state_dict())}
            wait = 0
        else:
            wait += 1
            if wait >= PATIENCE:
                break

    model.load_state_dict(best["state"])
    probs = predict(model, x, adj)
    threshold = best_f1_threshold(y[val_mask].numpy().astype(int), probs[val_mask_np])
    row = {
        "model": "full_pytorch_graphsage",
        "seed": seed,
        "fold": fold,
        "best_epoch": int(best["epoch"]),
        "best_val_ap": float(best["val_ap"]),
        "early_stopped": bool(best["epoch"] < MAX_EPOCHS),
        "threshold": threshold,
        "hidden_dim": int(hidden_dim),
        "dropout_1": float(dropout_1),
        "dropout_2": float(dropout_2),
        "lr": float(lr),
        "weight_decay": float(weight_decay),
        "feature_names": "|".join(feature_names),
    }
    for split, mask_np in [("train", train_mask_np), ("validation", val_mask_np), ("test", test_mask_np)]:
        metrics = metric_dict(y[torch.tensor(mask_np, dtype=torch.bool)].numpy().astype(int), probs[mask_np], threshold)
        row.update({f"{split}_{key}": value for key, value in metrics.items()})

    if save_checkpoint:
        MODEL_DIR.mkdir(parents=True, exist_ok=True)
        torch.save(model.state_dict(), MODEL_DIR / f"{checkpoint_prefix}_seed{seed}_fold{fold}.pt")
    return row


def summarize(full: pd.DataFrame) -> pd.DataFrame:
    metrics = ["test_auc", "test_ap", "test_f1", "test_precision", "test_recall", "test_brier"]
    row = {"model": "full_pytorch_graphsage", "runs": int(len(full))}
    for metric in metrics:
        row[f"{metric}_mean"] = float(full[metric].mean())
        row[f"{metric}_std"] = float(full[metric].std(ddof=1)) if len(full) > 1 else 0.0
        row[f"{metric}_mean_std"] = f"{row[f'{metric}_mean']:.4f} +/- {row[f'{metric}_std']:.4f}"
    return pd.DataFrame([row])


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    nodes, edges = load_data()
    hyperparams = final_hyperparameters()
    rows = []
    for seed in SEEDS:
        for fold, masks in enumerate(make_group_folds(nodes, seed)):
            rows.append(run_one(seed, fold, nodes, edges, masks, **hyperparams))
            print(f"done seed={seed} fold={fold}")
    full = pd.DataFrame(rows)
    summary = summarize(full)
    full.to_csv(OUT_DIR / "full_pytorch_graphsage_full_metrics.csv", index=False)
    summary.to_csv(OUT_DIR / "full_pytorch_graphsage_summary.csv", index=False)
    with open(AUDIT_DIR / "full_pytorch_graphsage_metadata.json", "w", encoding="utf-8") as f:
        json.dump(
            {
                "created_at_utc": datetime.now(timezone.utc).isoformat(),
                "seeds": SEEDS,
                "n_folds": N_FOLDS,
                "patience": PATIENCE,
                "max_epochs": MAX_EPOCHS,
                "early_stopping_metric": "validation average precision",
                "checkpoint": "best validation AP state_dict per seed/fold",
                "architecture": "two-layer weighted mean GraphSAGE, PyTorch",
                "hyperparameters": hyperparams,
                "hyperparameter_source": (
                    str(SELECTED_HYPERPARAMETERS_PATH)
                    if SELECTED_HYPERPARAMETERS_PATH.exists()
                    else "script_defaults"
                ),
            },
            f,
            indent=2,
        )
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
