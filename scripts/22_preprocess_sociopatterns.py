import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from phase04_graph_utils import adjacency_from_edges, topology_metrics


EVENT_DURATION_SEC = 20


DATASETS = {
    "sociopatterns_primary_school": {
        "raw_contacts": Path("data/raw/socioSchool/primaryschool.csv/primaryschool.csv"),
        "raw_metadata": Path("data/raw/socioSchool/primaryschool.csv/primaryschool_metadata.txt"),
        "out_dir": Path("data/processed/multi_dataset/sociopatterns_primary_school"),
        "site": "SocioPatterns primary school",
        "contact_columns": ["t", "source", "target", "source_group", "target_group"],
    },
    "sociopatterns_hospital": {
        "raw_contacts": Path("data/raw/socioHos/hospital_lyon_contacts.dat/detailed_list_of_contacts_Hospital.dat"),
        "raw_metadata": None,
        "out_dir": Path("data/processed/multi_dataset/sociopatterns_hospital"),
        "site": "SocioPatterns hospital ward",
        "contact_columns": ["t", "source", "target", "source_group", "target_group"],
    },
}


def read_contacts(path: Path, columns: list[str]) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing raw contact file: {path}")
    contacts = pd.read_csv(path, sep=r"\s+|,", header=None, names=columns, engine="python")
    contacts["source"] = contacts["source"].astype(str)
    contacts["target"] = contacts["target"].astype(str)
    contacts["source_group"] = contacts["source_group"].astype(str)
    contacts["target_group"] = contacts["target_group"].astype(str)
    contacts = contacts[contacts["source"] != contacts["target"]].copy()
    ordered = contacts.apply(lambda row: sorted([row["source"], row["target"]]), axis=1)
    contacts["source_canon"] = [pair[0] for pair in ordered]
    contacts["target_canon"] = [pair[1] for pair in ordered]
    return contacts


def read_primary_school_metadata(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=["node_id", "group", "sex"])
    meta = pd.read_csv(path, sep=r"\s+", header=None, names=["node_id", "group", "sex"], dtype=str)
    return meta


def infer_group_metadata(contacts: pd.DataFrame) -> pd.DataFrame:
    groups: dict[str, list[str]] = defaultdict(list)
    for row in contacts.itertuples(index=False):
        groups[str(row.source)].append(str(row.source_group))
        groups[str(row.target)].append(str(row.target_group))
    rows = []
    for node, values in sorted(groups.items()):
        rows.append({"node_id": node, "group": Counter(values).most_common(1)[0][0], "sex": "Unknown"})
    return pd.DataFrame(rows)


def aggregate_edges(contacts: pd.DataFrame, dataset: str) -> pd.DataFrame:
    edges = (
        contacts.groupby(["source_canon", "target_canon"])
        .agg(
            n_contacts=("t", "count"),
            first_t=("t", "min"),
            last_t=("t", "max"),
        )
        .reset_index()
        .rename(columns={"source_canon": "source", "target_canon": "target"})
    )
    edges["weight"] = edges["n_contacts"] * EVENT_DURATION_SEC
    edges["weight_raw"] = edges["weight"]
    edges["dataset"] = dataset
    edges["graph_id"] = dataset
    edges["region"] = "sociopatterns"
    edges["graph_family"] = "temporal_contact_aggregated"
    edges["traversal"] = "none"
    edges["include_in_main_experiment"] = True
    edges["source_file"] = ""
    return edges[
        [
            "dataset",
            "graph_id",
            "region",
            "graph_family",
            "traversal",
            "include_in_main_experiment",
            "source",
            "target",
            "weight",
            "weight_raw",
            "n_contacts",
            "first_t",
            "last_t",
            "source_file",
        ]
    ]


def add_weighted_metrics(nodes: pd.DataFrame, edges: pd.DataFrame) -> pd.DataFrame:
    weighted = defaultdict(float)
    contacts = defaultdict(float)
    for row in edges.itertuples(index=False):
        weighted[str(row.source)] += float(row.weight)
        weighted[str(row.target)] += float(row.weight)
        contacts[str(row.source)] += float(row.n_contacts)
        contacts[str(row.target)] += float(row.n_contacts)
    nodes["weighted_degree_sec"] = nodes["node_id"].map(lambda node: weighted[str(node)]).astype(float)
    nodes["contact_count"] = nodes["node_id"].map(lambda node: contacts[str(node)]).astype(float)
    return nodes


def process_dataset(name: str, spec: dict) -> dict:
    contacts = read_contacts(spec["raw_contacts"], spec["contact_columns"])
    if spec["raw_metadata"] is not None:
        meta = read_primary_school_metadata(spec["raw_metadata"])
    else:
        meta = infer_group_metadata(contacts)

    edges = aggregate_edges(contacts, name)
    edges["source_file"] = str(spec["raw_contacts"].as_posix())
    adj = adjacency_from_edges(edges)
    topology, profile = topology_metrics(adj)
    nodes = topology.copy()
    nodes["dataset"] = name
    nodes["graph_id"] = name
    nodes["region"] = "sociopatterns"
    nodes["graph_family"] = "temporal_contact_aggregated"
    nodes["traversal"] = "none"
    nodes["include_in_main_experiment"] = True
    nodes["label"] = "simulation_source_unknown_until_task_generation"
    nodes["structural_source_label"] = 0
    nodes["sars_label"] = np.nan
    nodes["source_file"] = str(spec["raw_contacts"].as_posix())

    meta = meta.copy()
    meta["node_id"] = meta["node_id"].astype(str)
    nodes["node_id"] = nodes["node_id"].astype(str)
    nodes = nodes.merge(meta, on="node_id", how="left")
    nodes["group"] = nodes["group"].fillna("Unknown")
    nodes["sex"] = nodes["sex"].fillna("Unknown")
    nodes["site"] = spec["site"]
    nodes["sars"] = "Unknown"
    nodes["index"] = "Unknown"
    nodes["hhid"] = nodes["component_id"].map(lambda value: f"{name}_component_{value}")
    nodes = add_weighted_metrics(nodes, edges)

    out_dir = spec["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)

    edges.to_csv(out_dir / "edges.csv", index=False)
    edges[["source", "target", "weight", "n_contacts", "graph_family"]].rename(
        columns={"graph_family": "transmission"}
    ).to_csv(out_dir / "edgelist.csv", index=False)

    node_cols = [
        "dataset",
        "graph_id",
        "region",
        "graph_family",
        "node_id",
        "component_id",
        "component_size",
        "label",
        "hhid",
        "site",
        "group",
        "sex",
        "sars",
        "index",
        "degree",
        "weighted_degree_sec",
        "contact_count",
        "degree_centrality",
        "betweenness_centrality",
        "closeness_centrality",
        "clustering",
        "core_number",
        "graph_center_score",
        "structural_source_label",
        "source_file",
    ]
    nodes[node_cols].to_csv(out_dir / "nodes.csv", index=False)
    nodes[
        [
            "node_id",
            "site",
            "group",
            "sex",
            "sars",
            "index",
            "hhid",
            "degree",
            "weighted_degree_sec",
            "contact_count",
            "degree_centrality",
            "betweenness_centrality",
            "closeness_centrality",
            "clustering",
            "core_number",
            "graph_center_score",
            "structural_source_label",
        ]
    ].to_csv(out_dir / "nodelist.csv", index=False)

    node_scores = nodes[
        [
            "node_id",
            "site",
            "group",
            "sex",
            "hhid",
            "degree",
            "weighted_degree_sec",
            "contact_count",
            "degree_centrality",
            "betweenness_centrality",
            "closeness_centrality",
            "clustering",
            "core_number",
            "graph_center_score",
        ]
    ].copy()
    max_weight = max(float(node_scores["weighted_degree_sec"].max()), 1.0)
    node_scores["composite_trace_score"] = (
        0.35 * node_scores["degree_centrality"]
        + 0.25 * (node_scores["weighted_degree_sec"] / max_weight)
        + 0.20 * node_scores["betweenness_centrality"]
        + 0.20 * node_scores["graph_center_score"]
    )
    node_scores = node_scores.sort_values(
        ["composite_trace_score", "weighted_degree_sec", "node_id"],
        ascending=[False, False, True],
        kind="mergesort",
    )
    node_scores["rank_by_composite_trace"] = range(1, len(node_scores) + 1)
    node_scores.to_csv(out_dir / "node_scores.csv", index=False)

    dataset_profile = {
        "dataset": name,
        "source": "SocioPatterns",
        "raw_contact_file": str(spec["raw_contacts"].as_posix()),
        "raw_metadata_file": str(spec["raw_metadata"].as_posix()) if spec["raw_metadata"] else None,
        "processed_output_folder": str(out_dir.as_posix()),
        "event_duration_sec_assumption": EVENT_DURATION_SEC,
        "nodes": int(profile["nodes"]),
        "edges": int(profile["edges"]),
        "components": int(profile["components"]),
        "largest_component": int(profile["largest_component"]),
        "density": float(profile["density"]),
        "features": [
            "degree",
            "weighted_degree_sec",
            "contact_count",
            "degree_centrality",
            "betweenness_centrality",
            "closeness_centrality",
            "clustering",
            "core_number",
            "graph_center_score",
            "group",
            "sex/status",
        ],
        "trace_task_policy": "true source will be generated by SI simulation in multi-dataset trace experiments",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    with open(out_dir / "dataset_profile.json", "w", encoding="utf-8") as f:
        json.dump(dataset_profile, f, indent=2)

    return dataset_profile


def main() -> None:
    profiles = []
    for name, spec in DATASETS.items():
        profile = process_dataset(name, spec)
        profiles.append(profile)
        print(
            f"{name}: nodes={profile['nodes']} edges={profile['edges']} "
            f"components={profile['components']}"
        )

    out = Path("results/metrics")
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(profiles).to_csv(out / "sociopatterns_preprocess_summary.csv", index=False)
    print("Exported results/metrics/sociopatterns_preprocess_summary.csv")


if __name__ == "__main__":
    main()
