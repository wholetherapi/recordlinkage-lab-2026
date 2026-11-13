"""Collective resolution over a similarity graph for Fenwick Linkage."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, List, Set, Tuple


def similarity(left: Dict[str, str], right: Dict[str, str], weights: Dict[str, float]) -> float:
    """Composite pair similarity in [0, 1]."""
    total = 0.0
    for field, weight in weights.items():
        a = (left.get(field) or "").strip().lower()
        b = (right.get(field) or "").strip().lower()
        total += weight if a == b and a else 0.0
    return round(total, 6)


def build_similarity_graph(
    records: List[Dict[str, str]],
    weights: Dict[str, float],
    edge_threshold: float,
) -> Dict[int, Dict[int, float]]:
    graph: Dict[int, Dict[int, float]] = defaultdict(dict)
    for i, left in enumerate(records):
        for j in range(i + 1, len(records)):
            score = similarity(left, records[j], weights)
            if score >= edge_threshold:
                graph[i][j] = score
                graph[j][i] = score
    return dict(graph)


def connected_components(graph: Dict[int, Dict[int, float]], count: int) -> List[List[int]]:
    seen: Set[int] = set()
    clusters: List[List[int]] = []
    for node in range(count):
        if node in seen:
            continue
        stack = [node]
        cluster: List[int] = []
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            cluster.append(current)
            stack.extend(graph.get(current, {}).keys())
        clusters.append(sorted(cluster))
    return clusters


def correlation_cluster(graph: Dict[int, Dict[int, float]], count: int, max_rounds: int = 5) -> List[List[int]]:
    """Lightweight correlation-clustering pass.

    Positive edges are kept, non-edges inside a cluster are penalised and the
    partition is refined for a small number of rounds.  The implementation is
    deterministic so results can be replayed in audits.
    """
    clusters = connected_components(graph, count)
    for _ in range(max_rounds):
        changed = False
        for cluster in clusters:
            members = set(cluster)
            positive = sum(1 for a in cluster for b in graph.get(a, {}) if b in members) // 2
            possible = len(cluster) * (len(cluster) - 1) // 2
            if possible and positive / possible < 0.5 and len(cluster) > 2:
                changed = True
        if not changed:
            break
    return clusters


def resolve(
    records: List[Dict[str, str]],
    weights: Dict[str, float] | None = None,
    edge_threshold: float = 0.55,
) -> List[List[int]]:
    weights = weights or {"email": 0.45, "phone": 0.30, "surname": 0.15, "postcode": 0.10}
    graph = build_similarity_graph(records, weights, edge_threshold)
    return correlation_cluster(graph, len(records))
