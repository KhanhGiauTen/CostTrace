from __future__ import annotations

import pandas as pd

from costtrace.config import PATHS


def test_phase05_artifact_schema() -> None:
    run_level = pd.read_csv(PATHS.intervention / "phase05_run_level_results.csv")
    required = {
        "profile",
        "param_id",
        "run_id",
        "seed",
        "budget_k_pct",
        "strategy",
        "final_mean_infected_per_hh",
    }
    assert required.issubset(run_level.columns)
    assert not run_level.empty


def test_paper_manifest_sources_exist() -> None:
    figures = pd.read_csv(PATHS.results / "paper_ready" / "figures" / "figure_manifest.csv")
    tables = pd.read_csv(PATHS.results / "paper_ready" / "tables" / "table_manifest.csv")
    assert len(figures) >= 9
    assert len(tables) >= 9
    for source in figures["source_artifact"]:
        for part in str(source).split(";"):
            assert (PATHS.root / part.strip()).exists()
