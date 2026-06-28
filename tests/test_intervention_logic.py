from __future__ import annotations

import networkx as nx
import pandas as pd

from costtrace.intervention.allocation import top_k_nodes
from costtrace.intervention.counterfactual import evaluate_selected_set
from costtrace.intervention.simulation import infection_probability, sir_on_household


def test_top_k_nodes_is_deterministic_with_ties() -> None:
    df = pd.DataFrame(
        {
            "node_id": ["b", "a", "c"],
            "risk": [0.8, 0.8, 0.4],
            "weighted_degree_sec": [2.0, 3.0, 9.0],
        }
    )
    assert top_k_nodes(df, "risk", 2) == ["a", "b"]


def test_counterfactual_selected_set_metrics() -> None:
    trans_df = pd.DataFrame(
        {
            "source": ["a", "b", "c"],
            "target": ["b", "c", "d"],
        }
    )
    metrics = evaluate_selected_set(
        selected={"b"},
        trans_df=trans_df,
        total_transmissions=3,
        index_nodes={"a"},
        contact_nodes={"b", "c", "d"},
        sars_positive_contacts={"b", "d"},
    )
    assert metrics["transmissions_blocked"] == 2
    assert metrics["transmission_block_rate_pct"] == 2 / 3 * 100
    assert metrics["infections_prevented"] == 1


def test_sir_transition_helpers_are_bounded_and_seeded() -> None:
    assert infection_probability(duration_sec=0, max_duration_sec=100, beta=0.25) <= 0.25
    graph = nx.Graph()
    graph.add_edge("a", "b", total_duration_sec=100.0)
    rng = __import__("numpy").random.default_rng(42)
    total = sir_on_household(
        sg=graph,
        index_node="a",
        max_duration_sec=100.0,
        beta=0.0,
        gamma=1.0,
        t_max=3,
        rng=rng,
    )
    assert total == 1
