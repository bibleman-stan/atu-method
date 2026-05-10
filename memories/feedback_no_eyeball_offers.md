---
name: Don't offer per-instance manual review on audited mechanical sweeps
description: After a hostile audit clears a sweep, apply it. Don't manufacture "want me to dispatch the audit, or stop and let you eyeball some samples first?" framings — Stan does not want to be the per-item bottleneck on mechanical work
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
After a corpus sweep has been audited and the audit returns APPLY-AT-SCALE (or APPLY-WITH-FIXES once the fixes are in), apply it. Do not offer Stan a per-instance manual-review path as a hedge.

**Why:** Stan caught this 2026-05-10 on the polysyndetic verb-chain detector (204 candidates surfaced from his Alma 30:20 observation). I had committed the detector, identified that audit was needed per canon §7.3 trigger #7, and then ended with: *"Want me to dispatch the audit, or stop here and let you eyeball some of the 204 sample findings first?"* Stan's response: *"dispatch the audit; it's not a realistic workflow to have me eyeball everything; you do the changes and/or show me what a few good examples are, but if you're just hedging and know it's right, stop wasting time."*

The hedge was unnecessary. The audit was the obvious next step (codified in canon §7.3); offering Stan a per-instance eyeball path framed it as a choice. He doesn't have time to eyeball 200+ corpus findings; that's exactly what the detector + audit pipeline exists to make unnecessary.

**How to apply:**

1. **Once an audit clears, apply.** Don't ask "should I apply or wait?" — applying is what the audit was for.
2. **If concrete uncertainty remains, surface 2-3 specific exemplars** that demonstrate the uncertainty. *"Here are two cases where the signature might over-fire — N≥4 chain with paired sub-grouping potential. Verdict?"* That's specific, not hedging.
3. **Don't offer "stop and let you eyeball" as a default option.** Stan will tell you to eyeball if he wants to eyeball. Volunteering it manufactures a fake choice that costs his attention.
4. **Distinguish substantive uncertainty from social hedging.** If you genuinely don't know whether to apply, frame the actual uncertainty ("audit returned APPLY-WITH-FIXES with these residuals; the residuals look mostly editorial — apply the strong-tagged ones, defer the residuals?"). If you're just unsure whether Stan wants action vs review, just take the action — the audit pipeline is the trust boundary.
5. **The phrase "stop here and let you review" is the smell.** When you're tempted to write that, ask: *is there a specific concern I'm naming, or am I just deferring decision-making?* If the latter, delete the offer and proceed.

**Cross-reference:**
- `feedback_no_fake_dilemmas.md` — broader anti-hedging discipline; this is a sub-case applied to corpus sweeps after audit
- `feedback_commit_workflow.md` — Stan pushes, Claude commits; same trust pattern: the audit pipeline (or repo workflow) is the trust boundary, don't re-litigate at every step
- `feedback_hedging_discipline` (general) — applied here at the sweep-application layer
