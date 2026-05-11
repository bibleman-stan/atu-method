# R21 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 21` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 21 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 21` (~11 lines mixing operational + rationale + diagnostic-test content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R21.md`](../R21.md) (full scholarship companion)

---

### R21: Participial Absolute Integrity

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A participial absolute — a subject-bearing participial clause of the form *"X having Y-ed"* or *"X being Y"* — MUST occupy its own v2-mine line, distinct from its matrix predication. The participial absolute is identified by the UD pattern of an `nsubj`-bearing non-finite VERB (participial form, no finite `aux`) attached as an adjunct (`advcl`, `acl`, or `parataxis`) to a matrix clause. The matrix's own subject and finite predication MUST appear on the following line. The participial absolute MUST NOT be split internally; subject, participle, and any complement of the participial remain on the one shared line.

**UD signature.**
```yaml
trigger:
  relation: [advcl, acl, parataxis]
  head:
    upos: VERB
    feats: { VerbForm: [Part, Ger] }     # participial / gerundive form
    has_finite_aux: false                 # no finite auxiliary in the participial clause
  required_dependent:
    relation: nsubj
    upos: [PROPN, PRON, NOUN]            # subject of the participial — what makes it absolute
  matrix:
    has_distinct_nsubj: true              # matrix carries its own subject (or co-referent restart)
action: STAND_OWN_LINE
```

*Note on action code.* The standard `§Action-Codes` table in [`docs/rule-template.md`](../../../docs/rule-template.md) does not include a code for "the matched span MUST occupy its own line, with breaks both before and after the span." `STAND_OWN_LINE` is the proposed extension for this operational effect; it covers R21 and parallels the conceptually similar effect of `STACK_LIST_MEMBERS` (each member earns its own line) but for a single-span case rather than a series. Per §Action-Codes, new codes require a meta-template change — flagged for migration-batch ratification. Pending ratification, implementers may treat the action as the conjunction of `SPLIT_BEFORE_SUBJECT` (before the participial's own subject) and `SPLIT_BEFORE_SUBJECT` (before the matrix's resumptive subject) — but the unified `STAND_OWN_LINE` code is preferred for operational clarity.

**Diagnostic — paraphrase test.** The participial clause MUST pass the finite-paraphrase test: rewriting *"X having Y-ed"* → *"X had Y-ed"* (or *"X being Y"* → *"X was Y"*) MUST yield a complete sentence that can stand alone. A failed paraphrase indicates the construction is not an absolute and routes elsewhere (see Exclusions).

**Scope.** Subject-bearing participial clauses functioning as absolute adjuncts to a matrix predication. The participial's subject is morphologically present in the text (named NP, PROPN, or non-elided PRON). The matrix clause has its own subject (or a restart of the participial's subject) and its own finite verb.

**Exclusions (closed list — each cites dominating rule).**

1. Bare participial without its own subject (subject-inheriting from matrix) — out of scope; routes to M3 (bare-governor indivisibility, framework §1.5 M3) including M3's bare-trailing-participial extension.
2. Bare participial-heading frames awaiting clausal complement (*"telling them / that there could be no atonement..."*) — out of scope; routes to M3 (bare-governor indivisibility) until the complement is resolved.
3. Vocative attached to or interleaved with the participial absolute (*"O Lord, thou having..."* shape) — R15 wins on the vocative's own-line mandate; the participial absolute remains own-line per R21, with R15 governing the vocative's boundary.
4. Participial absolute whose subject is the divine title in a stack-split INTRODUCING context — R22 governs the stack treatment of the divine-title head; R21 still places the participial absolute on its own line, but R22's STACK SPLIT for the appositive operates on the head NP before R21's own-line treatment of the whole absolute.
5. Date-colophon participials embedded in a date-colophon formula (*"in the Nth year of the reign of the judges, the X having Y-ed..."*) — R23 (date colophon integrity) wins on the formula's KEEP_WHOLE mandate; R21's own-line treatment yields within the colophon's protected span.

**Precedence.** §3.5 Tier 5. Yields to R15 (vocative environment), R23 (date-colophon integrity). Wins over M3 (M3 covers BARE participials only; subject-bearing participials are R21's territory by SCOPE distinction, not by tier ordering — the two rules partition the participial space rather than collide). Coexists with R17 / R26 / R19 / R7 / R27 on the matrix clause's separate operational treatment (R21 governs the absolute; the matrix's own complement / purpose / relative / consecutive analysis proceeds independently on the matrix line).

**Examples.**

- *Compliant (own line, participial absolute):* "I, Nephi, having been born of goodly parents, / therefore I was taught somewhat in all the learning of my father" (1 Ne 1:1) — "I, Nephi, had been born of goodly parents" passes the finite-paraphrase test.
- *Compliant (own line, participial absolute with matrix-restart):* "And yet, I being over-zealous to inherit the land of our fathers, / collected as many as were desirous to go up to possess the land" (Mos 9:3) — "I was over-zealous to inherit the land of our fathers" passes the finite-paraphrase test; matrix verb *collected* takes the participial's subject as restart.
- *Non-compliant (R21 violation — participial absolute merged with matrix):* "I, Nephi, having been born of goodly parents was taught somewhat in all the learning of my father" (one line) — the participial absolute is grammatically independent and MUST be set off.
- *Non-compliant (R21 violation — participial absolute split internally):* "I, Nephi, / having been born of goodly parents, / therefore I was taught..." — the subject and its participle MUST stay on the one absolute line.
- *Excluded by M3 (bare participial — no own subject):* "telling them / that there could be no atonement..." — *telling* has no morphological subject in its clause; M3 governs.
- *Excluded by R15 (vocative environment):* "O Lord, thou having delivered me..." — vocative *"O Lord"* takes its own line per R15; R21 places the *"thou having delivered me"* absolute on its own following line.

**Implementation.**

- Validator: `validators/colometry/validate_rule_21_ud.py` (to be created during migration)
- Applier: `validators/apply_rule_21_ud.py` (to be created during migration)
- Closed-list definitions: none — R21 fires on UD-feature pattern, not on a lexical closed list
- Audit trail: `readers-bofm/private/audit-trail/R21.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R21.md`](../R21.md)
