from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

PHASES = {
    "prepare": [
        "00_verify_data.py",
        "01_clean_data.py",
        "02_build_graph.py",
        "03_eda.py",
    ],
    "metrics": [
        "04_basic_metrics.py",
        "05_centrality.py",
        "06_community.py",
        "07_merge_scores.py",
    ],
    "model": [
        "08_gnn_model.py",
    ],
    "budget": [
        "09_topk_budget.py",
        "10_counterfactual.py",
        "11_sir_simulation.py",
        "12_metrics_summary.py",
    ],
    "notebooks": [
        "13_generate_experiment_notebooks.py",
    ],
}


def run_script(script_name: str) -> None:
    script_path = ROOT / "scripts" / script_name
    if not script_path.exists():
        raise FileNotFoundError(f"Missing script: {script_path}")

    print(f"\n=== Running {script_name} ===", flush=True)
    subprocess.run([sys.executable, str(script_path)], cwd=ROOT, check=True)


def selected_scripts(phase: str) -> list[str]:
    if phase == "all":
        ordered = []
        for key in ["prepare", "metrics", "model", "budget", "notebooks"]:
            ordered.extend(PHASES[key])
        return ordered
    return PHASES[phase]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the CostTrace analysis pipeline.")
    parser.add_argument(
        "--phase",
        choices=["all", *PHASES.keys()],
        default="all",
        help="Pipeline section to run.",
    )
    args = parser.parse_args()

    for script in selected_scripts(args.phase):
        run_script(script)

    print("\nCostTrace pipeline completed.", flush=True)


if __name__ == "__main__":
    main()
