# R27 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 27` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 27 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 27` (mixed operational + grammatical-basis + corpus-empirics content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R27.md`](../R27.md) (full scholarship companion)

---

### R27: "Insomuch That" Binding

**Status:** Proposed
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A consecutive-result clause introduced by the compound subordinator *insomuch that* attaching as `advcl` to its matrix MUST be split from the matrix by default. The merge MAY be applied only when **all three** conditions hold: (1) the result clause is ≤ 8 non-PUNCT word tokens; (2) the result clause's subject is co-referential with the matrix subject (`nsubj` of advcl equals `nsubj` of matrix, or the result-clause subject is elided and co-referential); and (3) no camera-angle shift occurs across the boundary (single-image diagnostic passes). When any condition fails, the break MUST be inserted before the *insomuch that* mark.

**UD signature.**
```yaml
trigger:
  relation: advcl
  mark: { lemma_in: INSOMUCH_THAT_MARK_PATTERNS }
default_action: SPLIT_BEFORE_MARK
merge_action: MERGE_HEAD_AND_DEPENDENT  # gated by all three conditions
merge_conditions:
  - word_count: { subtree: result_clause, exclude_punct: true, max: 8 }
  - subject_continuity: { nsubj_advcl: { equals_or_elided_coref: nsubj_matrix } }
  - camera_angle_shift: false
```

**Closed lists** (machine-readable).
```yaml
INSOMUCH_THAT_MARK_PATTERNS:
  # Compound subordinator; UD tokenizes in two patterns
  # Pattern A: insomuch=ADV/advmod + that=SCONJ/mark, both children of advcl head
  # Pattern B: insomuch=ADV/mark + that=SCONJ/fixed(head=insomuch)
  # Plus rare single-MWE token form
  - "insomuch that"
  - "insomuch + that"

CO_REF_PRONOUNS:
  - he
  - she
  - they
  - it
  - i
  - we
  - his
  - her
  - their
  - its
  - my
  - our
  - him
  - them
  - us
  - me
  # archaic BofM second-person
  - ye
  - thee
  - thou
  - thy
  - thine

ELIDED_SUBJECT_VERBS:
  - did
  - was
  - were
  - had
  - could
  - might
  - would
  - shall
  - will
  - hath
  - doth
  - art
  - am
  - are
  - began
  - fell
  - came
  - went
  - cried
  - spake
  - led
  - brought
  - felt
  - smote
  - became

EXPLETIVE_THERE_VERBS:
  - was
  - were
  - is
  - are
  - arose
  - came
  - stood
  - dwelt
  - shall
  - never
  - had
  - hath
  - began
```

**Scope.** Compound subordinator *insomuch that* in `advcl` attachment to its matrix. Simple `mark=that` cases are outside R27 territory (route to R7, R17, R19, or R26 per the §3.5.1 *that*-cluster precedence). The rule governs the OUTER boundary between the result clause and its matrix only; once that boundary is resolved, internal structure of the result clause is evaluated separately against J1–J5 (framework §1.4) — notably J5 (fronted substantive temporals/locatives/causals) and J1 (parallel series within the result) can license breaks INSIDE the merged unit.

**Exclusions (closed list — each cites dominating rule).**

1. Expletive-*there* + new-entity semantic subject (*there were many slain*, *there were thousands converted*) — condition 2 evaluated against the semantic subject (NP following *there were*); new-entity semantic subjects fail condition 2 → default SPLIT (per this rule's own expletive-*there* sub-clause)
2. Chained *insomuch that* clauses without coordinating conjunction — each subordinator introduces a fresh finite predication with its own degree-specification; default SPLIT each, applying the 3-condition merge test pairwise against the immediate antecedent (per this rule's own chained-*insomuch* sub-clause; canonical case Alma 24:2)
3. Result-clause internal structure firing J5 substantive adjunct or J1 parallel series — those breaks fire INSIDE the merged unit and are NOT excluded from R27; R27's outer-boundary verdict (merge) stands → framework `§1.4`
4. Layer 1 mid-phrase prohibition firing on the merge target (line-final CCONJ / DET / AUX / ADP after merge) → R9 / R10 / R11 / R12 / R13a (Tier 1 always wins)
5. AICTP closed token sequence overlap → R1 (Tier 2)

**Sub-clauses (operational).**

- **Expletive-*there* sub-clause.** When the result clause begins with expletive *there* + BE-verb (*there was*, *there were*, *there is*, *there are*, *there came*), condition 2 is evaluated against the **semantic subject** (the NP following the BE-verb), not the expletive. New-entity semantic subjects fail condition 2 → default SPLIT. Rare continuing-entity semantic subjects (*there was the same man as before*) MAY pass condition 2; in those cases condition 1 (word count) is typically decisive.

- **Chained *insomuch that* sub-clause.** When two or more *insomuch that* clauses chain asyndetically (no coordinating conjunction between them), default SPLIT each. The 3-condition merge test still applies pairwise — each *insomuch that* against its immediate antecedent, not against the top-level matrix. Camera angle typically shifts with each degree-intensification, so chained instances rarely pass all three conditions pairwise.

**Precedence.** §3.5 Tier 5. Wins over R7 when the subordinator is the compound *insomuch that* (R7's UD signature requires simple `mark=that`; the compound subordinator is its own mark, and the modal in *insomuch that + MODAL* belongs to consecutive-result semantics rather than purposive telic semantics). Yields to Tier 1 Layer 1 syntax vetoes (R9, R10, R11, R12, R13a), Tier 2 indivisibility/formula (R1, R15, R16, R18, R23), and Tier 0 input filters.

**Examples.**

- *Compliant (SPLIT — default):* "And he did minister unto them, / insomuch that his whole household were converted unto the Lord." (Alma 22:23) — result clause 9 words, new subject, camera shift
- *Compliant (SPLIT — chained insomuch):* "And their hatred became exceedingly sore against them, / even insomuch that they began to rebel against their king, / insomuch that they would not that he should be their king" (Alma 24:2) — three lines, each atomic
- *Compliant (MERGE — all three conditions hold):* "...insomuch that they were sore amazed" — result clause ≤8 words, subject elided and co-referential, no camera shift
- *Non-compliant (R27 violation — default SPLIT not applied where conditions fail):* "And he did minister unto them insomuch that his whole household were converted unto the Lord" — matrix and consecutive-result frame collapsed despite condition 1 failure (9 words) and condition 2 failure (new subject)
- *Excluded by expletive-*there* sub-clause (default SPLIT):* "...insomuch that there were many slain" — condition 2 evaluated against semantic subject *many slain* (new entity) → fails
- *Excluded by R7 yields-to:* none — when the compound mark is *insomuch that*, R27 governs (R7 yields, per §3.5 Tier 5)

**Implementation.**

- Validator (UD): [`validators/colometry/validate_rule_27_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_27_ud.py)
- Validator (regex precursor): [`validators/colometry/validate_rule_27_insomuch_that.py`](../../../../readers-bofm/validators/colometry/validate_rule_27_insomuch_that.py)
- Applier: [`validators/apply_rule_27_ud.py`](../../../../readers-bofm/validators/apply_rule_27_ud.py)
- Closed-list definitions: in validator source (`CO_REF_PRONOUNS`, `ELIDED_SUBJECT_VERBS`, `NEW_NP_STARTERS`, `EXPLETIVE_THERE_VERBS`)
- Audit trail: `readers-bofm/private/audit-trail/R27.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R27.md`](../R27.md)
