# R23 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 23` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 23` (~lines 976–984; mixed grammatical-basis + diagnostic + validator pointer)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R23.md`](../R23.md) (full scholarship companion)

---

### R23: Date Colophon Integrity

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern
**Layer:** 3

**Rule.** A token sequence matching any member of the closed list §Date-Colophons-R23 MUST be kept whole on a single v2-mine line. No line break MAY occur internal to a matched date-colophon span, regardless of resulting line length. When the matched span occupies its own line as a fronted or trailing temporal adjunct of an adjacent matrix predication, that own-line treatment is licensed by J5 (substantive adjunct as own focus) and does not affect R23's internal-indivisibility mandate.

**UD signature.**
~~~yaml
trigger:
  surface_pattern: DATE_COLOPHONS_R23
  match: contiguous_token_sequence
  anchor: { form_lower: "in", followed_by: { form_lower: "the", within: 1 } }
  spine: { ordinal_or_number_word_within: 4, then: { form_lower: "year" } }
action: KEEP_WHOLE
~~~

**Closed lists** (machine-readable).
~~~yaml
DATE_COLOPHONS_R23:
  - "in the <ordinal> year of the reign of the judges"
  - "in the <ordinal> year of the reign of king <name>"
  - "in the <ordinal> year since Lehi left Jerusalem"
ORDINAL_FORMS_R23:
  - first
  - second
  - third
  - fourth
  - fifth
  - sixth
  - seventh
  - eighth
  - ninth
  - tenth
  - eleventh
  - twelfth
  - thirteenth
  - fourteenth
  - fifteenth
  - sixteenth
  - seventeenth
  - eighteenth
  - nineteenth
  - twentieth
  - twenty
  - thirtieth
  - thirty
  - fortieth
  - forty
  - fiftieth
  - fifty
  - sixtieth
  - sixty
  - seventieth
  - seventy
  - eightieth
  - eighty
  - ninetieth
  - ninety
  - hundredth
  - hundred
NUMBER_WORDS_R23:
  - one
  - two
  - three
  - four
  - five
  - six
  - seven
  - eight
  - nine
  - ten
  - eleven
  - twelve
  - thirteen
  - fourteen
  - fifteen
  - sixteen
  - seventeen
  - eighteen
  - nineteen
  - twenty
  - thirty
  - forty
  - fifty
  - sixty
  - seventy
  - eighty
  - ninety
  - hundred
COMPOUND_ORDINAL_PATTERN:
  - "<number-word> and <ordinal>"   # e.g., "forty and second"
~~~

The closed list admits compound-ordinal variants of the form *"<number-word> and <ordinal>"* (e.g., *"forty and second year"*, *"twenty and seventh year"*). The detector spine — *in the [number-word and] <ordinal> year* — anchors all variants.

**Scope.** Multi-word date-colophon formulas in the BoFM register that timestamp narrative events. Operational boundary: the matched span begins at the anchor token *in* and ends at the formula's final token (*judges*, *king <name>*, or the token following *since*). Span-internal token order is fixed; no inflectional, ellipsis, or word-order variants are recognized as members. R23 governs the formula's internal indivisibility only; the formula's external boundary (whether it earns its own line as a fronted/trailing temporal PP) is governed by J5.

**Exclusions (closed list — each cites dominating rule).**

1. Non-date temporal PPs (*"in those days"*, *"in the days of"*, *"at that time"*) — not date-colophon formulas; governed by general PP break legality (Layer 1) and J5 at the line-boundary level.
2. Bare *"the Nth year"* anaphoric references without the *in the* anchor and without the *of the reign* / *since* continuation — surface-pattern does not match; outside R23's closed list.
3. AICTP formula's leftward token span (*And it came to pass*) when adjacent to a date-colophon → R1 (governs the AICTP span; R23 governs the date-colophon span; the two formulas coexist on the same line under their respective KEEP_WHOLE mandates, separated by the trailing-*that* per R16).
4. *it is expedient that* and other fixed idioms when adjacent to a date-colophon → R18 (governs the idiom span; R23 governs the date-colophon span; coexist on the same line).
5. Own-line placement of the date-colophon as a fronted temporal adjunct (e.g., *"in the forty and second year of the reign of the judges, / they came down..."*) → J5 (substantive adjunct as own focus; R23's internal-indivisibility mandate is preserved, the J5 own-line treatment applies at the formula's external boundary).

**Precedence.** §3.5 Tier 2. Indivisibility tier; wins over all subtractive vetoes and merge-overrides at the formula-internal level. Coexists with R1, R15, R16, R18 in Tier 2 (each governs a distinct closed-list span).

**Examples.**

- *Compliant:* "in the forty and second year of the reign of the judges" (formula whole on one line)
- *Compliant:* "in the seventh year of the reign of king Mosiah" (formula whole on one line)
- *Compliant:* "in the eighth year since Lehi left Jerusalem" (variant formula whole on one line)
- *Compliant (J5 own-line):* "And it came to pass / in the forty and ninth year of the reign of the judges, / there was continual peace established in the land" (R1 governs AICTP span; R23 keeps date-colophon whole; J5 earns it its own line)
- *Non-compliant:* "in the forty and second year / of the reign of the judges" (formula severed)
- *Non-compliant:* "in the seventh year of the reign / of king Mosiah" (formula severed)
- *Non-compliant:* "in the eighth year / since Lehi left Jerusalem" (variant formula severed)
- *Excluded by R1:* "And it came to pass / in the forty and second year of the reign of the judges..." (left-boundary break is between R1's span and R23's span, not internal to either)
- *Excluded by J5:* the date-colophon as its own line (the own-line is a J5 license, not an R23 violation; R23 cares only about internal indivisibility)

**Implementation.**

- Validator (surface-pattern): [`validators/colometry/validate_rule_23_date_colophon.py`](../../../../readers-bofm/validators/colometry/validate_rule_23_date_colophon.py)
- Validator (UD-query): [`validators/colometry/validate_rule_23_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_23_ud.py)
- Applier: (none — surface-pattern keep-whole; corpus is hand-authored at this granularity, validators report violations)
- Closed-list definitions: §Date-Colophons-R23 (in BoFM canon, supplementary section)
- Audit trail: `readers-bofm/private/audit-trail/R23.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R23.md`](../R23.md)
