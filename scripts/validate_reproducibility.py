from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd

from costtrace.config import PATHS, load_reproducibility_config, phase05_config
from costtrace.intervention.allocation import top_k_nodes


REQUIRED_ARTIFACTS = {
    "config": [
        "config/reproducibility.json",
        "requirements.txt",
        "requirements-lock.txt",
        "environment.yml",
    ],
    "authoritative": [
        "data/processed/sashts/eda_summary.json",
        "results/metrics/basic_metrics.json",
        "results/model/full_pytorch_graphsage_summary.csv",
        "results/metrics/benchmark_table.csv",
        "results/metrics/ablation_table.csv",
        "results/intervention/final_comparison.csv",
    ],
    "phase05": [
        "results/intervention/phase05_run_level_results.csv",
        "results/intervention/phase05_timeseries_results.csv",
        "results/intervention/phase05_budget_curve.csv",
        "results/intervention/phase05_uncertainty_summary.csv",
        "results/intervention/phase05_parameter_sweep.csv",
        "results/intervention/phase05_generation_metadata.json",
    ],
    "paper_ready": [
        "results/paper_ready/figures/figure_manifest.csv",
        "results/paper_ready/tables/table_manifest.csv",
        "docs/paper_upgrade/artifact_traceability.md",
        "docs/paper_upgrade/consistency_report.md",
    ],
    "supplement": [
        "supplement/README.md",
        "supplement/supplement_manifest.csv",
        "supplement/feature_definitions.md",
        "supplement/runtime_notes.md",
        "supplement/limitations.md",
        "supplement/reproduction_instructions.md",
    ],
}

REQUIRED_COLUMNS = {
    "results/intervention/phase05_run_level_results.csv": {
        "profile",
        "param_id",
        "run_id",
        "seed",
        "budget_k_pct",
        "strategy",
        "final_mean_infected_per_hh",
        "reduction_vs_baseline_pct",
    },
    "results/intervention/phase05_timeseries_results.csv": {
        "profile",
        "param_id",
        "run_id",
        "time_step",
        "strategy",
        "mean_ever_infected",
    },
    "results/paper_ready/figures/figure_manifest.csv": {
        "figure_id",
        "filename",
        "source_artifact",
        "source_script",
        "manuscript_section",
    },
    "results/paper_ready/tables/table_manifest.csv": {
        "table_id",
        "csv_path",
        "markdown_path",
        "latex_path",
        "source_artifact",
        "source_script",
    },
}


def require_file(path: str) -> Path:
    full_path = ROOT / path
    if not full_path.exists():
        raise FileNotFoundError(f"Missing required artifact: {path}")
    return full_path


def validate_required_artifacts() -> None:
    for paths in REQUIRED_ARTIFACTS.values():
        for path in paths:
            require_file(path)


def validate_columns() -> None:
    for path, columns in REQUIRED_COLUMNS.items():
        df = pd.read_csv(require_file(path))
        missing = sorted(columns - set(df.columns))
        if missing:
            raise ValueError(f"{path} missing columns: {missing}")


def validate_config() -> None:
    config = load_reproducibility_config()
    for key in ["runtime", "paths", "seeds", "phase05", "strategies"]:
        if key not in config:
            raise ValueError(f"reproducibility config missing key: {key}")
    smoke = phase05_config("smoke")
    if smoke.random_seed != int(config["phase05"]["smoke"]["random_seed"]):
        raise ValueError("phase05_config smoke seed does not match JSON config")
    if tuple(config["strategies"]) != smoke.strategies:
        raise ValueError("strategy list mismatch between config root and Phase 05 smoke profile")


def validate_determinism() -> None:
    df = pd.DataFrame(
        {
            "node_id": ["b", "a", "c"],
            "score": [0.8, 0.8, 0.2],
            "weighted_degree_sec": [2.0, 3.0, 9.0],
        }
    )
    first = top_k_nodes(df, "score", 2)
    second = top_k_nodes(df.sample(frac=1.0, random_state=42), "score", 2)
    if first != second or first != ["a", "b"]:
        raise ValueError("top_k_nodes deterministic tie-break check failed")


def validate_generated_tables_match_sources() -> None:
    benchmark_source = pd.read_csv(PATHS.metrics / "benchmark_table.csv")
    benchmark_table = pd.read_csv(PATHS.results / "paper_ready" / "tables" / "table03_model_benchmark.csv")
    if benchmark_source["test_auc_mean_std"].tolist() != benchmark_table["test_auc_mean_std"].tolist():
        raise ValueError("paper model benchmark table differs from source benchmark artifact")

    final_source = pd.read_csv(PATHS.intervention / "final_comparison.csv").sort_values(
        ["budget_k_pct", "strategy"]
    )
    strategy_table = pd.read_csv(PATHS.results / "paper_ready" / "tables" / "table05_strategy_comparison.csv").sort_values(
        ["budget_k_pct", "strategy"]
    )
    if final_source["prevention_rate_pct"].round(4).tolist() != strategy_table["prevention_rate_pct"].round(4).tolist():
        raise ValueError("paper strategy table differs from final comparison artifact")


def validate_figure_metadata() -> None:
    manifest = pd.read_csv(PATHS.results / "paper_ready" / "figures" / "figure_manifest.csv")
    for _, row in manifest.iterrows():
        figure_path = ROOT / row["filename"]
        if not figure_path.exists():
            raise FileNotFoundError(f"missing figure from manifest: {row['filename']}")
        for source in str(row["source_artifact"]).split(";"):
            source = source.strip()
            if source and not (ROOT / source).exists():
                raise FileNotFoundError(f"missing figure source artifact: {source}")


def validate_existing_validators() -> None:
    validators = [
        "scripts/validate_paths.py",
        "scripts/validate_authoritative_artifacts.py",
        "scripts/validate_phase05_artifacts.py",
        "scripts/validate_paper_artifacts.py",
    ]
    for validator in validators:
        result = subprocess.run(
            [sys.executable, validator],
            cwd=ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"{validator} failed:\n{result.stdout}\n{result.stderr}")


def main() -> int:
    validate_required_artifacts()
    validate_columns()
    validate_config()
    validate_determinism()
    validate_generated_tables_match_sources()
    validate_figure_metadata()
    validate_existing_validators()
    print("REPRODUCIBILITY_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
