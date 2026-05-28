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
