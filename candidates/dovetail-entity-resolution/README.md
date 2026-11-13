# Dovetail Entity Resolution

Unify partner records before they reach the warehouse.

## Overview

Dovetail Entity Resolution compares records coming from CRM, billing and support exports and
returns a scored decision for each candidate pair. The package ships
blocking, normalisation and survivorship helpers that fit the usual master
data pipeline, together with a small CLI for batch runs.

## Quick start

```bash
pip install -r requirements.txt
python -m dovetail_er.matcher --input pairs.jsonl --output decisions.jsonl
```

## Layout

- `src/dovetail_er/` - library source
- `tests/` - unit tests
- `results/` - benchmark snapshots
- `docs/` - design notes

## Status

🚧 **To be released.** This repository will contain the reference
implementation of Dovetail Entity Resolution. The code is currently under internal review and
will be published here once that review is complete. Coming soon.

## Planned design

When released, Dovetail Entity Resolution will ship a Rule-based matcher: declarative
normalisation and field-comparison rules with configurable thresholds, plus a
small survivorship layer for golden-record selection. There are no learned
components in the planned scope.

## Repository layout (planned)

- `data/` - sample record pairs (to be added)
- `src/` - package source (placeholder only)
- `tests/` - test suite (placeholder only)
- `results/` - benchmark output (to be added)
