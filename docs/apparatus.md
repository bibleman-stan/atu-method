# The ATU Apparatus — High-Level Overview

This document is the canonical statement of what the apparatus is and what it produces. It is the entry point for readers who want to understand the system before diving into the architecture, framework, or rule details.

---

## Purpose

The ATU apparatus produces **colometric reading editions of canonical texts** — editions where each line on the page renders one atomic thought unit (ATU), a span of text the reader can take in as a single complete unit of meaning.

ATU revelation, not invention. The apparatus exposes structure already present in the text rather than imposing structure derived from rhetorical theory, prosodic tradition, or editorial overlay.

## Inputs

- A **canonical source text** in the target language (2020 LDS Book of Mormon; SBLGNT for the Greek New Testament; Westminster Leningrad Codex for the Hebrew Bible).
- A **parse layer** — BHSA via Text-Fabric for Hebrew; Macula Greek for Greek; Stanza CoNLL-U for EME English. Provides clause-atom-level syntactic structure over the source.
- A **language-specific binding-rule catalog** — feature-driven rules that merge parse-derived clauses into ATU candidate groups (`docs/binding-rules-hebrew.md` for the validated Hebrew catalog).
- A **shared methodology framework** — bidirectional test, mechanical-first pipeline, change discipline (this repository, `docs/framework.md`).

## Outputs

- A **colometric reading edition** (one ATU per line on the page) usable by any reader — from ESL or child all the way to serious researcher.
- **Reader-facing delivery** in three forms per corpus: web reading app, optional audio narration, optional study-layer overlays (e.g., archaic-word modernization).

## What the reader sees (end-state per sibling)

The apparatus produces three sibling readers sharing one design language. When complete, each shows source text broken into ATU lines with study layers stacked under each line. Switching between readers, the user recognizes the topbar, the modern-mode pill, the swap behavior; only the source-language layers differ.

**readers-bofm** (reference implementation). Each English ATU line standalone. The modern-mode pill toggles archaic→modern in place: `hath`→`has`, `unto`→`to`, `thee`→`you`. Audio narration per chapter. The reference for all sibling UX behavior.

**readers-gnt**. Each Greek ATU line with its KJV English aligned beneath, line-for-line — never reordered, never straddling line breaks. The modern-mode pill toggles KJV archaic→modern on the English layer: `begat`→`fathered`, `verily`→`truly`. Greek source unchanged on toggle.

**readers-tanakh**. Each Hebrew ATU line with four layers stacked: Hebrew source (right-to-left, pointed) / transliteration (Latin phonetic) / interlinear morph+gloss (Macula-Hebrew structural) / KJV English (line-aligned). The modern-mode pill toggles the English layer only — Hebrew, transliteration, and interlinear layers don't move. Four-layer integrity is the single hardest invariant.

**Cross-sibling unification.** KJV is the unifying English voice across NT (gnt-reader) and OT (tanakh-reader). The swap-system is the unifying accessibility layer across all three. The ATU break is the unifying reading rhythm. The topbar / pill / settings sheet UX is identical.

## How the KJV-anchored English layer is produced

For non-English readers (gnt, tanakh), the English layer is **not generated translation**. It is KJV verbatim text distributed per source-language ATU line by Strong's-number matching:

```
Source-language token (TAGNT or TAHOT)  →  Strong's number(s)
                                              ↓
                                   ┌─────────────────────────┐
                                   │  Match against per-KJV-  │
                                   │  word Strong's tags in   │
                                   │  the same verse (MetaV   │
                                   │  KJV+Strong's database)  │
                                   └─────────────────────────┘
                                              ↓
                            KJV words flow to the ATU line of their
                            matched source-token, in KJV verse order.
                            Italic KJV words (translator additions
                            with no original-language backing) attach
                            to the line of the nearest non-italic
                            neighbor.
                                              ↓
                            Swap-system wraps KJV archaisms with
                            data-mod modern equivalents.
                                              ↓
                            HTML render — modern-mode pill toggles
                            archaic→modern in-place on the English
                            row only; source-language rows unchanged.
```

**Substrate components** (universal infrastructure at `atu-method/data/`):

- `tagnt-source/` (in readers-gnt, CC BY 4.0) / `stepbible-tahot/` (in readers-tanakh, CC BY 4.0) — STEPBible's per-source-token Strong's tagging for Greek (TAGNT) and Hebrew (TAHOT).
- `kjv-strongs/MetaV_*.csv` (viz.bible, CC-BY-SA 3.0) — per-KJV-word Strong's tagging + `Italic` flag for translator-supplied words.
- `lexicons/TBESG.txt` + `TBESH.txt` (STEPBible, CC BY 4.0) — Strong's brief gloss lexicons.

**Algorithm components** (universal infrastructure at `atu-method/atu_method/kjv_alignment/`):

- `metav_loader.py` — loads MetaV CSVs once; builds `(book, ch, vs) → [KjvWord]` index. Module-level cache.
- `strongs_normalize.py` — normalizes Strong's number formats across MetaV, TAGNT, TAHOT.
- `distribute.py` — multi-pass positional-aware distribution (claim → synonymy sweep → italic/orphan attachment → defensive positional fallback).
- `api.py` — `align_verse(book_osis, chapter, verse, source_atu_lines_with_tokens, metav_dir)` entry point.

**Per-corpus consumers** (per-repo thin wrappers, ~50–200 lines each):

- `readers-gnt/scripts/regenerate_english_kjv.py` — parses TAGNT, calls `align_verse()` per verse.
- `readers-tanakh/scripts/regenerate_english_kjv.py` — parses TAHOT (with BHS-vs-English versification offset handling), calls `align_verse()` per cola.

**Why this works.** Strong's exhaustive concordance was compiled by indexing the KJV — every Strong's number is a pointer to a set of KJV English words. So per-source-token Strong's (STEPBible) + per-KJV-word Strong's (viz.bible MetaV) yields a deterministic per-source-token-to-KJV-word mapping. The KJV is the verbatim English; the Strong's index is the routing table. No statistical alignment, no editorial translation, no per-corpus retraining.

**Why BoFM's swap-system carries over directly.** The BoFM uses KJV-style archaic English by construction (Skousen 2009, *The Earliest Text*). The BoFM `.swap` class system already modernizes BoFM's KJV-derivative archaisms. KJV NT and KJV OT share most of these archaisms with one corpus-specific extension each: KJV NT adds `begat`, `wist`, `holpen`; KJV OT adds `firmament`, `behold`, `peradventure`. Universal swap-lists at `atu-method/data/swaps/` with NT/OT-specific extensions.

## Mechanical-first architecture

The bidirectional test is the criterion: a line is a legitimate ATU if and only if it satisfies BOTH forward grammatical closure and backward referential self-containment.

The pipeline takes parse-derived clauses (BHSA clause-atoms for Hebrew; Macula clause nodes for Greek; CoNLL-U sentences for EME English) and applies a small catalog of feature-driven binding rules to merge them into ATU candidate groups. Each binding rule fires based on parse features (clause type, head verb lemma, text-prefix) and is justified by the bidirectional test.

**Validated for Hebrew (Tanakh) across four chapters / four genres**: narrative+dialogue, wisdom poetic, prophetic poetic, casuistic legal. Boundary F1 against the Lexham Discourse Hebrew Bible stays in the 85-91% range; recall stays ≥ 80%. Pipeline output is an editorially-refinable draft, not a final rendering — but the editorial work shifts from hours-per-chapter to minutes-per-chapter.

See `framework.md` for the methodology specification and `binding-rules-hebrew.md` for the validated 14-rule Hebrew catalog.

## What the apparatus is NOT

- **Not a rhetorical-parallelism analyzer.** Parallelism (Lowth, Kugel, Berlin, Watson, Parry) is a separate scholarly layer that may overlap with ATU revelation but is not the apparatus's target. Parallel cola where each colon independently passes the bidirectional test are separate ATUs regardless of whether the parallelism is synonymous, antithetic, or synthetic.
- **Not a critical text-edition tool.** The apparatus takes canonical text as a fixed input; textual criticism happens upstream.
- **Not a translation tool.** The English layer in non-English readers is KJV verbatim text (1769 Cambridge edition, public domain) distributed per source-language ATU line via Strong's-number matching — with swap-system modernization, not generated translation.
- **Not a deterministic prior on editorial overlays.** Te'amim, NA28 paragraph structure, BHS sifrei emet layout, ancient codex colometric arrangements are calibration evidence consulted at audit time only, never piped into the candidate-generation pipeline as adjudicators.

## Where to read next

- [`framework.md`](framework.md) — Methodology specification (bidirectional test, mechanical-first architecture).
- [`binding-rules-hebrew.md`](binding-rules-hebrew.md) — The 14 validated Hebrew binding rules.
- [`toolset-architecture.md`](toolset-architecture.md) — Pipeline implementation (v0→v3 stages).
- [`methodology-position.md`](methodology-position.md) — Relationship to LDHB / discourse-grammar references.
- [`glossary.md`](glossary.md) — Defined terms.
- [`../memories/`](../memories/) — Cross-project discipline lessons.

## Reference implementation

[`readers-bofm`](https://github.com/bibleman-stan/readers-bofm) is the reference implementation. Patterns in this repository were extracted from its applier patterns and methodology canon. Sibling reader editions (readers-gnt, readers-tanakh) are calibrated against the BoFM reference.
