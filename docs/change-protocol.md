# Change Protocol — §7 (Operational)

**This document is the canonical statement of the change protocol for ATU canons.** It supersedes per-repo §7 sections, which become one-line pointers to this document. Sections below are the authoritative specification; framework.md §7 is now a one-line pointer here.

The protocol governs: when a canon change requires hostile audit; what audit-evidence must appear in the commit message; how the commit-msg gate enforces compliance; the self-test, self-consistency audit trigger, and proposed-rule adoption protocol.

---


## §7.1 Authority

This document is the authoritative specification of the framework, categories, and change protocol. Per-corpus canons reference this document by stable section ID. They MUST NOT inline framework prose.

## §7.2 Proposal requirements

Proposals to change an existing rule, add a new rule, or retire a rule MUST:

1. **State the target-language syntactic fact.** Cite the UD label and traditional-grammar vocabulary. If no such fact can be cited, the proposal is insufficient.
2. **Provide corpus evidence.** Worked examples from the actual text — not hypotheticals.
3. **Survive adversarial audit** (when any mandatory-audit trigger fires; see §7.3).
4. **Apply uniformly.** If the rule fires in one place, run the validator or equivalent sweep to catch every instance. Sedimented inconsistency is the primary failure mode.
5. **Defensibility capture.** Every new rule, sub-rule, or merge-override added to the canon MUST carry three elements:
   - **WHY** — the editorial reason the rule exists.
   - **HOW WE KNOW** — corpus evidence + adversarial validation.
   - **SCOPE** — where the rule applies, where it doesn't, interaction with other rules.
   
   These elements live in the per-rule scholarship file (`scholarship/<rule-id>.md`), not in the operational canon entry.
6. **Re-evaluate deferred items when the rule-set changes.** Items previously classified as REVIEW-REQUIRED or deferred-editorial MUST be re-evaluated against the updated rule-set.
7. **Update the canon.** Per-change rationale (audit-dispatch evidence, retraction precedent, scope claim) lives in the commit message — the durable audit trail. The canon prose itself reads as the current method. Never edit history silently.

## §7.3 Mandatory-audit triggers (12 categories)

For proposals matching ANY of the following triggers, an adversarial audit (hostile-agent dispatch or equivalent external skeptical review) MUST be dispatched and its findings reflected in the commit. Skipping audit on a triggered proposal is a protocol violation.

1. **New named rules / sub-clauses / categories** — including precedence cross-references between rules.
2. **Rule status promotions** — *proposed* → *settled*. Removes the hedge; stakes increase.
3. **Spot-check-based proposals** — any canon claim resting on less than full-corpus-sweep evidence.
4. **Reclassification of canon-recorded Category B/C items** — once recorded, subsequent sessions cannot silently reclassify under a different rule-framing.
5. **Rule deletions or SCOPE narrowings that retire live applications** — retiring a rule is as high-stakes as adding one.
6. **Mechanical signature / validator changes under settled rules** — adding a verb class, refining a UD trigger, changing validator conditions silently expands or contracts rule coverage.
7. **Corpus sweeps ≥5 instances under a settled rule** — the collective scope-claim needs audit even when individual instances are Category A.
8. **Canonical example additions to settled rules** — examples shape rule interpretation.
9. **Meta-rule changes to §7 Change Protocol itself.**
10. **Discipline-shifting memory file additions** — new memory files that shape how the apparatus is operated are behaviorally-governing.
11. **Cross-project imports or recoveries from retired canon** — provenance from a sibling project or older version is not validation; the imported claim MUST have target-corpus evidence independent of its source.
12. **Corpus-fit verification — post-codification AND post-detection.**
    - **(a) Post-codification.** When a new rule, sub-clause, or named pattern is codified, the rule is **not "closed" until a corpus-wide goal-fit audit has confirmed** (i) all eligible instances conform OR (ii) all residuals are explicitly enumerated. Codifications based on partial-corpus evidence are vulnerable to undercount.
    - **(b) Post-detection.** This trigger ALSO fires when an existing (settled) rule's violation is detected. Application drift accumulates on long-codified rules. Schedule same-rule full-corpus re-sweep within the same session or as the next session's first task. Goal-fit failures cluster — finding one of a shape elsewhere is the predictable outcome of partial-sweep history.

**Audit dispatch — parallel by default.** When a proposal triggers multiple audit dimensions, dispatch all in a single message with multiple agent calls. Sequential only when audit A's verdict determines whether audit B should run.

## §7.4 Audit-skippable categories

All of the following MUST hold for a proposal to bypass audit:

- Category A mechanical corpus edits per already-codified rules (sweep-scale ≥5 still triggers #7 regardless).
- Typo fixes; cross-reference updates that don't assert precedence; internal formatting cleanups.
- Deletions of items already reverted in the same session (audit-trail cleanup).
- Defensibility-capture additions (WHY/HOW WE KNOW/SCOPE) to already-settled rules **without changing the rule's scope**.

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
4. Did this session codify a new rule or named pattern, AND has the corpus-fit sweep NOT yet been run on the full corpus? → run goal-fit + application-consistency audits before commit, OR enumerate residuals in the session's pending file as next-session FIRST item.
5. If no to all four → probably skip-safe.

## §7.7 Self-consistency audit trigger

When a session adds ≥2 new canon subsections, rules, or merge-overrides, run a light self-consistency audit before wrap:

- All new cross-references resolve.
- No new rule contradicts an existing rule.
- All three defensibility elements (WHY / HOW WE KNOW / SCOPE per §7.2) are captured for each addition (in the scholarship companion, not the canon).

Short pass; catches stale cross-refs and incompatibilities cheaply.

## §7.8 Proposed-rule adoption protocol

A rule labeled *proposed* is a rule awaiting corpus verification. "Proposed" is a testable state, not a hedging license.

**Adoption criteria.** A proposed rule is adopted when its first corpus sweep produces **≥80% clean categorization** — 80%+ of matched instances resolve to unambiguous SPLIT or MERGE decisions without heuristic ambiguity. Ambiguous residue ≥20% signals the rule needs refinement before adoption.

**Sweep-then-decide workflow.**
1. Write validator implementing the rule's conditions.
2. Run against full corpus.
3. If clean ≥80% → apply clean decisions mechanically (Category A per §2), remove "proposed" label; capture the adoption evidence (sweep counts, audit verdicts) in the commit message.
4. If clean <80% → identify the ambiguity pattern, refine the rule with an explicit sub-clause, re-run.
5. Repeat until clean ≥80%, then adopt.

**Do not flag clean categorizations for per-item review.** A proposed rule whose conditions are met is as authoritative as an adopted rule on those specific instances; the "proposed" label only gates corpus-wide sweep confidence, not per-instance application.

---

