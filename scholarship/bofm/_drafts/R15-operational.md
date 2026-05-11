# R15 Operational Entry — Proposed Restructured Form (Migration Wave 1)

**This is the proposed restructured operational entry for R15** per the MISRA-without-Rationale operational template ([`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 15` entry. The rationale, audit precedent, and empirical history previously inlined in §5 R15 are relocated to the scholarship companion at [`../R15.md`](../R15.md).

---

### R15: Vocative Units Are Indivisible

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A true vocative — a multi-word direct-address unit identifiable by the UD `vocative` relation — MUST occupy its own v2-mine line and MUST NOT contain an internal line break. The vocative MUST NOT be merged with the matrix clause that follows or precedes it. NP-object uses of phrases that are lexically vocative-shaped (e.g., *my brethren*, *my son*) but function as the syntactic object of a verb or preposition fall outside R15's scope and are not governed by this rule.

**UD signature.**
```yaml
trigger_internal_split:
  relation: vocative
  span: { contains_line_break: true }
action: KEEP_WHOLE

trigger_matrix_merge:
  relation: vocative
  span: { shares_line_with: matrix_clause }
  true_vocative_confirmed: true
action: SPLIT_BEFORE_SUBJECT
```

**Closed lists** (machine-readable).
```yaml
TRUE_VOCATIVE_CONFIRMERS:
  second_person_pronouns: [ye, thee, thou, you, thy, thine, your, yours, yourselves, thyself]
  imperative_verbs: [remember, hearken, hear, give, consider, behold, repent, come, listen, learn, know]

VOCATIVE_LEXICAL_SHAPES:
  - "O <NOUN/PROPN>"
  - "O <NOUN/PROPN> <NOUN/PROPN>"  # e.g., "O Lord God"
  - "(my|our) <kin_or_audience_noun>"  # e.g., "my son", "my brethren", "my people"
  - "<PROPN_address>"  # bare proper-name address

KIN_OR_AUDIENCE_NOUNS:
  - son
  - sons
  - daughter
  - brother
  - brethren
  - sister
  - sisters
  - people
  - beloved
  - friend
  - friends
```

**True-vocative test.** A vocative-shaped phrase is a true vocative WHEN the same predication contains a second-person pronoun from `TRUE_VOCATIVE_CONFIRMERS.second_person_pronouns` OR an imperative verb from `TRUE_VOCATIVE_CONFIRMERS.imperative_verbs`. Bare proper-name address (*"Moroni, ..."*) requires the same confirmer. Absent any confirmer, the phrase is treated as NP-object and falls outside R15.

**Scope.** Applies to multi-word direct-address constituents tagged with the UD `vocative` relation in v2-mine lines, including bare proper-name addresses confirmed by the true-vocative test. The rule governs (a) prohibition of internal line breaks within the vocative span, and (b) prohibition of same-line merger with the surrounding matrix clause. Single-word interjections without a following nominal addressee (e.g., *behold*) fall outside R15.

**Exclusions (closed list — each cites dominating rule).**
1. NP-object uses of vocative-shaped phrases (the phrase is the syntactic object of a matrix verb or preposition; no second-person or imperative confirmer in the predication) → out of scope; R10 (V+DO bond) governs the head-object relation.
2. Vocative + close divine-title appositive within a vocative environment (e.g., *"O God, the Eternal Father"*) → R15 still wins; the appositive joins the vocative as one indivisible address unit. (R22's INTRODUCING stack-split does not fire inside a vocative environment.)
3. Speech-tag introductions terminating in a colon (*"saying:"* followed by directly-quoted address) → J3 (speech-act announcement) governs the speech-tag break; R15 still governs the vocative occurring within the quoted material.

**Precedence.** §3.5 Tier 2. Wins over R22 in vocative environment. Wins over R17 when a true vocative sits on the matrix line (the matrix-complement merge yields to R15's own-line mandate for the vocative).

**Examples.**

- *Compliant:* "O Lord God, / how long wilt thou suffer..." (vocative own line; main clause on next line)
- *Compliant:* "My son, / I would that ye should make a proclamation..." (vocative own line; matrix follows)
- *Compliant (vocative + appositive bonded — R22 yields):* "O God, the Eternal Father," (Moroni 4:3, 5:2 sacrament prayer; appositive merged into vocative unit)
- *Non-compliant (matrix merge):* "My sons, I would that ye should remember..." (vocative merged with main clause on one line)
- *Non-compliant (internal split):* "O Lord / God" (vocative split internally — always forbidden)
- *Excluded — NP-object:* "I spake unto my brethren, saying:" (*my brethren* is prepositional object of *unto*; no second-person or imperative confirmer in the predication; R15 does not apply)
- *Excluded — NP-object:* "I went unto my brethren," (*my brethren* is prepositional object; no confirmer; R15 does not apply)
- *Excluded by J3 (speech-tag colon governs the tag break; R15 still governs the vocative inside the quoted material):* "And he said unto them: / O ye people of Nephi, hearken unto my words." (the colon-terminated tag yields to J3; the vocative *"O ye people of Nephi,"* still earns its own line per R15)

**Implementation.**

- Validator: [`validators/colometry/validate_rule_15_vocative.py`](../../../../readers-bofm/validators/colometry/validate_rule_15_vocative.py)
- Applier: [`validators/apply_rule_15_vocative_splits.py`](../../../../readers-bofm/validators/apply_rule_15_vocative_splits.py)
- Closed-list definitions: §Vocative-Confirmers-R15 (in BoFM canon, supplementary section)
- Audit trail: `readers-bofm/private/audit-trail/R15.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R15.md`](../R15.md)
