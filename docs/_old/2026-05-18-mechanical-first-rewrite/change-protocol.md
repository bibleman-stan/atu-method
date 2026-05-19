# Change Protocol — §7 (Operational)

This document is the canonical statement of the change protocol for ATU canons. Per-repo §7 sections are one-line pointers to this document.

The protocol governs: when a canon change requires hostile audit; what audit-evidence must appear in the commit message; how the commit-msg gate enforces compliance; the self-test, self-consistency audit trigger, and proposed-rule adoption protocol.

---

## §7.1 Authority

This document is the authoritative specification of the change protocol. Per-corpus canons reference this document by stable section ID. They MUST NOT inline protocol prose.

## §7.2 Proposal requirements

Proposals to change an existing constraint, add a new constraint, or retire a constraint MUST:

1. **State the target-language syntactic fact.** Cite the grammar authority (Joüon-Muraoka §X for Hebrew, Smyth §Y for Greek, etc.) and the encoded yes/no grammatical question the constraint answers. If no such fact can be cited, the proposal is insufficient.
2. **Provide corpus evidence.** Worked examples from the actual text — not hypotheticals. Both positive (constraint should fire) and negative (constraint should NOT fire).
3. **Survive adversarial audit** (when any mandatory-audit trigger fires; see §7.3).
4. **Apply uniformly.** If the constraint fires in one place, run the audit-stage sweep to catch every instance. Sedimented inconsistency is the primary failure mode.
5. **Defensibility capture.** Every new constraint, sub-constraint, or refinement added to the catalog MUST carry three elements:
   - **WHY** — the editorial reason the constraint exists.
   - **HOW WE KNOW** — corpus evidence + adversarial validation.
   - **SCOPE** — where the constraint applies, where it doesn't, interaction with other constraints.

   These elements live in the per-constraint scholarship file (`scholarship/<constraint-id>.md`), not in the operational catalog entry.
6. **Re-evaluate deferred items when the catalog changes.** Items previously flagged AMBIGUOUS or deferred-editorial MUST be re-evaluated against the updated catalog.
7. **Update the canon.** Per-change rationale (audit-dispatch evidence, retraction precedent, scope claim) lives in the commit message — the durable audit trail. The canon prose itself reads as the current method. Never edit history silently.

**Producer-style framing is forbidden.** Constraints answer yes/no grammatical questions about whether a proposed ATU break is licensed. Proposals framed as "split parallel clauses" or "merge synonymous cola" or "split at clause boundary X" describe producers, not constraints, and MUST be reframed before submission. See `rule-template.md` for the constraint-style template.

## §7.3 Mandatory-audit triggers (12 categories)

For proposals matching ANY of the following triggers, an adversarial audit (hostile-agent dispatch or equivalent external skeptical review) MUST be dispatched and its findings reflected in the commit. Skipping audit on a triggered proposal is a protocol violation.

1. **New named constraints / sub-clauses / categories** — including precedence cross-references between constraints.
2. **Constraint status promotions** — *proposed* → *settled*. Removes the hedge; stakes increase.
3. **Spot-check-based proposals** — any canon claim resting on less than full-corpus-sweep evidence.
4. **Reclassification of canon-recorded violation flags** — once recorded, subsequent sessions cannot silently reclassify under a different constraint framing.
5. **Constraint deletions or SCOPE narrowings that retire live applications** — retiring a constraint is as high-stakes as adding one.
6. **Audit-stage signature changes under settled constraints** — adding a verb class, refining a syntactic pattern, changing audit conditions silently expands or contracts constraint coverage.
7. **Corpus sweeps ≥5 instances under a settled constraint** — the collective scope-claim needs audit even when individual instances are unambiguous.
8. **Canonical example additions to settled constraints** — examples shape constraint interpretation.
9. **Meta-rule changes to §7 Change Protocol itself.**
10. **Discipline-shifting memory file additions** — new memory files that shape how the apparatus is operated are behaviorally-governing.
11. **Cross-project imports or recoveries from retired canon** — provenance from a sibling project or older version is not validation; the imported claim MUST have target-corpus evidence independent of its source.
12. **Corpus-fit verification — post-codification AND post-detection.**
    - **(a) Post-codification.** When a new constraint, sub-clause, or named pattern is codified, the constraint is **not "closed" until a corpus-wide goal-fit audit has confirmed** (i) all eligible instances conform OR (ii) all residuals are explicitly enumerated. Codifications based on partial-corpus evidence are vulnerable to undercount.
    - **(b) Post-detection.** This trigger ALSO fires when an existing (settled) constraint's violation is detected. Application drift accumulates on long-codified constraints. Schedule same-constraint full-corpus re-sweep within the same session or as the next session's first task. Goal-fit failures cluster.

**Audit dispatch — parallel by default.** When a proposal triggers multiple audit dimensions, dispatch all in a single message with multiple agent calls. Sequential only when audit A's verdict determines whether audit B should run.

## §7.4 Audit-skippable categories

All of the following MUST hold for a proposal to bypass audit:

- Mechanical corpus edits per already-codified constraints (sweep-scale ≥5 still triggers #7 regardless).
- Typo fixes; cross-reference updates that don't assert precedence; internal formatting cleanups.
- Deletions of items already reverted in the same session (audit-trail cleanup).
- Defensibility-capture additions (WHY/HOW WE KNOW/SCOPE) to already-settled constraints **without changing the constraint's scope**.

## §7.5 Audit-evidence in commit messages

Every commit message that touches a per-corpus canon MUST declare audit-status explicitly:

- `Audit-skippable per §7.3 ([reason])` with the reason citing one of §7.4 categories; OR
- `Audit dispatched: [evidence]` with concrete reference (parallel-agent verdicts, prior-commit pointer).

Omission is itself a discipline failure — visible at a glance in `git log`. The mechanical commit-msg gate detects extension patterns and requires an audit-evidence keyword; the explicit declaration is the editor-side discipline that front-loads (and complements) the gate.

## §7.6 Self-test before commit

Before committing a canon change, run the five-question self-test:

1. Does this change include a scope claim, a precedence claim, a closed-list extension, or a named-category carve-out? → audit.
2. Does this change rest on spot-check evidence rather than a full-corpus classification? → audit.
3. Does this change reclassify or delete previously-settled canon content? → audit.
4. Did this session codify a new constraint or named pattern, AND has the corpus-fit sweep NOT yet been run on the full corpus? → run goal-fit + application-consistency audits before commit, OR enumerate residuals in the session's pending file as next-session FIRST item.
5. Does this change re-frame a producer-style rule as a constraint, or vice versa? → audit. The producer-vs-constraint distinction is load-bearing for the architecture.
6. If no to all five → probably skip-safe.

## §7.7 Self-consistency audit trigger

When a session adds ≥2 new canon subsections, constraints, or refinements, run a light self-consistency audit before wrap:

- All new cross-references resolve.
- No new constraint contradicts an existing constraint.
- All three defensibility elements (WHY / HOW WE KNOW / SCOPE per §7.2) are captured for each addition (in the scholarship companion, not the canon).

Short pass; catches stale cross-refs and incompatibilities cheaply.

## §7.8 Proposed-constraint adoption protocol

A constraint labeled *proposed* is a constraint awaiting corpus verification. "Proposed" is a testable state, not a hedging license.

**Adoption criteria.** A proposed constraint is adopted when its first corpus sweep produces **≥80% clean categorization** — 80%+ of matched instances resolve to unambiguous BIND / SPLIT-CANDIDATE / MERGE / VIOLATION-FLAG decisions without heuristic ambiguity. Ambiguous residue ≥20% signals the constraint needs refinement before adoption.

**Sweep-then-decide workflow.**

1. Write the audit-stage implementation of the constraint.
2. Run against full corpus.
3. If clean ≥80% → apply clean decisions mechanically, remove "proposed" label; capture the adoption evidence (sweep counts, audit verdicts) in the commit message.
4. If clean <80% → identify the ambiguity pattern, refine the constraint with an explicit sub-clause, re-run.
5. Repeat until clean ≥80%, then adopt.

**Do not flag clean categorizations for per-item review.** A proposed constraint whose conditions are met is as authoritative as an adopted constraint on those specific instances; the "proposed" label only gates corpus-wide sweep confidence, not per-instance application.

---

## §7.9 Architecture-method alignment check

Periodic discipline: re-check that the as-built audit-stage implementations match what the catalog actually claims.

The risk: small defensible decisions accumulate over time. A constraint described as "is this break inside a construct chain?" can drift, in implementation, into a procedural rule that GENERATES split decisions. The drift is silent because each individual decision passed local scrutiny.

When an experiment produces an unexpected result, before refining the experiment, check whether the result reveals a constraint-vs-producer drift. Pattern signals:

- Audit-stage code that produces verdicts when the catalog says it should audit
- Catalog entries with verdict families that don't match the constraint's stated yes/no question
- Patches accumulating to make audit output match a desired rendering rather than to surface violations

The cost of unchecked drift: silent corpus pollution; contested results; cognitive overhead defending an architecture that doesn't match the catalog.

See `memories/feedback_architecture_must_match_method.md` for the full discipline.
