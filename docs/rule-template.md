# Rule Template — Operational Specification

**Every rule in every per-corpus canon's §5 (Rule Detail) MUST follow the template specified here.** The template is operational: it contains what an LLM agent or validator needs to apply the rule correctly. Rationale, defensibility arguments, scholarly grounding, audit trail, and corpus-experiment narratives **do not appear in the rule entry**; they live in the per-rule scholarship companion (`scholarship/r{N}.md`) and audit trail (`audit-trail/r{N}.md`).

This template draws on:

- **MISRA C:2012/2023** rule-spec format (per-rule template, Category, Decidability).
- **RFC 2119 / BCP 14 / RFC 8174** for normative-language keywords (MUST, MUST NOT, SHALL, SHOULD, MAY).
- **W3C Specification process** for Status flags.
- **UD Guidelines** for relation cross-references.

---

## Template

```markdown
### R{ID}: {Title}

**Status:** {Active | Proposed | Retired}
**Category:** {A (Mechanical, mandatory) | B (Editorial, judgment-required) | C (Theological, hand-curation)}
**Decidability:** {Surface-pattern | UD-pattern | Discourse-context-needed}
**Layer:** {1 | 3}

**Rule.** {One paragraph. Normative. Uses RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY). States WHAT the rule requires; does not justify or explain.}

**UD signature.**
~~~yaml
trigger:
  relation: [<deprel>, ...]
  head: { upos: <UPOS>, lemma_in: <closed-list-name> }
  mark: { lemma_in: [<lemma>, ...] }
action: <one of the standard action codes — see §Action-Codes below>
~~~

**Closed lists** (machine-readable).
~~~yaml
<closed-list-name>:
  - lemma1
  - lemma2
  ...
~~~

**Scope.** {Operational boundary — where the rule applies. Single paragraph.}

**Exclusions (closed list — each cites dominating rule).**
1. {Description of excluded case} → R{N} | J{N} | §{X}
2. ...

**Precedence.** §3.5 Tier {N}. {Yields-to / Wins-over notation, one line, stable rule-IDs only.}

*Note:* §3.5 is the single source of truth for cross-rule precedence. The per-rule Precedence field MUST be consistent with §3.5's tier placement and the rule's yields-to/wins-over relationships. Drift between the two is a conformance failure detectable by mechanical cross-check (see "Precedence-consistency check" below).

**Examples.**
- *Compliant:* "{example sentence as it should be on the page}"
- *Non-compliant:* "{example showing what the rule forbids}"
- *Excluded by R{N}:* "{example where the rule does NOT apply, with the dominating rule cited}"

**Implementation.**
- Validator: `validators/colometry/validate_rule_{N}_ud.py`
- Applier: `validators/apply_rule_{N}_ud.py`
- Closed-list definitions: §<list-section>
- Audit trail: `private/audit-trail/r{N}.md`
- Scholarship: `private/01-method/scholarship/r{N}.md`
```

---

## Required fields

Every rule entry MUST include all of the following:

| Field | Purpose | Allowed values |
|---|---|---|
| **Rule ID** | Stable, persistent identifier | `R{N}`, `M{N}`, `J{N}`, `EP-{N}` |
| **Title** | Short, descriptive name | Free text (max ~10 words) |
| **Status** | Lifecycle state | Active / Proposed / Retired |
| **Category** | Application-confidence tier | A / B / C |
| **Decidability** | Whether the rule can fire mechanically | Surface-pattern / UD-pattern / Discourse-context-needed |
| **Layer** | Which layer of the system | 1 (generic syntax) / 3 (editorial) |
| **Rule** | The normative statement | One paragraph, RFC 2119 keywords |
| **UD signature** | Machine-readable trigger | YAML block |
| **Scope** | Where the rule applies | One paragraph |
| **Exclusions** | Closed-list carve-outs | Numbered list, each citing dominating rule |
| **Precedence** | Reference to §3.5 | One-line reference |
| **Examples** | Compliant + non-compliant + excluded | At minimum: 1 compliant, 1 non-compliant, 1 excluded |
| **Implementation** | File path references | Validator, applier, audit trail, scholarship |

---

## Forbidden in rule entries

The following content **MUST NOT** appear in §5 rule entries. It belongs in companion documents:

| Content type | Belongs in |
|---|---|
| Rationale / WHY the rule exists | `scholarship/r{N}.md` |
| Grammatical-grounding citations (CGEL, BDF, Joüon, Smyth, Wallace, etc.) | `scholarship/r{N}.md` |
| Corpus empirics ("zero hits in v2-mine") | `scholarship/r{N}.md` (as empirical-validation evidence) |
| Audit precedent narratives | `audit-trail/r{N}.md` |
| Sweep results with dates | `audit-trail/r{N}.md` |
| Cross-project provenance ("BoFM coined; Tanakh ported") | `audit-trail/r{N}.md` or git log |
| Retirement narratives | `audit-trail/r{N}.md` + git log |
| Pragmatic-stance disclaimers | `scholarship/r{N}.md` |
| Stan-direct decision records | git log |
| Restatement of precedence already in §3.5 | (delete — §3.5 is the single source) |
| Cross-references by section position ("see §1 line 162") | (rewrite — use stable IDs only) |
| "WHY/HOW WE KNOW/SCOPE" defensibility-capture blocks | `scholarship/r{N}.md` |

The robot (LLM agent, validator code, fresh-session Claude doing the work) does not need this content to apply the rule correctly. The scholar (you, peer reviewers, dissertation readers) does need it — but in a different document with a different audience.

---

## Normative-language conventions (RFC 2119)

Within rule statements, use the following keywords with their RFC 2119 meanings:

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

| Status | Meaning | Detector behavior |
|---|---|---|
| **Active** | The rule is in force; detector fires on it; applier applies its verdicts | Normal operation |
| **Proposed** | The rule is under development; detector may exist but applier should NOT auto-apply | Output STRONG-* candidates but require manual review |
| **Retired** | The rule no longer governs; detector should be removed or returned to historical-reference status | Detector does not fire; canon entry retained as Retired stub with cross-reference to replacement |

Retired rules MUST cite their replacement (if any) or "no replacement; behavior absorbed by R{X}" if functionality was folded into another rule.

---

## Category semantics (A/B/C)

| Category | Application-confidence | Mechanical authority |
|---|---|---|
| **A — Mechanical, mandatory** | Any trained editor would apply this rule identically. | Detector firing IS the approval; auto-apply by default. |
| **B — Editorial, judgment-required** | Defensible, documented, but requires per-case editorial judgment. | Detector flags candidates; human reviews each before applying. |
| **C — Theological / textual-critical** | Break placement implicates doctrine, manuscript-base choice, or critical text decisions. | Hand-curation only; mechanical detectors do not apply. |

When a rule classified as A would interact with Category C territory (e.g., R17 would merge into a famous exegetical hot-spot), the case is escalated to Category B for that instance.

---

## Decidability semantics

| Decidability | Meaning | Implementation note |
|---|---|---|
| **Surface-pattern** | Rule can fire from raw text inspection alone (regex-feasible). | Validator may use regex; UD-pattern still preferred for cross-language portability. |
| **UD-pattern** | Rule requires UD parse (deprel + UPOS + lemma) to detect reliably. | Validator MUST use parsed corpus. |
| **Discourse-context-needed** | Rule requires information beyond the parse (anaphora resolution, prior-entity tracking, semantic-frame disambiguation). | Validator emits REVIEW-REQUIRED; auto-apply NOT available pre-Phase-2 discourse infrastructure. |

---

## §Action-Codes — standard action codes for the UD-signature `action` field

The `action` field of a rule's UD signature MUST be one of these standard action codes. New action codes require a meta-template change (§7.3 trigger #9 — meta-rule change to the change protocol itself).

| Action code | Effect | Used by rule types |
|---|---|---|
| `MERGE_FORWARD` | Merge the matched token's line with the next line | Layer 1 line-final-token prohibitions (e.g., line-final CCONJ, DET) |
| `MERGE_BACKWARD` | Merge the matched token's line with the previous line | Less common; trailing-fragment-to-predecessor cases |
| `MERGE_HEAD_AND_DEPENDENT` | Merge the line containing the rule's `head` with the line containing the matched `dependent` | Complement-integrity rules (matrix + ccomp / xcomp) |
| `MERGE_VERB_AND_TOPIC_PP` | Merge a speech-class verb's line with its obligatory topic-PP line | R17 topic-PP extension (BoFM speech-class verbs) |
| `MERGE_VERB_AND_OF_PP` | Merge an experience verb's line with its obligatory of-PP line | R17 experience-of-PP extension (repent/partake/forgive) |
| `MERGE_MATRIX_AND_COMPLEMENT` | Same effect as MERGE_HEAD_AND_DEPENDENT, specialized name for complement-integrity contexts | R17, R26 |
| `MERGE_COORDINATE_MEMBERS` | Merge two members of a coordinate construction | M1 gorgianic pair; N=2 synonymy cases |
| `SPLIT_BEFORE_MARK` | Insert a line break before the matched mark token | Purpose-clause rules (R7 — split before *that*) |
| `SPLIT_BEFORE_CONJUNCTION` | Insert a line break before the matched coordinating conjunction | Polysyndetic-verb-chain split rules |
| `SPLIT_BEFORE_SUBJECT` | Insert a line break before the matched subject NP of the matrix clause | R28 speech-act-after-frame |
| `SPLIT_BEFORE_RELATIVE` | Insert a line break before a relative pronoun introducing a cataphoric clause | R19 cataphoric relative |
| `STACK_LIST_MEMBERS` | Each member of a parallel series gets its own line | J1 formally-marked parallel series |
| `KEEP_WHOLE` | The matched span MUST NOT contain a line break | R1 AICTP, R15 vocative, R18 fixed idiom, R23 date colophon |
| `REVIEW` | Surface the candidate to human editorial review; do NOT auto-apply | Discourse-context-needed rules; ambiguity-routed cases |

Per-corpus action-code extensions (rare) MAY be added to a per-corpus canon's §5 entries when language-specific operations are required. New extensions MUST be documented at the top of the per-corpus canon's §3 quick-reference table and added to this list via a meta-template change.

---

## §Precedence-consistency check

The per-rule **Precedence** field is a redundant reference to §3.5 (the single source of cross-rule precedence). Drift between them is mechanically detectable.

**Convention.** When a rule cites a tier in its Precedence field (e.g., "§3.5 Tier 3"), §3.5 MUST list that rule in that tier. When a rule's Precedence field includes "Yields to R{X}" or "Wins over R{Y}", those relationships MUST appear in §3.5's tier ordering.

**Mechanical check.** A future validator (`validators/canon/check_precedence_consistency.py`) walks every §5 entry's Precedence field, parses tier and yields-to/wins-over claims, and verifies §3.5 agrees. Failures are flagged at commit time. For now (pre-validator): manual cross-check during canon edits.

---

## Worked example: applying the template

See [`framework.md`](framework.md) §Example for a complete worked rule entry in the template.

When migrating an existing canon entry to this template:

1. Extract the rule statement, UD signature, scope, exclusions, precedence, examples, and implementation references into the operational fields.
2. Move rationale / grounding / empirics into `scholarship/r{N}.md`.
3. Move audit-trail / sweep-results / retirement narratives into `audit-trail/r{N}.md`.
4. Delete any precedence re-statement that duplicates §3.5.
5. Replace section-position cross-references ("see §1 line 162") with stable-ID cross-references ("see §1.4 N=2 Adjudication").
6. Verify the rule entry contains no "WHY", "HOW WE KNOW", "audit precedent", or "Sweep results" content.

The migration is mechanically auditable: any rule entry containing forbidden content (per the table above) fails template conformance.
