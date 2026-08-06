---
name: corpus-pipeline-layer-map
description: Per-repo ATU pipeline layer naming (Tanakh/GNT/BoFM) + the shared mechanical-first method + which differences are genuine vs accidental drift to normalize
metadata: 
  node_type: memory
  type: reference
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`1fd1198a-abfe-4cfa-974f-8c5639773dd6/5749346b399ac69a@v3`); state as of 2026-05-24 (snapshot mtime); possibly stale — re-verify before relying.

The canonical ATU method is the same across corpora; the per-repo **directory naming has drifted** and must not be trusted to line up. This pins the map.

## Framework abstract stages (atu-method/docs/01-normative/framework.md §3)

`v0` source → `v1` treebank clause-atoms → `v1.5` binding rules (primary segmenter) → `v2` *optional* narrow LLM adjudication on residuals → `v3` editorial review. **There is no `v4` stage in the canonical scheme** — the binding-rule output (v1.5) is itself a publishable draft.

**Mechanical-first deploy = v0 → v1 → v1.5, skipping v2 (LLM) and v3 (editorial).** Those two are the *refinement* passes layered on later ("deploy then refine"). No corpus has run a real v2-LLM stage yet.

## Per-repo ACTUAL directory layers (do not assume they match the framework numbers)

| repo | source | clause-atoms (v1) | binding-rule output = LIVE | scratch draft | treebank | reconciler? |
|---|---|---|---|---|---|---|
| **readers-tanakh** | `v0` | `v1` | **`v2/heb`** (+ eng-kjv, translit, eng-interlinear) | `v2-pipeline-draft` | BHSA | **YES** (`_align_words_to_v0`) |
| **readers-gnt** | `v0-prose` | `v1` | **`v1.5/grk`** (+ eng-kjv) | — (draft removed) | sblgnt-lowfat + MorphGNT | **NO** |
| **readers-bofm** | `v0-bofm-original` | `v1-skousen-breaks` (NOT a treebank — borrowed from Skousen edition) | **`v2-mine`** | — | none yet | n/a |

So: the **live layer is `v2` in Tanakh, `v2-mine` in BoFM, `v1.5/grk` in GNT**; and **`v1` means treebank-clause-atoms in Tanakh/GNT but Skousen's textual breaks in BoFM**. That is accidental history, not design — though GNT's `v1.5` label is now *honest* (relabeled from `v4` on 2026-05-22 because "v4" overstated the stage; see below).

## What is GENUINELY different (must stay different)

- **Treebank source per language**: BHSA (Hebrew), sblgnt-lowfat+MorphGNT (Greek), and — for BoFM/LXX/Vulgate — *none exists*, so we must build our own v1 clause-atom source (see [[project-corpus-v1-substitutes]]). BoFM currently leans on Skousen/Parry breaks as a stopgap, not mechanical ATU derivation.
- **Reconciler**: needed ONLY when the treebank word-stream ≠ the display word-stream. Tanakh anchors on BHSA but emits TAHOT forms → needs `_align_words_to_v0` (source of the 3.5%/823-verse mismatch, the BHSA-canon-migration arc). GNT needs none because **sblgnt-lowfat IS the SBLGNT display text** — the architectural win of the GNT pivot.
- **Binding-rule catalog**: Hebrew B1–B14 vs Greek R1–R28. Language-specific (the cross-corpus-convergence thesis predicts they mirror, but each is re-derived, not assumed).

## "New hotness" = the high-fidelity method (replaces the old-and-busted)

- **Own-fabric, display-text-native treebank** (lowfat IS the display text) → no reconciler, no edition gap. (Old/busted: bridging from PROIEL — different+incomplete edition — via a reconciler; retired.)
- **Surface-ORDER emit**: a display line is a maximal run of surface-consecutive words sharing one ATU id, so flattened text == source order (`verify_word_order` = 0). (Old/busted: group-by-clause-then-order, which reordered discontinuous clauses — was silently corrupting word order.)
- **Binding rules ported to validator spec in v1.5** (GNT: R3/R4/R7/R8/R9 = "leader never trails a line, merge forward"; R10 cognition-ὅτι merge; R7 vocative whole), validated by `validators/run_all.py` + `verify_word_order` gates. (Old/busted: legacy post-hoc heuristic auto-fixers; BoFM's purged Firestore-PWA exploration.)

## Stage-naming reconciliation (2026-05-22 — SUPERSEDES the old "normalize-to-v4" plan)

The earlier open decision proposed normalizing every repo's final layer **to `v4`**. That is **reversed.** The canonical framework has **no `v4` stage** (v0 / v1 / v1.5 / v2 / v3; the v1.5 binding-rule output is itself the publishable draft). So "v4" was a fiction inherited from GNT's retired machine-tier scheme.

What was done instead: **GNT's deployed dir relabeled `v4/grk` → `v1.5/grk`** (and `v4/eng-kjv` → `v1.5/eng-kjv`), byte-identical deploy (commit b3e2547c). The honest label is what the stage actually is: a mechanical-first v1.5 baseline, not a methodology-complete edition. atu-method `architecture.md` + `glossary.md` reconciled to mechanical-first (commit f8a51cd; the stale 2026-05-17 LLM-primary three-stage language that caused the "v3/v4 are LLM-informed" confusion was retired 2026-05-18).

**The remaining genuine naming drift** (Tanakh live=`v2`, BoFM live=`v2-mine`, GNT live=`v1.5`) is not yet normalized; if/when it is, normalize toward the framework stage-names (v1.5 for binding-rule output), NOT toward a nonexistent v4.

## Convergence decision (2026-05-22): GNT adopts the idea-unit bar

GNT's measured status is **~72% on the idea-unit bar** (44–85% by genre) — vs the misleading "0 canon failures" structural proxy. Dominant failure mode = **over-splitting** (dependent clauses severed from their heads), the *opposite* of BoFM's over-merge. The cure is to **port the BoFM binding discipline** (bind subordinate/ccomp/restrictive-relative; subject+predicate together; vocatives bind to their clause) into the GNT v1.5 fabric. Stan chose "Converge to the idea-unit bar" — so GNT's per-repo R-rule canon (esp. the universal-vocative + over-split rules) is to be revised to match the idea-unit bar, which decides what counts as an error. This is the queued **GNT improvement play**.
