# EP-3 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 EP-3` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 EP-3` (~line 1059; compact grammatical-basis + UD-signature + diagnostic content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../EP-3.md`](../EP-3.md) (full scholarship companion)

---

### EP-3: Inverted Predicate

**Status:** Active
**Category:** B (Editorial, judgment-required)
**Decidability:** Discourse-context-needed
**Layer:** 3

**Rule.** When a copular construction surfaces with its predicate complement (ADJ, NOUN, or participial) fronted before its subject — producing the marked word-order *Pred + Cop + Subj* rather than the default *Subj + Cop + Pred* — and Tiers 1-6 leave the break decision open, the inverted predicate construction SHOULD earn its own line (SPLIT before the inverted predicate, or render the whole inverted construction as a single own-line ATU when the construction is short and bonded). Cases where the inversion is the rhetorical device SHOULD be revealed by the line break; cases where the inversion is grammatically forced (e.g., interrogative inversion, presentational *there is*) MUST NOT be treated as EP-3 candidates. When the inversion's rhetorical force is genuinely indeterminate, the case SHOULD route to REVIEW and MUST NOT be auto-applied. EP-3 is a Category B editorial tiebreaker; it does not authorize mechanical application without per-case judgment.

**UD signature.**
~~~yaml
trigger:
  relation: [cop]
  head: { upos: [ADJ, NOUN, VERB] }   # the predicate complement, fronted
  subject:
    relation: nsubj
    linear_order: after_head           # subject follows the predicate-head in surface order
action: REVIEW
~~~

*Note:* The UD signature identifies *candidate* locations only. The rhetorical-device-vs-grammatical-inversion disambiguation is not mechanically decidable from the parse — it requires reading the inversion against the matrix's discourse frame and against the inventory of grammatically-forced inversions in the corpus's register. The validator surfaces candidates; an editor applies the diagnostic.

**Diagnostic (per-case judgment).**

1. **Normal-order paraphrase test.** Re-order the construction to default *Subj + Cop + Pred* (e.g., *"Great is my joy"* → *"My joy is great"*; *"Blessed are they who repent"* → *"They who repent are blessed"*). If the paraphrase loses rhetorical emphasis, marked focus, or formulaic resonance, the inversion is the device — EP-3 fires. If the paraphrase reads as natural or equivalent, the inversion is grammatically incidental and EP-3 does NOT fire.
2. **Formulaic-frame check.** The inverted predicate often instantiates a recognized formula type (beatitude *"Blessed are…"*, woe *"Wo unto…"* in copular variants, exclamatory *"Great is…"* / *"Marvelous are…"*, prophetic *"Cursed is…"*). When the construction matches a formula type, EP-3 fires by default.
3. **Grammatical-forcing exclusion.** Confirm the inversion is NOT one of: interrogative inversion (*"Is it not…"*), presentational *there is/are* construction, conditional-protasis inversion (*"Were it not for…"*), or a relative-clause-internal inversion driven by extraction. These are syntactically obligatory rather than rhetorically marked; EP-3 does NOT fire.

If diagnostic 1-3 do not converge, route to REVIEW.

**Closed lists** (machine-readable; non-exhaustive — heuristic, not gating).
~~~yaml
EP_3_FORMULAIC_PREDICATES:
  # Predicate heads that, when fronted in a copular construction, typically signal an EP-3 inversion
  - blessed
  - cursed
  - great
  - greater
  - holy
  - marvelous
  - wonderful
  - mighty
  - awful
  - long              # "long was the time…"
  - better
  - good

EP_3_GRAMMATICAL_FORCING_EXCLUSIONS:
  # Surface patterns whose inversion is grammatically forced — NOT EP-3 territory
  - interrogative_inversion       # "Is it not…", "Are ye not…"
  - presentational_there          # "There is a God", "There are many"
  - conditional_protasis          # "Were it not for…", "Had I not…"
  - relative_internal_inversion   # extraction-driven within a relative clause
~~~

*Closed lists are heuristic indicators that focus editorial attention; they are NOT decision-gating. A fronted predicate not in `EP_3_FORMULAIC_PREDICATES` MAY still be an EP-3 inversion. The diagnostic above is the authoritative test.*

**Scope.** Copular constructions in v2-mine where the predicate complement (ADJ, NOUN, or participial) surfaces in linear position before its subject NP, and where the inversion is not one of the closed-list grammatically-forced patterns. EP-3 fires only when Tiers 1-6 (Layer 1 vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have not already settled the break. EP-3 is a Tier 7 post-hoc editorial tiebreaker, not a generator or veto.

**Exclusions (closed list — each cites dominating rule).**

1. Inverted predicate inside a vocative environment → R15 (vocative indivisibility wins).
2. Inverted predicate inside an AICTP formula span → R1 (formula integrity wins).
3. Inverted predicate inside a fixed idiom → R18 (idiom integrity wins).
4. Inverted predicate as one member of a J1 formally-marked parallel series at N≥3 → J1 (Tier 5 wins; e.g., a stacked beatitude chain receives J1 list-uniformity treatment, not per-member EP-3).
5. Inverted predicate inside a J3 speech-act announcement span when the announcement formula already mandates its own-line treatment → J3.
6. Grammatically-forced inversions (`EP_3_GRAMMATICAL_FORCING_EXCLUSIONS` — interrogative, presentational *there is*, conditional protasis, relative-internal extraction-driven inversion) → out of scope; EP-3 does not fire.

**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). No EP-3 cross-rule precedence is asserted within Tier 7; EP-3 and the other EP-rules / image-test are co-equal tiebreakers within the tier.

**Examples.**

- *Compliant (formulaic inversion — own-line ATU):* "Blessed are ye if ye shall give heed unto the words of these twelve." (Fronted predicate adjective *blessed* + copula + subject; beatitude formula; the inversion is the rhetorical device; the whole inverted construction stands as a single own-line ATU.)
- *Compliant (formulaic inversion — own-line ATU):* "Cursed is he that putteth his trust in man." (Fronted *cursed* + copula + subject + restrictive relative; prophetic-curse formula; own line.)
- *Compliant (exclamatory inversion — own-line ATU):* "Great are the reasons which we have to mourn." (Fronted *great* + copula + subject + relative; the marked order carries the exclamatory emphasis; normal-order paraphrase *"the reasons which we have to mourn are great"* loses the emphatic force.)
- *Compliant (introducing SPLIT):* "Great is my joy, / for I have seen the Lord." (Inverted predicate construction earns its own line; the trailing *for*-clause splits per its own grounds — proposition boundary.)
- *Excluded by R15:* "O Lord God, blessed is thy name." (Inverted predicate inside vocative environment; R15 vocative integrity wins — vocative and copular-predicate render together as one vocative-anchored line per R15's treatment.)
- *Excluded by R1:* "And it came to pass that great were the trials of the people." (Inverted predicate inside AICTP formula span; R1 formula integrity wins — AICTP stays whole.)
- *Excluded by J1 (N≥3 stack):* A 9-member beatitude chain (e.g., 3 Nephi 12:3-11 Sermon-at-Bountiful beatitudes) → each *"Blessed are…"* member earns its own line per J1 (Tier 5 stack-uniformity), not per per-member EP-3 invocation. The list-uniformity treatment is the operative rule; EP-3 would have produced the same outcome but J1's precedence is what governs the stack.
- *Excluded by grammatical forcing:* "Is it not so?" (Interrogative inversion; not rhetorical predicate-fronting; EP-3 does not fire.)
- *Excluded by grammatical forcing:* "There is a God in heaven." (Presentational *there is* construction; EP-3 does not fire.)
- *Non-compliant (inversion mis-merged into trailing matter):* "great is my joy for I have seen the Lord." (Inverted predicate run together with a distinct trailing proposition; the inversion should anchor its own line.)
- *Ambiguous → REVIEW:* "long was the way which they had taken" (mid-narrative; ambiguous whether *long* is marked-focus rhetorical inversion or a grammatically unremarkable descriptive copula; diagnostic 1-3 do not cleanly converge — route to REVIEW.)

**Implementation.**

- Validator: `validators/colometry/validate_ep_3_inverted_predicate.py` (to be implemented — surfaces predicate-fronted copular candidates; filters `EP_3_GRAMMATICAL_FORCING_EXCLUSIONS`; emits REVIEW-REQUIRED for editorial disposition).
- Applier: none (Category B; auto-applier MUST NOT exist for EP-3; editorial-judgment required per-case).
- Closed-list definitions: §EP-3-Indicators (in BoFM canon, supplementary section — heuristic indicators only).
- Audit trail: `readers-bofm/private/audit-trail/EP-3.md` (to be populated during BoFM canon migration).
- Scholarship: [`../EP-3.md`](../EP-3.md).

---

## Notes on the migration

**What was extracted out of the current §5 EP-3 entry into [`../EP-3.md`](../EP-3.md):**

- "Grammatical basis" prose paragraph (the WHY — fronted predicate as marked word-order for rhetorical emphasis).
- The diagnostic "if emphasis is lost, the inversion earns its own line" framing as standalone test (now operationalized as Diagnostic 1: normal-order paraphrase test).
- The provenance narrative — EP-3's origin as part of the 2026-04-19 three-layer architecture session where Tier 7 editorial principles were separated from mechanical rules.
- Intellectual lineage to traditional-grammar treatments of marked word-order, predicate fronting, and the rhetoric of inversion (CGEL on subject-complement inversion; Quirk on marked thematic structure).
- The "editorial principle — requires judgment" disclaimer (now expressed structurally through Category B + Decidability Discourse-context-needed).
- Connection to BoFM's formulaic-language inventory (beatitude, woe, exclamatory, prophetic-curse formulas) — corpus-distribution observation, not operational gate.

**What stays in the operational entry above:**

- Status, Category, Decidability, Layer metadata.
- The single-paragraph Rule statement (RFC 2119 SHOULD for editorial-judgment cases; MUST NOT for auto-applier prohibition and for grammatically-forced inversions).
- UD signature (REVIEW action — surfaces candidates only).
- Closed lists (heuristic predicate-head indicators + grammatical-forcing exclusion list — operational filtering, not decision-gating).
- Diagnostic 1-3 (operational per-case test).
- Scope statement (Tier 7 post-hoc operational boundary).
- Exclusions (numbered with rule-ID cites — operational discriminators).
- Precedence (one-line §3.5 Tier 7 reference).
- Examples (compliant formulaic + compliant exclamatory + compliant SPLIT + excluded R15/R1/J1/grammatical-forcing + non-compliant + ambiguous REVIEW — calibration data).
- Implementation references.

**Net effect:** the operational entry covers everything an editor or validator needs to identify EP-3 candidates, filter grammatically-forced inversions, route ambiguous cases to REVIEW, and respect Tier-7 post-hoc precedence. Rationale, audit-trail, and intellectual lineage are extracted to the scholarship companion.

**Template-conformance notes for EP-rules (Category B + Discourse-context-needed):**

- **RFC 2119 keyword choice.** EP-3 uses **SHOULD** for the editorial direction (inverted predicate → own line) because per-case editorial judgment is required by definition of Category B. **MUST NOT** is reserved for two absolute prohibitions: (a) auto-applier prohibition (no mechanical application without review), and (b) the grammatical-forcing exclusion (interrogative/presentational/conditional-protasis inversions cannot be treated as EP-3 candidates — these are syntactic, not rhetorical).
- **Decidability = Discourse-context-needed.** The rhetorical-device-vs-grammatically-incidental disambiguation cannot be made from the UD parse alone; it requires reading the inversion against the matrix's discourse frame and the corpus's register-specific inventory of marked/unmarked inversions. Per `framework.md` §Decidability, this entails REVIEW-REQUIRED action.
- **UD signature `action: REVIEW`.** EP-3 surfaces candidates but does not commit a break direction. The closed-list indicators (formulaic predicate heads) are heuristic focus-points for editorial attention, not gating conditions.
- **Precedence = Tier 7 (editorial tiebreakers, post-hoc).** EP-3 fires only after Tiers 1-6 (syntax vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have settled. It cannot generate breaks that would conflict with higher-tier rules, and it cannot veto breaks higher tiers produce. The J1 N≥3 stack exclusion is the canonical higher-tier-wins case for beatitude chains.
- **No applier.** Unlike mechanical Category-A rules, EP-3 does not have an applier script — the operational signal is REVIEW for human disposition. A future Phase-2 discourse-aware validator could lift some EP-3 candidates into mechanical resolution, but that is future infrastructure work.

**Template conformance check:**

- [x] Stable ID (EP-3)
- [x] Title (Inverted Predicate)
- [x] Status (Active)
- [x] Category (B — Editorial, judgment-required)
- [x] Decidability (Discourse-context-needed)
- [x] Layer (3 — project-specific editorial overlay)
- [x] Rule statement (one paragraph; RFC 2119 keywords SHOULD + MUST NOT)
- [x] UD signature (machine-readable YAML; `action: REVIEW`)
- [x] Closed lists (heuristic indicators + grammatical-forcing exclusions; non-gating)
- [x] Scope (operational boundary statement; Tier 7 post-hoc designation)
- [x] Exclusions (closed list, each citing dominating rule by ID)
- [x] Precedence (one-line §3.5 Tier 7 reference; no duplicate prose)
- [x] Examples (compliant formulaic + compliant exclamatory + compliant SPLIT + excluded R15/R1/J1/grammatical-forcing + non-compliant + ambiguous REVIEW)
- [x] Implementation references (validator, applier=none, closed-lists, audit-trail, scholarship)
- [x] No "Rationale" / "WHY" / "HOW WE KNOW" / "audit precedent" / "Sweep results" content in the operational entry
