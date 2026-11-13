"""Rule-based record comparison for Ashgrove Matcher."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

DEFAULT_RULES: Tuple["ComparisonRule", ...] = ()


@dataclass(frozen=True)
class ComparisonRule:
    """A single field-level comparison rule."""

    field: str
    weight: float
    normaliser: str = "lower"
    kind: str = "exact"


def _normalise(value: str, how: str) -> str:
    value = (value or "").strip()
    if how == "lower":
        return " ".join(value.lower().split())
    if how == "email":
        return value.lower().strip()
    if how == "phone":
        return re.sub(r"[^0-9]", "", value)
    if how == "postcode":
        return re.sub(r"\s+", "", value.upper())
    if how == "text":
        return " ".join(re.findall(r"[a-z0-9]+", value.lower()))
    raise ValueError(f"unknown normaliser: {how}")


def _jaccard(left: str, right: str) -> float:
    a, b = set(left.split()), set(right.split())
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def compare(left: str, right: str, rule: ComparisonRule) -> float:
    left = _normalise(left, rule.normaliser)
    right = _normalise(right, rule.normaliser)
    if rule.kind == "exact":
        return 1.0 if left == right else 0.0
    if rule.kind == "fuzzy":
        return _jaccard(left, right)
    raise ValueError(f"unknown comparison kind: {rule.kind}")


def score_pair(
    left: Dict[str, str],
    right: Dict[str, str],
    rules: Iterable[ComparisonRule] = DEFAULT_RULES,
) -> float:
    total = 0.0
    for rule in rules:
        total += rule.weight * compare(left.get(rule["field"], "") if isinstance(rule, dict) else left.get(rule.field, ""),
                                      right.get(rule["field"], "") if isinstance(rule, dict) else right.get(rule.field, ""),
                                      rule)
    return round(total, 6)


def decide(score: float, threshold: float = 0.72) -> bool:
    return score >= threshold


def load_rules(path: str) -> List[ComparisonRule]:
    import json

    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return [ComparisonRule(**item) for item in payload["rules"]]
