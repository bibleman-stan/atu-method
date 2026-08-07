# Constraint-Catalog Entry Template — Operational Specification

Every constraint in every per-corpus canon's §5 (Constraint Detail) MUST follow the template specified here. The template is operational: it contains what an audit-stage validator needs to apply the constraint correctly. Rationale, defensibility arguments, scholarly grounding, audit trail, and corpus-experiment narratives do not appear in the constraint entry; they live in the per-constraint scholarship companion (`scholarship/<constraint-id>.md`) and audit trail (`audit-trail/<constraint-id>.md`).

This template draws on:

- **MISRA C:2012/2023** rule-spec format (per-rule template, Category, Decidability)
- **RFC 2119 / BCP 14 / RFC 8174** for normative-language keywords (MUST, MUST NOT, SHALL, SHOULD, MAY)
- **W3C Specification process** for Status flags
- **UD Guidelines** for relation cross-references

---

## Scope — universal shape, per-corpus vocabulary

This template specifies a universal field shape that all per-corpus constraint entries follow (Constraint ID, Title, Status, Category, Decidability, Encoded-question, Verdict-family, Source-reference, UD signature, Scope, Exclusions, Precedence, Examples, Implementation). The vocabulary inside the fields is per-corpus:

- **Detector primitives** vary by corpus. Hebrew needs `verbless` as a primitive because Hebrew typologically requires verbless-clause handling; BoFM and GNT do not.
- **Closed-list contents** vary by corpus. The Hebrew restrictive-`אֲשֶׁר` constraint lists Hebrew relative-clause structures; the Greek restrictive-`ὅς` constraint lists Greek structures.
- **Verdict-family codes** are universal (see §Verdict-Families below).
- **UD signature templates** are universal in shape (`trigger:`, `head:`, `mark:`); the specific deprels, UPOS values, and lemmas are corpus-specific.

The cross-corpus equivalence map at [`rule-equivalence-map.md`](rule-equivalence-map.md) catalogues which constraints are doing the same underlying work across corpora vs which are corpus-unique.

---

## Template

```markdown
### {Constraint-ID}: {Title}

**Status:** {Active | Proposed | Retired}
**Category:** {A (Mechanical, mandatory) | B (Editorial, judgment-required) | C (Theological, hand-curation)}
**Decidability:** {Surface-pattern | UD-pattern | Discourse-context-needed}

**Encoded question.** {One sentence. A yes/no grammatical question. e.g., "Is this break inside a construct chain (bare governor + genitive)?" or "Is this `אֲשֶׁר`-clause restrictive (head not uniquely identified without it)?"}

**Verdict family.** {One of: BIND | SPLIT-CANDIDATE | MERGE | VIOLATION-FLAG | NO-EFFECT. See §Verdict-Families.}

**Source reference.** {Grammar authority citation. e.g., "Joüon-Muraoka §158a–c" or "Smyth §2496" or "Skousen *Critical Text* 2009, p.42".}

**Constraint.** {One paragraph. Normative. Uses RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY). States WHAT the constraint requires; does not justify or explain.}

**UD signature.**
~~~yaml
trigger:
  relation: [<deprel>, ...]
  head: { upos: <UPOS>, lemma_in: <closed-list-name> }
  mark: { lemma_in: [<lemma>, ...] }
verdict: <one of the standard verdict-family codes>
~~~

**Closed lists** (machine-readable).
~~~yaml
<closed-list-name>:
  - lemma1
  - lemma2
  ...
~~~

**Scope.** {Operational boundary — where the constraint applies. Single paragraph.}

**Exclusions (closed list — each cites dominating constraint).**
1. {Description of excluded case} → {Constraint-ID} | §{X}
2. ...

**Precedence.** §3.5 Tier {N}. {Yields-to / Wins-over notation, one line, stable IDs only.}

*Note:* §3.5 is the single source of truth for cross-constraint precedence. The per-constraint Precedence field MUST be consistent with §3.5's tier placement.

**Examples.**
- *Constraint fires (verdict applies):* "{example case where the constraint's yes/no question answers yes}"
- *Constraint does not fire (no-effect):* "{example case where the constraint's yes/no question answers no}"
- *Excluded by {Constraint-ID}:* "{example where dominating constraint takes precedence}"

**Implementation.**
- Validator: `validators/<subfolder>/validate_<constraint-id>.py`
- Closed-list definitions: §<list-section>
- Audit trail: `private/audit-trail/<constraint-id>.md`
- Scholarship: `private/01-method/scholarship/<constraint-id>.md`
```

---

## Required fields

Every constraint entry MUST include all of the following:

| Field | Purpose | Allowed values |
|---|---|---|
| **Constraint ID** | Stable, persistent identifier | Stable string (e.g., `Restrictive-Relative-Binding`, `Construct-Chain-Indivisibility`, `Discourse-Particle-Binding`) |
| **Title** | Short, descriptive name | Free text (max ~10 words) |
| **Status** | Lifecycle state | Active / Proposed / Retired |
| **Category** | Application-confidence tier | A / B / C, OR multi-valued split-form |
| **Decidability** | Whether the constraint can fire mechanically | Surface-pattern / UD-pattern / Discourse-context-needed, OR multi-valued split-form |
| **Encoded question** | The yes/no grammatical question | One sentence, ending with "?" |
| **Verdict family** | What the constraint flags when it fires | One of BIND / SPLIT-CANDIDATE / MERGE / VIOLATION-FLAG / NO-EFFECT |
| **Source reference** | Grammar authority citation | Joüon-Muraoka §X / Smyth §Y / etc. |
| **Constraint** | The normative statement | One paragraph, RFC 2119 keywords |
| **UD signature** | Machine-readable trigger | YAML block |
| **Scope** | Where the constraint applies | One paragraph |
| **Exclusions** | Closed-list carve-outs | Numbered list, each citing dominating constraint |
| **Precedence** | Reference to §3.5 | One-line reference |
| **Examples** | Constraint-fires + constraint-does-not-fire + excluded | At minimum: 1 fires, 1 no-effect, 1 excluded |
| **Implementation** | File path references | Validator, audit trail, scholarship. When no auto-applier exists (Category-B constraints), use: `Applier: (none — <reason>)` |

---

## §Verdict-Families — what a constraint flags when it fires

The `verdict` field of a constraint's UD signature MUST be one of these standard verdict families. New verdict families require a meta-template change (`change-protocol.md` §7.3 trigger #9).

| Verdict family | Effect | Used by |
|---|---|---|
| **BIND** | The constraint flags the proposed break as forbidden; the two sides must be one ATU | Restrictive-relative binding, construct-chain indivisibility, discourse-particle binding, attendant-circumstance participle binding |
| **SPLIT-CANDIDATE** | The constraint flags the line as containing two independent propositions; the editor should consider splitting | Coordinate `וְ` / `καί` / "and" linking two finite-verb clauses with same subject (each may be its own ATU under the bidirectional test) |
| **MERGE** | The constraint flags the proposed break as requiring merge; the line above fails forward closure | Bare construct-state noun awaiting genitive, bare resumptive pronoun, bare adverbial PP with no own verb |
| **VIOLATION-FLAG** | The constraint flags the break as violating a syntactic rule; editorial review required | Cases where the proposed break is in a syntactically illegal location but the resolution is not obvious from the constraint alone |
| **NO-EFFECT** | The constraint's yes/no question answered "no" for this break; no action required | Default for non-firing instances |

**Producer-style verdicts are forbidden.** The verdict field MUST NOT contain codes like `MERGE_FORWARD`, `SPLIT_BEFORE_MARK`, `STACK_LIST_MEMBERS`, `KEEP_WHOLE` — these are producer actions that GENERATE ATU rendering. Constraints AUDIT proposed rendering; they do not produce it. A proposal containing producer-style verdicts fails template conformance and MUST be reframed before submission.

---

## §Multi-valued-fields — constraints that legitimately span multiple values

Some constraints have sub-branches with different operational profiles. For these, the affected field MUST use multi-valued split-form notation:

| Pattern | Example | Use when |
|---|---|---|
| `Category: A (branches X, Y) / B (branch Z)` | Restrictive-Relative (Category A for clear restrictive/non-restrictive; Category B for ambiguous-binding cases) | Branch-by-branch category differs |
| `Decidability: UD-pattern (branches X, Y) / Discourse-context-needed (branch Z)` | Constraints that have UD-decidable surface cases plus discourse-needed edge cases | Different branches require different evidence |

Multi-valued fields MUST enumerate which branch falls in which value. Multi-valued is permitted only when the constraint has structurally distinct sub-branches; it MUST NOT be used to evade a definite single-value classification.

---

## §Editorial-judgment constraint conventions

Category B constraints apply with editorial judgment rather than mechanical certainty. Their template entries follow these conventions:

1. **Normative keywords.** Use **SHOULD** for the editorial direction (not MUST), and reserve **MUST NOT** for absolute prohibitions. MUST is reserved for mechanical-constraint mandates.
2. **Verdict family.** Editorial-judgment constraints typically use `VIOLATION-FLAG` as the primary verdict — the UD signature surfaces candidates only, never auto-applies a direction.
3. **Examples.** In addition to fires + no-effect + excluded, editorial-judgment constraints MUST include at least one ambiguous example showing what falls into the residual judgment-required space.
4. **Closed lists as heuristic only.** When an editorial constraint includes a closed list, the list is a heuristic indicator focusing editorial attention, NOT a decision gate. State this explicitly inline: `(heuristic — not decision-gating)`.
5. **No auto-applier.** Category B constraints typically have no auto-applier. Implementation block records this as `Applier: (none — Category B / editorial-judgment constraint)`.

---

## Forbidden in constraint entries

The following content MUST NOT appear in §5 constraint entries. It belongs in companion documents:

| Content type | Belongs in |
|---|---|
| Rationale / WHY the constraint exists | `scholarship/<constraint-id>.md` |
| Grammatical-grounding citations beyond the source-reference field | `scholarship/<constraint-id>.md` |
| Corpus empirics ("zero hits in v2-mine") | `scholarship/<constraint-id>.md` |
| Audit precedent narratives | `audit-trail/<constraint-id>.md` |
| Sweep results with dates | `audit-trail/<constraint-id>.md` |
| Cross-project provenance | `audit-trail/<constraint-id>.md` or git log |
| Retirement narratives | `audit-trail/<constraint-id>.md` + git log |
| Pragmatic-stance disclaimers | `scholarship/<constraint-id>.md` |
| Stan-direct decision records | git log |
| Restatement of precedence already in §3.5 | (delete — §3.5 is the single source) |
| Cross-references by section position | (rewrite — use stable IDs only) |
| Producer-style action codes | (reframe as constraint-style verdict family) |
| "WHY/HOW WE KNOW/SCOPE" defensibility-capture blocks | `scholarship/<constraint-id>.md` |

The robot (LLM agent, audit-stage validator code, fresh-session Claude doing the work) does not need this content to apply the constraint correctly. The scholar (you, peer reviewers, dissertation readers) does need it — but in a different document with a different audience.

---

## Normative-language conventions (RFC 2119)

Within constraint statements, use the following keywords with their RFC 2119 meanings:

| Keyword | Meaning |
|---|---|
| **MUST** / **SHALL** / **REQUIRED** | Absolute requirement |
| **MUST NOT** / **SHALL NOT** | Absolute prohibition |
| **SHOULD** / **RECOMMENDED** | Strong recommendation; deviation requires careful weighing |
| **SHOULD NOT** / **NOT RECOMMENDED** | Strong recommendation against; valid exceptions exist |
| **MAY** / **OPTIONAL** | Truly optional; equally valid to do or not do |

These keywords are reserved for normative requirements. In rationale, examples, and non-normative content, use plain English (always, never, typically, often).

---

## Status semantics

| Status | Meaning | Audit behavior |
|---|---|---|
| **Active** | The constraint is in force; audit stage fires on it | Normal operation |
| **Proposed** | The constraint is under development; audit stage may exist but verdicts NOT auto-applied | Output flagged candidates but require manual review |
| **Retired** | The constraint no longer governs; audit-stage implementation should be removed | Does not fire; canon entry retained as Retired stub with cross-reference to replacement |

Retired constraints MUST cite their replacement (if any) or "no replacement; functionality absorbed by <constraint-id>" if folded into another constraint.

---

## Category semantics (A/B/C)

| Category | Application-confidence | Audit-stage authority |
|---|---|---|
| **A — Mechanical, mandatory** | Any trained editor would apply this constraint identically. | Audit-stage firing IS the approval; verdict auto-flows to editorial-review surface. |
| **B — Editorial, judgment-required** | Defensible, documented, but requires per-case editorial judgment. | Audit-stage flags candidates; human reviews each before applying. |
| **C — Theological / textual-critical** | Break placement implicates doctrine, manuscript-base choice, or critical text decisions. | Hand-curation only; audit stage does not fire. |

---

## Decidability semantics

| Decidability | Meaning | Implementation note |
|---|---|---|
| **Surface-pattern** | Constraint can fire from raw text inspection alone (regex-feasible). | Audit-stage may use regex; UD-pattern still preferred for cross-language portability. |
| **UD-pattern** | Constraint requires UD parse (deprel + UPOS + lemma) to detect reliably. | Audit-stage MUST use parsed corpus. |
| **Discourse-context-needed** | Constraint requires information beyond the parse. | Audit-stage emits VIOLATION-FLAG; auto-apply NOT available. |

---

## §Precedence-consistency check

The per-constraint **Precedence** field is a redundant reference to §3.5. Drift between them is mechanically detectable.

**Convention.** When a constraint cites a tier in its Precedence field (e.g., "§3.5 Tier 3"), §3.5 MUST list that constraint in that tier. When a constraint's Precedence field includes "Yields to <constraint-id>" or "Wins over <constraint-id>", those relationships MUST appear in §3.5's tier ordering.

**Mechanical check.** A validator (`validators/canon/check_precedence_consistency.py`) walks every §5 entry's Precedence field, parses tier and yields-to/wins-over claims, and verifies §3.5 agrees. Failures are flagged at commit time.

---

## Migration from prior rule format

When migrating an existing canon entry to this template:

1. Extract the rule statement and reframe as a yes/no grammatical question in the **Encoded question** field. If the rule can only be expressed as a procedural directive ("split X," "merge Y"), it is a producer, not a constraint — REJECT, do not migrate.
2. Map the prior `action:` field value to the appropriate **Verdict family** code (BIND / SPLIT-CANDIDATE / MERGE / VIOLATION-FLAG / NO-EFFECT). If no clean mapping exists, the original rule was producer-style — see step 1.
3. Add the **Source reference** field citing the grammar authority. If no grammar authority can be cited, the constraint may not be a real syntactic constraint — investigate before promoting.
4. Move rationale / grounding / empirics into `scholarship/<constraint-id>.md`.
5. Move audit-trail / sweep-results / retirement narratives into `audit-trail/<constraint-id>.md`.
6. Delete any precedence re-statement that duplicates §3.5.
7. Verify the constraint entry contains no producer-style verdicts, no forbidden content per the table above.

The migration is mechanically auditable: any constraint entry containing producer-style verdicts or forbidden content fails template conformance.
