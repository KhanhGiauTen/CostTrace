import json
import importlib.util
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from phase04_graph_utils import adjacency_from_edges, betweenness_centrality, shortest_paths

PHASE04_HELPERS = Path(__file__).resolve().parent / "19_phase04_modeling_benchmarks_ablation.py"
spec = importlib.util.spec_from_file_location("phase04_helpers", PHASE04_HELPERS)
phase04_helpers = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(phase04_helpers)
train_logistic = phase04_helpers.train_logistic


DATASETS = {
    "sashts": {
        "edges": Path("data/processed/sashts/edgelist.csv"),
        "nodes": Path("data/processed/sashts/nodelist.csv"),
    },
    "sociopatterns_primary_school": {
        "edges": Path("data/processed/multi_dataset/sociopatterns_primary_school/edgelist.csv"),
        "nodes": Path("data/processed/multi_dataset/sociopatterns_primary_school/nodelist.csv"),
    },
    "sociopatterns_hospital": {
        "edges": Path("data/processed/multi_dataset/sociopatterns_hospital/edgelist.csv"),
        "nodes": Path("data/processed/multi_dataset/sociopatterns_hospital/nodelist.csv"),
    },
}

SEEDS = [11, 23, 42]
TASKS_PER_SEED = 20
TARGET_FRACS = [0.10, 0.20, 0.30]
OUT_DIR = Path("results/metrics")
AUDIT_DIR = Path("results/audit")
ORDERS_DIR = Path("results/orders")


def load_graph(dataset: str, spec: dict) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, set[str]], dict[tuple[str, str], float]]:
    edges = pd.read_csv(spec["edges"])
    nodes = pd.read_csv(spec["nodes"])
    edges["source"] = edges["source"].astype(str)
    edges["target"] = edges["target"].astype(str)
    edges["weight"] = pd.to_numeric(edges["weight"], errors="coerce").fillna(1.0)
    adj = adjacency_from_edges(edges)
    weights = {}
    for row in edges.itertuples(index=False):
        u, v = sorted([str(row.source), str(row.target)])
        weights[(u, v)] = float(row.weight)
    return nodes, edges, adj, weights


def weighted_neighbors(adj: dict[str, set[str]], weights: dict[tuple[str, str], float], node: str) -> list[tuple[str, float]]:
    out = []
    for nbr in adj.get(node, set()):
        key = tuple(sorted([node, nbr]))
        out.append((nbr, weights.get(key, 1.0)))
    return out


def simulate_si(
    adj: dict[str, set[str]],
    weights: dict[tuple[str, str], float],
    source: str,
    target_size: int,
    rng: np.random.Generator,
    beta: float = 0.35,
    max_steps: int = 200,
) -> tuple[set[str], int]:
    infected = {source}
    max_log_weight = max((np.log1p(w) for w in weights.values()), default=1.0)
    steps = 0
    while len(infected) < target_size and steps < max_steps:
        steps += 1
        new_infected = set()
        for node in list(infected):
            for nbr, weight in weighted_neighbors(adj, weights, node):
                if nbr in infected:
                    continue
                p = min(beta * np.log1p(weight) / max(max_log_weight, 1e-12), 0.95)
                if rng.random() < p:
                    new_infected.add(nbr)
        if not new_infected:
            frontier = sorted({nbr for node in infected for nbr in adj.get(node, set()) if nbr not in infected})
            if frontier:
                new_infected.add(str(rng.choice(frontier)))
            else:
                break
        infected.update(new_infected)
    return infected, steps


def induced_edges(infected: set[str], weights: dict[tuple[str, str], float]) -> pd.DataFrame:
    rows = []
    for (u, v), weight in weights.items():
        if u in infected and v in infected:
            rows.append({"source": u, "target": v, "weight": weight})
    return pd.DataFrame(rows)


def closeness(adj: dict[str, set[str]], nodes: list[str]) -> dict[str, float]:
    out = {}
    for node in nodes:
        dist = shortest_paths(adj, node)
        total = sum(dist.get(other, 0) for other in nodes)
        out[node] = (len(nodes) - 1) / total if total else 0.0
    return out


def eccentric_center_score(adj: dict[str, set[str]], nodes: list[str]) -> dict[str, float]:
    ecc = {}
    for node in nodes:
        dist = shortest_paths(adj, node)
        ecc[node] = max((dist.get(other, 9999) for other in nodes), default=0)
    radius = min(ecc.values()) if ecc else 0
    max_ecc = max(ecc.values()) if ecc else 0
    denom = max(max_ecc - radius, 1)
    return {node: 1.0 - ((ecc[node] - radius) / denom) for node in nodes}


def candidate_features(
    dataset: str,
    task_id: str,
    source: str,
    infected: set[str],
    full_adj: dict[str, set[str]],
    full_weights: dict[tuple[str, str], float],
) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
    edge_df = induced_edges(infected, full_weights)
    if edge_df.empty:
        return pd.DataFrame(), {}
    snap_adj = adjacency_from_edges(edge_df)
    nodes = sorted(infected)
    degree = {node: len(snap_adj.get(node, set())) for node in nodes}
    full_degree = {node: len(full_adj.get(node, set())) for node in nodes}
    close = closeness(snap_adj, nodes)
    bet = betweenness_centrality(snap_adj, nodes) if len(nodes) > 2 else {node: 0.0 for node in nodes}
    center = eccentric_center_score(snap_adj, nodes)
    weighted = defaultdict(float)
    for row in edge_df.itertuples(index=False):
        weighted[str(row.source)] += float(row.weight)
        weighted[str(row.target)] += float(row.weight)
    max_weighted = max(weighted.values(), default=1.0)
    max_degree = max(degree.values(), default=1)
    rows = []
    for node in nodes:
        boundary = len([nbr for nbr in full_adj.get(node, set()) if nbr not in infected])
        full_deg = max(full_degree[node], 1)
        rows.append(
            {
                "dataset": dataset,
                "task_id": task_id,
                "node_id": node,
                "true_source": source,
                "label": int(node == source),
                "snapshot_size": len(infected),
                "snapshot_degree": degree[node],
                "snapshot_degree_centrality": degree[node] / max(len(nodes) - 1, 1),
                "snapshot_weighted_degree_norm": weighted[node] / max(max_weighted, 1e-12),
                "snapshot_betweenness": bet[node],
                "snapshot_closeness": close[node],
                "snapshot_center_score": center[node],
                "full_degree_norm": full_degree[node] / max(max(full_degree.values()), 1),
                "boundary_degree_norm": boundary / full_deg,
                "infected_neighbor_ratio": degree[node] / full_deg,
            }
        )
    features = pd.DataFrame(rows)
    node_to_idx = {node: idx for idx, node in enumerate(nodes)}
    adj_mat = np.zeros((len(nodes), len(nodes)), dtype=float)
    for row in edge_df.itertuples(index=False):
        i, j = node_to_idx[str(row.source)], node_to_idx[str(row.target)]
        w = np.log1p(float(row.weight))
        adj_mat[i, j] += w
        adj_mat[j, i] += w
    row_sum = adj_mat.sum(axis=1, keepdims=True)
    adj_norm = np.divide(adj_mat, np.maximum(row_sum, 1e-12), out=np.zeros_like(adj_mat), where=row_sum > 0)
    return features, {"adj_norm": adj_norm}


def generate_tasks() -> tuple[pd.DataFrame, dict[str, np.ndarray], pd.DataFrame]:
    all_rows = []
    adj_by_task = {}
    task_meta = []
    for dataset, spec in DATASETS.items():
        _, edges, adj, weights = load_graph(dataset, spec)
        all_nodes = sorted(adj)
        eligible = [node for node in all_nodes if len(adj[node]) > 0]
        for seed in SEEDS:
            rng = np.random.default_rng(seed)
            sources = rng.choice(eligible, size=min(TASKS_PER_SEED, len(eligible)), replace=False)
            for source in sources:
                for frac in TARGET_FRACS:
                    target_size = max(5, int(round(len(all_nodes) * frac)))
                    infected, steps = simulate_si(adj, weights, str(source), target_size, rng)
                    if str(source) not in infected or len(infected) < 3:
                        continue
                    task_id = f"{dataset}_seed{seed}_source{source}_frac{int(frac*100)}"
                    rows, mats = candidate_features(dataset, task_id, str(source), infected, adj, weights)
                    if rows.empty:
                        continue
                    all_rows.append(rows)
                    adj_by_task[task_id] = mats["adj_norm"]
                    task_meta.append(
                        {
                            "dataset": dataset,
                            "task_id": task_id,
                            "true_source": str(source),
                            "snapshot_size": len(infected),
                            "target_fraction": frac,
                            "simulation_steps": steps,
                            "candidate_rows": len(rows),
                        }
                    )
    return pd.concat(all_rows, ignore_index=True), adj_by_task, pd.DataFrame(task_meta)


def scale(train: np.ndarray, all_x: np.ndarray) -> np.ndarray:
    mins = train.min(axis=0)
    maxs = train.max(axis=0)
    return (all_x - mins) / np.maximum(maxs - mins, 1e-12)


def train_graphsage_lodo(candidates: pd.DataFrame, adj_by_task: dict[str, np.ndarray]) -> pd.Series:
    feature_cols = [
        "snapshot_degree_centrality",
        "snapshot_weighted_degree_norm",
        "snapshot_betweenness",
        "snapshot_closeness",
        "snapshot_center_score",
        "full_degree_norm",
        "boundary_degree_norm",
        "infected_neighbor_ratio",
    ]
    probs = pd.Series(index=candidates.index, dtype=float)
    for test_dataset in sorted(candidates["dataset"].unique()):
        train_mask = candidates["dataset"] != test_dataset
        test_mask = candidates["dataset"] == test_dataset
        x_raw = candidates[feature_cols].to_numpy(float)
        x_scaled = scale(x_raw[train_mask.to_numpy()], x_raw)
        graph_blocks = []
        for task_id, group in candidates.groupby("task_id", sort=False):
            idx = group.index.to_numpy()
            block = x_scaled[idx]
            graph_blocks.append(pd.DataFrame(np.concatenate([block, adj_by_task[task_id] @ block], axis=1), index=idx))
        x_graph = pd.concat(graph_blocks).sort_index().to_numpy(float)
        y = candidates["label"].to_numpy(int)

        train_indices = np.where(train_mask.to_numpy())[0]
        rng = np.random.default_rng(100 + len(test_dataset))
        train_tasks = candidates.loc[train_mask, "task_id"].drop_duplicates().to_numpy()
        val_task_count = max(1, int(0.2 * len(train_tasks)))
        val_tasks = set(rng.choice(train_tasks, size=val_task_count, replace=False))
        val_mask = candidates["task_id"].isin(val_tasks).to_numpy() & train_mask.to_numpy()
        fit_mask = train_mask.to_numpy() & ~val_mask
        if not fit_mask.any() or not val_mask.any():
            fit_mask = train_mask.to_numpy()
            val_mask = train_mask.to_numpy()
        pred, _ = train_logistic(x_graph, y, fit_mask, val_mask, seed=911)
        probs.loc[test_mask] = pred[test_mask.to_numpy()]
    return probs


def distance_between(adj: dict[str, set[str]], source: str, target: str) -> int | None:
    dist = shortest_paths(adj, source)
    return dist.get(target)


def evaluate_rankings(candidates: pd.DataFrame, scores: dict[str, pd.Series]) -> pd.DataFrame:
    full_graphs = {}
    for dataset, spec in DATASETS.items():
        _, _, adj, _ = load_graph(dataset, spec)
        full_graphs[dataset] = adj
    rows = []
    for (dataset, task_id), group in candidates.groupby(["dataset", "task_id"], sort=True):
        true_source = str(group["true_source"].iloc[0])
        for method, score_series in scores.items():
            local = group.copy()
            local["score"] = score_series.loc[local.index].to_numpy(float)
            local = local.sort_values(["score", "node_id"], ascending=[False, True], kind="mergesort")
            ranked_nodes = local["node_id"].astype(str).tolist()
            rank = ranked_nodes.index(true_source) + 1
            pred = ranked_nodes[0]
            rows.append(
                {
                    "dataset": dataset,
                    "task_id": task_id,
                    "method": method,
                    "snapshot_size": int(local["snapshot_size"].iloc[0]),
                    "candidate_count": int(len(local)),
                    "true_source": true_source,
                    "predicted_source": pred,
                    "source_rank": int(rank),
                    "hit_at_1": int(rank == 1),
                    "hit_at_5": int(rank <= 5),
                    "mrr": 1.0 / rank,
                    "error_hops": distance_between(full_graphs[dataset], true_source, pred),
                }
            )
    return pd.DataFrame(rows)


def summarize(results: pd.DataFrame) -> pd.DataFrame:
    return (
        results.groupby(["dataset", "method"], as_index=False)
        .agg(
            tasks=("task_id", "nunique"),
            hit_at_1=("hit_at_1", "mean"),
            hit_at_5=("hit_at_5", "mean"),
            mean_rank=("source_rank", "mean"),
            median_rank=("source_rank", "median"),
            mrr=("mrr", "mean"),
            mean_error_hops=("error_hops", "mean"),
        )
        .sort_values(["dataset", "mrr"], ascending=[True, False])
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    ORDERS_DIR.mkdir(parents=True, exist_ok=True)
    candidates, adj_by_task, task_meta = generate_tasks()
    scores = {
        "random": pd.Series(np.random.default_rng(42).random(len(candidates)), index=candidates.index),
        "snapshot_degree": candidates["snapshot_degree_centrality"],
        "snapshot_weighted_degree": candidates["snapshot_weighted_degree_norm"],
        "snapshot_closeness": candidates["snapshot_closeness"],
        "snapshot_betweenness": candidates["snapshot_betweenness"],
        "snapshot_center": candidates["snapshot_center_score"],
        "graphsage_lodo": train_graphsage_lodo(candidates, adj_by_task),
    }
    results = evaluate_rankings(candidates, scores)
    summary = summarize(results)

    candidates.to_csv(ORDERS_DIR / "trace_candidate_features.csv", index=False)
    task_meta.to_csv(OUT_DIR / "trace_tasks.csv", index=False)
    results.to_csv(OUT_DIR / "trace_full_metrics.csv", index=False)
    summary.to_csv(OUT_DIR / "trace_summary_table.csv", index=False)

    dataset_rows = []
    for dataset, spec in DATASETS.items():
        nodes, edges, adj, _ = load_graph(dataset, spec)
        dataset_rows.append(
            {
                "dataset": dataset,
                "nodes": len(adj),
                "edges": len(edges),
                "source": str(spec["edges"]),
                "trace_tasks": int(task_meta[task_meta["dataset"] == dataset]["task_id"].nunique()),
            }
        )
    pd.DataFrame(dataset_rows).to_csv(OUT_DIR / "trace_dataset_summary.csv", index=False)

    with open(AUDIT_DIR / "trace_run_metadata.json", "w", encoding="utf-8") as f:
        json.dump(
            {
                "created_at_utc": datetime.now(timezone.utc).isoformat(),
                "seeds": SEEDS,
                "tasks_per_seed": TASKS_PER_SEED,
                "target_fractions": TARGET_FRACS,
                "simulation": "SI over real weighted contact graphs; true source known by construction",
                "graphsage_lodo": "mean-neighbor logistic source ranker trained leave-one-dataset-out",
            },
            f,
            indent=2,
        )
    print("=== MULTI-DATASET TRACE EXPERIMENT COMPLETE ===")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
