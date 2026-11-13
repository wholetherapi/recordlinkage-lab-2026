# Bellwether Dedupe

Fast duplicate detection for CRM and billing exports.

## Overview

Bellwether Dedupe compares records coming from CRM, billing and support exports and
returns a scored decision for each candidate pair. The package ships
blocking, normalisation and survivorship helpers that fit the usual master
data pipeline, together with a small CLI for batch runs.

## Quick start

```bash
pip install -r requirements.txt
python -m bellwether_dedupe.matcher --input pairs.jsonl --output decisions.jsonl
```

## Layout

- `src/bellwether_dedupe/` - library source
- `tests/` - unit tests
- `results/` - benchmark snapshots
- `docs/` - design notes

## Method

Bellwether Dedupe is driven by a declarative rule set. Normalisers, blocking keys and
field-level comparison rules are declared in `rules/`, and each rule
contributes a weighted score to the pair total. A pair is accepted when the
aggregate score crosses the configured threshold. This is a Rule-based
matching design: there are no learned parameters and every decision can be
traced back to a rule in the rule file.

## Benchmark

Latest numbers are stored under `results/benchmark.md`.

## License

Internal evaluation copy - not for redistribution.
