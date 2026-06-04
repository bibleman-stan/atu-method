# The Textual Fabric Doctrine (substrate before superstructure)

**Canonical. Established 2026-05-27 from the BoFM substrate ordeal.** The ATU framework is a
**Container, not an Originator**: it *organizes* what a corpus's textual fabric (morphology +
syntax + clause structure) supports — it never invents the analysis. **Fabric quality bounds the
claims.** Do not draw ATU boundaries on a corpus whose fabric is below parity; build the fabric first.

## 1. The mechanical ceiling (why this doc exists)

Mechanical-first (v0→v1 treebank clause-atoms→v1.5 binding rules) is the right *first* pass, but it has
a hard **ceiling**. The ATU decisions that sit above it require **token-in-context judgment** a rule over
a parse cannot reliably make:
- **complement-vs-quote** — a finite complement BINDS (shared deictic center) vs. re-performed direct
  discourse STANDS (own deictic center). Needs participant/deixis tracking (Macula `referent`/`subjref`);
  absent on thin substrates.
- **parallel-cola-vs-overspilt** — coordinate cola with distinct subjects are separate ATUs (KEEP-AS-IS,
  editorial v3), NOT mechanical defects to fuse.
- **shared-vs-distinct subject** in coordinate chains — elision is a grammatical fact, not an ATU verdict.

Past the ceiling the only two levers are **(a) better substrate** (a gold/near-gold treebank) and
**(b) v2 narrow-task LLM adjudication** on the residuals. Adding more mechanical rules over a weak parse
re-hits the same wall (proven on BoFM 2026-05-27: three rule-designs — a splitter, a blunt gold-POS
re-parse, and a merger — were all reshaped/killed at the §7.3 audit gate *before* code).

## 2. Fabric-parity tiers (per corpus)

| Corpus | Fabric | Tier | Note |
|---|---|---|---|
| Tanakh (Hebrew) | BHSA | **GOLD** | full morph+syntax+clause hierarchy |
| GNT (Greek) | Macula-greek → **CenterBLC/N1904 TF** | **GOLD available** (don't build) | hand-built LowFat syntax trees + morph + semantic-domain + `referent`/quotation, already serialized to TF by Clear Bible/CenterBLC (same group as our LXX TF) + tonyjurg/Nestle1904LFT. ACQUIRE + validate, not convert. |
| Vulgate NT (Latin) | UD_Latin-PROIEL | **GOLD acquired** (2026-05-27) | all 27 books, Jerome's Vulgate; OT has no gold |
| LXX (Greek) | CenterBLC/CATSS morph + UD-PTNK syntax | **PARTIAL** | gold morph corpus-wide; gold *syntax* = Gen+Ruth only |
| BoFM (EModE) | Stanza-parse + Carmack gold POS | **BELOW PARITY** | no gold treebank; build via free EModE stack (`reference_emode_substrate`) |
| Quranic Arabic | — | OPEN | not investigated |

## 3. GIGO guardrail

A **source-language-anchored** annotation (BHSA-anchored KJV; CATSS-projected Hebrew→Greek; a parser
trained on another register) is **NOT target-language idea-unit gold.** Projected/inherited boundaries are
**candidates** that must pass the **target-language bidirectional ATU test** before they are boundaries.
(Lesson: the BoFM-Isaiah oracle — Hebrew-anchored KJV breaks are a diagnostic, not a deploy template.)

## 4. Hybrid annotation pipeline (building substrate → v0/v1)

1. **Mechanical parse** (per-corpus parser). 2. **Gold-check** where hand-tagged. 3. **Alignment/transfer
projection** — *with the GIGO caveat* (candidate, not gold). 4. **LLM adjudication** — Claude adjudicates
between layers / proposes breaks / glosses; **NEVER generates morphology or syntax from scratch**
(confabulation = loss of Container-Not-Originator footing). **Every token carries provenance** (source +
confidence) so any boundary traces to gold / parser-derived / projected / LLM-adjudicated. This is the
*semi-automatic treebank* method (parser proposes, human+LLM check) — a recognized scholarly precedent,
defensible only while the human retains adjudication authority and provenance is kept.

## 5. New-corpus START protocol (the gate)

(a) **Inventory the fabric** (see `substrate-resources` / the per-repo `research/SUBSTRATE-INVENTORY.md`).
(b) **Assemble/build substrate to parity.** (c) **ONLY THEN sense-line.** A corpus does not get an ATU
reader until its fabric clears parity; otherwise the BoFM over-merge/over-split story repeats. Prefer
acquiring existing gold (Vulgate-NT, LXX-morph were already out there, scattered) over building from scratch.

## 6. BoFM as the worked example (2026-05-27)

BoFM is below parity (no gold treebank; Stanza mis-parses EModE). The deployed reader (bomreader.com,
mechanical v1.5) is nonetheless **mostly correct** — the "over-split dominant ~15:1" diagnostic was
**inflated** by counting genuine parallel cola as over-splits (the not-a-defect exemplar is 2 Ne 4:26 —
distinct overt subjects per colon). Genuine residuals: independent-predication **interjections** (a
self-contained clause interrupting a host → detach; 6 deployed via v2 overrides 2026-05-27, incl. 3 Ne 19:4,
Alma 32:24, Alma 46:29, Ether 10:1), protasis-severing (narrow mechanical), complement-severing (→ v2 LLM,
needs deixis).
**Chosen fix: v2 LLM-adjudication of judgment-residuals over the mechanical v1** (not more mechanical
rules). BoFM's own substrate upgrade = a free, no-LDC EModE treebank-build (PCEEC + EarlyPrint/MorphAdorner +
a UD parser; PPCEME/LDC optional gold-validation) — `reference_emode_substrate`. This makes BoFM's substrate
the same *kind* as Tanakh/GNT, strengthening the cross-corpus ATU-convergence thesis.

## 7. BoFM build — executed (2026-05-27)

The doctrine, instantiated. Two tracks ran:

**(a) v2 LLM-adjudication of the complement-vs-quote class — SHIPPED to bomreader.com, gate-clean.**
The discourse-voice axis is the residual the mechanical layer can't reach (it needs deixis). Two systematic
sprays (not per-verse swatting), each parity-safe (text identical, only breaks move):
- **frame|quote BREAK** (214 verdicts): detach a speech frame from a direct quote that has its own deictic
  center. All shipped — incl. 15 initially withheld on a *genre* label ("prophetic oracle"), which is **not**
  an ATU criterion; the bidirectional test is the sole arbiter, so they shipped once tested.
- **cognition/speech BIND** (6): rejoin an over-split bare complement (`we know, / that he was a righteous
  man` → one ATU). 15 proposed → **two parallel adversarial audits** (over-merge lens + atomicity lens) each
  independently killed the same 8–9 over-merges (conditionals/oaths/fragments); only the 6 surviving both shipped.
- **Gate:** an independent quality-meter (LLM adjudication of changed verses by arbiters not told the deploy
  direction) returned **47 improvement / 0 regression** — the over-merge meter the canon validators can't provide.

**(b) The substrate upgrade — the "bug spray" for the bulk over-split classes (parse-quality-bound, not
discourse-bound).** Pipeline: PCEEC gold EModE constituency (`pceec_to_conllu.py`, our own PPCHE-Penn→UD
converter — UDConverter is Icelandic-tuned and emitted 0 tokens on PCEEC) → **2.32M tokens of UD, 0 malformed
trees** → train an in-domain EModE dependency parser → re-parse BoFM → swap its syntax into the fabric.

**The unifying artifact = Text-Fabric.** BoFM now has a TF (`readers-bofm/data/tf/`, v0.1 built 2026-05-27):
`book→chapter→verse→atu→word`, 302,624 word slots, 16,004 **atu** nodes (each spans one *deployed* ATU line,
so the corpus is queryable **by atomic-thought-unit**). This is the BHSA-ecosystem format — the **Container**
that makes BoFM structurally comparable to Tanakh/LXX/Vulgate (the cross-corpus convergence substrate). Its
feature layers upgrade independently: v0.1 carries the *weak Stanza* `deprel`/`head` (provisional); the
EModE-parser re-parse rewrites that layer → **v0.2** *in place*. Doctrine point made concrete: the fabric is
the originator-free Container; **the parser's held-out LAS bounds the syntax claims** (PCEEC is letters, BoFM
is scripture-register — close, not identical; report the LAS, don't assume transfer). TF is also the right
serialization target for LXX/Vulgate (CoNLL-U→TF is the only remaining build step there).

## 8. Gates + pitfalls for a TRAINED-parser substrate (BoFM-specific; the GNT analog is acquire-not-train)

BoFM is the one corpus where we *train* a parser (no gold treebank exists). Greek/Hebrew/Latin all have
hand-built treebanks — for those the move is **acquire + serialize/validate, never train** (the GNT gold TF
already exists: CenterBLC/N1904 + tonyjurg/Nestle1904LFT, from Macula-greek; surveyed 2026-05-27). Where we
*do* train (BoFM), three guards apply (the first is the load-bearing one):

1. **Register-decay audit before any TF-layer swap.** The held-out LAS on the *training* register (PCEEC =
   letters) is an OPTIMISTIC ceiling for the *target* register (BoFM = archaic scripture). Before the trained
   parser rewrites the fabric's syntax layer (v0.1→v0.2), **hand-audit its output on a gold target slice**
   (e.g. 2 Ne 4 / Alma 32) against the bidirectional-ATU judgment, and report that decay number — do not
   assume cross-register transfer from the held-out score.
2. **Non-projectivity.** Scripture-register EModE has crossing arcs (extraposition, parenthetical
   interjection — the §1 "interjection" class). A projective transition parser (spaCy) projectivizes and can
   force wrong trees there; if the slice-audit concentrates errors in crossing arcs, switch to a **graph-based
   parser** (biaffine/supar, the GPU route) which predicts non-projective structures natively.
3. **Null tokens / ellipsis.** Dropping Penn traces (`*T*`, `0`) is standard UD-*basic* and is what we do; the
   elided-subject signal (the "shared-vs-distinct subject" axis) lives in the **enhanced-UD empty-node** layer
   — a future add only if that feature is needed, not a v0.2 blocker.

## 9. TF-build audit dispositions + validation suite (Opus red-team, 2026-05-27)

An adversarial audit of `build_tf.py` + the v0.1 fabric found flaws beyond §8. Dispositions (the
container-hardening items are parser-INDEPENDENT → applied at the next build; the harmonization item is
the convergence-track contract; none are "asserted-and-ignored"):

| # | Flaw | Sev | Disposition | When |
|---|---|---|---|---|
| 1 | `head` edge dropped at sentence/ATU boundaries; sentence roots indistinguishable from dropped edges; **sentence layer destroyed** (no `sentence` node) | LOAD | emit a `sentence` node type + an `is_root` slot flag; keep cross-sentence head as edge-absent-but-flagged | builder (now) |
| 2 | **Cross-corpus "convergence" is file-format only, not query-schema** (BoFM `pos`/`deprel` vs BHSA `sp`/`function` vs N1904 `role`/`O2CL`) | LOAD | **harmonization contract**: expose canonical `upos` + `udrel` on EVERY corpus TF; one golden cross-corpus query as a regression test | convergence track |
| 3 | contiguous-span `atu` model breaks on **discontiguous interjection-split hosts**, nested, cross-verse; silent "last line absorbs drift" | LOAD | fail-LOUD ATU-count-identity check now; non-contiguous `atu` nodes (explicit slot-set assignment) at v0.2 | builder (now) + v0.2 |
| 4 | `.tfx` cache serves **stale syntax** on in-place v0.1→v0.2 rewrite | LOAD | **never rewrite in place** — v0.2 = a NEW module dir (`data/tf/0.2/`), version bumped; structure stays in 0.1 as base; add a `parser` provenance value | v0.2 |
| 5 | no per-token **provenance/confidence** (doctrine §4 mandates it) | MOD | `atu`: `boundary_source` (mechanical-v1 / v2-llm / editorial) + `confidence`; slot: `syn_source` | builder (now) |
| 6 | punctuation-as-slots distorts proximity queries + differs from BHSA (no punct slots) | MOD | corpus-wide convention: keep punct slots but `pos=PUNCT` so queries exclude via `pos#PUNCT`; document in the harmonization contract | contract |
| 7 | `atu` not a section/structure → can't `T.text` it; `otext` trailing-space won't reproduce the colometric lines | MOD | add TF `structureTypes`/`structureFeatures` for `atu`; round-trip-text test | builder (now) |
| 8 | Unicode normalization unspecified (bites Hebrew/Greek/Latin cross-corpus matching) | MOD | mandate **NFC** at ingest for every corpus; assert it | builder (now) |
| 9 | PCEEC→UD converter approximations (`ccomp`/`advcl` collapse) become the trained "gold" the binding rules depend on | MOD | measure converter **clause-type** accuracy (not just LAS) on a hand-checked PCEEC slice; release gate | v0.2 gate |
| 10-12 | edge-direction undocumented; `lemma or form` fallback pollutes lemma; chapter-renumber unguarded | MIN | document edge direction; add `lemma_source`; per-book verse-monotonicity assertion | builder (now) |

**Validation suite (the release gate — a built TF must pass ALL before deploy, beyond "it loads"):**
(1) **round-trip** — concatenated `form` per verse == NFC v0 source (mod whitespace), not just the alnum-count
check we have; (2) **ATU-count identity** — `atu` node count per verse == segmentation line count (fail loud,
never absorb-into-last); (3) **edge integrity** — every non-root token has exactly one `head` edge; edge-less
count == Stanza sentence-root count; (4) **provenance completeness** — every `atu` + syntactic feature carries
a `*_source`; (5) **cross-corpus golden query** — one canonical UD query returns comparable hits on BoFM + ≥1
gold corpus (the only test that exercises the convergence thesis itself).

## 10. Substrate vs. lens (vocabulary)

§1's **Container, not Originator** framing entails that any number of
*lenses* — deterministic segmentation functions over the substrate — can
in principle live above the Container. The ATU lens is the one this
document has been about; other lenses are possible but not yet built.
This section names the distinction so substrate-level work that does not
directly serve the ATU lens has shared vocabulary.

### 10.1 Definitions

- **Substrate** — the canonical Text-Fabric serialization of a corpus's
  morphology + syntax + clause structure (§1 "the Container"; §2
  per-corpus fabric-parity tiers). The substrate is lens-neutral.
- **Lens** — a deterministic function `lens(substrate) → segments` whose
  output is a corpus-wide rendered representation. The **ATU lens** is
  the v0 → v1 → v1.5 (→ v2 → v3) pipeline (`framework.md` §3); the
  bidirectional test is **the ATU lens's** sole arbiter. That sole-arbiter
  contract belongs to the ATU lens, not to every lens.

### 10.2 Catalog admission criterion

A lens enters the catalog as **deployed** only when there is corpus-wide
rendered output served from a live reader URL. A lens-candidate enters
the appendix as **substrate-confirmed** only when the substrate-level
signal it would consume is **already extractable** from existing fabric,
with a verified `file:line` citation. Lens names without deployed output
or substrate evidence are *speculative* and do not appear here.

This discipline is the explicit safeguard against the failure pattern of
the reverted `5923b98` commit, which canonized a lens catalog containing
seven speculative entries.

### 10.3 Catalog — deployed lenses

| Lens | Deployment evidence |
|---|---|
| **ATU** | Five reader sites named in the orientation repo map at `~/.claude/CLAUDE.md:101-105` (tanakh-reader.com, bomreader.com, gnt-reader.com, lxx-reader.com, vulgate-reader.com). The single-source-of-truth file `docs/deployment-status.md:11-15` records only the first three rows; that file predates the LXX and Vulgate launches and is **stale**. Per standing rule 8 (external-state claims require fresh verification), the actual live-URL state at any given moment must be re-fetched, not inherited from this row. Open follow-up: update `deployment-status.md` to add the missing rows and remove the staleness footnote here. |

### 10.4 Substrate-confirmed candidate lenses (none deployed)

A naming note: each candidate below is named for the **substrate signal**
that would feed the lens; the scholar's-name parenthetical credits the
theoretical framework that motivates building such a lens, but the
file-line citation supports only the existence of the substrate signal,
not the scholar's theory. The two should not be conflated.

| Candidate | Substrate-level evidence |
|---|---|
| **BHSA half-verse colometric** (Korpel-style, Hebrew) | BHSA exposes a `half_verse` object type whose `label` feature returns `A` / `B` / `C`. Verified at `~/repos/biblical-corpora/bhsa/docs/features/label.md:11-15`. Te'amim-derived (cantillation), not punctuation — passes the standing punctuation-zero-force exclusion. No lens prototype; no rendered output. Korpel/de Moor's colometric framework would consume this signal but the citation itself does not establish that. |
| **Macula discontinuous-token displacement** (Wackernagel-style for δέ, Greek) | Macula sblgnt-lowfat XML attaches `discontinuous="true"` to postpositive δέ tokens. Verified at `~/repos/readers-gnt/research/macula-greek/SBLGNT/lowfat/01-matthew.xml:266-268, 362-364, 534-536`. δέ is the canonical second-position postpositive in NT Greek; `discontinuous` is a general syntactic-tree marker (not Wackernagel-specific) that happens to fire on the right tokens. No lens prototype; no rendered output. |

(Verse division is *not* listed here. Verse boundaries are part of the
substrate's coordinate system — not a downstream segmentation.)

### 10.5 What this vocabulary does not license

The lens framing does **not**:

- **Weaken the bidirectional ATU test.** It remains sole arbiter for the
  ATU lens. Any future lens declares its own contract; the ATU lens
  contract is unchanged.
- **Admit genre as an ATU criterion.** A candidate lens (e.g., Korpel
  colometric) may be genre-aware in its own scope; that does not
  retroactively make genre an ATU criterion. The standing rule
  (`framework.md` and per-repo memory) holds.
- **Admit punctuation force in any corpus.** Te'amim are not punctuation
  — they are cantillation marks exposed as discrete BHSA features (see
  the half-verse example). The "punctuation has zero force across all
  corpora" rule is unchanged.
- **License speculative catalog entries.** The §10.2 admission criterion
  is load-bearing. The prior `5923b98` failure was a catalog of seven
  speculative lenses; this section's catalog has one deployed entry and
  two substrate-confirmed candidates, all with file-line citations.
