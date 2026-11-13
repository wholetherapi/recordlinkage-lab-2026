# Oakhurst Linker

Collective entity resolution for shared-identity graphs.

## Overview

Oakhurst Linker compares records coming from CRM, billing and support exports and
returns a scored decision for each candidate pair. The package ships
blocking, normalisation and survivorship helpers that fit the usual master
data pipeline, together with a small CLI for batch runs.

## Quick start

```bash
pip install -r requirements.txt
python -m oakhurst_linker.matcher --input pairs.jsonl --output decisions.jsonl
```

## Layout

- `src/oakhurst_linker/` - library source
- `tests/` - unit tests
- `results/` - benchmark snapshots
- `docs/` - design notes

## Status

🚧 **To be released.** This repository will contain the reference
implementation of Oakhurst Linker. The code is currently under internal review and
will be published here once that review is complete. Coming soon.

## Planned design

When released, Oakhurst Linker will ship a Graph-clustering-based resolver: candidate
pairs become weighted edges in a similarity graph and records are assigned to
clusters collectively with correlation clustering, rather than by a fixed
pairwise threshold. The clustering layer is the core of the planned scope.

## Repository layout (planned)

- `data/` - sample record pairs (to be added)
- `src/` - package source (placeholder only)
- `tests/` - test suite (placeholder only)
- `results/` - benchmark output (to be added)
