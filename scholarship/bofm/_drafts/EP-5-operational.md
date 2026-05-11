# EP-5 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 EP-5` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 EP-5` (lines ~1075-1083; mixed grammatical-basis + diagnostic + note content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../EP-5.md`](../EP-5.md) (full scholarship companion)

---

### EP-5: Virtue/Vice Lists

**Status:** Active
**Category:** B (Editorial, judgment-required)
**Decidability:** Discourse-context-needed
**Layer:** 3

**Rule.** When a line contains a stack of coordinated moral-quality NPs or ADJs (virtue list or vice list) and Tiers 1-6 leave the break decision open, the editor SHOULD first examine the stack for a formally-marked rhetorical parallel pattern (dual / triadic / crescendo / antithetic pairing). When a parallel pattern is detected and the stack qualifies under J1's formally-marked parallel series, the members SHOULD each receive their own line per J1 (Tier 5 stacking). When no parallel pattern is detected, the stack SHOULD MERGE as a single compound-list complement of its governing predicate. Genuinely ambiguous cases (pattern weakly attested, member count or marker irregular) SHOULD route to REVIEW and MUST NOT be auto-applied. EP-5 is a Category B editorial tiebreaker; it does not authorize mechanical application without per-case judgment.

**UD signature.**
~~~yaml
trigger:
  relation: conj
  head: { upos: [NOUN, ADJ], lemma_in: MORAL_QUALITY_LEMMAS_EP5 }
  members:
    upos_in: [NOUN, ADJ]
    lemma_in: MORAL_QUALITY_LEMMAS_EP5
    count: ">=2"
action: REVIEW
~~~

*Note:* The UD signature identifies *candidate* stacks only. The parallel-pattern detection is not mechanically decidable from the parse — it requires reading the stack for rhythmic / structural shape (dual, triadic, crescendo, antithetic). The validator surfaces candidates; an editor applies the diagnostic. When the diagnostic resolves "parallel pattern detected" cleanly, the resulting action is `STACK_LIST_MEMBERS` per J1; when it resolves "no pattern" cleanly, the resulting action is `MERGE_COORDINATE_MEMBERS`; otherwise the action remains `REVIEW`.

**Diagnostic (per-case judgment).**

1. **Pattern-detection scan.** Read the stack aloud. Does a formally-marked rhythmic shape emerge — e.g., a dual pair (*faith and hope*), a fixed triad (*faith, hope, and charity*), a crescendo (*patience, mercy, and long-suffering*), an antithetic pairing (*meek and lowly*, *chastity and virtue*)? Formal markers include: repeated possessive (*his X, his Y, his Z*), repeated demonstrative, repeated preposition introducing each member, or canonical liturgical / formulaic ordering (e.g., the *faith / hope / charity* triad is corpus-attested and pre-coded).
2. **Member-count check.** At N=2, apply the §1.9 N=2 Adjudication Principle before reaching EP-5: synonymous / cognate pairs merge (M1); distinct non-synonymous pairs may split (J1) but typically merge as compound-object lists under EP-5's default-merge unless a parallel pattern is independently marked. At N≥3 with a marked pattern, J1 wins per the N=3+ cliff (§1.9) — EP-5 only confirms the J1 stacking, it does not override.
3. **Frame-uniformity check.** Are all members governed by a shared predicate or shared frame (single verb, single preposition, single possessor)? If so, the stack is a compound-list complement and the default is MERGE unless a marked parallel pattern fires J1.

If diagnostics 1-3 do not converge — pattern is weakly attested, members are mixed-class, frame is irregular — route to REVIEW.

**Closed lists** (machine-readable; non-exhaustive — heuristic, not gating).
~~~yaml
MORAL_QUALITY_LEMMAS_EP5:
  # Virtue-class lemmas (heuristic indicators of a virtue-list candidate)
  - faith
  - hope
  - charity
  - love
  - patience
  - long-suffering
  - meekness
  - lowliness
  - humility
  - diligence
  - mercy
  - virtue
  - chastity
  - temperance
  - knowledge
  - godliness
  - kindness
  # Vice-class lemmas (heuristic indicators of a vice-list candidate)
  - pride
  - envy
  - hatred
  - malice
  - lying
  - deceit
  - wickedness
  - iniquity
  - whoredom
  - murder

FORMULAIC_VIRTUE_TRIADS:
  # Corpus-attested fixed triads whose members each earn own line under J1
  - [faith, hope, charity]
~~~

*Closed lists are heuristic indicators that focus editorial attention; they are NOT decision-gating. A `MORAL_QUALITY_LEMMAS_EP5` hit MAY still resolve to MERGE under the no-pattern default, and a stack of non-listed lemmas MAY still qualify for J1 stacking if a parallel pattern is independently attested. The diagnostic above is the authoritative test.*

**Scope.** Coordinate stacks of NPs or ADJs naming moral qualities (virtues or vices), attaching under a shared governing predicate (verb, preposition, or possessor), where the stack functions as the compound complement of that governor. EP-5 fires only when Tiers 1-6 (Layer 1 vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have not already settled the break. EP-5 is a Tier 7 post-hoc editorial tiebreaker, not a generator or veto.

**Exclusions (closed list — each cites dominating rule).**

1. Virtue/vice stack inside a vocative environment → R15 (vocative indivisibility wins).
2. Virtue/vice stack inside an AICTP formula span → R1 (formula integrity wins).
3. Virtue/vice stack at N≥3 with formally-marked parallel structure (repeated possessive, repeated demonstrative, repeated preposition, polysyndetic *and*) → J1 (Tier 5 wins before EP-5 is consulted; EP-5 only confirms J1's stacking direction). The N=3+ cliff (§1.9) makes this unconditional.
4. Virtue/vice N=2 pair governed by §1.9 N=2 Adjudication — synonymy/cognate test resolves before EP-5 fires (synonymous → M1 merge; distinct → J1 split / EP-5 confirms).
5. Virtue/vice stack that is itself a member of a higher-level J1 series (e.g., a triad inside a larger catalogue) → the higher-level J1 governs the outer split; EP-5 governs only the internal disposition of the stack treated as a single member.
6. Virtue/vice stack appearing in a multi-verse parallel list with a shared explicit frame (Parallel-List Uniformity Principle, §1.12) → list-uniformity governs; EP-5 yields.

**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). When a parallel pattern is detected at N≥3, J1 (Tier 5) has already settled the outcome via the N=3+ cliff (§1.9); EP-5 confirms rather than generates. No EP-5 cross-rule precedence is asserted within Tier 7; EP-5 and the other EP-rules / image-test are co-equal tiebreakers within the tier.

**Examples.**

- *Compliant (formulaic triad — STACK per J1, EP-5 confirms):*
  ~~~
  And see that ye have
  faith,
  hope,
  and charity,
  ~~~
  (Alma 7:24 context; the *faith / hope / charity* fixed triad is corpus-attested with formal triadic shape — J1 stacks at the N=3+ cliff; EP-5 confirms the parallel-pattern reading.)
- *Compliant (no pattern — MERGE):* "for he hath neither faith, hope, nor charity;" (Moroni 10:21 — same triad lemmas appear in a single-line listing inside a negative-existential frame; the stack functions as a compound complement of *hath neither*, no separate rhythmic shape, default merge.)
- *Compliant (no pattern — MERGE):* "full of patience, mercy, and long-suffering," (Alma 9:26 — virtue-stack triad attached as compound complement of *full of*; no member earns independent predicative weight; merge.)
- *Compliant (crescendo pattern — STACK per J1, EP-5 confirms):*
  ~~~
  yea, nourish the tree as it beginneth to grow,
  by your faith
  with great diligence,
  and with patience,
  ~~~
  (Alma 32:41 context — each member introduced by repeated preposition *with* / *by* forms a formally-marked parallel series; J1 stacks; EP-5 confirms.)
- *Ambiguous → REVIEW:* "and his matchless power, and his wisdom, and his patience," (Mosiah 4:6 — repeated possessive *his* is a J1 marker, but the stack mixes attribute classes (power / wisdom / patience) under a single divine-attribute frame; whether the formal possessive-repetition triggers J1 stacking or the unified frame triggers EP-5 merge requires editorial judgment.)
- *Excluded by R15:* "O Lord God, give me faith, hope, and charity, / hear my prayer." (Stack inside vocative environment; R15 vocative integrity wins; EP-5 not consulted.)
- *Excluded by R1:* "And it came to pass that he was full of faith and hope and charity that..." (Stack inside AICTP formula span; R1 wins; EP-5 not consulted.)
- *Excluded by §1.9 N=2:* "having faith and hope" (N=2 cognate pair; §1.9 routes to M1 synonymy test before EP-5 fires; M1 merges as bonded pair.)

**Implementation.**

- Validator: `validators/colometry/validate_ep_5_virtue_vice.py` (to be implemented — surfaces virtue/vice coordinate-stack candidates; emits REVIEW-REQUIRED for editorial disposition with optional pattern-classification hint).
- Applier: none (Category B; auto-applier MUST NOT exist for EP-5; editorial-judgment required per-case).
- Closed-list definitions: §EP-5-Indicators (in BoFM canon, supplementary section — heuristic indicators only).
- Audit trail: `readers-bofm/private/audit-trail/EP-5.md` (to be populated during BoFM canon migration).
- Scholarship: [`../EP-5.md`](../EP-5.md).

---

## Notes on the migration

**What was extracted out of the current §5 EP-5 entry into [`../EP-5.md`](../EP-5.md):**

- "Grammatical basis" prose paragraph (the WHY — stacked moral qualities and rhetorical-parallel detectability)
- The diagnostic framing as standalone test (pattern detection, default-to-merge)
- The connection to J1 parallel-series stacking and the N=3+ cliff
- The provenance narrative — reclassification to EP-tier in the 2026-04-19 three-layer architecture session alongside EP-1 / EP-3 / EP-4
- The "Editorial principle — requires judgment" disclaimer (now expressed structurally through Category B + Decidability Discourse-context-needed)
- Intellectual lineage to traditional rhetorical analysis of virtue/vice catalogues (Pauline Haustafeln, Stoic virtue lists, NT vice-list precedent)
- Empirical evidence: corpus distribution of virtue/vice stacks, formulaic triads (*faith / hope / charity*), and the rhetoric-bandwagon discipline that EP-5 deliberately avoids (no enumerated "doctrinal-weight" virtue subclasses)

**What stays in the operational entry above:**

- Status, Category, Decidability, Layer metadata
- The single-paragraph Rule statement (RFC 2119 SHOULD for editorial-judgment cases; MUST NOT for auto-applier prohibition)
- UD signature (REVIEW action — surfaces candidates only)
- Closed lists (heuristic indicators only — not decision-gating)
- Diagnostic 1-3 (operational per-case test, including N=2 / N≥3 cliff routing)
- Scope statement (Tier 7 post-hoc operational boundary)
- Exclusions (numbered with rule-ID cites — operational discriminators including J1 interaction)
- Precedence (one-line §3.5 Tier 7 reference)
- Examples (compliant pattern-stack + compliant no-pattern-merge + ambiguous REVIEW + excluded — calibration data)
- Implementation references

**Net effect:** the operational entry covers everything an editor or validator needs to apply EP-5 in scope, route ambiguous cases to REVIEW, defer to J1 at N≥3 with marked parallel, and respect Tier-7 post-hoc precedence. Rationale, audit-trail, and intellectual lineage are extracted to the scholarship companion.

**Template-conformance notes for EP-rules (Category B + Discourse-context-needed):**

- **RFC 2119 keyword choice.** EP-5 uses **SHOULD** for the editorial direction (pattern → stack per J1; no pattern → merge) because per-case editorial judgment is required by definition of Category B. **MUST NOT** is reserved for the auto-applier prohibition (no mechanical application without review) — this is an absolute requirement even though the underlying break-direction is editorial.
- **Decidability = Discourse-context-needed.** The parallel-pattern detection cannot be made from the UD parse alone; it requires reading the stack for rhythmic / formal shape (dual, triadic, crescendo, antithetic) which depends on inter-member regularities the parser does not represent.
- **UD signature `action: REVIEW`.** EP-5 surfaces candidates but does not commit a break direction. The closed-list indicators are heuristic focus-points for editorial attention, not gating conditions.
- **Precedence = Tier 7 (editorial tiebreakers, post-hoc).** EP-5 fires only after Tiers 1-6 (syntax vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have settled. It cannot generate breaks that would conflict with higher-tier rules, and it cannot veto breaks higher tiers produce. At N≥3 with formal parallel marking, J1 (Tier 5) has already settled the outcome via the §1.9 N=3+ cliff before EP-5 is consulted; EP-5's role in those cases is confirmatory, not generative.
- **No applier.** Unlike mechanical Category-A rules (R1, R17), EP-5 does not have an applier script — the operational signal is REVIEW for human disposition. A future Phase-2 discourse-aware validator could lift some EP-5 candidates into mechanical resolution by encoding the parallel-pattern detection, but that is future infrastructure work.

**Template conformance check:**

- [x] Stable ID (EP-5)
- [x] Title (Virtue/Vice Lists)
- [x] Status (Active)
- [x] Category (B — Editorial, judgment-required)
- [x] Decidability (Discourse-context-needed)
- [x] Layer (3 — project-specific editorial overlay)
- [x] Rule statement (one paragraph; RFC 2119 keywords SHOULD + MUST NOT)
- [x] UD signature (machine-readable YAML; `action: REVIEW`)
- [x] Closed lists (heuristic indicators only — non-gating)
- [x] Scope (operational boundary statement; Tier 7 post-hoc designation)
- [x] Exclusions (closed list, each citing dominating rule by ID, including J1 / §1.9 / §1.12 interactions)
- [x] Precedence (one-line §3.5 Tier 7 reference; no duplicate prose)
- [x] Examples (compliant pattern-stack + compliant no-pattern-merge + ambiguous REVIEW + excluded)
- [x] Implementation references (validator, applier=none, closed-lists, audit-trail, scholarship)
- [x] No "Rationale" / "WHY" / "HOW WE KNOW" / "audit precedent" / "Sweep results" content in the operational entry
