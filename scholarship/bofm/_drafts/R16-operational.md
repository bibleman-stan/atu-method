# R16 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 16` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 16 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 16` (~9 lines mixing grammatical-basis + UD signature + diagnostic + example)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R16.md`](../R16.md) (full scholarship companion)

---

### R16: Dangling "That" After AICTP

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern
**Layer:** 3

**Rule.** When the fixed extraposition formula *And it came to pass* (R1, §AICTP-Variants) is immediately followed by the subordinator *that* introducing the extraposed content clause, *that* MUST NOT be line-final. A line break SHALL be inserted before *that* whenever the formula and its content cannot share a single line without violating the atomic-thought test; *that* MUST then lead the content clause on the next line. The formula's internal span (through *pass*) remains whole per R1.

**UD signature.**
~~~yaml
trigger:
  surface_pattern: AICTP_VARIANTS  # see R1 §AICTP-Variants
  ud_anchor: { relation: expl, head: { lemma: come }, dependent: { lemma: it } }
  mark: { lemma: that, position: immediately_following_pass }
  condition: that_would_be_line_final
action: SPLIT_BEFORE_MARK
~~~

**Closed lists** (machine-readable).
~~~yaml
AICTP_VARIANTS:  # inherited from R1
  - "And it came to pass"
  - "And now it came to pass"
  - "And it shall come to pass"
~~~

**Scope.** The right-edge boundary of an AICTP token-sequence (R1) when the formula is followed by subordinator *that*. R16 governs ONLY the placement of the break relative to *that*: *that* leads its content clause, never trails the formula. R1 governs the formula-internal span; R16 governs the formula-to-content seam. When AICTP content is short enough to keep AICTP-*that*-content all on one line under the atomic-thought test, no R16 break is required.

**Exclusions (closed list — each cites dominating rule).**
1. AICTP not followed by *that* (formula stands as scene-marker without an extraposed clause) → no R16 trigger; R1 keep-whole alone applies.
2. *That* in an AICTP-adjacent position but governed by a different rule (e.g., the *that* belongs to a higher-level R17 complement of an embedded matrix verb rather than to AICTP itself) → R17 governs that *that*; R16's trigger requires direct linear adjacency *pass that*.
3. AICTP followed by a substantive temporal/locative/causal PP that earns its own line BEFORE the *that*-clause → J5 (substantive adjunct as own focus); R16 still places the *that*-break, but the J5 slot-filler is on its own line per J5's mandate.

**Precedence.** §3.5 Tier 2 (couples to R1). Inherits R1's Tier-2 indivisibility status; together R1+R16 form the canonical AICTP line shape. Wins over R17 and R19 when both could apply to the *that* immediately following AICTP — the AICTP-coupling is most specific (§3.5.1 sub-hierarchy: "R1 / R16 AICTP *that*" is the first match in the *that*-cluster).

**Examples.**

- *Compliant (short content; one line):* "And it came to pass that I, Nephi, returned to my tent." (formula + *that* + short content all on one line; R16's break trigger does not fire because *that* is not line-final)
- *Compliant (long content; R16 break before *that*):* "And it shall come to pass / that whosoever shall believe on the Son of God, the same shall have everlasting life" (R16 break before *that* so *that* leads its content clause)
- *Non-compliant (R16 violation — *that* line-trails the formula):* "And it came to pass that / whosoever shall believe on the Son of God..." (the formula's *that* is stranded line-final; reader's attention dangles forward expecting "that what?")
- *Non-compliant (R1 violation — formula severed):* "And it came / to pass that whosoever..." (this is an R1 violation of the formula-internal span; R16 does not separately fire because R1 takes precedence at the formula-internal level)
- *Excluded by R17:* "And it came to pass that he said unto them that they should depart" (the second *that* is governed by R17 speech-class complement-integrity, not R16; R16 governs only the *that* immediately following *pass*)

**Implementation.**

- Validator: [`validators/colometry/validate_rule_16_aictp_dangling_that.py`](../../../../readers-bofm/validators/colometry/validate_rule_16_aictp_dangling_that.py) (also at `validate_rule_16_ud.py`)
- Applier: (none — surface-pattern split-before; corpus is hand-authored at this granularity, validator reports violations)
- Closed-list definitions: §AICTP-Variants (inherited from R1)
- Audit trail: `readers-bofm/private/audit-trail/R16.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R16.md`](../R16.md)
