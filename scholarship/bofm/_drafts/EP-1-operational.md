# EP-1 Operational Entry — Proposed Restructured Form (Draft)

**This is a draft operational entry following the MISRA-style template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current `readers-bofm/private/01-method/colometry-canon.md §5 EP-1` entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 EP-1` (lines ~1045-1057; mixed grammatical-basis + diagnostic + example content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../EP-1.md`](../EP-1.md) (full scholarship companion)

---

### EP-1: "According To" Manner vs. Source

**Status:** Active
**Category:** B (Editorial, judgment-required)
**Decidability:** Discourse-context-needed
**Layer:** 3

**Rule.** When a PP headed by *according to* attaches to a matrix predication as `obl` or `advmod` and Tiers 1-6 leave the break decision open, the PP's semantic function SHOULD determine the break:

- *Manner* reading (the PP answers HOW the action was done — describing the mechanism, style, measure, or conformity of the act) → MERGE the PP with its matrix predication.
- *Source / authority* reading (the PP answers BY WHAT POWER or FROM WHAT SOURCE the action occurs — naming an independent locus of authorization, divine commission, or external warrant) → SPLIT the PP onto its own line.

When the reading is genuinely ambiguous between manner and source/authority and no discourse cue resolves it, the case SHOULD route to REVIEW and MUST NOT be auto-applied. EP-1 is a Category B editorial tiebreaker; it does not authorize mechanical application without per-case judgment.

**UD signature.**
~~~yaml
trigger:
  relation: [obl, advmod]
  case: { lemma: "according to" }  # multi-word preposition
  head: { upos: [VERB, AUX] }
action: REVIEW
~~~

*Note:* The UD signature identifies *candidate* locations only. The manner-vs-source disambiguation is not mechanically decidable from the parse — it requires reading the PP's complement against the matrix predication's discourse frame. The validator surfaces candidates; an editor applies the diagnostic.

**Diagnostic (per-case judgment).**

1. **Substitute test.** Paraphrase the PP with "in the manner of X" (manner reading) vs. "by the authority of X" / "as authorized by X" (source reading). The paraphrase that preserves meaning identifies the function.
2. **Complement-noun class.** Source/authority readings cluster on complement nouns naming an agent, faculty, or warrant (*the Spirit*, *the workings of the Spirit*, *the power of God*, *the spirit which is in me*, *the feelings of his heart*). Manner readings cluster on complement nouns naming a standard, measure, or instruction (*his word*, *their faith*, *his memory*, *my plainness*, *their time*).
3. **Independence test.** Can the *according to* PP stand as an independent theological/factual assertion the matrix presupposes? If yes → source. If the PP only specifies HOW the matrix predication unfolds → manner.

If diagnostic 1-3 do not converge, route to REVIEW.

**Closed lists** (machine-readable; non-exhaustive — heuristic, not gating).
~~~yaml
SOURCE_AUTHORITY_INDICATORS:
  # Complement-NP heads that typically signal source/authority reading
  - spirit
  - power
  - will
  - workings
  - faith        # context-sensitive: "manifest according to their faith" is manner-mechanism, "given according to their faith" is source
  - commandments
  - covenant

MANNER_INDICATORS:
  # Complement-NP heads that typically signal manner reading
  - word
  - time
  - memory
  - plainness
  - manner
  - custom
~~~

*Closed lists are heuristic indicators that focus editorial attention; they are NOT decision-gating. A SOURCE_AUTHORITY_INDICATORS hit MAY still be a manner reading in context, and vice versa. The diagnostic above is the authoritative test.*

**Scope.** PPs surface-headed by the multi-word preposition *according to* (or its closed orthographic variants — *according unto* in archaic register), attaching to a matrix predication via `obl` or `advmod`. EP-1 fires only when Tiers 1-6 (Layer 1 vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have not already settled the break. EP-1 is a Tier 7 post-hoc editorial tiebreaker, not a generator or veto.

**Exclusions (closed list — each cites dominating rule).**

1. *According to* PP inside a vocative environment → R15 (vocative indivisibility wins).
2. *According to* PP inside an AICTP formula span → R1 (formula integrity wins; PP follows formula on its own line if substantive, per J5).
3. *According to* PP that itself constitutes a J5 substantive adjunct slot-filler (its own when/where/why frame, fronted or trailing) → J5 (Tier 5 split-trigger wins before EP-1 is consulted).
4. *According to* PP coordinated as one member of a J1 formally-marked parallel series → J1 (Tier 5).
5. *According to* PP whose complement is a bare proper noun naming a textual reference (*according to the record of Alma*) and the PP attaches as parenthetical attribution → out of scope; treated under J3 / Rule 22-class textual-attribution patterns rather than EP-1.

**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). No EP-1 cross-rule precedence is asserted within Tier 7; EP-1 and the other EP-rules / image-test are co-equal tiebreakers within the tier.

**Examples.**

- *Compliant (manner — MERGE):* "spoke unto them, according to his word." (PP specifies HOW the speaking conformed — manner adverbial, manner-mechanism reading, merge with matrix.)
- *Compliant (manner — MERGE):* "proceed with mine own prophecy, according to my plainness." (PP specifies the style of delivery — manner.)
- *Compliant (manner — MERGE):* "the king answered him not for the space of an hour, according to their time." (PP specifies the measure standard — manner-conformity reading.)
- *Compliant (source — SPLIT):* "it whispereth me, / according to the workings of the Spirit of the Lord." (PP names the source of the whispering — independent theological assertion, own line.)
- *Compliant (source — SPLIT):* "I give unto you a prophecy, / according to the spirit which is in me." (PP names the prophetic authorization — source.)
- *Compliant (source — SPLIT):* "had spoken unto all his household, / according to the feelings of his heart and the Spirit of the Lord." (PP names the dual source — own line.)
- *Ambiguous → REVIEW:* "manifest unto the children of men, according to their faith." (Reading 1: manner-mechanism — faith is the mechanism by which manifestation occurs. Reading 2: source — faith is the warrant. Diagnostic 1-3 do not cleanly converge; route to REVIEW.)
- *Excluded by J5:* "according to the workings of the Spirit of the Lord, / it whispereth me..." (Fronted-PP substantive temporal/causal slot-filler; J5 wins at Tier 5 before EP-1 is consulted.)
- *Excluded by R15:* "O Lord God, according to thy will, / hear my prayer." (PP inside vocative environment; R15 vocative integrity wins.)
- *Non-compliant (manner mis-split):* "spoke unto them, / according to his word." (Manner reading split as if source — punctuation-artifact break; mechanism-not-warrant test should have merged.)

**Implementation.**

- Validator: `validators/colometry/validate_ep_1_according_to.py` (to be implemented — surfaces *according to* PP candidates; emits REVIEW-REQUIRED for editorial disposition).
- Applier: none (Category B; auto-applier MUST NOT exist for EP-1; editorial-judgment required per-case).
- Closed-list definitions: §EP-1-Indicators (in BoFM canon, supplementary section — heuristic indicators only).
- Audit trail: `readers-bofm/private/audit-trail/EP-1.md` (to be populated during BoFM canon migration).
- Scholarship: [`../EP-1.md`](../EP-1.md).

---

## Notes on the migration

**What was extracted out of the current §5 EP-1 entry into [`../EP-1.md`](../EP-1.md):**

- "Grammatical basis" prose paragraph (the WHY — distinct rhetorical weight of manner-vs-source PPs)
- The diagnostic question framing as standalone test ("HOW vs. BY WHAT")
- The provenance narrative — discovery via the 2026-03-24 punctuation-dependency audit (comma-stripping test exposed punctuation-artifact breaks vs. genuine grammatically-justified splits)
- The PP-classification history (Rule 21 → renumbered EP-1 when editorial principles were separated from mechanical rules, 2026-04-19)
- The "Note. This rule requires judgment — editorial principle, not purely mechanical" disclaimer (now expressed structurally through Category B + Decidability Discourse-context-needed)
- Connection to the punctuation-is-not-a-break-signal principle (`framework.md §1.10`) — historical origin of EP-1 as the working example proving the principle
- Intellectual lineage to traditional grammar's manner-vs-source adverbial-PP distinction

**What stays in the operational entry above:**

- Status, Category, Decidability, Layer metadata
- The single-paragraph Rule statement (RFC 2119 SHOULD for editorial-judgment cases; MUST NOT for auto-applier prohibition)
- UD signature (REVIEW action — surfaces candidates only)
- Closed lists (heuristic indicators only — not decision-gating)
- Diagnostic 1-3 (operational per-case test)
- Scope statement (Tier 7 post-hoc operational boundary)
- Exclusions (numbered with rule-ID cites — operational discriminators)
- Precedence (one-line §3.5 Tier 7 reference)
- Examples (compliant manner-merge + compliant source-split + ambiguous REVIEW + excluded — calibration data)
- Implementation references

**Net effect:** the operational entry covers everything an editor or validator needs to apply EP-1 in scope, route ambiguous cases to REVIEW, and respect Tier-7 post-hoc precedence. Rationale, audit-trail, and intellectual lineage are extracted to the scholarship companion.

**Template-conformance notes for EP-rules (Category B + Discourse-context-needed):**

- **RFC 2119 keyword choice.** EP-rules use **SHOULD** for the editorial direction (manner → merge; source → split) because per-case editorial judgment is required by definition of Category B. **MUST NOT** is reserved for the auto-applier prohibition (no mechanical application without review) — this is an absolute requirement even though the underlying break-direction is editorial.
- **Decidability = Discourse-context-needed.** The manner-vs-source disambiguation cannot be made from the UD parse alone; it requires reading the PP's complement against the matrix's discourse frame. Per `framework.md` §Decidability, this entails REVIEW-REQUIRED action.
- **UD signature `action: REVIEW`.** EP-1 surfaces candidates but does not commit a break direction. The closed-list indicators are heuristic focus-points for editorial attention, not gating conditions.
- **Precedence = Tier 7 (editorial tiebreakers, post-hoc).** EP-rules fire only after Tiers 1-6 (syntax vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have settled. They cannot generate breaks that would conflict with higher-tier rules, and they cannot veto breaks higher tiers produce. This is the structural meaning of "editorial tiebreaker."
- **No applier.** Unlike mechanical Category-A rules (R1, R17), EP-1 does not have an applier script — the operational signal is REVIEW for human disposition. A future Phase-2 discourse-aware validator could lift some EP-1 candidates into mechanical resolution, but that is future infrastructure work.

**Template conformance check:**

- [x] Stable ID (EP-1)
- [x] Title ("According To" Manner vs. Source)
- [x] Status (Active)
- [x] Category (B — Editorial, judgment-required)
- [x] Decidability (Discourse-context-needed)
- [x] Layer (3 — project-specific editorial overlay)
- [x] Rule statement (one paragraph; RFC 2119 keywords SHOULD + MUST NOT)
- [x] UD signature (machine-readable YAML; `action: REVIEW`)
- [x] Closed lists (heuristic indicators only — non-gating)
- [x] Scope (operational boundary statement; Tier 7 post-hoc designation)
- [x] Exclusions (closed list, each citing dominating rule by ID)
- [x] Precedence (one-line §3.5 Tier 7 reference; no duplicate prose)
- [x] Examples (compliant manner-merge + compliant source-split + ambiguous REVIEW + excluded)
- [x] Implementation references (validator, applier=none, closed-lists, audit-trail, scholarship)
- [x] No "Rationale" / "WHY" / "HOW WE KNOW" / "audit precedent" / "Sweep results" content in the operational entry
