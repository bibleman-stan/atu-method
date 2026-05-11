# R17 Operational Entry — Proposed Restructured Form (PoC)

**This is a Proof-of-Concept demonstrating the new MISRA-without-Rationale operational template** (per [`../../docs/rule-template.md`](../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 R17` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 R17` (~75 lines of mixed operational + rationale + audit-trail content)
- **Proposed restructured state:** the operational entry below (~55 lines, purely operational)
- **Extracted rationale:** [`R17.md`](R17.md) (full scholarship companion)

---

### R17: Complement Integrity

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A matrix verb's clausal complement MUST be on the same v2-mine line as the matrix verb when the verb's lemma belongs to one of the six closed verb classes (§Verb-Classes-R17) and the complement is marked by *that*, *whether*, *if*, a WH-word, or an infinitival *to*. Speech-class verbs additionally require their obligatory topic-PP complement (*of*/*concerning*/*unto*/*against*) on the same line. Experience verbs (`repent`, `partake`, `forgive`) require their obligatory *of*-PP complement on the same line.

**UD signatures.**
```yaml
trigger_clausal:
  relation: [ccomp, xcomp]
  head: { upos: VERB, lemma_in: GOVERNING_LEMMAS_R17 }
  mark: { lemma_in: [that, whether, if, "WH-*"] }
action: MERGE_MATRIX_AND_COMPLEMENT

trigger_topic_pp:
  relation: obl
  head: { upos: VERB, lemma_in: SPEECH_CLASS_R17 }
  case: { lemma_in: [of, concerning, unto, against] }
action: MERGE_VERB_AND_TOPIC_PP

trigger_experience_of_pp:
  relation: obl
  head: { upos: VERB, lemma_in: [repent, partake, forgive] }
  case: { lemma: of }
action: MERGE_VERB_AND_OF_PP
```

**Closed lists** (defined at §Verb-Classes-R17):

- `GOVERNING_LEMMAS_R17` — six closed verb classes:
  - **Causative:** `cause`, `suffer`, `permit`, `command`, `grant`
  - **Aspectual:** `begin`, `cease`, `continue`
  - **Speech-indirect:** `say`, `speak`, `declare`, `testify`, `swear`, `proclaim`, `tell`, `confess`, `rehearse`, `preach`, `answer`, `cry`, `beseech`, `ask`, `plead`
  - **Cognition:** `know`, `believe`, `perceive`, `remember`, `understand`, `hear`, `see`, `suppose`, `imagine`, `forget`, `think`
  - **Volition:** `wish`, `desire`, `hope`, `long`, `trust`, `pray`, `seek`
  - **FEF-extraposition:** `it was their lot to`, `it is expedient to`, copular extraposition patterns
- `SPEECH_CLASS_R17` — subset of GOVERNING_LEMMAS_R17 taking obligatory topic-PP: `speak`, `declare`, `preach`, `testify`, `prophesy`, `bear record`, `bear testimony`, `bear witness`, `say`, `cry`, `write`
- `PETITION_FRAME_VERBS` — speech- and volition-class verbs whose modal-aux *that*-complement reads ambiguously between content and purpose: `cry`, `pray`, `beseech`, `ask`, `seek`, `plead`

**Scope.** Matrix VERB head only. ADJ head → R26 territory. NOUN head → out of scope (no R17-equivalent for NOUN-headed ccomp).

**Exclusions (closed list — each cites dominating rule).**

1. Direct discourse (colon-terminated speech-tag) → J3 (speech-act announcement)
2. AICTP-that → R16
3. Purpose-that with modal under non-cognitive motion verb → R7
4. Parallel that-series at N≥3 → J1 (per N=3+ cliff)
5. Meta-announcement (BE-verb + predicate-noun + appositive-that) — *that*-clause is appositive to the noun, not complement of the verb
6. Direct divine speech with recitativum-*that* (*saith the Lord, that [first-person content]*) → J3
7. Speech-indirect long-complement: matrix lemma in `{say, speak, tell, declare}` AND ccomp body ≥8 word tokens → J3 (long-complement exception)
8. Petition-frame ambiguity: matrix lemma in `PETITION_FRAME_VERBS` AND ccomp body has modal aux (`may`, `might`, `will`, `would`, `shall`, `should`, `can`, `could`, `must`) → REVIEW-REQUIRED (not auto-applied)
9. Vocative on matrix line → R15 (vocative-aware filter — vocative wins; matrix's complement merge yields to R15's own-line mandate for the vocative)

**Precedence.** §3.5 Tier 3. Yields to R26 (when ADJ is direct head). Wins over R19 (when both apply on a *that*-clause).

**N=2 sub-rule (coordinate that-series).** When R17 governor takes exactly 2 coordinate *that*-complements (e.g., *"declared unto them that they were a people who were under him, and that they were a free people"*), apply the M1 synonymy test (§1.9 N=2 Adjudication Principle):

- Synonymous / cognate / restatement → MERGE both *that*-clauses with the matrix.
- Distinct non-synonymous (each member with its own finite verb) → MERGE first *that*-clause with the matrix; SPLIT second per J1.

The sub-rule fires only when the matrix governor is in `GOVERNING_LEMMAS_R17`. Out-of-list matrix verbs (e.g., `wondereth`, `marveleth`) fall outside R17 territory entirely.

**Examples.**

- Compliant: *"He caused that his servants should stand forth"* (causative + that-clause merged)
- Compliant: *"I say unto you that the time shall come"* (speech-indirect + that-clause merged)
- Compliant (topic-PP): *"Nephi spake of the things which he had seen"* (speech + obligatory of-PP merged)
- Compliant (experience of-PP): *"he hath forgiven us of those our many sins"* (experience verb + of-PP merged; Alma 24:10)
- Non-compliant (violates R17): *"He caused / that his servants should stand forth"* (matrix severed from complement)
- Excluded by J3: *"And he said unto them: / Take what ye need..."* (colon-marked direct discourse)
- Excluded by long-complement exception (split is correct): *"said unto them / that they were a hard-hearted and a stiffnecked people"* (Alma 9:31; ccomp body ≥8 words)

**Implementation.**

- Validator: [`validators/colometry/validate_rule_17_ud.py`](../../../readers-bofm/validators/colometry/validate_rule_17_ud.py)
- Applier: [`validators/apply_rule_17_ud.py`](../../../readers-bofm/validators/apply_rule_17_ud.py)
- Verb-class definitions: §Verb-Classes-R17 (in BoFM canon, supplementary section)
- Audit trail: `readers-bofm/private/audit-trail/R17.md` (to be populated during BoFM canon migration)
- Scholarship: [`R17.md`](R17.md)

---

## Notes on the migration

**What was extracted out of the current §5 R17 entry into [`R17.md`](R17.md):**

- "Grammatical basis" prose paragraph (the WHY)
- "Why UD is cleaner" rationale block
- "Relative-clause environment is the primary violation site" narrative
- "WHY / HOW WE KNOW / SCOPE summary" block
- "Phase-1 hostile audit 2026-04-23" empirical findings narrative
- "Sweep results (2026-04-23): ~57 genuine Rule-17-scoped two-member series..." sweep narrative
- "Audit precedent. Stan caught Moroni 8:2..." audit history
- CGEL Ch. 14 §2 grammatical-grounding citation
- Cross-project provenance ("Tier-A: 4 cognition-class clean-cognate cases applied — 1 Ne 15:14, 1 Ne 18:4, Jacob 5:75, Alma 7:3")
- The 2026-05-10 Wave 6 detailed audit findings (Defects A/B/C narrative)
- The doctrinal-weight enumerated-list retirement history (2026-04-23 AM codified, retired 2026-04-23 PM)
- Future-work speculation (Phase 2 discourse-context, threshold tuning)

**What stays in the operational entry above:**

- Status, Category, Decidability, Layer metadata
- The single-paragraph Rule statement
- UD signatures in machine-readable YAML
- Closed-list definitions (verb classes, petition-frame verbs)
- Scope statement (operational boundary)
- Exclusions (numbered with rule-ID cites — operational discriminators)
- Precedence (one-line §3.5 reference; no duplicated cross-rule precedence prose)
- N=2 sub-rule (operational treatment of coordinate that-series)
- Examples (compliant + non-compliant + excluded — calibration data, not rhetorical illustration)
- Implementation references

**Net effect:** the operational entry is 55 lines (down from ~75) but every line is load-bearing operational content. The 20+ lines of rationale, history, and empirical-narrative are not lost — they are relocated to the scholarship companion where the scholar can read them. A fresh-session LLM agent reading the operational entry has everything needed to apply R17 correctly; no rationale-detritus distracts from the operational signal.

**Template conformance check:**

- [x] Stable ID (R17)
- [x] Title (Complement Integrity)
- [x] Status (Active) — note: "Active" status implies the rule is settled and applies; "Proposed" would mean awaiting corpus verification per §7.8
- [x] Category (A — Mechanical, mandatory)
- [x] Decidability (UD-pattern)
- [x] Layer (3 — project-specific editorial overlay)
- [x] Rule statement (one paragraph, RFC 2119 keywords used: MUST)
- [x] UD signature (machine-readable YAML; three triggers covering clausal, topic-PP, experience of-PP)
- [x] Closed lists (named with cross-references to §Verb-Classes-R17)
- [x] Scope (operational boundary statement)
- [x] Exclusions (closed list, each citing dominating rule by ID)
- [x] Precedence (one-line §3.5 Tier 3 reference; no duplicate prose)
- [x] Examples (compliant + non-compliant + excluded)
- [x] Implementation references (validator, applier, verb-classes, audit-trail, scholarship)
- [x] No "Rationale" / "WHY" / "HOW WE KNOW" / "audit precedent" / "Sweep results" content in the operational entry

The template's forbidden-content table is satisfied: rationale, grammatical-grounding citations, corpus empirics narratives, audit precedent narratives, sweep-result narratives, cross-project provenance, retirement narratives, pragmatic-stance disclaimers, restatements of precedence already in §3.5, and section-position cross-references are all extracted out of the operational entry into the scholarship companion or elsewhere.
