import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd


SEEDS = [11, 23, 42, 77, 101]
N_FOLDS = 3
PATIENCE = 50
MAX_EPOCHS = 800
LR = 0.05
L2 = 1e-3

OUT_DIR = Path("results/metrics")
AUDIT_DIR = Path("results/audit")
SASHTS_SCORES = Path("results/metrics/node_scores.csv")
SASHTS_NODES = Path("data/processed/sashts/nodelist.csv")
SASHTS_EDGES = Path("data/processed/sashts/edgelist.csv")
SOCIOPATTERNS_PROFILES = {
    "sociopatterns_primary_school": Path(
        "data/processed/multi_dataset/sociopatterns_primary_school/dataset_profile.json"
    ),
    "sociopatterns_hospital": Path(
        "data/processed/multi_dataset/sociopatterns_hospital/dataset_profile.json"
    ),
}


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35, 35)))


def rank_average(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg = (i + j + 2) / 2.0
        ranks[order[i : j + 1]] = avg
        i = j + 1
    return ranks


def roc_auc(y_true: np.ndarray, score: np.ndarray) -> float:
    y = y_true.astype(int)
    pos = y == 1
    neg = y == 0
    n_pos = int(pos.sum())
    n_neg = int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        return np.nan
    ranks = rank_average(score)
    return float((ranks[pos].sum() - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg))


def average_precision(y_true: np.ndarray, score: np.ndarray) -> float:
    y = y_true.astype(int)
    n_pos = int(y.sum())
    if n_pos == 0:
        return np.nan
    order = np.argsort(-score, kind="mergesort")
    y_sorted = y[order]
    tp = np.cumsum(y_sorted)
    precision = tp / (np.arange(len(y_sorted)) + 1)
    return float((precision * y_sorted).sum() / n_pos)


def classification_metrics(
    y_true: np.ndarray, probs: np.ndarray, threshold: float
) -> dict[str, float]:
    y = y_true.astype(int)
    pred = (probs >= threshold).astype(int)
    tp = int(((pred == 1) & (y == 1)).sum())
    tn = int(((pred == 0) & (y == 0)).sum())
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    precision = tp / max(tp + fp, 1)
    recall = tp / max(tp + fn, 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-12)
    brier = float(np.mean((probs - y) ** 2))
    return {
        "auc": roc_auc(y, probs),
        "ap": average_precision(y, probs),
        "accuracy": float((tp + tn) / max(len(y), 1)),
        "f1": float(f1),
        "precision": float(precision),
        "recall": float(recall),
        "brier": brier,
        "positives": int(y.sum()),
        "n": int(len(y)),
    }


def best_threshold(y_true: np.ndarray, probs: np.ndarray) -> float:
    thresholds = np.linspace(0.05, 0.95, 91)
    scores = [classification_metrics(y_true, probs, thr)["f1"] for thr in thresholds]
    return float(thresholds[int(np.argmax(scores))])


def load_sashts() -> tuple[pd.DataFrame, pd.DataFrame]:
    if SASHTS_SCORES.exists():
        nodes = pd.read_csv(SASHTS_SCORES)
    elif SASHTS_NODES.exists():
        nodes = pd.read_csv(SASHTS_NODES)
        nodes["sars_label"] = (nodes["sars"] == "Positive").astype(int)
        nodes["weighted_degree_sec"] = nodes.get("weighted_degree", 0.0)
        nodes["degree_centrality"] = nodes["degree"] / nodes.groupby("hhid")["node_id"].transform(
            lambda s: max(len(s) - 1, 1)
        )
        nodes["betweenness_centrality"] = 0.0
        nodes["closeness_centrality"] = 0.0
    else:
        raise FileNotFoundError("Missing SASHTS node scores/nodelist")

    edges = pd.read_csv(SASHTS_EDGES)
    required = {"node_id", "hhid", "sars_label"}
    missing = sorted(required - set(nodes.columns))
    if missing:
        raise ValueError(f"Missing required SASHTS columns: {missing}")
    return nodes.sort_values("node_id").reset_index(drop=True), edges


def build_adjacency(nodes: pd.DataFrame, edges: pd.DataFrame) -> np.ndarray:
    node_to_idx = {node: idx for idx, node in enumerate(nodes["node_id"].astype(str))}
    n = len(nodes)
    adj = np.zeros((n, n), dtype=float)
    for row in edges.itertuples(index=False):
        u = str(row.source)
        v = str(row.target)
        if u not in node_to_idx or v not in node_to_idx:
            continue
        weight = math.log1p(float(getattr(row, "weight", 1.0)))
        i, j = node_to_idx[u], node_to_idx[v]
        adj[i, j] += weight
        adj[j, i] += weight
    row_sum = adj.sum(axis=1, keepdims=True)
    return np.divide(adj, np.maximum(row_sum, 1e-12), out=np.zeros_like(adj), where=row_sum > 0)


def encode_features(nodes: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, list[str]]]:
    df = nodes.copy()
    for col in ["sleep_room_enc", "cared_by_enc", "sex_enc", "site_enc", "age_enc"]:
        if col not in df.columns:
            df[col] = 0.0
    if "weighted_degree_sec" not in df.columns:
        df["weighted_degree_sec"] = df.get("weighted_degree", 0.0)
    df["log_weighted_degree_sec"] = np.log1p(df["weighted_degree_sec"].fillna(0.0))
    df["log_degree"] = np.log1p(df["degree"].fillna(0.0))

    feature_sets = {
        "full": [
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
        ],
        "remove_metadata": [
            "degree_centrality",
            "betweenness_centrality",
            "closeness_centrality",
            "log_degree",
            "log_weighted_degree_sec",
        ],
        "remove_centrality": [
            "log_degree",
            "log_weighted_degree_sec",
            "sleep_room_enc",
            "cared_by_enc",
            "age_enc",
            "sex_enc",
            "site_enc",
        ],
        "remove_edge_contact": [
            "degree_centrality",
            "betweenness_centrality",
            "closeness_centrality",
            "sleep_room_enc",
            "cared_by_enc",
            "age_enc",
            "sex_enc",
            "site_enc",
        ],
        "topology_only": [
            "degree_centrality",
            "betweenness_centrality",
            "closeness_centrality",
            "log_degree",
            "log_weighted_degree_sec",
        ],
    }
    for cols in feature_sets.values():
        for col in cols:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)
    return df, feature_sets


def make_group_folds(nodes: pd.DataFrame, seed: int, n_folds: int) -> list[tuple[np.ndarray, np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed)
    summary = (
        nodes.groupby("hhid")
        .agg(n=("node_id", "size"), positives=("sars_label", "sum"))
        .reset_index()
    )
    summary["rate"] = summary["positives"] / summary["n"]
    summary["rand"] = rng.random(len(summary))
    summary = summary.sort_values(["rate", "n", "rand"], ascending=[False, False, True], kind="mergesort")

    fold_groups = [[] for _ in range(n_folds)]
    fold_counts = [0 for _ in range(n_folds)]
    for row in summary.itertuples(index=False):
        fold = int(np.argmin(fold_counts))
        fold_groups[fold].append(row.hhid)
        fold_counts[fold] += int(row.n)

    out = []
    households = nodes["hhid"].to_numpy()
    for fold in range(n_folds):
        test_groups = set(fold_groups[fold])
        val_groups = set(fold_groups[(fold + 1) % n_folds])
        train_mask = np.array([h not in test_groups and h not in val_groups for h in households])
        val_mask = np.array([h in val_groups for h in households])
        test_mask = np.array([h in test_groups for h in households])
        out.append((train_mask, val_mask, test_mask))
    return out


def scale_by_train(x: np.ndarray, train_mask: np.ndarray) -> np.ndarray:
    out = x.astype(float).copy()
    mins = out[train_mask].min(axis=0)
    maxs = out[train_mask].max(axis=0)
    denom = np.maximum(maxs - mins, 1e-12)
    return (out - mins) / denom


def train_logistic(
    x: np.ndarray,
    y: np.ndarray,
    train_mask: np.ndarray,
    val_mask: np.ndarray,
    seed: int,
    lr: float = LR,
    l2: float = L2,
    max_epochs: int = MAX_EPOCHS,
    patience: int = PATIENCE,
) -> tuple[np.ndarray, dict]:
    rng = np.random.default_rng(seed)
    n_features = x.shape[1]
    weights = rng.normal(0.0, 0.02, size=n_features)
    bias = 0.0
    best = {"val_ap": -np.inf, "epoch": 0, "weights": weights.copy(), "bias": bias}
    wait = 0

    x_train = x[train_mask]
    y_train = y[train_mask]
    n_pos = max(float(y_train.sum()), 1.0)
    n_neg = max(float(len(y_train) - y_train.sum()), 1.0)
    sample_weight = np.where(y_train == 1, n_neg / n_pos, 1.0)

    for epoch in range(1, max_epochs + 1):
        probs = sigmoid(x_train @ weights + bias)
        error = (probs - y_train) * sample_weight
        grad_w = (x_train.T @ error) / len(y_train) + l2 * weights
        grad_b = float(error.mean())
        weights -= lr * grad_w
        bias -= lr * grad_b

        val_probs = sigmoid(x[val_mask] @ weights + bias)
        val_ap = average_precision(y[val_mask], val_probs)
        if np.nan_to_num(val_ap, nan=-np.inf) > best["val_ap"] + 1e-8:
            best = {
                "val_ap": float(val_ap),
                "epoch": epoch,
                "weights": weights.copy(),
                "bias": float(bias),
            }
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                break

    probs_all = sigmoid(x @ best["weights"] + best["bias"])
    metadata = {
        "best_epoch": int(best["epoch"]),
        "best_val_ap": float(best["val_ap"]),
        "patience": patience,
        "max_epochs": max_epochs,
        "early_stopped": bool(best["epoch"] < max_epochs),
    }
    return probs_all, metadata


def train_mlp(
    x: np.ndarray,
    y: np.ndarray,
    train_mask: np.ndarray,
    val_mask: np.ndarray,
    seed: int,
    hidden_dim: int = 8,
    lr: float = 0.03,
    l2: float = L2,
    max_epochs: int = MAX_EPOCHS,
    patience: int = PATIENCE,
) -> tuple[np.ndarray, dict]:
    rng = np.random.default_rng(seed)
    n_features = x.shape[1]
    w1 = rng.normal(0.0, 0.05, size=(n_features, hidden_dim))
    b1 = np.zeros(hidden_dim)
    w2 = rng.normal(0.0, 0.05, size=hidden_dim)
    b2 = 0.0
    best = {
        "val_ap": -np.inf,
        "epoch": 0,
        "w1": w1.copy(),
        "b1": b1.copy(),
        "w2": w2.copy(),
        "b2": b2,
    }
    wait = 0

    x_train = x[train_mask]
    y_train = y[train_mask]
    n_pos = max(float(y_train.sum()), 1.0)
    n_neg = max(float(len(y_train) - y_train.sum()), 1.0)
    sample_weight = np.where(y_train == 1, n_neg / n_pos, 1.0)

    for epoch in range(1, max_epochs + 1):
        z1 = x_train @ w1 + b1
        h = np.maximum(z1, 0.0)
        logits = h @ w2 + b2
        probs = sigmoid(logits)
        dz2 = (probs - y_train) * sample_weight / len(y_train)
        grad_w2 = h.T @ dz2 + l2 * w2
        grad_b2 = float(dz2.sum())
        dh = np.outer(dz2, w2)
        dz1 = dh * (z1 > 0)
        grad_w1 = x_train.T @ dz1 + l2 * w1
        grad_b1 = dz1.sum(axis=0)

        w2 -= lr * grad_w2
        b2 -= lr * grad_b2
        w1 -= lr * grad_w1
        b1 -= lr * grad_b1

        val_h = np.maximum(x[val_mask] @ w1 + b1, 0.0)
        val_probs = sigmoid(val_h @ w2 + b2)
        val_ap = average_precision(y[val_mask], val_probs)
        if np.nan_to_num(val_ap, nan=-np.inf) > best["val_ap"] + 1e-8:
            best = {
                "val_ap": float(val_ap),
                "epoch": epoch,
                "w1": w1.copy(),
                "b1": b1.copy(),
                "w2": w2.copy(),
                "b2": float(b2),
            }
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                break

    h_all = np.maximum(x @ best["w1"] + best["b1"], 0.0)
    probs_all = sigmoid(h_all @ best["w2"] + best["b2"])
    metadata = {
        "best_epoch": int(best["epoch"]),
        "best_val_ap": float(best["val_ap"]),
        "patience": patience,
        "max_epochs": max_epochs,
        "early_stopped": bool(best["epoch"] < max_epochs),
        "hidden_dim": hidden_dim,
    }
    return probs_all, metadata


def gaussian_nb(
    x: np.ndarray, y: np.ndarray, train_mask: np.ndarray
) -> np.ndarray:
    x_train = x[train_mask]
    y_train = y[train_mask].astype(int)
    classes = [0, 1]
    means = {}
    vars_ = {}
    priors = {}
    for cls in classes:
        cls_x = x_train[y_train == cls]
        if len(cls_x) == 0:
            cls_x = x_train
        means[cls] = cls_x.mean(axis=0)
        vars_[cls] = cls_x.var(axis=0) + 1e-6
        priors[cls] = len(cls_x) / max(len(x_train), 1)

    log_probs = []
    for cls in classes:
        ll = -0.5 * np.sum(np.log(2 * np.pi * vars_[cls]) + ((x - means[cls]) ** 2) / vars_[cls], axis=1)
        log_probs.append(np.log(max(priors[cls], 1e-12)) + ll)
    logits = log_probs[1] - log_probs[0]
    return sigmoid(logits)


def evaluate_run(
    y: np.ndarray,
    probs: np.ndarray,
    train_mask: np.ndarray,
    val_mask: np.ndarray,
    test_mask: np.ndarray,
) -> dict[str, dict[str, float]]:
    threshold = best_threshold(y[val_mask], probs[val_mask])
    return {
        "threshold": {"value": threshold},
        "train": classification_metrics(y[train_mask], probs[train_mask], threshold),
        "validation": classification_metrics(y[val_mask], probs[val_mask], threshold),
        "test": classification_metrics(y[test_mask], probs[test_mask], threshold),
    }


def flatten_metrics(
    model: str,
    model_family: str,
    feature_set: str,
    seed: int,
    fold: int,
    metrics: dict,
    train_meta: dict | None = None,
) -> dict:
    row = {
        "model": model,
        "model_family": model_family,
        "feature_set": feature_set,
        "seed": seed,
        "fold": fold,
        "threshold": metrics["threshold"]["value"],
    }
    if train_meta:
        row.update(train_meta)
    for split in ["train", "validation", "test"]:
        for key, value in metrics[split].items():
            row[f"{split}_{key}"] = value
    return row


def summarize(full: pd.DataFrame, model_col: str = "model") -> pd.DataFrame:
    metrics = ["test_auc", "test_ap", "test_f1", "test_precision", "test_recall", "test_brier"]
    rows = []
    for keys, group in full.groupby([model_col, "feature_set"], dropna=False):
        model, feature_set = keys
        row = {
            model_col: model,
            "feature_set": feature_set,
            "runs": int(len(group)),
        }
        for metric in metrics:
            row[f"{metric}_mean"] = float(group[metric].mean())
            row[f"{metric}_std"] = float(group[metric].std(ddof=1)) if len(group) > 1 else 0.0
            row[f"{metric}_mean_std"] = (
                f"{row[f'{metric}_mean']:.4f} +/- {row[f'{metric}_std']:.4f}"
            )
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["test_ap_mean", "test_auc_mean"], ascending=False)


def dataset_summary() -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    rows.append(
        {
            "dataset": "sashts",
            "main_graph_id": "sashts_household_contact_graph",
            "nodes": int(pd.read_csv(SASHTS_NODES).shape[0]),
            "edges": int(pd.read_csv(SASHTS_EDGES).shape[0]),
            "components": int(pd.read_csv(SASHTS_NODES)["hhid"].nunique()),
            "evaluation_task": "infection-risk classification",
            "label_definition": "sars == Positive",
            "main_evaluation_status": "supervised_metrics_available",
        }
    )
    for dataset, path in SOCIOPATTERNS_PROFILES.items():
        if not path.exists():
            rows.append(
                {
                    "dataset": dataset,
                    "main_graph_id": "sociopatterns_weighted_contact_graph",
                    "nodes": np.nan,
                    "edges": np.nan,
                    "components": np.nan,
                    "evaluation_task": "source tracing",
                    "label_definition": "SI-simulated source labels; processed dataset profile missing",
                    "main_evaluation_status": "blocked_missing_processed_profile",
                }
            )
            continue
        profile = json.load(open(path, encoding="utf-8"))
        rows.append(
            {
                "dataset": dataset,
                "main_graph_id": "sociopatterns_weighted_contact_graph",
                "nodes": profile.get("nodes"),
                "edges": profile.get("edges"),
                "components": profile.get("components"),
                "evaluation_task": "source tracing",
                "label_definition": "true source generated by SI simulation on the observed weighted contact graph",
                "main_evaluation_status": "trace_metrics_available",
            }
        )
    summary = pd.DataFrame(rows)
    experiment = summary[
        [
            "dataset",
            "main_graph_id",
            "evaluation_task",
            "label_definition",
            "main_evaluation_status",
        ]
    ].copy()
    experiment["phase04_metric_source"] = np.where(
        experiment["evaluation_task"] == "infection-risk classification",
        "results/metrics/benchmark_table.csv",
        "results/metrics/trace_summary_table.csv",
    )
    return summary, experiment


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    nodes_raw, edges = load_sashts()
    nodes, feature_sets = encode_features(nodes_raw)
    y = nodes["sars_label"].astype(int).to_numpy()
    adj = build_adjacency(nodes, edges)

    benchmark_rows = []
    ablation_rows = []
    score_baselines = {
        "random": None,
        "degree_centrality": "degree_centrality",
        "weighted_degree": "weighted_degree_sec",
        "betweenness_centrality": "betweenness_centrality",
        "closeness_centrality": "closeness_centrality",
        "composite_risk_score": "composite_risk_score",
    }

    for seed in SEEDS:
        folds = make_group_folds(nodes, seed, N_FOLDS)
        for fold_idx, (train_mask, val_mask, test_mask) in enumerate(folds):
            x_full = nodes[feature_sets["full"]].to_numpy(float)
            x_full = scale_by_train(x_full, train_mask)

            for model_name, score_col in score_baselines.items():
                if model_name == "random":
                    rng = np.random.default_rng(seed * 100 + fold_idx)
                    probs = rng.random(len(nodes))
                else:
                    raw = pd.to_numeric(nodes[score_col], errors="coerce").fillna(0.0).to_numpy(float)
                    probs = (raw - raw.min()) / max(raw.max() - raw.min(), 1e-12)
                metrics = evaluate_run(y, probs, train_mask, val_mask, test_mask)
                benchmark_rows.append(
                    flatten_metrics(
                        model_name,
                        "network_heuristic",
                        "native_score",
                        seed,
                        fold_idx,
                        metrics,
                    )
                )

            nb_probs = gaussian_nb(x_full, y, train_mask)
            benchmark_rows.append(
                flatten_metrics(
                    "gaussian_naive_bayes",
                    "traditional_ml",
                    "full",
                    seed,
                    fold_idx,
                    evaluate_run(y, nb_probs, train_mask, val_mask, test_mask),
                )
            )

            log_probs, log_meta = train_logistic(
                x_full, y, train_mask, val_mask, seed + fold_idx
            )
            benchmark_rows.append(
                flatten_metrics(
                    "no_graph_logistic",
                    "traditional_ml",
                    "full",
                    seed,
                    fold_idx,
                    evaluate_run(y, log_probs, train_mask, val_mask, test_mask),
                    log_meta,
                )
            )

            mlp_probs, mlp_meta = train_mlp(
                x_full, y, train_mask, val_mask, seed + 500 + fold_idx
            )
            benchmark_rows.append(
                flatten_metrics(
                    "no_graph_mlp",
                    "traditional_ml",
                    "full",
                    seed,
                    fold_idx,
                    evaluate_run(y, mlp_probs, train_mask, val_mask, test_mask),
                    mlp_meta,
                )
            )

            graph_x = np.concatenate([x_full, adj @ x_full], axis=1)
            graph_probs, graph_meta = train_logistic(
                graph_x, y, train_mask, val_mask, seed + 1000 + fold_idx
            )
            benchmark_rows.append(
                flatten_metrics(
                    "graphsage_mean_neighbor",
                    "graph_model",
                    "full",
                    seed,
                    fold_idx,
                    evaluate_run(y, graph_probs, train_mask, val_mask, test_mask),
                    graph_meta,
                )
            )

            for ablation_name, cols in {
                "graph_full": feature_sets["full"],
                "no_graph_mlp_full": feature_sets["full"],
                "graph_remove_metadata": feature_sets["remove_metadata"],
                "graph_remove_centrality": feature_sets["remove_centrality"],
                "graph_remove_edge_contact": feature_sets["remove_edge_contact"],
            }.items():
                ablation_feature_name = {
                    "graph_full": "full",
                    "no_graph_mlp_full": "full_no_graph",
                    "graph_remove_metadata": "remove_metadata",
                    "graph_remove_centrality": "remove_centrality",
                    "graph_remove_edge_contact": "remove_edge_contact",
                }[ablation_name]
                x = scale_by_train(nodes[cols].to_numpy(float), train_mask)
                if ablation_name == "no_graph_mlp_full":
                    design = x
                    probs, meta = train_mlp(
                        design, y, train_mask, val_mask, seed + 2000 + fold_idx
                    )
                else:
                    design = np.concatenate([x, adj @ x], axis=1)
                    probs, meta = train_logistic(
                        design, y, train_mask, val_mask, seed + 2000 + fold_idx
                    )
                ablation_rows.append(
                    flatten_metrics(
                        ablation_name,
                        "ablation",
                        ablation_feature_name,
                        seed,
                        fold_idx,
                        evaluate_run(y, probs, train_mask, val_mask, test_mask),
                        meta,
                    )
                )

    benchmark_full = pd.DataFrame(benchmark_rows)
    ablation_full = pd.DataFrame(ablation_rows)
    benchmark_table = summarize(benchmark_full)
    ablation_table = summarize(ablation_full)
    multi_summary, multi_experiment = dataset_summary()

    benchmark_full.to_csv(OUT_DIR / "benchmark_full_metrics.csv", index=False)
    benchmark_table.to_csv(OUT_DIR / "benchmark_table.csv", index=False)
    ablation_full.to_csv(OUT_DIR / "ablation_full_metrics.csv", index=False)
    ablation_table.to_csv(OUT_DIR / "ablation_table.csv", index=False)
    multi_summary.to_csv(OUT_DIR / "multi_dataset_summary.csv", index=False)
    multi_experiment.to_csv(OUT_DIR / "multi_dataset_experiment_table.csv", index=False)

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "seeds": SEEDS,
        "n_folds": N_FOLDS,
        "split_protocol": "household-grouped 3-fold; validation fold is next household fold; no household overlap",
        "early_stopping": {
            "metric": "validation average precision",
            "patience": PATIENCE,
            "max_epochs": MAX_EPOCHS,
            "checkpoint": "best validation AP weights retained per run",
        },
        "feature_sets": feature_sets,
        "notes": [
            "Main external trace evaluation uses SocioPatterns primary school and hospital contact graphs.",
            "GraphSAGE-style model is numpy mean-neighbor aggregation plus trainable logistic layer.",
            "SASHTS-only supervised labels use sars_label from existing node_scores.csv.",
        ],
    }
    with open(AUDIT_DIR / "phase04_run_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("=== PHASE 04 MODELING OUTPUTS ===")
    print(f"Benchmark runs: {len(benchmark_full)}")
    print(f"Ablation runs : {len(ablation_full)}")
    print(f"Output dir    : {OUT_DIR}")
    print("\nTop benchmark rows:")
    print(benchmark_table.head(5)[["model", "feature_set", "runs", "test_auc_mean_std", "test_ap_mean_std"]].to_string(index=False))
    print("\nAblation rows:")
    print(ablation_table[["model", "feature_set", "runs", "test_auc_mean_std", "test_ap_mean_std"]].to_string(index=False))


if __name__ == "__main__":
    main()
