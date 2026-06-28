from __future__ import annotations

import json

import networkx as nx
import pandas as pd

from costtrace.config import PATHS


def test_processed_node_and_edge_counts_match_authoritative_summary() -> None:
    nodes = pd.read_csv(PATHS.processed_nodelist)
    edges = pd.read_csv(PATHS.processed_edgelist)
    summary = json.loads(PATHS.eda_summary.read_text(encoding="utf-8"))
    assert len(nodes) == summary["n_nodes"] == 340
    assert len(edges) == summary["n_edges"] == 542


def test_graph_construction_from_processed_edgelist() -> None:
    edges = pd.read_csv(PATHS.processed_edgelist)
    graph = nx.from_pandas_edgelist(edges, "source", "target", edge_attr=True)
    assert graph.number_of_edges() == 542
    assert graph.number_of_nodes() == 340
    assert all("weight" in data for _, _, data in graph.edges(data=True))
