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
| GNT (Greek) | Macula | **ADEQUATE** | rich: `that-VP`/`sub-CL`, role, frame, `referent` |
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
**inflated** by counting genuine parallel cola as over-splits. Genuine residuals: protasis-severing (narrow
mechanical), complement-severing (→ v2 LLM, needs deixis), the rare parenthetical-aside over-merge.
**Chosen fix: v2 LLM-adjudication of judgment-residuals over the mechanical v1** (not more mechanical
rules). BoFM's own substrate upgrade = a free, no-LDC EModE treebank-build (PCEEC + EarlyPrint/MorphAdorner +
a UD parser; PPCEME/LDC optional gold-validation) — `reference_emode_substrate`. This makes BoFM's substrate
the same *kind* as Tanakh/GNT, strengthening the cross-corpus ATU-convergence thesis.
