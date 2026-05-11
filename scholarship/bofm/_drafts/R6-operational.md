# R6 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 6` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 6 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 6` (~10 lines mixing operational + rationale content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R6.md`](../R6.md) (full scholarship companion)

---

### R6: Causal Clauses Break

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A finite causal clause MUST be split from its matrix when the clause is in `advcl` attachment to a matrix VERB or ADJ head, is marked by the subordinator *because*, and the *because*-clause is NOT inside a clausal complement (`ccomp`) under a Rule-17 governor. The break MUST be inserted before the *because* mark. Non-clausal *because of* + NP prepositional constructions are NOT in scope and MUST NOT be split by this rule. Fronted-*because* (causal clause preceding the matrix) MUST be routed to REVIEW rather than mechanically split.

**UD signature.**
```yaml
trigger:
  relation: advcl
  head: { upos_in: [VERB, ADJ] }
  mark: { lemma: because }
  position: trailing   # because-clause follows the matrix
action: SPLIT_BEFORE_MARK
```

**Closed lists** (machine-readable).
```yaml
CAUSAL_MARK_LEMMAS:
  - because

# Rule 17 governor classes (defined at canon §Verb-Classes-R17).
# When a because-clause sits inside a ccomp under any verb in this set,
# R6 yields to R17's complement-integrity mandate.
R17_GOVERNOR_CLASSES:
  - causative      # cause, suffer, permit, command, grant
  - aspectual      # begin, cease, continue
  - speech         # say, speak, declare, testify, swear, proclaim, tell, ...
  - cognition      # know, believe, perceive, remember, understand, suppose, ...
  - volition       # wish, desire, hope, long, trust, pray, seek
  - FEF            # it was their lot to, it is expedient to
```

**Scope.** Finite *because*-clauses in trailing `advcl` attachment to a VERB or ADJ matrix head. The `advcl` head MUST be a VERB or ADJ; constructions where *because* heads a PP-equivalent (*"because of NP"*) fall outside this signature and are out of scope.

**Exclusions (closed list — each cites dominating rule).**

1. *Because of NP* PP-construction — *because* heads a prepositional construction (*"because of their wickedness"*); the `advcl` head is not a finite VERB/ADJ and no embedded subject + finite verb is present → out of scope (no R6 split)
2. Fronted-*because*: causal clause precedes the matrix predication (*"Because they had hardened their hearts, the Lord did smite them"*) → REVIEW-REQUIRED (break direction differs from trailing-because; not auto-applied)
3. *Because*-clause inside `ccomp` under an R17 governor (e.g., *"Do not suppose, because it has been spoken concerning restoration, that ye shall be restored..."* — Alma 41:10): the matrix + ccomp complement-integrity bond wins; splitting on the embedded causal would sever the R17 matrix from its *that*-complement → R17 (yields per §3.5 Tier 3 precedence over Tier 5)
4. Short-line context where the combined line passes the atomic-thought test → MAY merge under M4 (fragmented atomic thought-unit)

*Note on Exclusion 3 — Rule 17 precedence guard.* The check is structural: when the causal `advcl` attaches inside an enclosing `ccomp` whose `ccomp` head lemma is in `R17_GOVERNOR_CLASSES`, R17's complement-integrity bond between the R17 governor and its *that*-complement takes priority. Applying R6 inside such a configuration produces a Rule-17 violation (matrix governor severed from its *that*-complement across the embedded because-clause). The detector MUST traverse the parent chain of the *because*-advcl to verify no enclosing R17-governed ccomp before firing.

**Precedence.** §3.5 Tier 5. Yields to R17 (when the *because*-clause is inside a `ccomp` under an R17-class governor), to §1.12 Parallel-List Uniformity (within multi-verse parallel lists), and to M4 (short-line atomic-thought merge).

**Examples.**

- *Compliant (SPLIT):* "they did murmur against their father / because he had brought them out of the land"
- *Compliant (out of scope — because-of-NP PP, no split):* "because of their iniquities the Lord did chasten them" (PP-construction; no finite embedded clause)
- *Non-compliant (R6 violation — trailing finite because-clause not split):* "they did murmur against their father because he had brought them out of the land" (one line — matrix and causal frame not separated)
- *Excluded by R17 (no R6 split):* "Do not suppose, / because it has been spoken concerning restoration, / that ye shall be restored..." would violate R17 by severing *suppose* from its *that*-complement; correct treatment merges per R17 → "Do not suppose, because it has been spoken concerning restoration, that ye shall be restored..." (Alma 41:10; R6 yields)
- *Excluded by REVIEW (fronted-because):* "Because they had hardened their hearts, ..." — break direction differs; routed to REVIEW

**Implementation.**

- Validator: [`validators/colometry/validate_rule_06_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_06_ud.py)
- Applier: [`validators/apply_rule_06_ud.py`](../../../../readers-bofm/validators/apply_rule_06_ud.py)
- Closed-list definitions: in validator source (`CAUSAL_MARK_LEMMAS`, R17 governor classes per `validate_rule_17_ud.py`)
- Audit trail: `readers-bofm/private/audit-trail/R6.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R6.md`](../R6.md)
