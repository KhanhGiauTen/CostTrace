from collections import deque

import pandas as pd


def adjacency_from_edges(edges: pd.DataFrame) -> dict[str, set[str]]:
    adj: dict[str, set[str]] = {}
    for row in edges.itertuples(index=False):
        u = str(row.source)
        v = str(row.target)
        if u == v:
            continue
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    return adj


def shortest_paths(adj: dict[str, set[str]], source: str) -> dict[str, int]:
    source = str(source)
    dist = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for nbr in adj.get(node, set()):
            if nbr not in dist:
                dist[nbr] = dist[node] + 1
                queue.append(nbr)
    return dist


def connected_components(adj: dict[str, set[str]]) -> list[list[str]]:
    seen = set()
    components = []
    for node in sorted(adj):
        if node in seen:
            continue
        comp = []
        queue = deque([node])
        seen.add(node)
        while queue:
            current = queue.popleft()
            comp.append(current)
            for nbr in adj.get(current, set()):
                if nbr not in seen:
                    seen.add(nbr)
                    queue.append(nbr)
        components.append(sorted(comp))
    return components


def betweenness_centrality(adj: dict[str, set[str]], nodes: list[str] | None = None) -> dict[str, float]:
    nodes = sorted(str(node) for node in (nodes if nodes is not None else adj.keys()))
    cb = {node: 0.0 for node in nodes}
    node_set = set(nodes)
    for source in nodes:
        stack = []
        predecessors = {node: [] for node in nodes}
        sigma = dict.fromkeys(nodes, 0.0)
        dist = dict.fromkeys(nodes, -1)
        sigma[source] = 1.0
        dist[source] = 0
        queue = deque([source])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in sorted(adj.get(v, set()) & node_set):
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    predecessors[w].append(v)
        delta = dict.fromkeys(nodes, 0.0)
        while stack:
            w = stack.pop()
            for v in predecessors[w]:
                if sigma[w]:
                    delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != source:
                cb[w] += delta[w]
    scale = 1.0 / 2.0
    norm = ((len(nodes) - 1) * (len(nodes) - 2)) / 2.0
    for node in cb:
        cb[node] *= scale
        if norm > 0:
            cb[node] /= norm
    return cb


def clustering_coefficient(adj: dict[str, set[str]], node: str) -> float:
    nbrs = list(adj.get(node, set()))
    degree = len(nbrs)
    if degree < 2:
        return 0.0
    links = 0
    for i, u in enumerate(nbrs):
        for v in nbrs[i + 1 :]:
            if v in adj.get(u, set()):
                links += 1
    return 2.0 * links / (degree * (degree - 1))


def core_numbers(adj: dict[str, set[str]]) -> dict[str, int]:
    remaining = {node: set(nbrs) for node, nbrs in adj.items()}
    cores = {}
    current_core = 0
    while remaining:
        node, degree = min(remaining.items(), key=lambda item: len(item[1]))
        current_core = max(current_core, len(degree))
        cores[node] = current_core
        for nbr in list(remaining[node]):
            if nbr in remaining:
                remaining[nbr].discard(node)
        del remaining[node]
    return cores


def topology_metrics(adj: dict[str, set[str]]) -> tuple[pd.DataFrame, dict]:
    nodes = sorted(adj)
    components = connected_components(adj)
    comp_id = {}
    comp_size = {}
    for idx, comp in enumerate(components):
        for node in comp:
            comp_id[node] = idx
            comp_size[node] = len(comp)

    bet = betweenness_centrality(adj, nodes)
    cores = core_numbers(adj)
    rows = []
    n = len(nodes)
    for node in nodes:
        dist = shortest_paths(adj, node)
        reachable = [d for other, d in dist.items() if other != node]
        total_dist = sum(reachable)
        rows.append(
            {
                "node_id": node,
                "component_id": comp_id[node],
                "component_size": comp_size[node],
                "degree": len(adj.get(node, set())),
                "degree_centrality": len(adj.get(node, set())) / max(n - 1, 1),
                "betweenness_centrality": bet[node],
                "closeness_centrality": (len(reachable) / total_dist) if total_dist else 0.0,
                "clustering": clustering_coefficient(adj, node),
                "core_number": cores.get(node, 0),
                "graph_center_score": 1.0 / max(max(reachable, default=0), 1),
            }
        )
    profile = {
        "nodes": n,
        "edges": int(sum(len(nbrs) for nbrs in adj.values()) / 2),
        "components": len(components),
        "largest_component": max((len(comp) for comp in components), default=0),
    }
    profile["density"] = (
        (2.0 * profile["edges"] / (n * (n - 1))) if n > 1 else 0.0
    )
    return pd.DataFrame(rows), profile
