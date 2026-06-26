import json
from pathlib import Path

import pandas as pd


OUT_DIR = Path("results/model")
AUDIT_DIR = Path("results/audit")
MODEL_DIR = Path("models/graphsage")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    full_path = OUT_DIR / "full_pytorch_graphsage_full_metrics.csv"
    summary_path = OUT_DIR / "full_pytorch_graphsage_summary.csv"
    metadata_path = AUDIT_DIR / "full_pytorch_graphsage_metadata.json"
    gap_path = OUT_DIR / "gap_summary.csv"
    require(full_path.exists(), f"Missing {full_path}")
    require(summary_path.exists(), f"Missing {summary_path}")
    require(metadata_path.exists(), f"Missing {metadata_path}")
    require(gap_path.exists(), f"Missing {gap_path}; run scripts/29_phase04_gap_summary.py")

    full = pd.read_csv(full_path)
    summary = pd.read_csv(summary_path)
    gap = pd.read_csv(gap_path)
    require(len(full) == 15, "Expected 15 full PyTorch runs")
    require(int(summary.loc[0, "runs"]) == 15, "Summary should report 15 runs")
    require(full["early_stopped"].all(), "Every run should early-stop before max epochs")
    require(full["best_epoch"].between(1, 500).all(), "Best epochs outside expected range")
    for col in ["train_ap", "validation_ap", "test_ap", "test_auc", "test_f1"]:
        require(full[col].notna().all(), f"NaN values in {col}")
    require(
        {"auc", "ap", "f1", "brier"}.issubset(set(gap["metric"])),
        "Gap summary must include AUC, AP, F1, and Brier gaps",
    )

    tuning_summary_path = OUT_DIR / "hyperparameter_search_summary.csv"
    selected_path = AUDIT_DIR / "selected_hyperparameters.json"
    if tuning_summary_path.exists() or selected_path.exists():
        require(tuning_summary_path.exists(), f"Missing {tuning_summary_path}")
        require(selected_path.exists(), f"Missing {selected_path}")
        tuning = pd.read_csv(tuning_summary_path)
        require(len(tuning) >= 2, "Hyperparameter tuning should compare multiple configs")
        require(
            {"hidden_dim", "dropout_1", "dropout_2", "lr", "weight_decay", "validation_ap_mean"}.issubset(
                set(tuning.columns)
            ),
            "Hyperparameter tuning summary missing required columns",
        )
        with open(selected_path, encoding="utf-8") as f:
            selected = json.load(f)["selected_config"]
        for col in ["hidden_dim", "dropout_1", "dropout_2", "lr", "weight_decay"]:
            require(col in full.columns, f"Full metrics missing selected hyperparameter column {col}")
            expected = float(selected[col])
            actual = full[col].astype(float)
            require(
                (abs(actual - expected) < 1e-12).all(),
                f"Final full GraphSAGE metrics do not use selected {col}={expected}",
            )

    checkpoints = list(MODEL_DIR.glob("graphsage_seed*_fold*.pt"))
    require(len(checkpoints) == 15, "Expected 15 model checkpoints")

    print("FULL_PYTORCH_GRAPHSAGE_VALIDATION_OK")
    print(f"runs={len(full)} checkpoints={len(checkpoints)}")
    print(f"gap_rows={len(gap)}")
    print(
        "test_auc="
        + str(summary.loc[0, "test_auc_mean_std"])
        + " test_ap="
        + str(summary.loc[0, "test_ap_mean_std"])
    )


if __name__ == "__main__":
    main()
