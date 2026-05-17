# Retraction-Precedent Log Protocol

This document specifies the format and threshold protocol for retraction-precedent logs maintained per reader repo. The retraction log bounds discipline-codification latency by catching recurring anti-default patterns at the 3rd occurrence rather than the 5th-or-later.

## Where the log lives

- **Protocol specification:** this file at `atu-method/docs/retraction-log-protocol.md`
- **Per-repo logs:** `<reader-repo>/retraction-log.md` at repo root, tracked in git

Rationale for repo-root + tracked: discipline-propagation across siblings is manual. A tracked log file means new clones inherit the log; sibling-repo Claudes can grep across siblings; the codification trigger is visible to anyone reviewing the repo.

## Log entry format

Each retraction is a structured block under a `## Retractions` H2 section, chronological, append-only:

```
### YYYY-MM-DD — short title
- **Factor:** A | B | C | structural
- **Sub-pattern:** specific named anti-default (e.g., "grammatical-pattern smuggling," "spot-check confirmation," "punctuation-as-evidence," "producer-style framing")
- **What was retracted:** one-sentence description of the constraint / closed-list / scope claim withdrawn
- **What surfaced it:** Stan correction / adversarial audit / spot-check / cascade revert (cite specifically)
- **Reference:** commit hash that retracted; canon §X if applicable
```

No prose narration around entries. The compact format is the discipline.

## Threshold protocol

When **3 retractions share the same factor AND the same sub-pattern**, the sub-pattern is **promoted**:

1. The sub-pattern is named explicitly in [`atu-method/memories/feedback_three_anti_default_factors.md`](../memories/feedback_three_anti_default_factors.md) under its factor; if substantial enough, a dedicated memory file is created and indexed.
2. A corresponding rule-proposal gate refinement is added to [`atu-method/memories/feedback_rule_proposal_gates.md`](../memories/feedback_rule_proposal_gates.md) if the sub-pattern reveals a check the existing gates don't catch.
3. The promotion is recorded as a `## YYYY-MM-DD — DISCIPLINE PROMOTED — <sub-pattern name>` block at the top of the log, citing the 3 triggering retractions.

## What counts as a retraction

- A proposed constraint withdrawn before commit (after audit catches the failure)
- A committed constraint later reverted
- A closed-list extension removed
- A scope or precedence claim narrowed or retracted
- A cascade reverted due to canon-misapplication
- A producer-style framing reframed as a constraint (the original framing is retracted)

Does NOT count: typo fixes; formatting cleanups; mechanical-implementation refinements that don't retract a claim; file moves.

## Cross-corpus propagation

When a sub-pattern promotes on one repo's log, the discipline propagates to all sibling repos via the shared `feedback_three_anti_default_factors.md` and `feedback_rule_proposal_gates.md` files. Sibling repos do NOT duplicate the discipline — they inherit it via the shared memory references.

Sibling logs may cite each other's retractions when the pattern is genuinely shared: the GNT log's "grammatical-pattern smuggling" retractions count toward the same 3-strike threshold as Tanakh's, when they share the sub-pattern. The 3 strikes need not all come from one repo.

## Operational notes

- The log is append-only. Entries are never edited after commit; if a retraction is later determined to have been wrong, a new entry SHOULD be added documenting the re-evaluation, rather than altering the original.
- The discipline-codification latency the log targets is real and observable. Sub-patterns that recurrent ≥3 times without being named accumulate development cost out of proportion to their individual instance cost.
- Logging a retraction is itself audit-skippable per `change-protocol.md` §7.4 (defensibility-capture; the retraction event was prior).
