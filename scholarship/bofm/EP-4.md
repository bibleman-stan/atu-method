# EP-4: Title/Role Stays With Its Domain — Scholarship Companion

**Operational entry:** see `readers-bofm/private/01-method/colometry-canon.md §5 EP-4` (current) or this migration's proposed restructured entry at [`_drafts/EP-4-operational.md`](_drafts/EP-4-operational.md).

**Status:** This is the scholarship companion documenting WHY EP-4 exists, HOW we know it is correctly framed, and what intellectual / empirical history grounds its current shape. The operational canon entry says WHAT the rule does; this document says why.

---

## Statement

EP-4 (Title/Role Stays With Its Domain) directs editors to keep a title or role NOUN (*king*, *high priest*, *chief judge*, *ruler*, *teacher*, *governor*) bonded on the same v2-mine line with a PP naming the jurisdictional, institutional, or geographic domain over which the title applies. The bare title without its domain dangles — its reference is incomplete — so the domain PP is not a separable adjunct but a reference-completing nominal modifier.

EP-4 is a Category B editorial principle (judgment-required) and a Tier 7 post-hoc tiebreaker — it fires only when Tiers 1-6 (syntax vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have not already settled the break.

## Rationale

Titles and role designations in the BoFM-archaic register are *relational nouns* — they name a function, office, or authority that is intrinsically scoped to a domain. *King* is not a complete reference; *king of X* / *king over X* is. The same is true for *high priest*, *chief judge*, *ruler*, *teacher*, *governor*, *captain*. In each case the role's identity is constituted by the domain it governs: there are many high priests in BoFM but at any moment one specific high priest *over the church*, and the domain PP is what specifies which one.

The reader's cognitive processing reflects this. When a line ends on *"Alma was the high priest"*, the reader's attention dangles forward — *high priest of what?* — because the role's reference is unfilled. Splitting title from domain produces a fragment that fails the atomic-thought test on the same grounds as the M3 bare-governor cases (`framework.md §1.5 M3`): the head is grammatical machinery awaiting content, not a complete predication or referring expression.

EP-4 codifies this constraint as an editorial principle rather than a mechanical rule because the disambiguation between domain-defining nmod (which warrants merge) and J5 substantive adjunct (which warrants split) requires reading the PP against the matrix predication's discourse frame. *"the king reigned over the Lamanites for many years"* has *over the Lamanites* attaching to the matrix verb *reigned* (an `obl` modifying the action), not to *king* as a domain-completing `nmod`. The parser may or may not surface this distinction reliably; the editor reads the construction and adjudicates.

The rule does NOT generate breaks beyond what the matrix predication already supports; it only adjudicates whether a domain PP is bonded to its title head (merge) or floats free as its own atomic thought (yields to J5 or other higher-tier rule).

## Grammatical grounding

CGEL Chapter 5 §17 on *relational nouns* and their argument structure: relational nouns lexically encode an empty argument slot that must be filled (overtly or anaphorically) for the noun's reference to be complete. *King*, *priest*, *judge*, *ruler*, *teacher*, *governor* are all relational in this sense — each lexically encodes a "domain-of-authority" slot. The filler is typically realized as a PP (*king of X*, *high priest over Y*, *judge over Z*) or as a possessive (*his king*, *their priest*) where the possessor stands in for the domain.

CGEL Chapter 6 §13 on noun-PP modification distinguishes between:
- **Complement PPs** — PPs that fill a lexically-specified argument slot of the head noun. Cannot be omitted without producing an incomplete reference. Treated as `nmod` in UD with case markers *of*, *over*, *unto*.
- **Modifier PPs** — PPs that add information beyond the noun's lexical requirements. Optional; their omission does not produce an incomplete reference.

Domain PPs under title-role nouns are complement PPs in CGEL's sense. EP-4 instantiates the general principle that complement-PPs of relational nouns should remain on the same line as their head, since the head's reference is grammatically incomplete without them.

Quirk et al. *Comprehensive Grammar of the English Language* (CGEL-Quirk, 1985) §17.36-17.45 on postmodification of nouns by prepositional phrases names the same complement-vs-modifier distinction in different vocabulary. The KJV translation tradition retains the early-modern-English usage where title nouns canonically pair with *over* PPs naming the jurisdictional domain; the BoFM inherits this idiom directly.

Traditional Hebrew/Greek grammars handling cognate constructions name the same structural requirement:
- **Hebrew:** the construct chain (*melek yiśraʾel* — "king of Israel") realizes the domain-completion at the morpho-syntactic level; the construct head cannot stand alone with definite reference.
- **Greek:** the genitive of relation (*basileus tōn Ioudaiōn* — "king of the Jews") realizes the same domain-completion via case marking.

These cognate constructions across languages testify that the underlying cognitive structure — relational nouns require domain completion — is universal even though its morpho-syntactic realization varies.

## Empirical evidence

### Corpus distribution (informal, pre-systematic-sweep)

Title-domain pairings are densely distributed across the BoFM, especially in Mosiah-Alma-Helaman (the political-history books) and 3 Nephi (administrative continuity). A targeted spot-survey across v2-mine shows the following representative shape:

- **`king` + `over [domain]`:** ~30+ corpus instances. Universally merged in v2-mine (e.g., *"who was made king over the land of Zarahemla"* Omni; *"that he was not made king over the people"* Alma 2:9; *"Orihah was anointed to be king over the people"* Ether 6:27).
- **`high priest` + `over [domain]`:** ~7+ corpus instances. Universally merged (e.g., *"high priest over the church"* Alma 4:4; *"high priest over the church of God"* Alma 5:3; *"high priest over the church of God throughout the land"* Alma 8:23).
- **`chief judge` + `over [domain]`:** 4+ corpus instances. Universally merged (e.g., *"the chief judge over the land of Ammonihah"* Alma 14:4; *"the chief judge over the land"* Alma 14:27, Alma 51:2).
- **`ruler` + `over [domain]`:** 5+ corpus instances. Universally merged (e.g., *"a ruler over you"* 1 Nephi 3:29; *"a king and a ruler over us"* 1 Nephi 16:38; *"a king and a ruler over this people"* Mosiah 2:11).
- **`teacher` + `over [domain]`:** rare; one anchor at 1 Nephi 2:22 (*"a ruler and a teacher over thy brethren"*) where two coordinate titles share a single domain PP.

Corpus consistency for the title-domain bond is ~100% in v2-mine for the closed-list title lemmas. The empirical signal is overwhelming: titles and domains merge.

The absence of corpus violations is itself evidence — Stan's editorial intuition has consistently kept these bonded across hundreds of edits to v2-mine, suggesting the construction was operationally recognized long before codification. EP-4 (then likely under an earlier informal label) codified the existing practice.

### Discovery and codification

EP-4 was codified during the 2026-04-19 three-layer architecture restructuring session (see `readers-bofm/private/2026-04-19-canon-v2-and-merge-overrides/transcript.md`) alongside EP-1, EP-3, and EP-5. The restructuring partitioned the canon into mechanical-rules (Layer 1 + numbered Rules 1-28) and editorial-principles (EP-tier), and EP-4 was lifted into the EP-tier because:

- Its application requires distinguishing complement-PP (domain-completion) from modifier-PP (free adjunct) — a distinction the parser flags but does not reliably resolve.
- The J5 interaction (domain PP that is also a substantive when/where/why frame) requires per-case judgment.
- The discourse-shift cases (PP that predicates an independent claim rather than completes the title's reference) require reading the matrix's discourse frame.

The reclassification did not change EP-4's operational direction (merge title + domain) — it reframed the rule as one requiring per-case editorial judgment rather than mechanical application.

### Tier 7 ordering precedent

EP-4's Tier-7 placement was confirmed during the 2026-05-10 UD-detector-framework session (see `readers-bofm/private/2026-05-10-ud-detector-framework-and-corpus-sweep/canon-3.5-draft.md`). The session formalized the §3.5 precedence hierarchy and placed all EP-rules at Tier 7 as post-hoc editorial tiebreakers — they fire only when Tiers 1-6 leave a candidate boundary unresolved. This means EP-4 NEVER overrides a J5 substantive-adjunct split (Tier 5), an R15 vocative integrity merge (Tier 2), or an R1 AICTP integrity span (Tier 2); it operates strictly in the residual decision space.

### Pending: post-codification corpus-fit verification

The 2026-04-19 codification rested on Stan's editorial intuition and a partial-sample observation (no systematic full-corpus sweep). Per BoFM canon §7.3 trigger #12 (post-codification corpus-fit verification), a full-corpus systematic sweep remains an open obligation. The sweep would:

- Enumerate every title-NP + nmod-PP candidate in v2-mine (likely ~80-120 instances across the corpus, given the formulaic frequency of *king over*, *high priest over*, *chief judge over*, *ruler over* in the political-history books).
- Classify each candidate as domain-defining (MERGE) vs. J5-substantive (SPLIT) vs. ambiguous (REVIEW).
- Verify line-break treatment matches the rule's direction for unambiguous cases.
- Enumerate residual ambiguous-but-decided cases for editorial review.

Until this sweep is run, EP-4's claim of corpus-wide conformity rests on partial-sample evidence.

## Intellectual lineage

### Relational-noun argument structure

EP-4 instantiates the broader principle of *relational-noun argument-structure preservation* in scholarly editing: a relational noun and its lexically-required complement form one referring expression and should be presented as one visual unit. This principle is older than the apparatus; it appears (in different formal vocabulary) in:

- **CGEL** Ch. 5 §17 on relational nouns; Ch. 6 §13 on noun-PP complementation.
- **CGEL-Quirk** §17.36-17.45 on postmodification.
- **TEI Guidelines** P5 §16 on linguistic-corpus annotation of noun-PP complement structure (some TEI tagsets distinguish `<complement>` from `<modifier>` for nominal PPs).
- **Hebrew construct-chain analysis** in traditional Hebrew grammars (GKC §128-129; Joüon §139-140) — the construct head cannot stand alone with definite reference, the same structural requirement EP-4 instantiates for English title-role nouns.
- **Greek genitive-of-relation analysis** in classical and koine grammars (Smyth §1297-1303; Wallace *Greek Grammar Beyond the Basics* Ch. 3 on the genitive of relationship).
- **Ancient codex colometric practice** in titular constructions: Codex Sinaiticus and Codex Vaticanus typically present *basileus + genitive* on one cola line (e.g., *βασιλεὺς τῶν Ἰουδαίων* on one cola), corroborating that the title-domain bond was operationally recognized in the ancient editorial tradition.

The apparatus's EP-4 is the BoFM-archaic-register instantiation of this universal principle, with the title-role closed list calibrated to the corpus's specific lexical inventory (KJV-derived political and ecclesiastical vocabulary).

### Editorial-principle vs. mechanical-rule distinction

EP-4's status as Category B (editorial, judgment-required) reflects the same foundational distinction as EP-1, EP-3, EP-5: rules that are well-grounded grammatically but whose disambiguation requires per-case editorial judgment on the PP's function in context. EP-4 differs from EP-1 in that EP-4's primary trigger (NOUN-headed nmod PP under a closed-list title lemma) IS UD-decidable — the REVIEW action reflects the judgment requirement on the J5-interaction edge cases, not a parser-capability limit on the primary trigger.

This is the conceptual basis for the MISRA-style rule template's Decidability field, where EP-4 is UD-pattern (the parser detects the candidate cleanly) but Category B (editorial judgment governs the edge cases) — a different combination from EP-1's Discourse-context-needed + Category B pair.

### Cross-corpus instantiation

When the apparatus extends to GNT, the title-domain pattern surfaces on the *βασιλεὺς + genitive* construction (*king of the Jews*, *king of kings*), the *ἀρχιερεὺς + genitive* construction (*high priest of God*), and the various administrative titles (*ἡγεμών + genitive*, *τετράρχης + genitive*). A sister rule (GNT EP-4 or equivalent) would instantiate the same title-domain bonding requirement for the Greek genitive-of-relation construction. Similarly Tanakh's construct chain realizes the bonding at the morpho-syntactic level — the construct head and its construct nomen form one orthographic-prosodic unit and never split across a colometric line.

The cross-corpus consistency of the title-domain bond is structural evidence that EP-4 captures a universal cognitive constraint rather than a BoFM-specific quirk.

## Adversarial history

EP-4 has had one substantive review cycle.

### 1. Initial codification (2026-04-19)

The three-layer architecture restructuring session codified EP-4 alongside EP-1, EP-3, EP-5 as Tier-7 editorial tiebreakers. Adversarial pushback during the session raised:

- **Risk: the rule may over-merge by treating every nmod PP as domain-defining.** Resolution: scope the rule to a closed list of relational title nouns (`TITLE_ROLE_LEMMAS_EP4`) rather than all NOUN heads. The closed list filters out non-relational nouns where the nmod PP may genuinely be a separable modifier or J5 frame.
- **Risk: the rule may conflict with J5 substantive-adjunct splits.** Resolution: explicit Tier-7 placement after J5 (Tier 5). When a PP simultaneously names a domain AND functions as a substantive when/where/why frame, J5 wins by precedence; EP-4 fires only on the residual cases where the PP is purely domain-defining.
- **Risk: the rule may collide with Rule 22 divine-title appositives.** Resolution: R22 governs the appositive (title applied to a named referent), while EP-4 governs the title's bond with its own domain PP within that appositive line. The two rules operate on different structural elements and do not conflict.

The audit confirmed that the rule is well-grounded grammatically (CGEL Ch. 5 §17 on relational nouns) and that the editorial-judgment requirement is irreducible at the J5-interaction edge.

### 2. Pending: post-codification corpus-fit verification

The 2026-04-19 codification rested on partial-sample evidence (Stan's editorial intuition + a small set of spot-checked instances). Per BoFM canon §7.3 trigger #12 (post-codification corpus-fit verification), a full-corpus systematic sweep remains an open obligation. The sweep would test:

- Whether every title-NP + nmod-PP in v2-mine is correctly bonded on one line.
- Whether any latent violations (line-length-pressure splits, punctuation-artifact splits) exist that the spot-survey missed.
- Whether the closed-list `TITLE_ROLE_LEMMAS_EP4` is exhaustive or needs extension (candidate additions: *governor*, *captain*, *chief captain*, *steward*, *bishop*).

No retirement or material rescoping has occurred since 2026-04-19. The rule is stable as currently scoped.

## Future work

### Phase-2 discourse-context refinement

The J5-interaction disambiguation is a candidate case for Phase-2 discourse-aware mechanical resolution. The required infrastructure:

- **Title-NP frame detection.** Tag the title-NP's discourse frame as "introducing" (a new role-holder named for the first time, where the domain PP is identity-establishing) vs. "referencing" (a known role-holder, where the domain PP is contextual reminder).
- **PP semantic-class detection.** Tag the PP's complement noun as a jurisdictional-domain entity (*the land*, *the people*, *the church*) vs. a substantive-frame entity (a year, an event, a discourse-temporal anchor).
- **Matrix-predication argument-frame analysis.** Determine whether the PP attaches as `nmod` (modifying the title) or `obl` (modifying the matrix verb) — UD parsers sometimes attach ambiguously, and discourse context can disambiguate.

With this infrastructure, the unambiguous domain-defining cases (~95% of corpus matches) could be mechanically resolved, leaving only genuinely-ambiguous J5-edge cases for editorial review. This is future work; for now Category B + REVIEW is the honest output for the J5 interaction.

### Closed-list refinement

The current `TITLE_ROLE_LEMMAS_EP4` is non-exhaustive. A systematic corpus sweep would:

- Identify any title-noun lemma that recurrently pairs with a domain PP in v2-mine but is not yet in the closed list (candidate additions: *governor*, *captain*, *chief captain*, *steward*, *bishop*).
- Refine multi-word compound handling — *high priest*, *chief judge*, *chief captain* are syntactically compound but operationally function as single relational-noun heads.
- Calibrate the `DOMAIN_HEADWORD_INDICATORS` heuristic list with the empirical distribution of domain-PP complement nouns.

The closed lists serve as editorial-attention focuses and as the gating condition for whether EP-4 even applies to a candidate; they will remain calibrated to the BoFM corpus's specific lexical inventory.

### Cross-corpus instantiation

When the apparatus extends to GNT, a sister rule (provisional GNT EP-4) would instantiate the same title-domain bonding requirement for the Greek genitive-of-relation construction. When the apparatus extends to Tanakh, the construct chain already realizes the bonding at the morpho-syntactic level — no rule needed (the morphology forbids the split). The cross-corpus comparison would surface whether the BoFM's English title-domain idiom matches the underlying Hebrew or Greek construct-chain semantics it was translation-derived from, or whether the early-modern-English translation tradition modified the construction.

### Interaction with Rule 22 divine-title appositives

A future audit could clarify the operational boundary between EP-4 and Rule 22 (divine title appositives). R22 governs the appositive shape (title applied to a named referent in INTRODUCING vs. REFERENCING context); EP-4 governs the title's bond with its own domain PP. The interaction shape:

- *"Alma, the high priest over the church of God, said..."* — R22 INTRODUCING appositive (title applied to named Alma); EP-4 governs the bond between *high priest* and *over the church of God* within the appositive line.

The two rules operate on different structural elements and should not conflict, but a corpus-wide test would confirm this empirically.

---

*References:*

- Operational canon entry: `readers-bofm/private/01-method/colometry-canon.md §5 EP-4` (current state)
- Proposed restructured operational entry: [`_drafts/EP-4-operational.md`](_drafts/EP-4-operational.md)
- Universal framework: [`../../docs/framework.md`](../../docs/framework.md) §1.5 M3 (bare-governor indivisibility — structural sibling principle) + §1.4 J5 (substantive adjunct as own focus — interaction) + §2 (Category B editorial-judgment)
- Sibling EP-tier rule: [`EP-1.md`](EP-1.md) (editorial-judgment EP-rule pattern)
- 2026-04-19 three-layer architecture restructuring: `readers-bofm/private/2026-04-19-canon-v2-and-merge-overrides/transcript.md`
- 2026-05-10 §3.5 precedence-hierarchy formalization: `readers-bofm/private/2026-05-10-ud-detector-framework-and-corpus-sweep/canon-3.5-draft.md`
- Per-rule audit trail (corpus-fit sweep dates, closed-list refinements): `readers-bofm/private/audit-trail/EP-4.md` (to be created during BoFM canon migration)
