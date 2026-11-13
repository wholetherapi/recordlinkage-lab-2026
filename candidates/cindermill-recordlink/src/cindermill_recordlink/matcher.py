"""Probabilistic (Fellegi-Sunter) scoring for Cindermill Recordlink."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List


@dataclass(frozen=True)
class FieldModel:
    """m/u probabilities for a single field."""

    field: str
    m: float
    u: float


DEFAULT_MODEL: tuple[FieldModel, ...] = (
    FieldModel("email", 0.95, 0.02),
    FieldModel("phone", 0.90, 0.05),
    FieldModel("surname", 0.85, 0.30),
    FieldModel("postcode", 0.80, 0.10),
)


def agreement_weight(model: FieldModel) -> float:
    """log2(m/u) for an agreeing field."""
    if model.m <= 0 or model.u <= 0:
        raise ValueError("probabilities must be positive")
    return math.log2(model.m / model.u)


def disagreement_weight(model: FieldModel) -> float:
    """log2((1-m)/(1-u)) for a disagreeing field."""
    return math.log2((1.0 - model.m) / (1.0 - model.u))


def score_pair(
    left: Dict[str, str],
    right: Dict[str, str],
    model: Iterable[FieldModel] = DEFAULT_MODEL,
) -> float:
    score = 0.0
    for field in model:
        agree = left.get(field.field, "").strip().lower() == right.get(field.field, "").strip().lower()
        score += agreement_weight(field) if agree else disagreement_weight(field)
    return round(score, 6)


def estimate_parameters(pairs: List[Dict[str, str]]) -> List[FieldModel]:
    """Estimate m/u probabilities from labelled pairs.

    ``pairs`` must carry a boolean ``is_match`` key.  Smoothing is applied so
    the weights stay finite for small samples.
    """
    matches = [pair for pair in pairs if pair.get("is_match")]
    non_matches = [pair for pair in pairs if not pair.get("is_match")]
    if not matches or not non_matches:
        raise ValueError("both matched and non-matched pairs are required")
    result = []
    for field in DEFAULT_MODEL:
        m = sum(1 for pair in matches if pair.get(field.field)) / len(matches)
        u = sum(1 for pair in non_matches if pair.get(field.field)) / len(non_matches)
        result.append(FieldModel(field.field, max(m, 1e-3), max(u, 1e-3)))
    return result


def decide(score: float, threshold: float = 4.0) -> bool:
    return score >= threshold
