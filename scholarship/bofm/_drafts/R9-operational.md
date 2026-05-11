# R9 Operational Entry — Layer-1 Pointer

### R9: Never End a Line on a Conjunction

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** Surface-pattern (UD-confirmable)
**Layer:** 1 (generic English grammar)

**Rule.** A v2-mine line MUST NOT end on a coordinating conjunction (`CCONJ`). When the line-final token is tagged `CCONJ`, that token MUST be moved to lead the next line.

**UD signature.**
```yaml
trigger:
  line_final_token: { upos: CCONJ }
action: MERGE_FORWARD
```

**Scope.** Generic English-grammatical fact, not a BoFM-specific editorial decision. Applies to every line where the final token's UPOS is `CCONJ`. Coordinating conjunctions (`and`, `or`, `nor`, `but`, `for`, `yet`, `so`) stranded at line end create the expectation of a following member and therefore violate the atomic-thought test.

**Exclusions.**
1. CCONJ within fixed multi-word units → R18 keeps the unit whole; R9 does not fire on conjunctions inside the protected span.
2. CCONJ that is the LAST token of the entire verse with no following line → handled by terminal-position discipline (not R9 territory).

**Precedence.** §3.5 Tier 1 (Layer 1 syntax veto; MALFORMED-class). Wins over all Tier 2+ generative rules at the same location.

**Examples.**
- Compliant: `"the heavens and the earth / and all things therein"` (the `and` leads the new line)
- Non-compliant: `"the heavens and the earth and /\n all things therein"` (line-final `and`; MALFORMED)
- Excluded: `"He died in old age, / having fulfilled all his days,"` (no line-final CCONJ; R9 does not fire)

**Implementation.**
- Layer 1 reference: [`data/syntax-reference/ud-taxonomy.md §7`](../../../../readers-bofm/data/syntax-reference/ud-taxonomy.md) row: *line-final `CCONJ`* → `REQUIRED-MERGE`
- Validator: `validators/syntax/validate_line_final_tokens.py`
- Applier: (none — surface-pattern Layer-1; corpus is hand-authored at this granularity, validator reports MALFORMED on violations)
- Audit trail: `private/audit-trail/R9.md`
- Scholarship: `atu-method/scholarship/bofm/R9.md`
