import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


OUT_DIR = Path("results/model")
AUDIT_DIR = Path("results/audit")
PHASE04_SCRIPT = Path("scripts/26_phase04_full_pytorch_graphsage.py")

TUNING_SEEDS = [11, 23, 42]
HYPERPARAMETER_GRID = [
    {"hidden_dim": 8, "dropout_1": 0.20, "dropout_2": 0.10, "lr": 0.005, "weight_decay": 1e-4},
    {"hidden_dim": 8, "dropout_1": 0.35, "dropout_2": 0.20, "lr": 0.010, "weight_decay": 5e-4},
    {"hidden_dim": 16, "dropout_1": 0.20, "dropout_2": 0.10, "lr": 0.010, "weight_decay": 1e-4},
    {"hidden_dim": 16, "dropout_1": 0.35, "dropout_2": 0.20, "lr": 0.010, "weight_decay": 5e-4},
    {"hidden_dim": 16, "dropout_1": 0.50, "dropout_2": 0.30, "lr": 0.005, "weight_decay": 1e-3},
    {"hidden_dim": 32, "dropout_1": 0.20, "dropout_2": 0.10, "lr": 0.010, "weight_decay": 5e-4},
    {"hidden_dim": 32, "dropout_1": 0.35, "dropout_2": 0.20, "lr": 0.010, "weight_decay": 5e-4},
    {"hidden_dim": 32, "dropout_1": 0.50, "dropout_2": 0.30, "lr": 0.005, "weight_decay": 1e-3},
]


def load_phase04_module():
    spec = importlib.util.spec_from_file_location("phase04_full_graphsage", PHASE04_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {PHASE04_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def summarize(full: pd.DataFrame) -> pd.DataFrame:
    group_cols = ["config_id", "hidden_dim", "dropout_1", "dropout_2", "lr", "weight_decay"]
    metrics = [
        "validation_ap",
        "validation_auc",
        "validation_brier",
        "test_ap",
        "test_auc",
        "best_epoch",
    ]
    rows = []
    for keys, group in full.groupby(group_cols, dropna=False):
        row = dict(zip(group_cols, keys))
        row["runs"] = int(len(group))
        for metric in metrics:
            row[f"{metric}_mean"] = float(group[metric].mean())
            row[f"{metric}_std"] = float(group[metric].std(ddof=1)) if len(group) > 1 else 0.0
            row[f"{metric}_mean_std"] = (
                f"{row[f'{metric}_mean']:.4f} +/- {row[f'{metric}_std']:.4f}"
            )
        row["early_stopped_runs"] = int(group["early_stopped"].sum())
        rows.append(row)
    return pd.DataFrame(rows).sort_values(
        ["validation_ap_mean", "validation_auc_mean", "validation_brier_mean"],
        ascending=[False, False, True],
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    phase04 = load_phase04_module()
    nodes, edges = phase04.load_data()
    rows = []

    for config_id, params in enumerate(HYPERPARAMETER_GRID, start=1):
        for seed in TUNING_SEEDS:
            for fold, masks in enumerate(phase04.make_group_folds(nodes, seed)):
                row = phase04.run_one(
                    seed=seed,
                    fold=fold,
                    nodes=nodes,
                    edges=edges,
                    masks=masks,
                    save_checkpoint=False,
                    **params,
                )
                row["config_id"] = config_id
                rows.append(row)
                print(
                    "done "
                    f"config={config_id} seed={seed} fold={fold} "
                    f"val_ap={row['validation_ap']:.4f}"
                )

    full = pd.DataFrame(rows)
    summary = summarize(full)
    selected = summary.iloc[0].to_dict()

    full.to_csv(OUT_DIR / "hyperparameter_search_full_metrics.csv", index=False)
    summary.to_csv(OUT_DIR / "hyperparameter_search_summary.csv", index=False)
    with open(AUDIT_DIR / "selected_hyperparameters.json", "w", encoding="utf-8") as f:
        json.dump(
            {
                "created_at_utc": datetime.now(timezone.utc).isoformat(),
                "selection_metric": "mean validation average precision across tuning seeds/folds",
                "tuning_seeds": TUNING_SEEDS,
                "n_folds": phase04.N_FOLDS,
                "candidate_configs": HYPERPARAMETER_GRID,
                "selected_config": selected,
            },
            f,
            indent=2,
        )

    print("\n=== PHASE 04 TORCH HYPERPARAMETER TUNING ===")
    print(summary.head(8)[
        [
            "config_id",
            "hidden_dim",
            "dropout_1",
            "dropout_2",
            "lr",
            "weight_decay",
            "runs",
            "validation_ap_mean_std",
            "test_ap_mean_std",
        ]
    ].to_string(index=False))


if __name__ == "__main__":
    main()
