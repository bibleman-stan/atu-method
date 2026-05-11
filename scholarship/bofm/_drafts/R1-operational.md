# R1 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 1` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 1` (~lines 641–651; mixed grammatical-basis + diagnostic + example content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R1.md`](../R1.md) (full scholarship companion)

---

### R1: AICTP Formula Integrity

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern
**Layer:** 3

**Rule.** The fixed extraposition formula *And it came to pass* (and its closed-list variants, §AICTP-Variants) MUST be kept whole on a single v2-mine line. No line break MAY occur internal to the formula's token sequence. The formula's trailing subordinator *that* — when present — couples to R16 (dangling-*that*), which governs the break placement at the formula's right edge. R1 governs only the formula-internal span.

**UD signature.**
~~~yaml
trigger:
  surface_pattern: AICTP_VARIANTS
  ud_anchor: { relation: expl, head: { lemma: come }, dependent: { lemma: it } }
action: KEEP_WHOLE
~~~

**Closed lists** (machine-readable).
~~~yaml
AICTP_VARIANTS:
  - "And it came to pass"
  - "And now it came to pass"
  - "And it shall come to pass"
~~~

**Scope.** The formula's token-sequence span, beginning at *And* (or *And now*) and ending at *pass*. Trailing-*that* boundary handling is delegated to R16. Layer 3 editorial rule; supersedes Layer 1 mid-phrase prohibitions only at the formula-internal level (no Layer 1 break could occur inside the formula because the formula contains no eligible split-point — but R1 codifies the indivisibility for editorial sweep purposes).

**Exclusions (closed list — each cites dominating rule).**
1. Trailing *that* placement (whether *that* line-leads vs. line-trails) → R16 (couples to R1; R16 forces break before *that*).
2. AICTP followed by a substantive temporal/locative/causal slot-filler PP earning its own line → J5 (substantive adjunct as own focus; AICTP integrity is preserved, and the slot-filler simply follows on its own line).

**Precedence.** §3.5 Tier 1 (most specific — closed token sequence). Wins over all subtractive vetoes and merge-overrides at the formula-internal level. Couples to R16 at the formula's right edge.

**Examples.**

- *Compliant:* "And it came to pass that in the seventh year of the reign of the judges, / there were about three thousand five hundred souls..." (formula whole on one line; trailing *that* leads its content per R16)
- *Compliant (variant):* "And now it came to pass that..." (variant form preserved whole)
- *Compliant (J5 slot-filler):* "And it came to pass that Moroni did arrive with his army at the land of Bountiful, / in the latter end of the twenty and seventh year of the reign of the judges over the people of Nephi." (Alma 52:18; AICTP-that whole on line 1, substantive temporal PP own-lines per J5)
- *Non-compliant:* "And it came to / pass that..." (formula severed)
- *Non-compliant:* "And it came / to pass that..." (formula severed)
- *Excluded by R16:* "And it came to pass / that in the seventh year..." (break before *that* is R16's domain, not an R1 violation; R1 governs only the formula-internal span up through *pass*)

**Implementation.**

- Validator: [`validators/colometry/validate_rule_01_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_01_ud.py)
- Applier: (none — surface-pattern keep-whole; corpus is hand-authored at this granularity, validator reports violations)
- Closed-list definitions: §AICTP-Variants (in BoFM canon, supplementary section)
- Audit trail: `readers-bofm/private/audit-trail/R1.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R1.md`](../R1.md)
