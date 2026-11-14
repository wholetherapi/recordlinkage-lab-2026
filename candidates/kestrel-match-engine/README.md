# Kestrel Match Engine

Link records that refer to the same person across regions.

## Overview

Kestrel Match Engine compares records coming from CRM, billing and support exports and
returns a scored decision for each candidate pair. The package ships
blocking, normalisation and survivorship helpers that fit the usual master
data pipeline, together with a small CLI for batch runs.

## Quick start

```bash
pip install -r requirements.txt
python -m kestrel_match_engine.matcher --input pairs.jsonl --output decisions.jsonl
```

## Layout

- `src/kestrel_match_engine/` - library source
- `tests/` - unit tests
- `results/` - benchmark snapshots
- `docs/` - design notes

## How it works

Kestrel Match Engine ingests candidate pairs after blocking and returns clusters of records
that refer to the same entity. The pair model and the clustering strategy are
described in [docs/design.md](docs/design.md); the Python package exposes a
single `resolve()` entry point and a CLI for batch runs.

## Benchmark

Latest numbers are stored under `results/benchmark.md`.

## License

Internal evaluation copy - not for redistribution.
