# R13a Operational Entry — Layer-1 Pointer

### R13a: Never End a Line on a Preposition Seeking Its Object

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern (UD-confirmable)
**Layer:** 1 (generic English grammar)

**Rule.** A v2-mine line MUST NOT end on an adposition (`ADP`) that has a pending `case` relation to an object on the following line. When the line-final token is tagged `ADP` and its object-NP is on the next line, the `ADP` MUST be moved to lead the next line (joined with its object).

**UD signature.**
```yaml
trigger:
  line_final_token: { upos: ADP, pending_case: true }
action: MERGE_FORWARD
```

**Scope.** Generic English-grammatical fact. A preposition alone at line end strands its object on the next line, fragmenting the PP and failing the atomic-thought test.

**Exclusions.**
1. **Phrasal-verb particles tagged `compound:prt`** — these are part of the verb's lexical structure, not prepositions seeking an object. R13a does not fire.
2. **Stranded prepositions in relative clauses** — *"the man whom he spake of"* — the `of` is grammatically licensed as stranded; R13a does not fire when UD parse marks the ADP as stranded.
3. ADP within a fixed multi-word unit → R18 keeps the unit whole.

**Precedence.** §3.5 Tier 1 (Layer 1 syntax veto; MALFORMED-class). Wins over all Tier 2+ generative rules at the same location.

**Examples.**
- Compliant: `"He sat down / on the throne"` (ADP `on` leads the new line with its NP)
- Non-compliant: `"He sat down on /\n the throne"` (line-final `on`; MALFORMED)
- Excluded (phrasal-particle): `"He gave up / and departed"` (`up` here is `compound:prt`, part of the verb)
- Excluded (stranded relative): `"the man whom he spake of, / who came from afar"` (stranded `of` in relative clause)

**Implementation.**
- Layer 1 reference: [`data/syntax-reference/ud-taxonomy.md §7`](../../../../readers-bofm/data/syntax-reference/ud-taxonomy.md) row: *line-final `ADP` with pending `case` relation* → `REQUIRED-MERGE`
- Validator: `validators/syntax/validate_line_final_tokens.py`
- Applier: (none — surface-pattern Layer-1)
- Audit trail: `private/audit-trail/R13a.md`
- Scholarship: `atu-method/scholarship/bofm/R13a.md`
