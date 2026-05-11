# EP-4 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 EP-4` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 EP-4` (lines ~1067-1073; mixed grammatical-basis + UD-signature + diagnostic content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../EP-4.md`](../EP-4.md) (full scholarship companion)

---

### EP-4: Title/Role Stays With Its Domain

**Status:** Active
**Category:** B (Editorial, judgment-required)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** When a title or role NOUN (e.g., *king*, *high priest*, *chief judge*, *ruler*, *teacher*, *governor*) heads a noun phrase modified by a PP naming the jurisdictional, institutional, or geographic domain over which the title applies, and Tiers 1-6 leave the break decision open, the title-NP and its domain PP SHOULD remain on the same v2-mine line. A break between title and domain MUST NOT be introduced on the basis of punctuation alone, line-length pressure, or local PP-trailing convention; the title's reference is incomplete without the domain. When the PP is itself a J5 substantive adjunct (its own when/where/why frame) or when discourse context shifts the PP from defining the title to predicating an independent claim about the role-holder, the case SHOULD route to REVIEW.

**UD signature.**
~~~yaml
trigger:
  relation: nmod
  head: { upos: NOUN, lemma_in: TITLE_ROLE_LEMMAS_EP4 }
  case: { lemma_in: [over, of, in, unto] }
action: REVIEW
~~~

*Note:* The UD signature identifies *candidate* locations only. The disambiguation between domain-defining nmod (MERGE) and substantive-adjunct PP (yields to J5 / SPLIT) requires reading the PP against the matrix's discourse frame; the validator surfaces candidates and emits REVIEW for editorial disposition.

**Diagnostic (per-case judgment).**

1. **Reference-completion test.** Strip the PP. Does the bare title-NP refer unambiguously to a known entity in the discourse? If NO — the bare title would dangle (e.g., *"high priest"* without specifying *"over the church"* leaves the reference open) — the PP is domain-defining → MERGE.
2. **Domain-headword class.** Domain-defining PPs cluster on complement nouns naming a jurisdiction (*the land*, *the people*, *the church*, *the Nephites*, *Zarahemla*), a body governed (*the people of the church*, *that people*), or a relational scope (*us*, *them*, *thy brethren*). When the headword names a domain-of-authority entity, the PP is domain-defining → MERGE.
3. **Independence test.** Can the PP stand as its own substantive when/where/why frame answering a question the matrix predication leaves open? If yes → J5 wins at Tier 5 (yields to J5 before EP-4 is consulted). If the PP only completes the title's reference → MERGE.

If diagnostic 1-3 do not converge, route to REVIEW.

**Closed lists** (machine-readable).
~~~yaml
TITLE_ROLE_LEMMAS_EP4:
  # Title / role nouns whose reference is canonically completed by a domain PP
  - king
  - queen
  - priest          # incl. compound "high priest"
  - judge           # incl. compound "chief judge"
  - ruler
  - teacher
  - governor
  - captain
  - prophet         # context-sensitive: "prophet of the Lord" is domain-defining; "prophet in Israel" may be J5
  - high_priest     # multi-word compound
  - chief_judge     # multi-word compound
  - chief_captain   # multi-word compound

DOMAIN_HEADWORD_INDICATORS:
  # Complement-NP heads that typically signal a domain-defining PP (heuristic)
  - land
  - people
  - church
  - city
  - kingdom
  - tribe
  - host
  - army
~~~

*Closed lists are operational focus-points. `TITLE_ROLE_LEMMAS_EP4` is the gating list for whether EP-4 even applies to a candidate; `DOMAIN_HEADWORD_INDICATORS` is heuristic — a hit raises confidence the PP is domain-defining, but the diagnostic above remains authoritative.*

**Scope.** Title- or role-headed noun phrases (head lemma ∈ TITLE_ROLE_LEMMAS_EP4) with an attached `nmod` PP whose head case-marker is *over*, *of*, *in*, or *unto*. EP-4 fires only when Tiers 1-6 (Layer 1 vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have not already settled the break. EP-4 is a Tier 7 post-hoc editorial tiebreaker, not a generator or veto.

**Exclusions (closed list — each cites dominating rule).**

1. Title-NP inside a vocative environment (*"O thou king over the land, hear me"*) → R15 (vocative indivisibility wins).
2. Title-NP inside an AICTP formula span → R1 (formula integrity wins).
3. Domain PP that is itself a J5 substantive adjunct (its own when/where/why frame, fronted or trailing) → J5 (Tier 5 split-trigger wins before EP-4 is consulted).
4. Title-NP coordinated as one member of a J1 formally-marked parallel series of titles (*"a king and a ruler over us"*) → J1 governs the series; EP-4 governs each title's bond with the shared domain PP.
5. Title-NP appositive to a named referent introducing the title (Rule 22 INTRODUCING shape, formal anchor present) → R22 STACK SPLIT applies to the appositive; EP-4 still governs the title's bond with its own domain PP within that line.
6. PP that does not name a domain but predicates an action / relation independent of the title (*"the king who reigned over the Lamanites"* — the *over* PP modifies *reigned*, not *king*) → out of scope; the PP attaches to the matrix verb, not to the title noun.

**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). No EP-4 cross-rule precedence is asserted within Tier 7; EP-4 and the other EP-rules / image-test are co-equal tiebreakers within the tier.

**Examples.**

- *Compliant (domain-defining — MERGE):* "Now Alma did not grant unto him the office of being high priest over the church," (PP completes the title's reference — without *"over the church"*, the bare *"high priest"* dangles. Domain-defining; merge.)
- *Compliant (domain-defining — MERGE):* "who was made king over the land of Zarahemla;" (PP names the jurisdictional domain; domain-defining; merge.)
- *Compliant (domain-defining — MERGE):* "and Orihah was anointed to be king over the people." (PP names the body governed; merge.)
- *Compliant (domain-defining — MERGE):* "that the chief judge over the land of Ammonihah and many of their teachers and their lawyers went in unto the prison" (chief judge + domain PP merged; subject of matrix verb.)
- *Compliant (domain-defining — MERGE):* "I am Alma, and am the high priest over the church of God throughout the land." (Title + domain PP merged; nested *throughout the land* is part of the domain specification.)
- *Compliant (J1 series, each title bonded to shared domain — MERGE within member):* "he has thought to make himself a king and a ruler over us," (Two coordinate titles share one domain PP; J1 governs the coordinate-title series but EP-4 keeps the shared *over us* bonded to the title cluster.)
- *Excluded by R15:* "O thou king over the land, / hear my prayer." (Title-NP inside vocative environment; R15 indivisibility wins.)
- *Excluded by J5:* "In the eighth year of the reign of the judges over the people of Nephi, / Alma went forth..." (Fronted year-formula + role-PP cluster is a J5 substantive adjunct slot-filler; J5 wins at Tier 5 before EP-4 is consulted.)
- *Excluded (out of scope — PP attaches to matrix verb):* "the king reigned over the Lamanites for many years." (PP *over the Lamanites* attaches to *reigned* — matrix verb's `obl` — not to *king* as `nmod`; EP-4 does not apply.)
- *Non-compliant (domain split as punctuation-artifact):* "Alma was the high priest / over the church of God." (Bare *"high priest"* dangles; the domain PP completes the title's reference. The break is a punctuation-artifact or line-length-pressure split, not warranted by grammar.)

**Implementation.**

- Validator: `validators/colometry/validate_ep_4_title_domain.py` (to be implemented — surfaces title-NP + domain-PP candidates; emits REVIEW-REQUIRED for editorial disposition).
- Applier: none (Category B; auto-applier MUST NOT exist for EP-4; editorial-judgment required per-case).
- Closed-list definitions: §EP-4-Title-Role-Lemmas (in BoFM canon, supplementary section).
- Audit trail: `readers-bofm/private/audit-trail/EP-4.md` (to be populated during BoFM canon migration).
- Scholarship: [`../EP-4.md`](../EP-4.md).

---

## Notes on the migration

**What was extracted out of the current §5 EP-4 entry into [`../EP-4.md`](../EP-4.md):**

- "Grammatical basis" prose paragraph (the WHY — titles require domain completion; bare title dangles)
- The grammatical-grounding citations (CGEL on nominal complementation; nominal `nmod` PP as domain-of-reference)
- The intellectual lineage to traditional grammar's treatment of relational nouns
- The reclassification narrative (renumbered to EP-tier in 2026-04-19 three-layer architecture restructuring alongside EP-1/EP-3/EP-5)
- The "editorial principle — requires judgment" disclaimer (now expressed structurally through Category B + Decidability UD-pattern with REVIEW action)
- Cross-references to the J5 interaction (when does a PP become a J5 substantive adjunct vs. a domain-completion nmod)
- Future-work speculation (Phase 2 discourse-context refinement; closed-list expansion via systematic sweep)

**What stays in the operational entry above:**

- Status, Category, Decidability, Layer metadata
- The single-paragraph Rule statement (RFC 2119 SHOULD for editorial-judgment direction; MUST NOT for punctuation-driven splits)
- UD signature (REVIEW action — surfaces candidates only)
- Closed lists (gating TITLE_ROLE_LEMMAS_EP4; heuristic DOMAIN_HEADWORD_INDICATORS)
- Diagnostic 1-3 (operational per-case test: reference-completion, domain-headword class, independence)
- Scope statement (Tier 7 post-hoc operational boundary)
- Exclusions (numbered with rule-ID cites — operational discriminators)
- Precedence (one-line §3.5 Tier 7 reference)
- Examples (compliant domain-merge + excluded by higher-tier + non-compliant punctuation-artifact split — calibration data)
- Implementation references

**Net effect:** the operational entry covers everything an editor or validator needs to apply EP-4 in scope, route ambiguous cases to REVIEW, and respect Tier-7 post-hoc precedence. Rationale, audit-trail, and intellectual lineage are extracted to the scholarship companion.

**Template-conformance notes for EP-rules (Category B + UD-pattern with REVIEW action):**

- **RFC 2119 keyword choice.** EP-4 uses **SHOULD** for the editorial direction (title + domain → merge) because per-case editorial judgment is required by definition of Category B. **MUST NOT** is reserved for the punctuation-artifact-split prohibition — that is an absolute requirement (no punctuation-only split between title and domain) even though the underlying merge-direction is editorial.
- **Decidability = UD-pattern.** Unlike EP-1 (Discourse-context-needed), EP-4's primary trigger (NOUN-headed `nmod` PP under a closed-list title lemma) IS UD-decidable. The REVIEW action reflects the Category B requirement for editorial judgment on the J5-interaction and discourse-shift cases, not a parser-capability limit.
- **UD signature `action: REVIEW`.** EP-4 surfaces candidates but does not commit a break direction. The closed-list `TITLE_ROLE_LEMMAS_EP4` is gating (EP-4 does not apply to non-title nouns); `DOMAIN_HEADWORD_INDICATORS` is heuristic focus.
- **Precedence = Tier 7 (editorial tiebreakers, post-hoc).** EP-4 fires only after Tiers 1-6 settle. It cannot generate merges that would conflict with a higher-tier split (J5 substantive adjunct, J1 parallel-list member as its own beat), and it cannot veto breaks higher tiers produce. This is the structural meaning of "editorial tiebreaker."
- **No applier.** Unlike mechanical Category-A rules, EP-4 does not have an applier script — the operational signal is REVIEW for human disposition. A future Phase-2 discourse-aware validator could lift the unambiguous domain-defining cases (where TITLE_ROLE_LEMMAS_EP4 hits AND a DOMAIN_HEADWORD_INDICATORS hit AND no J5 reading is plausible) into mechanical resolution, but that is future infrastructure work.

**Template conformance check:**

- [x] Stable ID (EP-4)
- [x] Title (Title/Role Stays With Its Domain)
- [x] Status (Active)
- [x] Category (B — Editorial, judgment-required)
- [x] Decidability (UD-pattern)
- [x] Layer (3 — project-specific editorial overlay)
- [x] Rule statement (one paragraph; RFC 2119 keywords SHOULD + MUST NOT)
- [x] UD signature (machine-readable YAML; `action: REVIEW`)
- [x] Closed lists (gating TITLE_ROLE_LEMMAS_EP4 + heuristic DOMAIN_HEADWORD_INDICATORS)
- [x] Scope (operational boundary statement; Tier 7 post-hoc designation)
- [x] Exclusions (closed list, each citing dominating rule by ID)
- [x] Precedence (one-line §3.5 Tier 7 reference; no duplicate prose)
- [x] Examples (compliant domain-merge + excluded by higher-tier + non-compliant punctuation-artifact split)
- [x] Implementation references (validator, applier=none, closed-lists, audit-trail, scholarship)
- [x] No "Rationale" / "WHY" / "HOW WE KNOW" / "audit precedent" / "Sweep results" content in the operational entry
