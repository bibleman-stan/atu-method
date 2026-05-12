# The ATU Apparatus — High-Level Overview

**This document is the canonical statement of what the apparatus is and what it produces.** It is the entry point for readers who want to understand the system before diving into the architecture, framework, or rule details.

---

## Purpose

The ATU apparatus produces **colometric reading editions of canonical texts** — editions where each line on the page renders one atomic thought unit (ATU), a span of text the reader can take in as a single complete unit of meaning.

ATU revelation, not invention. The apparatus exposes structure already present in the text rather than imposing structure derived from rhetorical theory, prosodic tradition, or editorial overlay.

## Inputs

- A **canonical source text** in the target language (2020 LDS Book of Mormon; SBLGNT for the Greek New Testament; Westminster Leningrad Codex for the Hebrew Bible).
- A **parsed corpus** — Universal Dependencies (UD) annotation, Macula constituent trees, or equivalent — providing morpho-syntactic structure over the source.
- A **language-specific editorial canon** — proposition-first generative principle plus language-specific rule detail (§5 of each per-corpus canon).
- A **shared methodology framework** — atomic-thought criterion, five structural justifications, four merge-overrides, decision procedure, change protocol (this repository, `docs/framework.md`).

## Outputs

- A **colometric reading edition** (one ATU per line on the page) suitable for ESL readers, students, and general audiences.
- A **transaction log** of every editorial decision made by the mechanical pipeline, supporting full rollback.
- A **per-rule audit trail** documenting where each rule was applied and where it was excluded.
- **Reader-facing delivery** in three forms per corpus: web reading app, optional audio narration, optional study-layer overlays (e.g., archaic-word modernization).

## What the Reader Sees (end-state per sibling)

The apparatus produces three sibling readers sharing one design language. When complete, each shows source text broken into ATU lines with study layers stacked under each line. Switching between readers, the user recognizes the topbar, the modern-mode pill, the swap behavior; only the source-language layers differ.

**readers-bofm** (reference implementation). Each English ATU line standalone. The modern-mode pill toggles archaic→modern in place: `hath`→`has`, `unto`→`to`, `thee`→`you`, etc. Audio narration per chapter. The reference for all sibling UX behavior.

**readers-gnt**. Each Greek ATU line with its KJV English aligned beneath, line-for-line — never reordered, never straddling line breaks. The modern-mode pill toggles KJV archaic→modern on the English layer: `begat`→`fathered`, `verily`→`truly`. Greek source unchanged on toggle.

**readers-tanakh**. Each Hebrew ATU line with four layers stacked: Hebrew source (right-to-left, pointed) / transliteration (Latin phonetic) / interlinear morph+gloss (Macula-Hebrew structural) / KJV English (line-aligned). The modern-mode pill toggles the English layer only — Hebrew, transliteration, and interlinear layers don't move. Four-layer integrity is the single hardest invariant.

**Cross-sibling unification.** KJV is the unifying English voice across NT (gnt-reader) and OT (tanakh-reader). The swap-system is the unifying accessibility layer across all three — same `.swap` class with `data-orig`/`data-mod` attributes, same modern-mode pill UX, same per-toggle DOM-level word replacement. The ATU break is the unifying reading rhythm. The topbar / pill / settings sheet UX is identical.

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

**Substrate components (universal infrastructure at `atu-method/data/`):**
- `tagnt-source/` (in readers-gnt, CC BY 4.0) / `stepbible-tahot/` (in readers-tanakh, CC BY 4.0) — STEPBible's per-source-token Strong's tagging for Greek (TAGNT) and Hebrew (TAHOT).
- `kjv-strongs/MetaV_*.csv` (viz.bible, CC-BY-SA 3.0) — per-KJV-word Strong's tagging + `Italic` flag for translator-supplied words. STEPBible publishes per-source-token Strong's but NOT a Tagged-KJV file; viz.bible's MetaV is the KJV-side wiring.
- `lexicons/TBESG.txt` + `TBESH.txt` (STEPBible, CC BY 4.0) — Strong's brief gloss lexicons. Used as fallback / sanity reference when MetaV has gaps.

**Algorithm components (universal infrastructure at `atu-method/atu_method/kjv_alignment/`):**
- `metav_loader.py` — loads MetaV CSVs once, builds `(book, ch, vs) → [KjvWord]` index. Module-level cache.
- `strongs_normalize.py` — normalizes Strong's number formats across MetaV (`G846`), TAGNT (`G0846=V-AAI-3S`, alt-Strong's), TAHOT (`{H7225G}`, compound `H9003/H7225G`, backslash-separated meta-codes).
- `distribute.py` — three-pass distribution: first-match-wins claim → synonymy sweep for unclaimed KJV words → nearest-neighbor attachment for italics/orphans.
- `api.py` — `align_verse(book, ch, vs, source_atu_lines, metav_dir)` convenience entry point.

**Per-corpus consumers (per-repo thin wrappers, ~50–200 lines each):**
- `readers-gnt/scripts/regenerate_english_kjv.py` — parses TAGNT, calls `align_verse()` per verse.
- `readers-tanakh/scripts/regenerate_english_kjv.py` — parses TAHOT (with BHS-vs-English versification offset handling), calls `align_verse()` per cola.

**Why this works:** Strong's exhaustive concordance was compiled BY indexing the KJV — every Strong's number IS a pointer to a set of KJV English words. So per-source-token Strong's (STEPBible) + per-KJV-word Strong's (viz.bible MetaV) = deterministic per-source-token-to-KJV-word mapping. The KJV is the verbatim English; the Strong's index is the routing table. No statistical alignment, no editorial translation, no per-corpus retraining.

**Why bomreader's swap-system carries over directly:** the BoFM uses KJV-style archaic English by construction (Skousen 2009, *The Earliest Text*). The bomreader `.swap` class system already modernizes BoFM's KJV-derivative archaisms. KJV NT (gnt-reader) and KJV OT (tanakh-reader) share most of these archaisms — `hath`, `thee`, `verily`, `unto`, `betwixt` — with one corpus-specific extension each: KJV NT adds `begat`, `wist`, `holpen`; KJV OT adds `firmament`, `behold`, `peradventure`. Universal swap-lists at `atu-method/data/swaps/` with NT/OT-specific extensions. Same `apply_swaps()` mechanism.

## What the apparatus is NOT

- Not a rhetorical-parallelism analyzer. Parallelism (Lowth, Kugel, Berlin, Watson, Parry) is a separate scholarly layer that may overlap with ATU revelation but is not the apparatus's target.
- Not a critical text-edition tool. The apparatus takes canonical text as a fixed input; textual criticism happens upstream.
- Not a translation tool. The English layer in non-English readers is KJV verbatim text (1769 Cambridge edition, public domain) distributed per source-language ATU line via Strong's-number matching between STEPBible TAGNT/TAHOT and viz.bible MetaV — with swap-system modernization, not generated translation. See "How the KJV-anchored English layer is produced" above.
- Not a deterministic prior on editorial overlays (te'amim, NA28 paragraph structure, BHS sifrei emet layout, ancient codex colometric arrangements). External editorial overlays are **calibration evidence consulted at audit time only**, never piped into the candidate-generation pipeline.

## Where to read next

- [`architecture.md`](architecture.md) — Four-plane architectural decomposition with interface contracts between planes.
- [`framework.md`](framework.md) — Operational framework consumed by per-corpus canons.
- [`rule-template.md`](rule-template.md) — The MISRA-style template every per-corpus rule must follow.
- [`glossary.md`](glossary.md) — Defined terms (ATU, J1–J5, M1–M4, N=2 adjudication, etc.).
- [`change-protocol.md`](change-protocol.md) — §7 — audit-extension rules for canon changes.
- [`../memories/`](../memories/) — Cross-project discipline lessons learned during BoFM development.

## Reference implementation

[`readers-bofm`](https://github.com/bibleman-stan/readers-bofm) is the proof-of-concept and reference implementation. Patterns in this repository were extracted from its validator suite, applier patterns, and methodology canon. Sibling reader editions (readers-gnt, readers-tanakh) are calibrated against the BoFM reference.
