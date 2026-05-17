---
name: rule-proposal-gates
description: "Four-gate checklist run before any rule proposal, closed-list extension, scope claim, or precedence claim. Operationalizes the three anti-default factors plus the bidirectional atomic-thought test as mandatory pre-proposal checks. Bounds discipline-codification latency by catching factor-A/B/C failures before they enter the canon."
type: feedback
---

Before proposing any new rule, closed-list extension, scope claim, or precedence claim, work through the four gates explicitly. **If any gate fails, the proposal is not ready** — the gate failure itself is the next investigation, not the proposal's surface motivation.

## Gate A — Surface-feature check

Am I citing a surface feature (UD signature, rhetorical figure, punctuation, lexical pattern) as evidence?

- If yes: have I run the bidirectional atomic-thought test on the motivating case?
- Have I verified the surface feature corresponds to atomic-thought-failure, not just to a salient grammatical pattern?

A surface feature is a constraint, not a determination. See [`feedback_three_anti_default_factors.md`](feedback_three_anti_default_factors.md) Factor A.

## Gate B — Uniform-application check

Have I checked whether the existing rule set, applied uniformly, already covers this case?

- Queried the per-repo structured layer (Stanza UD / Macula-Greek+MorphGNT / Macula-Hebrew lowfat) for instances of the pattern?
- Checked the existing validator suite at `validators/`?

**New-rule proposals require an explicit "no existing rule applies uniformly" claim with evidence.** See Factor B.

## Gate C — Sample-size check

What's my sample size?

- <50 cases → spot-check; not adoption-ready (per `change-protocol.md` §7.3 trigger #3)
- ≥50 cases but <full corpus → run validator across full corpus before adoption
- Full corpus with ≥80% clean categorization → adoption threshold met (per §7.8)
- <80% clean → refine the rule before adoption

## Gate D — Bidirectional atomic-thought check

Have I run both:

- **Forward grammatical closure** — head not awaiting complement; no dangling subordinator / preposition; predication complete
- **Backward referential self-containment** — no unresolved deictic demonstratives, anaphoric particles, pronouns without on-line antecedent

Anaphoric reference FAILS. Cataphoric reference (presentative + indefinite NP, "thus says X:") PASSES. Cite `framework.md §1.1` (not a merge-override mechanism — M3/M4 are deprecated under the bidirectional test framework, 2026-05-17) when invoking. The bidirectional test is INFORMATIONAL DIAGNOSTIC, not precedence override — validators fire on canon-encoded UD signatures, not on bidirectional-test outcome.

## If all four gates pass

Proposal is ready for `change-protocol.md` §7.3 mandatory-audit dispatch (≥2 parallel adversarial agents) before any validator infrastructure is built. Per §7.3, building validator infrastructure first is the "fake rule" failure mode.

## If any gate fails

The gate failure is itself the next investigation. **Do not** proceed by patching around the failure to make the proposal "work" — that's the new-rule reflex (Factor B) compounding on top of whatever the original failure was.

## How to apply

Run these gates mentally before drafting any §5 rule entry, closed-list extension, scope claim, or precedence claim. When dispatching adversarial audits per §7.3, include the gate-status of the proposal in the dispatch prompt so the audit can verify rather than re-derive.

Codified 2026-05-16 from the readiness-arc adversarial audit's identification of discipline-codification latency as the load-bearing 13-month cost. Cross-references: [`feedback_three_anti_default_factors.md`](feedback_three_anti_default_factors.md) (factor compression these gates operationalize); `framework.md §1.1` (bidirectional test); `change-protocol.md` §7.3 / §7.8 (audit triggers + adoption threshold).
