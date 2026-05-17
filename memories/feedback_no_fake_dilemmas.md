---
name: Don't bring fake dilemmas — apply rules, route only genuine edge cases
description: When canon mechanically resolves a case, apply it. Do NOT route mechanically-resolved cases through Stan-deference framings ("borderline", "pending judgment", "want me to also..."). The framings preserve withdrawn rules' effects and waste Stan's time. Genuine edge cases — where mechanical rules underdetermine — get explicit "this needs you because X." Everything else: just fix it.
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
**The rule:** When canon's mechanical test resolves to a clean answer, apply that answer. Don't frame as a decision point. Don't bring to Stan as "review."

**Why:** This is the SAME smuggling pattern the meta-audit caught — and Stan named it directly: *"if you are doing that, it means you either aren't following the rules, you don't understand them, or they are not written in a correct way that forces you to follow."* The route through Stan-deference preserves the effect of withdrawn or non-existent rules, exactly when the canon has been sharpened to deny them.

The 2026-04-25 catch: I brought Moroni 10:19 to Stan as item #8 on a "review list" with framing *"likely Category-A reclassification, not pending-judgment."* But the meta-audit had already resolved it: §1 line 162 (minimal-rubric verb-synonymy constraint, `framework.md §1.2`) — *is* (copular) vs *be done away* (cessation predicate) — distinct non-synonymous → SPLIT. The corpus is already split. There is no decision. The pending.md entry was a residual from the withdrawn doctrinal-weight bump. Bringing it to Stan re-instantiated the bump's effect by routing through deference.

Same shape with 3 Ne 15:3 image-gate proposal: meta-audit said REJECT not audit. I framed as *"want me to also strip..."* — fake dilemma. The audit's verdict WAS the answer. Just remove from pending and move on.

**How to apply:**

1. **Mechanical-test gate before any review-list framing.** Before writing *"pending Stan's judgment"* or *"want me to also..."* or *"want me to walk through these one at a time"*, check: does an existing canon rule mechanically resolve this? If yes, apply. The framing is the fake dilemma.

2. **§7.3 skip-safe means skip.** Typo fixes, cross-reference updates without precedence claims, mechanical Category-A applications: don't ask. Apply. The canon explicitly authorizes this.

3. **Bring genuine edge cases — and only those — with explicit framing.** A genuine edge case has: (a) a specific named rule that does NOT cover the situation, (b) a clear question about how to extend or constrain the rule, (c) my own attempted mechanical reading and why it fails. Not a vague *"borderline"* or *"complex"* tag.

4. **The wording test.** If I find myself writing *"borderline,"* *"complex,"* *"genuinely unclear,"* *"want me to walk through,"* *"want me to also,"* — STOP. That phrasing is the smuggling channel. Either:
   - There IS a mechanical answer → apply, don't bring
   - There ISN'T a mechanical answer → state the canon gap explicitly with "rule X doesn't cover Y; should we [specific framing decision]?"

5. **Trust the audit verdicts.** When a hostile audit resolves a case (REJECT, CLEAN, SMUGGLING with specific reframe), the verdict IS the answer. Don't re-route the verdict through Stan-deference. The audit was the deference.

6. **For pending.md hygiene specifically:** items inherited from withdrawn rules don't survive the withdrawal. If Rule X was deleted, items tagged *"pending under Rule X"* are resolved by deletion. Strip them mechanically.

7. **Per-item review discriminator (added 2026-04-27 from carry-forward-inertia catch):** for each item on a deferred/pending list, ask explicitly: *"has the deciding move already been made elsewhere?"* If yes, the item is residue, not deliberation — fix on first contact, don't re-defer. The Stan-named precedent: BofM canon §1 retired breath as a diagnostic 2026-04-19 PM, and Rule 6/Rule 7/Parallel-List Uniformity/Rule 15 still cited "breath tests" as parallel gates a week later — including in newly-codified principles I authored 2026-04-26 while editing the canon. Worse than carry-forward, *active reinjection* of a retired diagnostic. The mechanical safeguard is `validators/colometry/validate_canon_retirement_residue.py` (added 2026-04-27) — when a retirement is added to canon, the validator's RETIRED_TERMS list gets the new entry; future commits are gated against active residue automatically. Don't rely on memory-as-discipline for this; the validator is the gate.

**The cost of getting this wrong:** every fake dilemma is a context-tax on Stan. He has to read it, recognize it's resolved, tell me to stop. The 5-catch session (2026-04-22→23) demonstrated the propose-channel discipline; this is the operate-channel sibling that needs the same discipline.

**Cross-reference:**
- `feedback_rhetoric_bandwagon.md` — meta-audit failure mode (judgment-handoff smuggling section)
- `feedback_application_consistency_vs_rule_coverage.md` — the OPERATE-side family this belongs to
- canon §2 closing instruction: when uncertain between A and B/C → treat as B → but FIRST run the mechanical test; only invoke §2 when the mechanical test is genuinely silent.
