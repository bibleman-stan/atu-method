# Canon-Validator Alignment Protocol

This document specifies the structural alignment check that per-repo canon-validator alignment scripts MUST implement. The check is mechanical and structural-only — it verifies that what canon §5 constraint entries *name* actually *exists* in the audit-stage validator code. It does NOT verify semantic alignment (whether validator predicate logic implements the test the canon prose claims) — that would require formal verification and is out of scope.

## What the check verifies (four classes)

For each constraint entry in canon §5:

1. **Validator file presence.** The Implementation field's named validator path resolves to an actual file. If canon says `validators/syntax/validate_restrictive_relative.py` and the file doesn't exist, emit `NO_IMPL`.
2. **Closed-list presence.** Every closed-list named in the constraint's encoded-question or prose appears as a Python constant (uppercase identifier) in the named validator source file OR in shared modules under `validators/_shared/`. If canon names `DISCOURSE_PARTICLES` and the constant is found nowhere, emit `DRIFT`.
3. **Encoded-question field consistency.** The deprels, UPOS values, and lemma sets named in the constraint's encoded-question YAML appear in the validator's query code (as string literals or constants). Mechanical check; does not interpret query semantics.
4. **Multi-valued field branches.** If the constraint uses multi-valued field notation (`Layer: 1 (profile a) / 3 (profile b)`), every named branch has corresponding handling in the validator (named function, branch in conditional, etc.).

## Search-scope requirements

To avoid false-positive verdicts, per-repo alignment scripts MUST handle two scope cases.

### Search across `validators/_shared/` in addition to named-detector files

Many closed-list constants legitimately live in shared modules (`validators/_shared/*.py`) rather than in the named-detector source file. A constant found in any shared module counts as PRESENT for the closed-list-presence check. Scripts that grep only the named-detector file will report DRIFT verdicts for constants that legitimately exist in shared modules — this is a script-scope bug, not real drift.

### Parse inline-prose detector references in addition to YAML list-form

Some canon §5 entries name their validator via inline prose ("the detector at `validators/syntax/validate_speech_intro_framing.py` covers this") rather than in a structured YAML `detectors:` list field. Scripts that only parse YAML detector lists will report NO_IMPL for constraints that have working validators with prose-form footers.

### Implementation guidance

When implementing the alignment script:

- **Validator file presence check**: parse both YAML `Implementation:` blocks AND inline-prose detector path references in the constraint entry body. Use a regex that matches `validators/[^\s]+\.py` patterns broadly.
- **Closed-list presence check**: search the named detector file FIRST, then fall back to a broader search across `validators/_shared/` and the rest of `validators/`. Only emit DRIFT if the constant is found nowhere.
- **Cross-constraint reference resolution**: if a constant is found in another constraint's validator file (because canon prose references it cross-constraint), count it as PRESENT — not DRIFT for the constraint whose entry names it.

## Verdict taxonomy

For each constraint entry, the script emits one of:

- `ALIGNED` — all four checks pass
- `NO_IMPL` — canon names a validator file that doesn't exist
- `DRIFT` — validator file exists but named closed-lists or encoded-question fields are missing/divergent
- `PARTIAL` — validator file exists; some named branches/closed-lists present, others missing (multi-valued field case)
- `EDITORIAL_ACK` — canon entry explicitly declares `Applier: (none — <reason>)` (e.g., Category B editorial constraints); the script does NOT flag this as failure

## What is OUT of scope

- **Semantic alignment.** "Does the validator's predicate logic actually implement what the canon prose says?" requires formal methods or extensive worked-example fixtures. Out of scope for this check.
- **Behavioral validation.** "Does the validator emit the right verdicts on the corpus?" is what `validators/run_all.py --baseline-check` does. Different check, different scope.
- **Cross-corpus consistency.** "Does the Hebrew restrictive-`אֲשֶׁר` constraint do the same thing as the Greek restrictive-`ὅς` constraint where the equivalence map says they cluster?" — that's a cross-corpus question. See `rule-equivalence-map.md` for the map; cross-corpus consistency audits are a separate intervention.
- **Producer-vs-constraint framing.** Whether a validator implements producer-style or constraint-style logic is a separate architectural question, covered by the periodic architecture-method alignment check (`change-protocol.md` §7.9).

## Output format

Each per-repo implementation emits a report — markdown or plain text — listing every §5 constraint entry with its verdict and evidence:

```
Restrictive-Relative-Binding: ALIGNED
Gapped-Verb-Tolerance: PARTIAL — closed-list GAPPED_VERB_TRIGGERS present; conditions 2-3 from canon prose have no corresponding branch in validator
Discourse-Particle-Binding: NO_IMPL — canon names validator path that doesn't exist
Construct-Chain-Indivisibility: ALIGNED
Verbless-Clause-Closure: EDITORIAL_ACK — Applier: (none — Category B / editorial-judgment constraint)
```

Sort by verdict severity: NO_IMPL first, then DRIFT, then PARTIAL, then EDITORIAL_ACK, then ALIGNED.

## Per-repo implementation guidance

Each repo writes its own short structural-alignment script targeting its own canon §5 format. Don't try to write one cross-corpus parser — the three canons' §5 formats genuinely diverge, and per-repo scripts can be small (~50–150 lines).

Suggested locations:

- BoFM: `validators/canon/check_canon_alignment.py`
- GNT: `validators/canon/check_canon_alignment.py`
- Tanakh: `validators/canon/check_canon_alignment.py`

Run as part of `run_all.py` or as a standalone CI gate. Output to stdout (so it lands in the commit-msg hook's audit-evidence flow) or to a `validators/.canon-alignment.md` baseline file (so divergences are visible in PRs).

## Threshold protocol

The script reports findings; it does NOT auto-act on them. Per the retraction-log protocol at [`retraction-log-protocol.md`](retraction-log-protocol.md), divergences logged across runs that recur N times under the same factor become candidates for canon revision or validator implementation work.

For the first run on each repo: surface findings to Stan. Per-constraint judgment calls on what to do with each NO_IMPL / DRIFT / PARTIAL belong to Stan, not to the script.
