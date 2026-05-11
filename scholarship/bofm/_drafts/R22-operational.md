# R22 Operational Entry — Proposed Restructured Form (Migration Wave 2)

**This is the proposed restructured operational entry for R22** per the MISRA-without-Rationale operational template ([`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 22` entry. The rationale, audit precedent, and empirical history previously inlined in §5 R22 are relocated to the scholarship companion at [`../R22.md`](../R22.md).

---

### R22: Divine Title Appositives

**Status:** Active
**Category:** B (Editorial, judgment-required) — for INTRODUCING detection. Once a case is classified INTRODUCING via a formal anchor (closed-list), the stack-split action is mechanical.
**Decidability:** UD-pattern + Discourse-context-needed
**Layer:** 3

**Rule.** A divine-title appositive — an appositional NP whose head lemma is in `DIVINE_TITLE_HEADS` and which appears as `appos` to a divine-name referent — MUST be split onto its own line (STACK SPLIT) when the construction is INTRODUCING, and MUST remain merged with its referent on one line (REFERENCING default) otherwise. A construction is INTRODUCING when AT LEAST ONE of the three closed-list formal anchors (§Formal-Anchors-R22) is present. When R22 and R15 (Vocative Indivisibility) both fire on the same span — i.e., the divine-title appositive sits inside a vocative environment — R15 wins and the appositive MUST merge into the vocative as one indivisible address unit. Within a single unified rhetorical passage, repeated invocations of the same divine-title appositive MUST receive uniform treatment; oscillation between STACK and MERGE within one passage is forbidden.

**UD signature.**
```yaml
trigger_introducing:
  relation: appos
  head: { upos: PROPN, lemma_in: DIVINE_NAME_REFERENTS }
  dependent: { upos: [NOUN, PROPN], lemma_in: DIVINE_TITLE_HEADS }
  formal_anchor: { any_of: FORMAL_ANCHORS_R22 }
  vocative_environment: false
action: STACK_LIST_MEMBERS

trigger_referencing:
  relation: appos
  head: { upos: PROPN, lemma_in: DIVINE_NAME_REFERENTS }
  dependent: { upos: [NOUN, PROPN], lemma_in: DIVINE_TITLE_HEADS }
  formal_anchor: { any_of: FORMAL_ANCHORS_R22 }
  vocative_environment: false
  match_condition: no_anchor_present
action: MERGE_HEAD_AND_DEPENDENT
```

**Closed lists** (machine-readable).
```yaml
DIVINE_NAME_REFERENTS:
  # Proper-name heads that may carry a divine-title appositive
  - Jesus
  - Christ
  - "Jesus Christ"
  - God
  - Lord
  - Father
  - Messiah
  - Redeemer
  - Savior

DIVINE_TITLE_HEADS:
  # Head lemmas of the appositional NP recognized as divine titles
  - Son          # "Son of God", "Son of the living God", "Son of Righteousness"
  - Father       # "Eternal Father", "Heavenly Father"
  - Lamb         # "Lamb of God"
  - Holy         # "Holy One of Israel"
  - Almighty
  - Redeemer
  - Savior
  - Messiah
  - King         # "King of kings", "King of heaven"
  - Lord         # "Lord of hosts", "Lord God Omnipotent"
  - Christ
  - Creator
  - Maker

FORMAL_ANCHORS_R22:
  # The three closed-list formal anchors that trigger INTRODUCING classification.
  # AT LEAST ONE must be present in the surrounding context for STACK SPLIT to fire.

  formal_naming_formula:
    # Surface patterns introducing a name + title pairing as an act of naming
    patterns:
      - "his name shall be called <X>, <title>"
      - "they shall call his name <X>, <title>"
      - "his name shall be <X>, <title>"
      - "thou shalt call his name <X>, <title>"
      - "and he shall be called <X>, <title>"

  first_occurrence_context:
    # The named-plus-titled identity is being revealed for the first time in the
    # current pericope/discourse window. Discourse-context-needed; validator emits
    # REVIEW unless a first-occurrence anchor token is co-present (e.g., a verb
    # of revelation/showing/manifesting in the matrix).
    revelation_verbs:
      - show
      - reveal
      - manifest
      - make known
      - declare unto
      - prophesy of

  prophetic_proclamation_frame:
    # Surrounding frame establishes prophetic / revelatory authority
    speech_tags:
      - "Thus saith the Lord"
      - "Behold, I say unto you"
      - "the word of the Lord came"
      - "I beheld"             # vision-frame
      - "the angel said unto"  # angelic-announcement frame
      - "an angel of the Lord"
```

**Formal-anchor test.** A divine-title appositive is INTRODUCING (STACK SPLIT) WHEN at least one anchor from `FORMAL_ANCHORS_R22` is present in the same predication or in the immediately governing speech-tag/frame. Absent any anchor, the construction is REFERENCING and MERGE is the default. The formal_naming_formula anchor and the prophetic_proclamation_frame anchor are surface-detectable; the first_occurrence_context anchor requires discourse tracking and the validator emits REVIEW-REQUIRED when no surface anchor is present but the case may be first-occurrence.

**Vocative-environment filter.** Before applying the INTRODUCING vs REFERENCING test, check whether the divine-title appositive sits in a vocative environment (the head of the appositional construction is itself the head of a UD `vocative`-tagged span, OR the surrounding predication satisfies R15's true-vocative test). If yes, R22 MUST NOT fire — R15 wins and the appositive remains within the vocative as one indivisible address unit.

**Scope.** Applies to appositional NPs (UD `appos` relation) whose head is a divine-name referent in `DIVINE_NAME_REFERENTS` and whose appositional dependent has a head lemma in `DIVINE_TITLE_HEADS`. Both narrative third-person uses (*"his name shall be Jesus Christ, the Son of God"*) and possessive-framed uses (*"Christ, the Holy One of Israel"*) are in scope. Single-token name-with-title compounds without an `appos` relation (e.g., *"Lord God Omnipotent"* as one unitary title) fall outside R22 — they are governed by R18 (fixed-idiom integrity) when the compound is lexicalized.

**Exclusions (closed list — each cites dominating rule).**

1. Divine-title appositive within a vocative environment (head of `appos` is also head of a `vocative`-tagged span, OR matrix predication satisfies R15's true-vocative test) → R15 (vocative indivisibility wins; appositive merges into vocative as one unit).
2. Single-token compound title without `appos` relation (e.g., *"Lord God Omnipotent"*, *"Lord of Sabaoth"* parsed as one lexicalized NP) → R18 (fixed-idiom integrity).
3. AICTP-frame-internal appositive (the appositional span occurs inside the AICTP token sequence) → R1 (AICTP integrity — the token sequence stays whole).
4. Date-colophon-frame-internal appositive (rare; the appositive occurs inside a date-colophon span) → R23 (date colophon integrity).
5. Same-passage repeated invocation already settled as MERGE earlier in the passage → boundary-case discipline (uniform treatment within one rhetorical beat; the first instance's classification governs subsequent instances in the same passage).
6. Same-passage repeated invocation already settled as STACK earlier in the passage → boundary-case discipline (uniform treatment; first instance governs).

**Precedence.** §3.5 Tier 5. Yields to R15 in vocative environment. Yields to R1/R18/R23 when the appositive falls inside a Tier-2 lexicalized closed-list span. Does NOT engage the §1.9 N=2 Adjudication Principle — appositional constructions are explicitly excluded from §1.9 (the synonymy test would mechanically fire "merge" on every appositive, which is the inverse of the rule's INTRODUCING/REFERENCING discrimination).

**Examples.**

- *Compliant (STACK — formal naming formula anchor):* "his name shall be Jesus Christ, / the Son of God" (2 Ne 25:19)
- *Compliant (STACK — prophetic proclamation frame anchor):* (a first-occurrence revelatory frame where the title appositive earns its own line)
- *Compliant (MERGE — REFERENCING default, no anchor):* "I am a disciple of Jesus Christ, the Son of God" (3 Ne 5:13)
- *Non-compliant (STACK split fired without any formal anchor):* "I am a disciple of Jesus Christ, / the Son of God" (REFERENCING context; the stack split is wrong because no anchor licenses it)
- *Non-compliant (MERGE retained despite formal naming formula anchor):* "his name shall be Jesus Christ, the Son of God" (the formal naming formula licenses STACK; merging is the violation)
- *Excluded by R15 (vocative environment):* "O God, the Eternal Father," (Moroni 4:3, 5:2 sacrament prayers; appositive merges into vocative as one indivisible address unit)
- *Excluded by R18 (fixed idiom):* "Lord God Omnipotent" (single lexicalized compound, no `appos` relation)
- *Excluded by uniform-treatment discipline:* a second invocation of *"Jesus Christ, the Son of God"* within the same rhetorical passage that opened with the MERGE-treatment must MERGE; the boundary case forbids oscillation within one passage.

**Implementation.**

- Validator: `validators/colometry/validate_rule_22_divine_title_appositive.py` (to be created; not yet implemented)
- Applier: `validators/apply_rule_22_divine_title_appositive.py` (to be created; not yet implemented)
- Closed-list definitions: §Divine-Title-Closed-Lists-R22 (in BoFM canon, supplementary section — to be created during validator implementation)
- Audit trail: `readers-bofm/private/audit-trail/R22.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R22.md`](../R22.md)
