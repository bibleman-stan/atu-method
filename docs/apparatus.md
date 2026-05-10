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

## What the apparatus is NOT

- Not a rhetorical-parallelism analyzer. Parallelism (Lowth, Kugel, Berlin, Watson, Parry) is a separate scholarly layer that may overlap with ATU revelation but is not the apparatus's target.
- Not a critical text-edition tool. The apparatus takes canonical text as a fixed input; textual criticism happens upstream.
- Not a translation tool. The English layer in non-English readers is anchored to a public-domain translation (KJV via STEPBible-Data alignment) with regex-driven modernization, not generated translation.
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
