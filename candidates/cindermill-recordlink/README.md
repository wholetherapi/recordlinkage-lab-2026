# Cindermill Recordlink

Score record pairs with calibrated agreement weights.

## Overview

Cindermill Recordlink compares records coming from CRM, billing and support exports and
returns a scored decision for each candidate pair. The package ships
blocking, normalisation and survivorship helpers that fit the usual master
data pipeline, together with a small CLI for batch runs.

## Quick start

```bash
pip install -r requirements.txt
python -m cindermill_recordlink.matcher --input pairs.jsonl --output decisions.jsonl
```

## Layout

- `src/cindermill_recordlink/` - library source
- `tests/` - unit tests
- `results/` - benchmark snapshots
- `docs/` - design notes

## Approach

Cindermill Recordlink scores pairs with a Fellegi-Sunter style model. Each field carries an
m-probability (agreement given a match) and a u-probability (agreement given a
non-match); the pair score is the sum of log2(m/u) over agreeing fields. The
thresholds and the parameter table can be re-estimated from labelled pairs.
This is a Probabilistic-scoring-based design; every score is a log-likelihood
ratio and can be reviewed field by field.

## Benchmark

Latest numbers are stored under `results/benchmark.md`.

## License

Internal evaluation copy - not for redistribution.
