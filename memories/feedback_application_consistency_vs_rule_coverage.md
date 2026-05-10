---
name: Application-consistency precedes rule-coverage (consistency is prior to correctness)
description: The failure mode usually isn't missing rules; it's the same rule applied inconsistently across instances. Before proposing a new rule, audit whether the existing rule is applied uniformly to all instances of the target phrase/construction
type: feedback
---
**The insight (articulated in GNT trench session 2026-04-19, ported here because BofM's formulaic language is even denser and more vulnerable to this failure mode):**

> *"The failure is application-consistency, not rule-coverage. The existing rules probably cover this case already. We've just been failing to apply them uniformly. Consistency is prior to correctness. Being uniformly-wrong is fixable in one pass; being inconsistent is sediment that takes multiple passes to even surface."*

## Why this fires hard in BofM specifically

BofM's language is formulaic-dense: AICTP variants, "it is expedient that," "Yea, verily I say unto you," "And now, my brethren," "Behold," "And it came to pass that," rhetorical-address openings. These recurring phrases are exactly the kind of fixed formulas most vulnerable to sedimented inconsistency — dozens of instances across the corpus, multiple sessions touching them on different days, none asking "do all 28 instances get the same treatment?"

## The architectural blind spot

The current scanner family (Rules 1-22, Class A-P splits, Goldilocks refinement, etc.) asks:

> **Does THIS LINE violate THIS PATTERN?**

Nothing yet asks:

> **Does THIS PHRASE / CONSTRUCTION get THE SAME TREATMENT across all its instances?**

The first question catches novel violations. The second catches sedimented drift — cases where prior sessions patch-fixed the visible issue that day without auditing the recurring formula corpus-wide.

## How to apply

**Before proposing a new rule or Class:** audit whether the existing rule is already applied uniformly to all instances of the target phrase / construction. If inconsistency is the real finding, the fix is uniform application, not a new rule. This is the discipline that caught the withdrawn "long interjection earns split" proposal 2026-04-18 — the existing "unless" case already handled it.

**Before patch-fixing a specific verse:** ask *"where else does this same phrase/construction appear?"* Patch-fix one visible instance and you seed future inconsistency; audit corpus-wide and you prevent the sediment.

**In session notes:** when you fix a specific verse, note whether the corpus-wide application audit was done. If not, flag it for a future session.

## Consistency is ordered prior to correctness

Stan's four-C quality signature (clear, consistent, comprehensive, concise) isn't flat. **Consistency is prior to correctness** because uniform-wrong is fixable in one pass while inconsistent-application requires multiple passes just to surface the drift. An inconsistency finding is a bigger red flag than a disputed rule call.

## Flagged future tooling

A **phrase-consistency scanner** orthogonal to the current pattern-scanner family — asks "does this formula get the same treatment across all N instances?" Do NOT build speculatively; build only if Stan directs.

## Cross-reference

- `feedback_over_structuring_disposition.md` (this memory's ADD-side twin)
- `feedback_goldilocks_refinement.md` — subordinate-vs-coordinate Goldilocks discipline
- `feedback_rhetorical_force.md` — rhetorical force alone never justifies a split
