# R19 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 19` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 19 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 19` (~32 lines mixing operational + rationale + validator-architecture narrative + audit-empirics content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R19.md`](../R19.md) (full scholarship companion)

---

### R19: Cataphoric "That"/Relative Clauses Break; Anaphoric Merge

**Status:** Active
**Category:** A (Mechanical, mandatory) for the PROPN and PRON/DET branches; B (Editorial, judgment-required) for the NOUN branch routed to REVIEW
**Decidability:** Mixed — UD-pattern for PROPN-head and PRON/DET-head branches; Discourse-context-needed for NOUN-head branch (routed to REVIEW-REQUIRED)
**Layer:** 3

**Rule.** A relative clause (UD `acl:relcl`) or non-complement *that*-clause (UD `acl`) attached to a head noun-phrase MUST be classified by the head token's UPOS and treated as follows. When the head UPOS is **PROPN**, the relative is anaphoric and the relative MUST be merged onto the head's line. When the head UPOS is **PRON** or **DET**, the relative is cataphoric and a line break MUST be inserted before the relative pronoun (*which*, *that*, *who*, *whoso*, *whatsoever*). When the head UPOS is **NOUN**, the case MUST be routed to REVIEW-REQUIRED — mechanical resolution is not authorized. Expletive *it* in cleft constructions (*"that it is by his grace"*) and result/purpose clauses with new predication (*"that it is good"*) are NOT anaphoric regardless of surface anaphor-like material; these route per Exclusions below. When a *that*-clause is the complement of a Rule 17 governing verb, R17 wins and R19 MUST NOT fire.

**UD signature.**
```yaml
trigger_anaphoric_propn:
  relation: [acl:relcl, acl]
  head: { upos: PROPN }
  excludes: { relation_at_head: ccomp }   # R17 wins
action: MERGE_HEAD_AND_DEPENDENT

trigger_cataphoric_pron_det:
  relation: [acl:relcl, acl]
  head: { upos: [PRON, DET] }
  excludes: { relation_at_head: ccomp }   # R17 wins
action: SPLIT_BEFORE_RELATIVE

trigger_noun_head_ambiguous:
  relation: [acl:relcl, acl]
  head: { upos: NOUN }
  excludes: { relation_at_head: ccomp }   # R17 wins
action: REVIEW

trigger_predicative_identifier:
  relation: [acl:relcl, acl]
  head: { upos: NOUN }
  mark: { lemma: which }
  relative_body_pattern: "(is|was|are|were|became) + classifier-NP"
  semantic_role: predicative-identifier   # classifies/identifies head; advances no new action
action: MERGE_HEAD_AND_DEPENDENT
```

**Closed lists** (machine-readable).
```yaml
ANAPHORIC_UPOS:
  - PROPN

CATAPHORIC_UPOS:
  - PRON
  - DET

REVIEW_UPOS:
  - NOUN

PREDICATIVE_IDENTIFIER_COPULAS:
  - is
  - was
  - are
  - were
  - became
```

The `CATAPHORIC_UPOS` set captures the generic forward-pointer heads characteristic of BoFM-English: *those*, *whoso*, *whatsoever*, *all*, *any*, *every*, *this*, *that*, *these*. Membership is determined by the UD parser's UPOS tag, not by a lexical list.

**Scope.** Non-complement *that*-clauses and relative clauses (`acl:relcl` or `acl`) attached to a noun-phrase head. The rule fires on the head token's UPOS only; lemma membership is not consulted. The unified "which"-clause decision tree (predicative-identifier MERGE, completing-predication MERGE, non-restrictive-relative-introducing-new-info SPLIT, cataphoric-advancing SPLIT, anaphoric-backward-referring MERGE) operates as a sub-rule of the three UPOS branches above: predicative-identifier and completing-predication patterns under NOUN heads are MERGE; all other NOUN-head cases route to REVIEW pending discourse-context resolution.

**Exclusions (closed list — each cites dominating rule).**

1. Complement of a Rule 17 governing verb (matrix VERB lemma in `GOVERNING_LEMMAS_R17`; `ccomp` relation at the head) → R17 wins; *that*-clause merges with matrix per complement integrity
2. Complement of a Rule 26 predicate (ADJ or NOUN-as-predicate head in `RULE_26_HEAD_LEMMAS`) → R26 wins; *that*-clause merges with predicate
3. AICTP *that* (token sequence "And it came to pass that") → R1 / R16 win
4. Purpose finite *that* + MODAL (advcl + modal aux) → R7
5. Compound subordinator *insomuch that* → R27
6. Fixed-idiom contexts (*it is expedient that*, etc., per Rule 18 fixed-idiom list) → R18 wins
7. Expletive *it* in cleft constructions (*"that it is by his grace"*) — structural placeholder, NOT anaphoric; routes per other applicable rules
8. Result/purpose clauses with new predication (*"that it is good"*) — cataphoric semantics override anaphor-like surface form; the relative-pronoun head test does not apply
9. Cross-line attachments where the relative is NOT adjacent to its head (gap > 1 v2 line) → REVIEW-REQUIRED (parser ambiguity guard)
10. Merged-line length > 130 characters → REVIEW-REQUIRED (length backstop, per applier convention)

**Precedence.** §3.5 Tier 5. Yields to R1/R16 (AICTP), R17 (complement integrity), R26 (predicate complement), R7 (purpose + modal), R18 (fixed idiom), R27 (insomuch-that). Per §3.5.1 "that"-cluster sub-hierarchy, R19 is the residual-relative branch — the most-specific-first detection order routes R1/R16, R26, R17, R27, and R7 ahead of R19. R19 fires only on `acl:relcl` (and non-complement `acl`) attachments after all complement / formulaic / purposive readings have been excluded.

**Examples.**

- *Compliant (cataphoric SPLIT, PRON head):* "I say unto you / that the good shepherd doth call you" — *that*-clause advances new image and new action under a generic forward-pointing head
- *Compliant (cataphoric SPLIT, DET head):* "those / which shall keep my commandments" — *those* is a generic forward-pointer; relative introduces qualifying predication
- *Compliant (anaphoric MERGE, PROPN head):* "the brass plates which Lehi obtained" — *Lehi* is a named referent; relative is backward-pointing characterization
- *Compliant (anaphoric MERGE, established discourse):* "The Spirit hath not said unto me that this should be the case" — *this* and *the case* both point back; merge
- *Compliant (predicative-identifier MERGE, NOUN head sub-rule):* "commandment which is the word of God" — *which is + classifier-NP* names/classifies the head without advancing new action
- *Non-compliant (R19 violation — cataphoric not split):* "I say unto you that the good shepherd doth call you" (one line — generic frame not separated from new image)
- *Non-compliant (R19 violation — anaphoric improperly split):* "Adam / which was the first man" (PROPN head; anaphoric relative wrongly broken from named referent)
- *Excluded by R17 (complement integrity wins):* "He caused that his servants should stand forth" — *that*-clause is the `ccomp` of the causative VERB *cause*; R17 governs the merge, R19 does not fire
- *Excluded by R26:* "if it were possible that our first parents..." — matrix is ADJ *possible* in `RULE_26_HEAD_LEMMAS`; R26 governs the merge
- *Routed to REVIEW (NOUN head, ambiguous):* "records which were engraven upon the plates of brass" — anaphoricity depends on whether *plates of brass* was established earlier in the passage; mechanical resolution not authorized

**Implementation.**

- Validator: [`validators/colometry/validate_rule_19_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_19_ud.py)
- Applier (anaphoric MERGE branch): [`validators/apply_rule_19_ud_merge.py`](../../../../readers-bofm/validators/apply_rule_19_ud_merge.py)
- Closed-list definitions: `ANAPHORIC_UPOS`, `CATAPHORIC_UPOS` in validator source
- Applier filters: adjacency gap = 1, merged-line length ≤ 130 characters (Jarom-1:8-style catastrophe guard)
- Audit trail: `readers-bofm/private/audit-trail/R19.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R19.md`](../R19.md)
