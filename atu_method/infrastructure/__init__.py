"""Pipeline infrastructure: transaction logging, applier scaffolding, dashboard, parity-test.

- tx_log: transaction-logged corpus mutations with rollback
- applier_base: shared scaffolding for char-offset-precise appliers (split/merge)
- dashboard: validator-suite runner with baseline-check
- parity: regex-vs-UD detector parity-test framework
- review_queue: REVIEW-item aggregator across detectors

Populated by extraction from readers-bofm/validators/.
"""
