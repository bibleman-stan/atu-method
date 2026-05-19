# Stage 1 canonical prompts

The three canonical Stage 1 prompts for ATU rendering per `../toolset-architecture.md` §Stage 1. Each prompt embodies the minimal rubric: bidirectional test + restrictive-relative binding + a small set of language-specific syntactic constraints + default KEEP-AS-IS. NO cognitive-unity gate. NO parallelism class adjudication. NO genre anchors as primary licenses.

Three Opus passes use the per-language prompt; agreement scoring across passes determines auto-apply (unanimous) vs editorial review (non-unanimous).

- [`minimal_rubric_hebrew.md`](minimal_rubric_hebrew.md) — for Tanakh
- [`minimal_rubric_eme_english.md`](minimal_rubric_eme_english.md) — for BoFM
- [`minimal_rubric_koine_greek.md`](minimal_rubric_koine_greek.md) — for GNT (and LXX when ported)

## Per-corpus deployment

Per-repo pipelines copy or symlink the relevant prompt to their `scripts/atu_pipeline/prompts/` directory. The atu-method version is canonical; per-repo copies may add corpus-specific calibration items but should NOT modify the rubric's structural discipline (no cognitive-unity gate, no parallelism categories, no genre anchors).

## Versioning

These are v1 prompts based on the 2026-05-17 empirical validation (cross-tier × cross-genre study). Refinements based on production rendering experience get codified per the change protocol (`../change-protocol.md`).
