"""Embedding-based record matching for Kestrel Match Engine."""

from __future__ import annotations

import hashlib
import math
from typing import Dict, List, Sequence

DIMENSIONS = 256


def _bucket(token: str) -> int:
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % DIMENSIONS


def encode(text: str) -> List[float]:
    """Deterministic hashing encoder used in the offline evaluation build."""
    vector = [0.0] * DIMENSIONS
    for token in text.lower().split():
        vector[_bucket(token)] += 1.0
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    return [value / norm for value in vector]


def cosine(left: Sequence[float], right: Sequence[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def featurise(left: Dict[str, str], right: Dict[str, str]) -> List[float]:
    features: List[float] = []
    for field in ("name", "email", "address"):
        features.append(cosine(encode(left.get(field, "")), encode(right.get(field, "")))
    features.append(1.0 if left.get("postcode") == right.get("postcode") else 0.0)
    return features


class EmbeddingMatcher:
    """Logistic head over cosine-similarity features."""

    def __init__(self, weights: Sequence[float] = (1.4, 1.1, 0.9, 0.6), bias: float = -1.2) -> None:
        self.weights = list(weights)
        self.bias = bias

    def probability(self, features: Sequence[float]) -> float:
        score = self.bias + sum(w * f for w, f in zip(self.weights, features))
        return 1.0 / (1.0 + math.exp(-score))

    def match(self, left: Dict[str, str], right: Dict[str, str], threshold: float = 0.5) -> bool:
        return self.probability(featurise(left, right)) >= threshold


def train(pairs: List[Dict[str, str]], labels: Sequence[int], epochs: int = 50) -> EmbeddingMatcher:
    """Placeholder gradient fit used by the benchmark harness."""
    matcher = EmbeddingMatcher()
    for _ in range(epochs):
        for pair, label in zip(pairs, labels):
            error = label - matcher.probability(featurise(pair["left"], pair["right"]))
            matcher.bias += 0.01 * error
    return matcher
