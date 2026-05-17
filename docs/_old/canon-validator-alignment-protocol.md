# Canon-Validator Alignment Protocol

This document specifies the **structural alignment check** that per-repo canon-validator alignment scripts MUST implement. The check is mechanical and structural-only — it verifies that what canon §5 entries *name* actually *exists* in the validator code. It does NOT verify semantic alignment (whether validator predicate logic implements the test the canon prose claims) — that would require formal verification and is out of scope.

Codified 2026-05-16 from the readiness-arc adversarial audit's finding that current canon-validator alignment is asserted rather than enforced; the audit identified per-repo structural alignment scripts as the right shape (small, repo-specific, runnable as CI gate) rather than one cross-corpus meta-validator (which would have to handle three divergent canon §5 formats).

## Why this exists

The 2026-05-16 canon-validator alignment audit (Q2) surfaced concrete divergences:

- **GNT R25** ships a 3-condition canon test; validator implements only condition 1. Structurally aligned (validator exists, named closed-lists present), substantively under-implementing 2/3 of the test.
- **GNT** has at least 8 Mechanical-class rules in §3 Rule Index carrying "not yet implemented" or "scanner only" annotations (R8, R9, R10, R12-14, R17, R22, R23). Canon-named, validator-absent.
- **Tanakh M1** ships a 7-pair `HEBREW_BONDED_PAIRS` closed list while canon names an 88-pair `BONDED_LEMMA_PAIRS` lexicon. Validator silently implements a subset of what canon names.

The structural check catches naming-vs-presence drift; it does NOT catch the GNT R25 under-implementation (that's semantic). Detecting the catchable subset uniformly across repos is the goal.

## What the check verifies (four classes)

For each rule entry in canon §5:

1. **Validator file presence.** The Implementation field's named validator path resolves to an actual file. If canon says `validators/colometry/validate_rule_17_ud.py` and the file doesn't exist, emit `NO_IMPL`.
2. **Closed-list presence.** Every closed-list named in the rule's UD signature or prose appears as a Python constant (uppercase identifier) in the named validator source file OR in shared modules under `validators/_shared/`. If canon names `GOVERNING_LEMMAS` and the constant is found nowhere, emit `DRIFT`.
3. **UD signature field consistency.** The deprels, UPOS values, and lemma sets named in the rule's UD signature YAML appear in the validator's query code (as string literals or constants). Mechanical check; does not interpret query semantics.
4. **Multi-valued field branches.** If the rule uses multi-valued field notation (`Layer: 1 (profile a) / 3 (profile b)`), every named branch has corresponding handling in the validator (named function, branch in conditional, etc.).

## Search-scope requirements

To avoid false-positive verdicts, per-repo alignment scripts MUST handle two scope cases the original spec did not enumerate. These were surfaced 2026-05-16 by the Tanakh implementation, which found that ~half the non-ALIGNED verdicts in its first run were false positives traceable to scope narrowness in these two dimensions.

### Search across `validators/_shared/` in addition to named-detector files

Many closed-list constants legitimately live in shared modules (`validators/_shared/*.py`) rather than in the named-detector source file. A constant found in any shared module counts as PRESENT for the closed-list-presence check. Scripts that grep only the named-detector file will report DRIFT verdicts for constants that legitimately exist in shared modules — this is a script-scope bug, not real drift.

Concrete example from Tanakh: H14's `DISCOURSE_PARTICLES` lives in `validators/_shared/morphology.py` (line 2784). The named detector file does not contain the constant directly; it imports from shared. An alignment script that searches only the named detector file will flag this as DRIFT — false positive.

### Parse inline-prose detector references in addition to YAML list-form

Some canon §5 entries name their validator via inline prose ("the detector at `validators/colometry/validate_speech_intro_framing.py` covers this") rather than in a structured YAML `detectors:` list field. Scripts that only parse YAML detector lists will report NO_IMPL for rules that have working validators with prose-form footers.

Concrete example from Tanakh: H5b and H15 both have working validators (`validate_speech_intro_framing.py`, `validate_clause_nucleus_split.py`) but their canon footers describe the detector inline, not in a list. The Tanakh alignment script flagged both as NO_IMPL — false positives.

### Implementation guidance

When implementing the alignment script:

- Validator file presence check: parse both YAML `Implementation:` blocks AND inline-prose detector path references in the rule entry body. Use a regex that matches `validators/[^\s]+\.py` patterns broadly.
- Closed-list presence check: search the named detector file FIRST, then fall back to a broader search across `validators/_shared/` and the rest of `validators/`. Only emit DRIFT if the constant is found nowhere.
- Cross-rule reference resolution: if a constant is found in another rule's validator file (because canon prose references it cross-rule), count it as PRESENT — not DRIFT for the rule whose entry names it.

The Tanakh implementation surfaced these patterns; BoFM and GNT implementations should adopt the same search scope to avoid the same false-positive class.

## Verdict taxonomy

For each rule entry, the script emits one of:

- `ALIGNED` — all four checks pass
- `NO_IMPL` — canon names a validator file that doesn't exist
- `DRIFT` — validator file exists but named closed-lists or UD signature fields are missing/divergent
- `PARTIAL` — validator file exists; some named branches/closed-lists present, others missing (multi-valued field case)
- `EDITORIAL_ACK` — canon entry explicitly declares `Applier: (none — <reason>)` (e.g., Category B editorial rules); the script does NOT flag this as failure

## What is OUT of scope

- **Semantic alignment.** "Does the validator's predicate logic actually implement what the canon prose says?" requires formal methods or extensive worked-example fixtures. Out of scope for this check.
- **Behavioral validation.** "Does the validator emit the right verdicts on the corpus?" is what `validators/run_all.py --baseline-check` does. Different check, different scope.
- **Cross-corpus consistency.** "Does R17 (BoFM) do the same thing as R10 (GNT) where the rule-equivalence map says they cluster?" — that's a cross-corpus question. See `rule-equivalence-map.md` for the map; cross-corpus consistency audits are a separate intervention.

## Output format

Each per-repo implementation emits a report — markdown or plain text — listing every §5 rule entry with its verdict and evidence:

```
R17 (Complement Integrity): ALIGNED
R25 (ὥστε short-consecutive-result): PARTIAL — closed-list HOSTE_LEMMAS present; conditions 2-3 from canon prose have no corresponding branch in validator (lines 11-19 self-declare semantic-only handling)
R8 (Framing devices): NO_IMPL — canon §3 lists R8; no validate_rule_08_ud.py exists in validators/colometry/
EP-1 (according-to manner vs source): EDITORIAL_ACK — Applier: (none — Category B / editorial-judgment rule)
H1 (Maqqef-group): ALIGNED
M1 (Bonded pair): PARTIAL — validator HEBREW_BONDED_PAIRS has 7 pairs; canon §5 names 88-pair BONDED_LEMMA_PAIRS lexicon as reference-only / dormant — script flags this for explicit Stan decision
```

Sort by verdict severity: NO_IMPL first, then DRIFT, then PARTIAL, then EDITORIAL_ACK, then ALIGNED (the aligned cases are the long tail and don't need to be at the top).

## Per-repo implementation guidance

Each repo writes its own short structural-alignment script targeting its own canon §5 format. Don't try to write one cross-corpus parser — the three canons' §5 formats genuinely diverge, and per-repo scripts can be small (~50-150 lines).

Suggested locations:

- BoFM: `validators/canon/check_canon_alignment.py`
- GNT: `validators/canon/check_canon_alignment.py`
- Tanakh: `validators/canon/check_canon_alignment.py` — Tanakh already has a meta-validator precedent at `validate_canon_retirement_residue.py`; the new alignment check can sit alongside it

Run as part of `run_all.py` or as a standalone CI gate. Output to stdout (so it lands in the commit-msg hook's audit-evidence flow) or to a `validators/.canon-alignment.md` baseline file (so divergences are visible in PRs).

## Threshold protocol

The script reports findings; it does NOT auto-act on them. Per the retraction-log protocol at [`retraction-log-protocol.md`](retraction-log-protocol.md), divergences logged across runs that recur N times under the same factor become candidates for canon revision or validator implementation work.

For the first run on each repo: surface findings to Stan. Per-rule judgment calls on what to do with each NO_IMPL / DRIFT / PARTIAL belong to Stan, not to the script.

## Tanakh's existing precedent

`readers-tanakh/validators/colometry/validate_canon_retirement_residue.py` is the structural-precedent meta-validator. It scans canon prose for references to retired rules (factor: catch when canon and apparatus drift). The alignment check is a generalization — same shape (scan canon, scan validator code, compare), different target (naming/presence vs retirement-residue). New implementations should follow that precedent.

## Codification

Specified 2026-05-16. The audit identified this as item 3 of the restructured readiness arc. Per-repo implementations are deferred to per-repo work (each reader-repo Claude implements its own script against this spec when engaged for its readiness-arc per-repo items).
