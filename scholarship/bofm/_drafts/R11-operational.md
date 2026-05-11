# R11 Operational Entry — Layer-1 Pointer

### R11: Never End a Line on an Article (Determiner)

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern (UD-confirmable)
**Layer:** 1 (generic English grammar)

**Rule.** A v2-mine line MUST NOT end on a determiner (`DET`). When the line-final token is tagged `DET`, that token MUST be moved to lead the next line (with its head noun phrase).

**UD signature.**
```yaml
trigger:
  line_final_token: { upos: DET }
action: MERGE_FORWARD
```

**Scope.** Generic English-grammatical fact. A determiner alone at line end strands its head noun on the next line, creating an incomplete NP and failing the atomic-thought test at the line boundary.

**Exclusions.**
1. DET within a fixed multi-word unit → R18 keeps the unit whole.
2. Determiner-pronoun uses where the DET stands alone as a referent (rare in BoFM-English) → context-dependent, route to REVIEW.

**Precedence.** §3.5 Tier 1 (Layer 1 syntax veto; MALFORMED-class). Wins over all Tier 2+ generative rules at the same location.

**Examples.**
- Compliant: `"He gathered together / the people of his land"` (DET `the` leads the new line)
- Non-compliant: `"He gathered together the /\n people of his land"` (line-final `the`; MALFORMED)
- Excluded: `"He saw the sun rise"` (no line-final DET; R11 does not fire)

**Implementation.**
- Layer 1 reference: [`data/syntax-reference/ud-taxonomy.md §7`](../../../../readers-bofm/data/syntax-reference/ud-taxonomy.md) row: *line-final `DET`* → `REQUIRED-MERGE`
- Validator: `validators/syntax/validate_line_final_tokens.py`
- Applier: (none — surface-pattern Layer-1)
- Audit trail: `private/audit-trail/R11.md`
- Scholarship: `atu-method/scholarship/bofm/R11.md`
