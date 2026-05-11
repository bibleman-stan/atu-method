# R26 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 26` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 26 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 26` (~23 lines mixing operational + rationale + closed-list audit narrative + dropped-lemma history)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R26.md`](../R26.md) (full scholarship companion)

---

### R26: Adjective (or NOUN-as-Predicate) + "That" Complement Stays Together

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A predicate complement-taker's clausal *that*-complement MUST be on the same v2-mine line as its predicate head when the head lemma belongs to one of the two closed lists below. The ADJ-predicate sub-class fires when the head UPOS is `ADJ` and the lemma is in `R26_ADJ_PREDICATES`. The NOUN-as-predicate sub-class fires when the head UPOS is `NOUN`, the lemma is in `R26_NOUN_PREDICATES`, and the head bears a copular dependent (`cop`) plus an `acl` *that*-clause. When the LLM annotator tags the *that*-clause as `advcl` but the matrix head lemma is in either closed list, the annotation MUST be overridden and treated as `ccomp` (ADJ branch) or `acl` (NOUN branch) for purposes of this rule.

**UD signature.**
```yaml
trigger_adj_predicate:
  relation: ccomp
  head: { upos: ADJ, lemma_in: R26_ADJ_PREDICATES }
  mark: { lemma: that }
action: MERGE_HEAD_AND_DEPENDENT

trigger_noun_as_predicate:
  relation: acl
  head: { upos: NOUN, lemma_in: R26_NOUN_PREDICATES }
  cop: { lemma_in: [be] }
  mark: { lemma: that }
action: MERGE_HEAD_AND_DEPENDENT
```

**Closed lists** (machine-readable).
```yaml
R26_ADJ_PREDICATES:
  - possible
  - expedient
  - desirous
  - necessary
  - needful
  - impossible
  - better
  - well
  - requisite

R26_NOUN_PREDICATES:
  - wisdom
```

**Scope.** Predicate complement-taker frames of the form *it is X that Y* (and minor inversions, e.g., *X it is that Y*) where X is the head lemma. The rule governs the outer boundary between the predicate head and its *that*-clause. Internal structure of the *that*-clause is evaluated separately. Matrix VERB heads are out of scope (route to R17). Matrix NOUN heads not in `R26_NOUN_PREDICATES` are out of scope.

**Exclusions (closed list — each cites dominating rule).**

1. AICTP *that* — token sequence "And it came to pass that" → R1 / R16
2. Vocative on matrix line — vocative wins its own-line mandate → R15
3. Compound subordinator *insomuch that* — mark is the compound, not simple *that* → R27
4. Direct discourse (colon-terminated speech-tag introducing the *that*-clause as quotation onset) → J3
5. *for*-infinitive frame instead of finite *that*-complement (e.g., *it is meet for X to Y*) — not a R26 trigger; out of scope
6. Head lemma in `R26_NOUN_PREDICATES` used as noun-modifier rather than predicate (no `cop` dependent on the head) — out of scope; R26 does not fire

**Precedence.** §3.5 Tier 3. Wins over R7 (purpose) and R17 (verb-complement) when the matrix head is ADJ in `R26_ADJ_PREDICATES` or NOUN in `R26_NOUN_PREDICATES`. Yields to Tier 1 (Layer 1 mid-phrase prohibitions), Tier 2 (R1 / R16 AICTP, R15 vocative, R18 fixed idiom, R23 date colophon), and J3 direct-discourse onset.

**Examples.**

- *Compliant (ADJ predicate, MERGE):* "if it were possible that our first parents..."
- *Compliant (ADJ predicate, MERGE):* "it is expedient that ye should know the things..."
- *Compliant (NOUN-as-predicate, MERGE):* "it is wisdom in God that these things should be shown unto you..."
- *Non-compliant (R26 violation):* "if it were possible / that our first parents..." (matrix predicate severed from *that*-complement)
- *Excluded by R7 (matrix VERB, out of R26 scope):* "he went forth among the people / that he might preach the word of God" — matrix is VERB; R7 governs
- *Excluded by R17 (matrix VERB, out of R26 scope):* "I say unto you that the time shall come" — matrix is VERB in R17 governing class
- *Excluded by R15 (vocative wins):* a vocative on the matrix line keeps the vocative on its own atomic-thought unit per R15
- *Excluded (out of scope — for-infinitive frame):* *it is meet for X to Y* — non-finite *for*-infinitive, not a finite *that*-complement; R26 does not fire

**Implementation.**

- Validator: [`validators/colometry/validate_rule_07_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_07_ud.py) (R26 routing applied via `RULE_26_HEAD_LEMMAS` set + `is_rule_26_class` filter — Rule 7 detector routes R26-class matches away from R7)
- Applier: shares R7 applier pipeline; R26-class matches resolve to MERGE rather than SPLIT
- Closed-list definitions: in validator source (`RULE_26_HEAD_LEMMAS`)
- Audit trail: `readers-bofm/private/audit-trail/R26.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R26.md`](../R26.md)
