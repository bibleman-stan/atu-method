# Multi-Lens Protocol — substrate-as-apparatus

## 1. The reframe — substrate IS the apparatus; ATU is ONE lens

The deployed readers (tanakh-reader.com, bomreader.com, gnt-reader.com, lxx-reader.com, vulgate-reader.com) present ATU-segmented text. ATU is the **first lens we shipped**, not the architectural endpoint. The load-bearing claim of this protocol:

> **A mature substrate decouples WHAT-IS-THERE (rich per-token / per-clause / per-relation features in Text-Fabric) from HOW-IT-IS-SEGMENTED (the rendering function that produces a reader's surface text).** Each segmentation theory — ATU, Korpel-colometric, Wackernagel-period, Skousen-parenthetical, Wallace-diagrammatic, cantillation-prosody, Croft/Scheppers full-grammatical-unit, KJV-verse — is a **deterministic function `f(substrate) → lens-rendered text`**. The substrate carries the truth; the lens carries the *reading*.

Stan 2026-06-03: *"We are in the business of making our apparatuses as optimized as possible for our purposes of ATU revelation. As we create substrates/TFs that are truly optimized and mature, it should theoretically let us do other interesting things like colometric analysis based on other segmentation criteria — exposing the true poetic/rhetorical structures."*

Operational consequences:

- **Substrate work is upstream of every lens.** A binding-rule addition that improves ATU output is a substrate improvement (richer clause-atom features, better boundary signals) that *every future lens* inherits. Effort spent on substrate is never lens-specific waste.
- **A lens is cheap once the substrate is mature.** Korpel-colometric for Hebrew is not "another year of methodology" — it is a rendering function that consumes BHSA te'amim disjunctive hierarchy already present in the substrate. The cost is the function, not the data.
- **The reader-website is a substrate viewer with a default lens.** Today the default is ATU. The architecture must admit additional lenses without forking the substrate.
- **Stan's cross-corpus ATU-convergence thesis is one *result* the substrate exposes; it is not the substrate's purpose.** Other lenses surface other convergences (cantillation-prosody vs. Korpel-colometric vs. ATU on the same Hebrew verse is a three-way *test* of the verse's structure, not a referendum on ATU).

This reframe does **not** retire ATU. ATU remains the deployed canon, the FEF/AICTP paper's claim, the bidirectional-test object. The reframe is **architectural**: it names what we already half-knew — that the discipline of building ATU forced us to build a substrate that is more general than ATU.

---

## 2. The lens catalog

Lenses are cataloged by status: **deployed**, **planned** (substrate sufficient, lens function not yet written), **research** (substrate insufficient, requires upstream work), **legacy** (cataloged for comparison, not advanced).

| Lens | Corpus scope | Status | Substrate source | Notes |
|---|---|---|---|---|
| **ATU** (current canon) | All five deployed corpora | deployed | v1 treebank → v1.5 binding rules → v2 LLM adjudication | The bidirectional-test object. Sole arbiter rule applies HERE ONLY. |
| **Korpel/Masoretic-colometric** | Hebrew (Tanakh) | planned | BHSA te'amim disjunctive hierarchy (already in substrate) | Disjunctive-accent hierarchy yields colometric units; pure deterministic render. |
| **Cantillation-prosody** | Hebrew (Tanakh) | planned | BHSA te'amim (same source, different rule) | Melodic-phrase units; differs from Korpel-colometric in treatment of conjunctive accents. Three-way Hebrew comparison: ATU vs. Korpel vs. cantillation-prosody. |
| **Wackernagel periods** | Greek (GNT, LXX) | research | Macula clause-role + part-of-speech; substrate has it, lens needs P1/P2-postpositive position detection | Period boundary = clitic-anchor point. Substrate-sufficient; lens function is the work. |
| **Marschall hand-segmented periods** | Greek (2 Cor 10–13 gold) | planned (gold-only) | Marschall's published segmentation, encoded as a substrate annotation layer | Gold yardstick for Wackernagel-lens evaluation; not corpus-wide. Stays in `private/substrate/` per repo. |
| **Skousen parenthetical structure** | BoFM | planned | EModE substrate ([[reference_emode_substrate]]) + Skousen's *Analysis* parenthetical markers, encoded as structural-signal layer | Per [[feedback_em_dashes_illustrative_not_text]]: render the **clause-boundary signal** (where the parenthetical opens/closes), NOT the dash marks. Punctuation has zero force; this is a structural lens, not a typographic overlay. |
| **Wallace diagrammatic** | Greek (GNT) | research | Macula `that-VP` / `sub-CL` / clause-role / frame / referent / person — all present per [[reference_greek_datasets]] | Didactic clause-structure diagram (subject/verb/complement on indented lines). Mechanical from Macula; the lens is a tree-render of substrate features already deployed. |
| **Croft/Scheppers full-grammatical-unit** | Cross-corpus (FEF/AICTP framing) | research | Croft's grammatical-unit criteria + Scheppers' colon criteria; needs explicit encoding as a lens function, NOT as ATU criteria | Per [[feedback_external_unit_is_not_atu.md]]: external units are NOT our ATU; they ARE valid lenses. The lens vocabulary is exactly the right home for them. |
| **KJV verse boundaries** | All corpora with KJV (Tanakh, GNT, BoFM) | legacy | KJV verse divisions (already present as substrate `verse` node) | Cataloged for comparison; not architecturally advanced; the substrate carries it for free. |

**Catalog discipline:**
- A lens enters this catalog only after Stan or the methodology canon names it. No speculative lenses.
- "Status: research" means the substrate is insufficient or the lens function is non-trivial — *not* that the lens is undecided. Decisions are tracked at `memory/_deferred_queue.md`.
- A lens leaves "planned" → "deployed" when the lens-contract gates (§3) pass and Stan signs off on the pill-button being lit (§4).

---

## 3. The lens contract

Every lens, before it ships behind a pill-button, must provide:

1. **A deterministic rendering function `f(substrate) → lens-rendered text file`.** No runtime computation at the reader site; lenses are pre-rendered (§5).
2. **A named substrate-feature set the lens consumes.** Documented in the lens's spec doc at `atu-method/docs/lenses/<lens-name>.md`. If the substrate is insufficient, the lens is status: research, not status: planned.
3. **A gold yardstick or canon-conformance target.** ATU's yardstick is the bidirectional test on genre-spread sample. Korpel-colometric's yardstick is Korpel/de Moor's published segmentations. Marschall's IS its own gold. Cantillation-prosody's is the Masoretic chant tradition as encoded in BHSA. *No lens ships without a measurable target.*
4. **A failure-mode catalog.** ATU's: over-merge (red line) + over-split (tail). Korpel-colometric's: te'amim ambiguity in poetry vs. prose. Wackernagel's: clitic-host ambiguity. The catalog drives the lens's audit gates.
5. **An adversarial audit at the §7.3 gate.** Per the Standing Behavioral Defaults rule 7: new lens = new mechanism = §7.3 audit BEFORE the lens function is written. ≥2 parallel adversarial audits encoded as a `Workflow` script, lenses chosen for the failure-mode catalog (e.g., for Korpel: lens-1 = "does the renderer respect *atnach* vs. *zaqef qatan* hierarchy?"; lens-2 = "does it over-split on conjunctive accents adjacent to disjunctive?").
6. **A standing-rule conformance check.** §6 below enumerates rules that propagate to all lenses; the lens's spec doc explicitly states how each is honored.

A lens that fails any of (1)–(6) does not ship. There is no soft-launch tier for lenses.

---

## 4. Pill-button-toggle UX direction

Stan 2026-06-03: *"Pill-button toggle UX — switch lenses on the same view; side-by-side compare deprioritized."*

The reader's verse view (or pericope view) gains a row of pill-buttons above the rendered text — one pill per available lens for that corpus. Clicking a pill swaps the rendered text *in place* with that lens's pre-rendered output. No layout shift, no scroll-position loss, no side-by-side panel (deprioritized — the cognitive load of comparing two segmentations simultaneously is high; toggling between them on the same locus is the intended interaction). The default pill is ATU. The pill bar is hidden for lenses the corpus doesn't carry (e.g., no Wackernagel pill on the Tanakh reader).

The architectural implication is §5: lens-toggle must be *cheap at the reader*, which means lenses are pre-rendered files, not runtime computations.

---

## 5. Pre-rendered text-file architecture

Each lens, for each corpus, produces a static file per pericope (or per book, or per chapter — granularity matches the corpus's existing chunking). The reader site holds one bundle per (corpus × lens × pericope). Toggling a pill swaps the loaded file; no JS computation, no substrate query at runtime, no Text-Fabric on the client.

Consequences:

- **The lens rendering function runs at build time**, alongside the existing v0 → v1 → v1.5 → v2 → v3 → deploy pipeline. A lens is one more stage in the build, producing one more set of static files. No new runtime architecture.
- **The substrate (Text-Fabric, treebanks, gold annotations) stays server-side / dev-side only.** It never ships to the reader. The reader gets the rendered text + minimal metadata for the pill-bar.
- **Cache invalidation is per-(corpus × lens × pericope).** A substrate change that affects only the Korpel lens invalidates only Korpel files for the touched verses. A substrate change that affects clause-atoms invalidates ATU + every lens that consumes clause-atoms.
- **A new lens is a new build stage, not a new runtime feature.** Promotion criterion (§9) gates when this stage becomes a repo of its own vs. a script inside an existing reader repo.
- **No client-side lens computation, ever.** The reader is a viewer of pre-rendered substrates-through-lenses; it is not a renderer itself. Any temptation to "just compute the Korpel split in JS at load time" is the wrong layer — it puts substrate-equivalent logic in the client and breaks the lens contract.

---

## 6. Standing rules that propagate to all lenses

These rules are corpus-wide and lens-wide unless explicitly scoped otherwise. They are the substrate's discipline expressed at the lens layer.

1. **Bidirectional test is the sole arbiter — for the ATU lens ONLY.** Per [[feedback_external_unit_is_not_atu.md]] and the methodology canon, the bidirectional test (§2.1 of `framework.md`) decides ATU. Other lenses have their own arbiters: Korpel-colometric is arbited by te'amim disjunctive hierarchy + Korpel/de Moor's published criteria; Wackernagel by clitic-host position; cantillation-prosody by Masoretic chant tradition; Wallace by his own diagrammatic conventions. **Do not import the bidirectional test into a non-ATU lens.** Each lens's arbiter is the lens's own theoretical commitment.

2. **Punctuation has zero force — across ALL lenses, ALL corpora.** Per the canon. No lens may use a punctuation mark as a split / bind signal. Skousen's parentheticals render as structural-signal boundaries, NOT as dashes (per [[feedback_em_dashes_illustrative_not_text]]). KJV-verse-boundary lens uses the *verse node*, not the period at the end of the verse. This rule is non-negotiable and propagates without exception.

3. **Genre is NEVER an ATU criterion — but other lenses CAN be genre-aware.** The ATU lens does not branch on Torah-narrative vs. Latter-Prophets-oracle vs. Sifrei-Emet-poetry; per the closed-routes ban on genre criteria. Korpel-colometric IS explicitly genre-aware (different rules for prose vs. poetry per Korpel/de Moor). Cantillation-prosody IS explicitly genre-aware (the 21-book vs. 3-book te'amim systems are genre-defined in the Masoretic tradition). The genre ban is **scoped to ATU**; other lenses inherit their theoretical commitments, which may include genre branching.

4. **Conformance ≠ correctness — applied per lens.** Per [[feedback_conformance_is_not_correctness.md]]. Each lens's conformance metric (does the renderer respect the lens's rules?) is an upper bound on its correctness (does the rendered text match the lens's theoretical target?). Both are measured separately; conformance is never reported as completeness.

5. **Substrate-first for Claude's own reasoning — applied per lens.** Per [[feedback_mechanical_first_for_own_review.md]]. Before hand-reasoning a Korpel call, query BHSA te'amim. Before hand-reasoning a Wackernagel call, query Macula clause-role + POS. The stop signal "cannot / impossible / needs LLM" is the trigger to inventory the substrate.

6. **Cross-corpus learning propagates.** Per [[feedback_check_prior_corpora.md]]. If Tanakh's Korpel-colometric lens solves a te'amim-hierarchy ambiguity, the LXX-colometric lens (when it ships) inherits the solution. Lens functions are versioned and shared across corpora where the substrate features align.

---

## 7. Forbidden moves

1. **No fly-swatting at the lens layer either.** Per [[feedback_no_fly_swatting.md]]. A lens that mis-segments a single verse is **not** patched by hand-coding a verse-specific override. The class is identified; the rule is added to the lens function; the substrate is improved if the substrate caused it. Single-instance fixes are the anti-pattern at every layer — substrate, ATU, and every other lens.

2. **No rhetorical-figure mechanical determination for the ATU lens.** Chiasmus / inclusio / parallelism / climactic-parallelism are reading observations, not ATU criteria. The ATU lens does not branch on rhetorical figures. Other lenses (Croft/Scheppers, eventually) may incorporate rhetorical-structure features; the ATU lens does not.

3. **No runtime lens computation at the reader.** Per §5. Lenses are pre-rendered. Any "let's just compute it on the client" temptation is rejected at architecture review.

4. **No lens without a §3 contract.** A speculative lens does not get a pill-button mockup, a stub file, or a placeholder. It gets a row in §2 with status: planned/research and a spec-doc TODO.

5. **No leaking lens vocabulary into ATU prose.** ATU's documentation, paper drafts, and methodology canon refer to ATU as ATU. The "ATU is one lens" framing lives in this protocol and `_north_star.md`, not in the FEF/AICTP paper's claims (§8).

6. **No collapsing lenses into each other.** Korpel-colometric and cantillation-prosody both consume te'amim, but they are distinct lenses with distinct rules and distinct outputs. The fact that two lenses share substrate features does not justify merging them — the theoretical commitments differ, and the value of the multi-lens architecture is *exactly* the comparison between distinct lenses on the same substrate.

7. **No promoting a lens by aesthetic appeal.** Korpel-colometric output is beautiful on Psalms. That is not a promotion criterion. The §3 lens contract is the promotion criterion. The §9 repo-promotion criterion is separate again.

---

## 8. Scope boundary — paper-draft prose excluded

The FEF/AICTP paper (`project_fef_aictp_paper`) is in active drafting. Its current framing is ATU-specific: empty-frame ATU definition, "and"/"that" translation-artifact statistics (367 vs. 533), cross-corpus convergence as thesis-not-result. The paper's claim is about ATU — about a *specific* lens's theoretical commitment to the bidirectional test and the resulting cross-corpus structural convergence.

**The substrate-vs-lens reframe MUST NOT leak into paper-draft prose** until Stan explicitly signals the paper is ready for it. The paper stakes a claim about ATU; introducing "ATU is one of many lenses" into that prose dilutes the claim and pre-empts what is properly a *future* paper's territory.

Per [[feedback_staged_paper_scope_discipline.md]]: stage-1 papers stake nothing beyond their narrow claim; defer named theory and cross-corpus claims. The multi-lens architecture is **named theory** — it is named *here*, in this internal doctrine document. The paper continues to speak ATU-only until Stan says otherwise.

Operational rule: when editing paper prose, any sentence that would reach for "lens" or "multi-lens" or "substrate-vs-lens" or "rendering function" or "ATU is one of" is the stop signal. Re-anchor on the ATU claim; defer the architectural framing to the docs layer.

The doctrine documents themselves (`atu-method/docs/`, this file, `_north_star.md`, the memory namespace) are **internal substrate concerns**, not published claims. They guide our build; they are not yet a thesis we are defending in print.

---

## 9. Promotion criterion — when does multi-lens get its own repo?

Today this protocol lives in `atu-method/docs/substrate/multi-lens-protocol.md` (or its eventual canonical location), and lens implementations live in their respective reader repos (Korpel-colometric for Tanakh → `readers-tanakh/`; Wackernagel for Greek → `readers-gnt/` and eventually `readers-lxx/`; Skousen-parenthetical → `readers-bofm/`). The cross-cutting concern — what makes a lens a lens, the contract, the pill-button standard, the propagating rules — is methodology canon and lives in `atu-method/`.

**Promotion criterion: a new repo (`reader-lenses/` or similar) is created when, and only when, a SECOND lens ships to a deployed reader.** Until then, the architectural framing lives in `atu-method/docs/` and the lens functions live in each reader repo. Premature repo-promotion is the canonical [[feedback_simplicity_bias.md]] failure — Stan's instinct (and the architectural temptation) pulls toward a clean separation; the right move is to let two lenses ship in-repo and *then* observe whether the shared code wants to extract.

Indicators that the promotion criterion is being approached:

- Two reader repos have independently implemented their lens functions, and the shared structure (pre-render pipeline, pill-bar metadata schema, cache-invalidation logic) is visibly duplicating.
- The lens contract (§3) has evolved past what each reader repo encodes locally — i.e., the contract has a shape that wants to live somewhere shared.
- Stan names the new repo. (Per the standing pattern: the moment of repo-creation is Stan's call, after the duplication is visible.)

Until then: this protocol is the canon, the reader repos hold the implementations, and the pill-button toggles wait for their second pill before the architecture is extracted.

---

*Document status: canonical methodology canon, internal substrate concern. Not for paper-draft propagation (§8). Reload on compaction; cross-reference from `_north_star.md` under "BoFM forward" and from each reader repo's `CLAUDE.md` on lens-trigger.*