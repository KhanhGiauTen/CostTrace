# Feature Definitions

## Node And Household Fields

- `node_id`: processed individual identifier.
- `hhid`: household identifier.
- `sars_label`: binary SARS positivity label used for evaluation.
- `degree_centrality`, `betweenness_centrality`, `closeness_centrality`: topology-derived node metrics.
- `weighted_degree_sec`: summed contact duration in seconds.
- `gnn_infection_prob`: saved GraphSAGE risk score used only as a ranking signal.

## Edge Fields

- `source`, `target`: endpoint node identifiers.
- `weight`: aggregated contact duration.
- `n_contacts`: number of proximity events aggregated into the edge.
- `transmission`: retrospective observed transmission label used for counterfactual evaluation.

## Intervention Fields

- `budget_k_pct`: percentage of nodes eligible for selection.
- `budget_k_nodes`: selected node count.
- `precision_k_pct`: selected nodes that are SARS positive.
- `transmission_coverage`: observed transmission edges incident to selected nodes.
- `prevention_rate_pct`: retrospective percentage of SARS-positive contacts prevented in counterfactual evaluation.
- `reduction_vs_baseline_pct`: SIR reduction against the no-intervention baseline.
