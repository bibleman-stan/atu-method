# R7 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 7` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 7 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 7` (~35 lines mixing operational + rationale + corpus-empirics + audit-precedent content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R7.md`](../R7.md) (full scholarship companion)

---

### R7: Purpose Clauses Break

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A finite purpose clause MUST be split from its matrix when the clause is in `advcl` attachment to a matrix VERB, is marked by the simple subordinator *that*, and contains a modal auxiliary (`may`, `might`, `shall`, `should`, `will`, `would`, `can`, `could`, `must`). The break MUST be inserted before the *that* mark. Non-finite infinitival purpose adjuncts (*to + VERB + complement*, without subject or modal) are NOT in scope and MUST NOT be split from their matrix motion verb by this rule.

**UD signature.**
```yaml
trigger:
  relation: advcl
  head: { upos: VERB }
  mark: { lemma: that }
  aux: { lemma_in: MODAL_AUX_LEMMAS }
action: SPLIT_BEFORE_MARK
```

**Closed lists** (machine-readable).
```yaml
MODAL_AUX_LEMMAS:
  - may
  - might
  - shall
  - should
  - will
  - would
  - can
  - could
  - must

RULE_26_HEAD_LEMMAS:
  - expedient
  - needful
  - necessary
  - wisdom        # NOUN-as-predicate
  - possible
  - desirous
  - impossible
  - better
  - well
  - requisite

RESULT_DEGREE_MARKERS:
  - so
  - such
```

**Scope.** Finite *that* + MODAL purpose clauses with VERB matrix head. Non-finite infinitival purpose adjuncts (bare *to + VERB*) are out of scope and merge with their matrix motion verb. Matrix ADJ or NOUN-as-predicate heads are out of scope (route to R26).

**Exclusions (closed list — each cites dominating rule).**

1. Compound subordinator *insomuch that* — the mark is the compound, not simple *that*; consecutive-result semantics → R27
2. Matrix head lemma in `RULE_26_HEAD_LEMMAS` (ADJ predicate or NOUN-as-predicate *wisdom*) — the LLM annotation is likely mistagged; structural truth is ccomp/acl complement-integrity → R26
3. Consecutive-result construction: matrix's modifier (ADJ or ADV) carries `advmod` or `amod` dependent in `RESULT_DEGREE_MARKERS`, AND the *that*-clause is in `advcl` attachment as the consequence (*"so numerous that they could not be numbered"*, *"such great force that the city was destroyed"*) — result-clause reading governs; no R7 split
4. Idiomatic *even so that* result connector — pre-mark token sequence *even ... so* in the preceding 3 tokens → result-clause reading
5. Multi-verse list with parallel-list uniformity scope (e.g., Moroni 10:8-17) → §1.12 Parallel-List Uniformity wins
6. Short-line context where the combined line passes the atomic-thought test → MAY merge under M4 (fragmented atomic thought-unit)

*Note on Exclusion 3 discriminator:* Surface presence of *so/such* alone is not sufficient. The discriminator is the UD attachment. *Such great X (NP) that ye may Y* — where *such* attaches as `det` to the head noun, not as `advmod`/`amod` scoping a modifier — is genuine R7 purpose territory, not consecutive-result.

**Precedence.** §3.5 Tier 5. Yields to R27 (insomuch-that compound mark), R26 (matrix ADJ/NOUN-as-predicate complement), result-clause reading (so/such as advmod/amod scoping matrix modifier), and §1.12 Parallel-List Uniformity (multi-verse parallel lists).

**Examples.**

- *Compliant (SPLIT):* "he went forth among the people / that he might preach the word of God unto them"
- *Compliant (non-finite infinitive merges, NOT R7):* "he has gone to the land of Ishmael, to teach the people of Lamoni" (Alma 22:4)
- *Non-compliant (R7 violation — finite purpose clause not split):* "he went forth among the people that he might preach the word of God unto them" (one line — matrix and purpose-frame not separated)
- *Excluded by R27:* "And he did minister unto them, / insomuch that his whole household were converted unto the Lord" (Alma 22:23) — compound subordinator *insomuch that*; R27's 3-condition test governs
- *Excluded by R26:* "if it were possible that our first parents..." — matrix is ADJ `possible` in RULE_26_HEAD_LEMMAS; structural truth is ccomp complement-integrity → MERGE
- *Excluded by result-clause reading:* "so numerous that they could not be numbered" — *so* scopes *numerous* as `advmod`; consecutive consequence, not purpose

**Implementation.**

- Validator: [`validators/colometry/validate_rule_07_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_07_ud.py)
- Applier: [`validators/apply_rule_07_ud.py`](../../../../readers-bofm/validators/apply_rule_07_ud.py)
- Closed-list definitions: in validator source (`MODAL_AUX_LEMMAS`, `RULE_26_HEAD_LEMMAS`, `RESULT_DEGREE_MARKERS`)
- Audit trail: `readers-bofm/private/audit-trail/R7.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R7.md`](../R7.md)
