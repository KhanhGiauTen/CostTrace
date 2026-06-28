from __future__ import annotations

from costtrace.config import PATHS, load_reproducibility_config, phase05_config


def test_canonical_paths_exist() -> None:
    assert PATHS.raw_contact_network.exists()
    assert PATHS.raw_metadata.exists()
    assert PATHS.processed_graph.exists()
    assert PATHS.processed_nodelist.exists()
    assert PATHS.processed_edgelist.exists()


def test_reproducibility_config_loads_phase05_profiles() -> None:
    config = load_reproducibility_config()
    assert config["seeds"]["default"] == 42
    smoke = phase05_config("smoke")
    paper = phase05_config("paper")
    assert smoke.n_runs == 3
    assert paper.n_runs >= smoke.n_runs
    assert smoke.strategies == tuple(config["strategies"])
