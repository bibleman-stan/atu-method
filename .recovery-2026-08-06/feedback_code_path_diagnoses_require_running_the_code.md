---
name: code-path-diagnoses-require-running-the-code
description: "Before naming any file:line as a bug-locus or design-locus, the turn MUST contain a fresh Read of that range AND a Grep of the containing file for analogous canonical helpers AND (for control-flow claims) an executed probe that observes the claimed firing. Static read + plausible inference is NOT verification. Discovered 2026-06-04: 4 consecutive §7.3 audits rejected proposals on the same shape — wrong line, wrong file, wrong gating order, parallel detector when canonical helper existed."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/9cc4375571f3865d@v3`); state as of 2026-06-04 (snapshot mtime); possibly stale — re-verify before relying.

**The rule.** A code-path diagnosis ("rule R at file F line N is the bug-locus / will fire on this case / governs this verse class") is a STATE-CLAIM about the live source tree with the same status as external-artifact claims under standing default #8. It requires fresh in-turn verification on three axes:

1. **`Read` the cited range in THIS turn**, not from memory. A 40-line window minimum (the cited line + the gating context that determines reachability).
2. **`Grep` the containing file for analogous helpers** before proposing a new detector / new rule / new exclusion. The canonical helpers `_is_copular_independent_predication`, `_has_finite`, `_has_own_subject`, `_detect_stack_leaders` etc. are easy to miss when reading top-down. If a helper with a related name exists, the proposal MUST cite it and explain why a new one is needed.
3. **For control-flow claims, RUN A PROBE** — `python -c`, `pytest -k`, or inline-instrumented re-execution that observes the rule actually firing on the target verse. Static read + "R should fire here because the function looks like it should" is the failure mode that produced the four-audit-loss session.
4. **Identify the LIVE INPUT FILE before reasoning about behavior.** A proposal grounded in the wrong-layer file is moot before any audit runs.

**Live-input-file pins (do not re-derive from memory):**

| Corpus | Live fabric reads | NOT (wrong layer) |
|---|---|---|
| BoFM | `data/parses/v0-cache-conllu/<book>.conllu` (lever-2-LLM-corrected) | `data/parses/ensemble/stanza/<book>.conllu` (raw Stanza ensemble) |
| Tanakh | `data/text-files/v2/heb/` + BHSA via TF | (no second wrong-layer trap documented) |
| GNT | `data/text-files/v1.5/grk/` + Macula at `readers-gnt/research/macula-greek/SBLGNT/lowfat/` | `biblical-corpora/.../sblgnt-lowfat/xml/` (lacks rich cltype/rule/role attributes per Pipeline B finding) |

**Why this rule exists — 2026-06-04 session failures.** Four consecutive §7.3 audits all returned `needs-revision` on the same shape — proposals written from MENTAL MODELS of the code rather than from RUNNING the code. Concrete failures:

- **Audit 1 (cleft-conjunct proposal):** proposed fix at `bofm_v1_fabric.py:555`. Actual gate was line 529, which filtered the verse's NOUN-headed conj token before line 555 ever ran. Existing canonical helper `_is_copular_independent_predication` at line 229 was the right path; the proposal designed a parallel detector. *Diagnosis was inferred from a top-down read; never Grep-checked for analogous helpers; never ran code to observe which gate filtered the token.*

- **Audit 2 (purpose-`that` proposal):** proposal cited `data/parses/ensemble/stanza/alma.conllu` — the deployed pipeline reads `data/parses/v0-cache-conllu/alma.conllu`. In the corrected parse, T20 `healed` is `advcl head=12 casting`, not the `acl:relcl head=15 eyes` the proposal argued against. The proposal's central claim was moot. *Diagnosis was grounded in the wrong-layer parse file; never confirmed which parse the live fabric reads.*

- **Audit 2 (continued):** proposal asserted *"fabric line 354-355 says purpose/result `that` BREAKS per canon R6/R7"* — fabrication; R6/R7 BREAK was REPEALED, the comment at the cited lines explicitly says it manufactured 338 stranded "that" fragments and now binds. *Diagnosis was inferred from a paraphrased recollection of the fabric, never Read-verified.*

- **Audit 2 (continued):** *"comma-T21 hypothesis was topologically impossible. The comma sits between T20 and T22, not between T15 and T16. I invented a mechanism that can't exist."* *Diagnosis was a fabricated structural mechanism with no parse-evidence anchor.*

- **Audit 3 (coordinate-VP-elision proposal):** targeted wrong file entirely (`bofm_v1_fabric.py` instead of `bofm_generate.py`); real cause was `_detect_stack_leaders` deprel filter. The auditor monkey-patched the function to return empty and confirmed the verse rendered as one bound segment — concrete experimental verification I had not done. *Diagnosis was inferred without running the generator.*

- **Audit 4 (framework refinement v2):** cited a 0-byte audit-output file as evidence; inverted a `framework.md:109` cross-reference. *Citation forge under embedded-citation pattern; never `wc -c`-checked.*

The orchestrator recognized the pattern after audit 1 returned but had ALREADY DISPATCHED audits 2/3/4 on proposals written in the same untested-mental-model pattern. The audit-token cost was already sunk.

**Trigger conditions (when this rule must fire as a pre-output check):**

- Any draft sentence of the shape `"<verb> at <file>:<line>"` where verb ∈ {fix, modify, extend, gate, filter, bind, break, fire, govern, target, reach}.
- Any draft sentence introducing a new helper / detector / exclusion / rule within a file that already has analogous helpers.
- Any reasoning about "which rule fires on verse V" or "why fabric R didn't bind clause C".
- Any draft proposal headed for §7.3 audit dispatch.

If matched and the turn does NOT contain Read + Grep + Run for each cited locus: the proposal does NOT get sent to a §7.3 audit. It gets rewritten or abandoned. Dispatching an audit on an unverified proposal is the failure mode the 2026-06-04 four-audit-loss episode exhibited.

**Framework-first ordering (proposal-authoring discipline).** When a proposal cites a framework.md (or other paper-cited canon) rule as warrant, the proposal MUST lead with the operative-word analysis of that rule BEFORE writing code. Concretely: §0 quotes the canon line verbatim with `file:line`, identifies the operative words (e.g., framework.md:112 = "**coordinate** indicative **complement/appositive** clauses"), and explains how the proposed mechanism keys on those exact words. Code blocks come AFTER this analysis, not before. Cost of skipping it: 2026-06-04 stack-leaders cycle took three iterations (v1 → v2 → v3) to land on the "coordinate" interpretation that framework.md:112 had already named verbatim. If v1 had led with "the operative word is **coordinate** — what does that mean structurally?" the matrix-walk (or equivalent) would have been the day-1 proposal. This isn't a separate rule — it's the natural order under rules #6 (consult prior work first) + #9 (Read + Grep + Run before code).

**Cross-pollination check (ship discipline).** Before shipping a fix, run the simulation against ALL audit-failed proposals in the immediate cluster, not just the one being fixed. A root-cause fix often resolves multiple symptom-proposals. 2026-06-04 example: the v3 `_detect_stack_leaders` fix subsumed BOTH the purpose-`that` symptom (audit-2) AND the coord-VP-elision symptom (audit-3) — the same stack-split was creating both. Verifying cross-pollination AFTER the cluster is too late; verifying it BEFORE ship is value-added in one Bash invocation.

**Aligns with:**
- `~/.claude/CLAUDE.md` standing default #5 (data/treebank-first for OWN reasoning — this file extends it from corpus data to the source tree)
- `~/.claude/CLAUDE.md` standing default #6 (consult prior work — applied at within-file granularity, not only cross-corpus)
- `~/.claude/CLAUDE.md` standing default #7 (verify empirically; §7.3 audit gate before code)
- `~/.claude/CLAUDE.md` standing default #8 (external-artifact state requires fresh verification — this file is the source-tree analog)
- `feedback_mechanical_first_for_own_review.md` (the same discipline applied to corpus data)
- `feedback_debug_trace_values.md` (trace value origin FIRST — same family)
- `feedback_never_skip_audit_gate.md` (the §7.3 gate catches the unrun proposal; this rule prevents the proposal from reaching the gate)
- `feedback_pre_output_checks.md` (gate #9 — the regex pre-output enforcement)
