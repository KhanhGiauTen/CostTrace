from pathlib import Path

import pandas as pd


OUT_DIR = Path("results/metrics")
AUDIT_DIR = Path("results/audit")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    required_files = [
        "benchmark_table.csv",
        "benchmark_full_metrics.csv",
        "ablation_table.csv",
        "ablation_full_metrics.csv",
        "multi_dataset_summary.csv",
        "multi_dataset_experiment_table.csv",
    ]
    for name in required_files:
        require((OUT_DIR / name).exists(), f"Missing {OUT_DIR / name}")
    require((AUDIT_DIR / "phase04_run_metadata.json").exists(), "Missing results/audit/phase04_run_metadata.json")

    benchmark_full = pd.read_csv(OUT_DIR / "benchmark_full_metrics.csv")
    benchmark = pd.read_csv(OUT_DIR / "benchmark_table.csv")
    ablation_full = pd.read_csv(OUT_DIR / "ablation_full_metrics.csv")
    ablation = pd.read_csv(OUT_DIR / "ablation_table.csv")
    dataset_summary = pd.read_csv(OUT_DIR / "multi_dataset_summary.csv")
    multi_exp = pd.read_csv(OUT_DIR / "multi_dataset_experiment_table.csv")

    require(len(benchmark_full) == 150, "Expected 150 benchmark run rows")
    require(len(ablation_full) == 75, "Expected 75 ablation run rows")
    require((benchmark["runs"] == 15).all(), "Every benchmark summary row must have 15 runs")
    require((ablation["runs"] == 15).all(), "Every ablation summary row must have 15 runs")
    require(
        {"graphsage_mean_neighbor", "no_graph_logistic", "no_graph_mlp", "gaussian_naive_bayes"}.issubset(
            set(benchmark["model"])
        ),
        "Missing required trainable benchmark models",
    )
    require(
        {"random", "degree_centrality", "weighted_degree", "betweenness_centrality"}.issubset(
            set(benchmark["model"])
        ),
        "Missing required network heuristic models",
    )
    require(
        {"graph_full", "no_graph_mlp_full", "graph_remove_metadata", "graph_remove_centrality", "graph_remove_edge_contact"}.issubset(
            set(ablation["model"])
        ),
        "Missing required ablation rows",
    )
    metric_cols = [
        "test_auc",
        "test_ap",
        "test_f1",
        "validation_ap",
        "train_ap",
    ]
    for col in metric_cols:
        require(col in benchmark_full.columns, f"Missing benchmark metric column {col}")
        require(benchmark_full[col].notna().all(), f"NaN values found in {col}")

    expected_datasets = {
        "sashts",
        "sociopatterns_primary_school",
        "sociopatterns_hospital",
    }
    require(
        expected_datasets == set(dataset_summary["dataset"]),
        "Dataset summary must include SASHTS, SocioPatterns primary school, and SocioPatterns hospital",
    )
    require(
        {"evaluation_task", "phase04_metric_source"}.issubset(set(multi_exp.columns)),
        "Multi-dataset experiment table must name the evaluation task and metric source",
    )
    require(
        (
            multi_exp.loc[
                multi_exp["dataset"].str.startswith("sociopatterns"),
                "phase04_metric_source",
            ]
            == "results/metrics/trace_summary_table.csv"
        ).all(),
        "SocioPatterns rows must point to the trace evaluation metrics",
    )

    print("PHASE04_VALIDATION_OK")
    print(f"benchmark_rows={len(benchmark_full)} ablation_rows={len(ablation_full)}")
    print("datasets=" + ",".join(sorted(dataset_summary["dataset"].tolist())))


if __name__ == "__main__":
    main()
