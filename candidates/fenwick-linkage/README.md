# Fenwick Linkage

Resolve entities across sources without pairwise thresholds.

## Overview

Fenwick Linkage compares records coming from CRM, billing and support exports and
returns a scored decision for each candidate pair. The package ships
blocking, normalisation and survivorship helpers that fit the usual master
data pipeline, together with a small CLI for batch runs.

## Quick start

```bash
pip install -r requirements.txt
python -m fenwick_linkage.matcher --input pairs.jsonl --output decisions.jsonl
```

## Layout

- `src/fenwick_linkage/` - library source
- `tests/` - unit tests
- `results/` - benchmark snapshots
- `docs/` - design notes

## How it works

Fenwick Linkage ingests candidate pairs after blocking and returns clusters of records
that refer to the same entity. The pair model and the clustering strategy are
described in [docs/design.md](docs/design.md); the Python package exposes a
single `resolve()` entry point and a CLI for batch runs.

## Benchmark

Latest numbers are stored under `results/benchmark.md`.

## License

Internal evaluation copy - not for redistribution.
