# R18 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 18` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 18` (~lines 873–891; mixed grammatical-basis + diagnostic + fixed-idiom list)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R18.md`](../R18.md) (full scholarship companion)

---

### R18: Fixed Idiom Integrity

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern
**Layer:** 3

**Rule.** A token sequence matching any member of the closed list §Fixed-Idioms-R18 MUST be kept whole on a single v2-mine line. No line break MAY occur internal to a matched idiom's token sequence, regardless of resulting line length.

**UD signature.**
~~~yaml
trigger:
  surface_pattern: FIXED_IDIOMS_R18
  match: contiguous_token_sequence
action: KEEP_WHOLE
~~~

**Closed lists** (machine-readable).
~~~yaml
FIXED_IDIOMS_R18:
  - "put to death"
  - "from time to time"
  - "prevailed upon"
  - "put an end to"
  - "one with another"
  - "it is expedient that"
  - "insomuch as"
~~~

Date-colophon formulas are governed by R23 (sister rule, same KEEP_WHOLE logic; separate closed list of year-formula patterns).

**Scope.** Multi-word lexicalized expressions in the BoFM register that function as single lexical items. The closed list is the operational inventory; surface-token match against the v2-mine line stream is the detection mechanism. Idiom-internal token order is fixed; no inflectional or word-order variants are recognized as members.

**Exclusions (closed list — each cites dominating rule).**
1. *And it came to pass [that]* and its variants → R1 (sister formula-integrity rule with its own closed list and right-edge R16 coupling).
2. Date-colophon formulas (*"in the Nth year of the reign of the judges"*) → R23 (sister formula-integrity rule with its own closed list).
3. *insomuch that* (distinct subordinator from *insomuch as*) → R27 (consecutive-result subordinator with its own 3-condition merge test, not a fixed idiom).
4. *it is expedient that* matched as ADJ predicate complement frame governing a clausal complement → R26 governs the predicate+complement merge at the matrix-clausal level; R18's KEEP_WHOLE applies to the formula's internal token sequence, R26 governs the matrix+ccomp boundary.

**Precedence.** §3.5 Tier 2. Indivisibility tier; wins over all subtractive vetoes and merge-overrides at the formula-internal level. Coexists with R1, R15, R16, R23 in Tier 2 (each governs a distinct closed-list span).

**Examples.**

- *Compliant:* "they should be put to death" (idiom whole on one line)
- *Compliant:* "they did meet together from time to time" (idiom whole on one line)
- *Compliant:* "and they spake one with another" (idiom whole on one line)
- *Compliant:* "it is expedient that ye should keep the commandments" (formula whole on one line; matrix+ccomp merge governed by R26)
- *Non-compliant:* "they should be put / to death" (idiom severed)
- *Non-compliant:* "from time / to time" (idiom severed)
- *Non-compliant:* "it is expedient / that ye should keep the commandments" (formula severed)
- *Excluded by R1:* "And it came to pass that..." (governed by R1's AICTP_VARIANTS closed list, not R18).
- *Excluded by R23:* "in the seventh year of the reign of the judges" (date-colophon — governed by R23).
- *Excluded by R27:* "he did labor insomuch that his strength returned" (compound subordinator *insomuch that* is R27 territory; R18 covers only *insomuch as*).

**Implementation.**

- Validator (surface-pattern): [`validators/colometry/validate_rule_18_fixed_idioms.py`](../../../../readers-bofm/validators/colometry/validate_rule_18_fixed_idioms.py)
- Validator (UD-query): [`validators/colometry/validate_rule_18_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_18_ud.py)
- Applier: (none — surface-pattern keep-whole; corpus is hand-authored at this granularity, validators report violations)
- Closed-list definitions: §Fixed-Idioms-R18 (in BoFM canon, supplementary section)
- Audit trail: `readers-bofm/private/audit-trail/R18.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R18.md`](../R18.md)
