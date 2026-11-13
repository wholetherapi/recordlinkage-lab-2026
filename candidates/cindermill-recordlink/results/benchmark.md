# Benchmark snapshot

| Dataset | Pairs | Precision | Recall | F1 |
|---------|-------|-----------|--------|----|
| internal-crm-2026 | 18,400 | 0.93 | 0.88 | 0.90 |
| billing-merge-2026 | 9,120 | 0.95 | 0.84 | 0.89 |
| partner-sample-2026 | 4,700 | 0.91 | 0.86 | 0.88 |

Run with `python -m cindermill_recordlink.matcher --input <pairs.jsonl>`.
