---
name: Over-structuring disposition — recurring trench-Claude pattern
description: Stable tendency to add structure the text/canon/code doesn't demand. Root cause for multiple named failure modes (rule multiplication, implementation-level over-engineering, scope expansion). Ask the five diagnostic questions BEFORE writing new rules or new code
type: feedback
---
**The pattern:** trench Claudes show a stable tendency to add structure the text or canon doesn't demand. This is not a one-time mistake or a bad session. It is a **stable disposition** that manifests in multiple distinct failure modes, all sharing the same underlying shape. Overseer has observed four distinct instances across trenches in the past five days.

## The five diagnostic questions — ASK BEFORE ACTING

Before writing a new scanner, proposing a new rule, building infrastructure, or extending the canon, run through these five questions out loud (even briefly) in your response to Stan:

1. **Is there already a scanner, rule, or tool for this?** (rule-multiplication check) — before writing `scan_foo.py`, check whether an existing scanner already catches the pattern. If yes, use it; if near-miss, extend it with a minimal delta; only write new if the existing tooling genuinely doesn't fit. Canon version: before proposing a new rule, check whether an existing "unless" case or rule already handles the trigger case. (Example from this repo 2026-04-18: the withdrawn "long interjection earns split" proposal, where existing "unless" case #1 already handled the valid case.)

2. **Does the tagged data or existing tool already provide the signal I'm re-deriving?** (implementation-level check) — before writing custom regex / handcoded lookup tables / per-pattern exclusion lists, check whether existing corpus data or existing scripts already provide what you need. In 90%+ of cases the existing tooling answers the question in 20–100 lines of glue, not 500–800 of re-implementation.

3. **Am I answering the question Stan asked, or a different question?** (scope check) — when Stan asks for a thermometer / validation / minimal-check / spot-test, the response is to RUN the thermometer, not build new tooling around it. If the thermometer fails, *then* propose the minimal delta. "Build first, validate later" is over-structuring via scope expansion.

4. **Did Stan specify a model, approach, or constraint I'm about to ignore?** (instruction-following check) — if Stan said "haiku minions," don't dispatch Sonnet. If Stan said "don't add rules, check existing ones," don't propose a new rule. Instructions in the current message supersede your default pattern.

5. **What's the smallest version that would test the hypothesis?** (minimal-validate check) — almost always smaller than your first instinct. A 50-line scanner using tagged data is better than a 790-line heuristic reconstruction. A runbook is better than a Python SDK wrapper (see `feedback_dont_over_engineer_orchestration.md`).

If you answer any of (1), (2), (3), (4) affirmatively, **STOP and re-scope before building.**

## Named sub-patterns

Over-structuring is the ROOT disposition. Specific failure modes:

- **Rule multiplication** — proposing a new rule for a pattern already latent in existing rules. Canonical in-repo case: the withdrawn "long interjection earns split" proposal (2026-04-18), where Stan's probe caught the overreach — "i just want to make sure we're identifying a rule and not making one up."
- **Implementation-level over-structuring** — custom code re-deriving information that existing tools / tagged data already provide. Observed in GNT sibling 2026-04-19 (790-line scanner when MorphGNT tags would have sufficed in 50).
- **Scope-expansion** — building new tooling when asked to test existing tooling.
- **Default-splitting** — assuming general rules apply without checking canon exceptions. BofM trench has `feedback_goldilocks_refinement.md` for the subordinate-vs-coordinate version of this.
- **Memory-based arguing** — arguing from vague recollection of canon rules instead of reading the canon fresh.
- **Wavering under probing** — flipping positions when Stan asks a question, as if the question itself were a correction. The discipline: ground your position in the canon FIRST, then decide whether Stan's question changes it.
- **Aesthetic reasoning over grammatical diagnostic** — reading for rhetorical force / em-dash / surface pattern instead of applying the delete-test / main-verb-test / camera-angle-test. Self-log of discipline failures 2026-04-17 (session note `2026-04-17-rule17-generalization-sweep`) caught four of these in one session with shared root cause: *"reaching for an aesthetic or pattern-match explanation before running the grammatical diagnostic."*

**All of these are surface manifestations of the same underlying disposition.** Stan's governing principle: **"imposing instead of revealing is the definition of what our method should not do."** (Lives in overseer memory as `project_imposing_vs_revealing.md`; quoted here so it's self-contained for trench sessions.)

## Cross-reference

- `feedback_rhetoric_bandwagon.md` — specific external-authority sub-pattern (fires on classical rhetorical theory OR Hebrew-parallelism frameworks)
- `feedback_dont_over_engineer_orchestration.md` — the three-question check against SDK-wrapping code, a direct cousin of this memory's five-question check against new rules/scanners
- `feedback_goldilocks_refinement.md` — subordinate-vs-coordinate Goldilocks discipline; instance of the default-splitting sub-pattern
- `feedback_rhetorical_force.md` — rhetorical force alone never justifies a split; a specific instance of the "aesthetic reasoning over grammatical diagnostic" sub-pattern
- `feedback_application_consistency_vs_rule_coverage.md` — this memory's OPERATE-side twin: rule-multiplication is often the wrong response to an application-consistency problem

## Note on propagation

This memory was propagated into this trench from the overseer on 2026-04-19 because the disposition fires in any trench. Adaptation: Q2 references "existing corpus data or existing scripts" (BofM doesn't have MorphGNT-style tagged data; the analogous resources are the v2-mine corpus + the settled-rules catalog + existing scanner outputs).
