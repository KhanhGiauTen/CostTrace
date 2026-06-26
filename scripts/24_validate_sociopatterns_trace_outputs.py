from pathlib import Path

import pandas as pd


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    processed = [
        Path("data/processed/multi_dataset/sociopatterns_primary_school"),
        Path("data/processed/multi_dataset/sociopatterns_hospital"),
    ]
    for folder in processed:
        require(folder.exists(), f"Missing processed folder: {folder}")
        for name in ["edges.csv", "edgelist.csv", "nodes.csv", "nodelist.csv", "node_scores.csv", "dataset_profile.json"]:
            require((folder / name).exists(), f"Missing {folder / name}")
        edges = pd.read_csv(folder / "edges.csv")
        nodes = pd.read_csv(folder / "nodes.csv")
        require(len(edges) > 0, f"No edges in {folder}")
        require(len(nodes) > 0, f"No nodes in {folder}")
        require((edges["source"].astype(str) != edges["target"].astype(str)).all(), f"Self-loop found in {folder}")
        require(edges.duplicated(["source", "target"]).sum() == 0, f"Duplicate canonical edge in {folder}")
        node_ids = set(nodes["node_id"].astype(str))
        require(set(edges["source"].astype(str)).issubset(node_ids), f"Missing source nodes in {folder}")
        require(set(edges["target"].astype(str)).issubset(node_ids), f"Missing target nodes in {folder}")

    out = Path("results/metrics")
    audit = Path("results/audit")
    orders = Path("results/orders")
    for name in [
        "trace_dataset_summary.csv",
        "trace_full_metrics.csv",
        "trace_summary_table.csv",
        "trace_tasks.csv",
    ]:
        require((out / name).exists(), f"Missing {out / name}")
    require((orders / "trace_candidate_features.csv").exists(), "Missing results/orders/trace_candidate_features.csv")
    require((audit / "trace_run_metadata.json").exists(), "Missing results/audit/trace_run_metadata.json")

    summary = pd.read_csv(out / "trace_summary_table.csv")
    datasets = set(summary["dataset"])
    require(
        datasets == {"sashts", "sociopatterns_primary_school", "sociopatterns_hospital"},
        f"Unexpected datasets: {datasets}",
    )
    require("graphsage_lodo" in set(summary["method"]), "Missing graphsage_lodo method")
    require(summary["tasks"].min() > 0, "Every dataset/method must have tasks")

    print("SOCIOPATTERNS_TRACE_VALIDATION_OK")
    print("datasets=" + ",".join(sorted(datasets)))
    print(f"summary_rows={len(summary)}")


if __name__ == "__main__":
    main()
