# R10 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 10` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 10 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 10` (mixed operational + grammatical-basis + scope-prose content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R10.md`](../R10.md) (full scholarship companion)

---

### R10: Never Split Verb from Direct Object

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 1

**Rule.** A transitive verb and its direct object MUST appear on the same v2-mine line. When a line ends on a `VERB` whose `obj` relation points to a bare noun-phrase head on the immediately following line, the two lines MUST be merged. Intervening adverbials or prepositional phrases attached to the verb MUST remain with the verb, not the object.

**UD signature.**
```yaml
trigger:
  line_final_token: { upos: VERB }
  next_line_head:
    relation: obj
    head_ref: line_final_token   # the obj dependent of the verb on the prior line
    upos: [NOUN, PROPN, PRON]
    shape: bare_NP               # determiner + noun + optional PP/relative; not a new clause
  excludes:
    - { next_line_shape: complete_clause_with_finite_verb }   # Subject-NP continuation → R20
    - { next_line_shape: relative_clause_on_complete_NP }      # "Which"-clause decision tree / Class P
    - { coordinate_object_series: { n: ">=2", shared_verb: true } }   # J1 compound-list signals govern
action: MERGE_FORWARD
```

**Closed lists** (machine-readable).
```yaml
BARE_NP_SHAPES:
  - determiner + noun
  - determiner + noun + PP
  - determiner + noun + relative_clause
  - bare_noun
  - bare_PROPN
  - bare_PRON
```

**Scope.** Line-final transitive `VERB` whose `obj` dependent heads the next v2-mine line as a bare noun-phrase continuation of the same predication. The rule fires on the verb-object syntactic bond only; it does not govern verb-complement (clausal) bonds (R17 territory) or verb-PP-complement bonds (R17 topic-PP extension territory).

**Exclusions (closed list — each cites dominating rule).**

1. Already-complete clauses followed by a relative clause (next line begins a relative on a complete antecedent NP) → R19 / Class P "Which"-clause decision tree governs
2. Subject-NP continuations with their own predication (next line is a new finite clause whose subject NP appears to be an object of the prior verb but actually heads a new predication) → R20 territory (no-anchor / restructure)
3. Parallel coordinate object series at N≥2 under a shared verb — bare *"and [noun]"* compound objects do NOT individually trigger R10 against the shared verb. The §1.4 J1 compound-list-break-signals sub-rule governs: bare coordinate items MERGE with the shared verb unless one of the four break signals fires (elided-auxiliary + stacked participles; possessive restart; demonstrative; attached relative clause). Per framework §1.9, the N=3+ cliff is scoped to coordinate **predications**, NOT coordinate **objects** under a single shared verb
4. The third (or final) item in a compound object list carrying a trailing PP modifier — when the modifier attaches semantically to the joint object-set, M1 asymmetric-modifier sub-clause (framework §1.5 M1) keeps the modified item bonded with its co-objects; R10 still merges the entire object-set with the shared verb
5. Verb-complement clausal bonds (matrix verb + `ccomp` / `xcomp`) → R17 governs (complement integrity)
6. Verb-PP obligatory-complement bonds (speech-class verbs + topic-PP; experience verbs + *of*-PP) → R17 topic-PP / experience-of-PP extensions govern

**Precedence.** §3.5 Tier 1 (Layer 1 syntax veto). Wins over all Tier 3+ generative rules (R10 violations are MALFORMED, not editorial). Coordinates with R9, R11, R12, R13a as the closed-list Layer 1 mid-phrase prohibitions.

**Examples.**

- *Compliant:* "have you sufficiently retained in remembrance the captivity of your fathers?" (Alma 5:6 — V *retained* + bare DO *the captivity of your fathers* on one line)
- *Compliant (compound object — J1 sub-rule, R10 still binds):* "preach unto them repentance, and redemption, and faith on the Lord" (Mosiah 18:7 — shared verb *preach unto them* binds the three bare *"and [noun]"* objects; no break-signals fire; the third item's trailing PP *on the Lord* attaches to the joint object-set per M1 asymmetric-modifier; one line)
- *Non-compliant (violates R10):* "have you sufficiently retained in remembrance / the captivity of your fathers?" (V severed from bare-NP DO)
- *Excluded by R19 / Class P:* "the brass plates / which Lehi obtained" (next line is a relative clause on a complete antecedent NP, not a bare DO continuation)
- *Excluded by R20:* "[matrix predication ending in V] / [new finite clause whose NP would otherwise look like an object]" (next line carries its own finite predication — R20 territory, not R10)
- *Excluded by R17:* "He caused / that his servants should stand forth" (the next line begins a *that*-clause `ccomp` of the matrix VERB *caused* — complement integrity governs, not V+DO)

**Implementation.**

- Validator: [`validators/colometry/validate_rule_10_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_10_ud.py) (UD-pattern); [`validators/colometry/validate_rule_10_verb_do_split.py`](../../../../readers-bofm/validators/colometry/validate_rule_10_verb_do_split.py) (surface heuristic)
- Applier: [`validators/apply_rule_10_ud.py`](../../../../readers-bofm/validators/apply_rule_10_ud.py)
- Closed-list definitions: `BARE_NP_SHAPES` in validator source
- Audit trail: `readers-bofm/private/audit-trail/R10.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R10.md`](../R10.md)
