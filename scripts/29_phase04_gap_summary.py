from pathlib import Path

import pandas as pd


IN_PATH = Path("results/model/full_pytorch_graphsage_full_metrics.csv")
OUT_DIR = Path("results/model")


def main() -> None:
    if not IN_PATH.exists():
        raise FileNotFoundError(f"Missing {IN_PATH}")

    full = pd.read_csv(IN_PATH)
    metric_names = ["auc", "ap", "f1", "brier"]
    rows = []
    by_seed_rows = []

    for metric in metric_names:
        train_col = f"train_{metric}"
        val_col = f"validation_{metric}"
        test_col = f"test_{metric}"
        if not {train_col, val_col, test_col}.issubset(full.columns):
            continue

        full[f"train_test_{metric}_gap"] = full[train_col] - full[test_col]
        full[f"validation_test_{metric}_gap"] = full[val_col] - full[test_col]
        for gap_col in [f"train_test_{metric}_gap", f"validation_test_{metric}_gap"]:
            rows.append(
                {
                    "model": "full_pytorch_graphsage",
                    "metric": metric,
                    "gap": gap_col,
                    "runs": int(len(full)),
                    "mean": float(full[gap_col].mean()),
                    "std": float(full[gap_col].std(ddof=1)) if len(full) > 1 else 0.0,
                    "min": float(full[gap_col].min()),
                    "max": float(full[gap_col].max()),
                    "mean_std": (
                        f"{full[gap_col].mean():.4f} +/- "
                        f"{full[gap_col].std(ddof=1) if len(full) > 1 else 0.0:.4f}"
                    ),
                }
            )

        for seed, group in full.groupby("seed"):
            by_seed_rows.append(
                {
                    "model": "full_pytorch_graphsage",
                    "seed": int(seed),
                    "metric": metric,
                    "runs": int(len(group)),
                    "train_mean": float(group[train_col].mean()),
                    "validation_mean": float(group[val_col].mean()),
                    "test_mean": float(group[test_col].mean()),
                    "train_test_gap_mean": float((group[train_col] - group[test_col]).mean()),
                    "validation_test_gap_mean": float((group[val_col] - group[test_col]).mean()),
                }
            )

    gap_summary = pd.DataFrame(rows)
    gap_by_seed = pd.DataFrame(by_seed_rows)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    gap_summary.to_csv(OUT_DIR / "gap_summary.csv", index=False)
    gap_by_seed.to_csv(OUT_DIR / "gap_by_seed.csv", index=False)

    print("PHASE04_GAP_SUMMARY_OK")
    print(gap_summary[["metric", "gap", "runs", "mean_std"]].to_string(index=False))


if __name__ == "__main__":
    main()
