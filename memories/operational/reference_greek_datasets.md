---
name: reference-greek-datasets
description: "Per-dataset capability catalog for GNT work — what each Greek treebank/resource encodes, WHERE it lives, what it can/can't discriminate. The record whose absence caused the 'structurally impossible' error."
metadata:
  node_type: memory
  type: reference
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/aaf6bcc5922399a7@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

The GNT ATU work has MULTIPLE Greek datasets. The engine currently sources only the THIN `sblgnt-lowfat`; before declaring any feature "unavailable" check the richer ones here. Forgetting this catalog is what produced the 2026-05-26 "the mechanical layer structurally cannot see deixis/complement-role" error — Macula tags exactly those. See [[feedback_mechanical_first_for_own_review]] + [[feedback_verify_deploy_state_never_assert]].

## Macula Greek — the RICH treebank (use for binding decisions)
- **Path:** clone `C:\Users\bibleman\repos\readers-gnt\research\macula-greek\SBLGNT\lowfat\` (per-book `01-matthew.xml` … `27-revelation.xml`); flat TSV `C:\Users\bibleman\Dropbox\03-Biblical_Studies\Greek\corpora\macula-greek-data\macula-greek-SBLGNT.tsv`; format note `readers-gnt\research\macula-format.md`.
- **Encodes (the discriminating features):**
  - **clause-level `role`** on `<wg class="cl">`: `o` (object-complement) vs `adv` (adverbial) — the **object-slot test**.
  - **`rule`** on the clause wrapper: **`that-VP`** = ὅτι/ἵνα + VP **complement** clause (bind-eligible) vs **`sub-CL`** = causal/subordinate (stand). The complement-vs-causal distinction, marked explicitly. (Verified on Matt 5:36 `sub-CL`=causal→stand; Rev 10:6 `that-VP`=oath-content→bind; Rom 8:16 `that-VP`→bind.)
  - word-level **`person`** (first/second/third) + **`subjref`/`referent`** participant tracking — the **deixis test** (shared vs. shifted deictic center; person alone is insufficient, needs referent).
  - **`frame`** = PropBank-style semantic argument structure (A0/A1); plus `role`, `lemma`, `morph`, `domain`/`ln` (Louw-Nida), `gloss`, `after` (punctuation), `discontinuous`.
- **Clause rules of colometric interest:** `Conj-CL`, `sub-CL`, `that-VP`, `ClCl`/`ClCl2`/`CLaCL`, `DetCL` (nominalized/relative). The DISCRIMINATING tag sits on the **immediate** wrapper around the ὅτι-clause, not the outer combination node.
- **Helper scripts (plumbing partly built):** `readers-gnt/scripts/macula_clauses.py`, `macula_predication.py`, `macula_valency.py`, `macula_wordgroups.py`, `audit_anaphoric_gen_abs_macula.py`.

## sblgnt-lowfat — the THIN treebank (current LIVE v1 source)
- **Path:** `C:\Users\bibleman\repos\biblical-corpora\greek-new-testament\syntax-trees\sblgnt-lowfat\xml\`.
- Clauses pre-marked `<wg class="cl">` (nested); each `<w>` carries `osisId`, word-level `role` (`s/v/vc/p/adv/o/io/o2`), POS `class`, `lemma`. Mood/tense/case joined from MorphGNT (FINITE=`IDSO`, ptcp=`P`, inf=`N`).
- **LIMITS (verified):** the `<wg class="cl">` wrapper `role` is **empty** — does NOT mark complement-vs-adverbial; **person is NOT extracted** by the current loader (only tense/mood/case). These limits are real for THIS source — and were wrongly generalized to "the mechanical layer can't see it" when Macula can. Engine = `sblgnt_generate.py` + `sblgnt_v1_fabric.py`.

## Lexham Discourse GNT (LDGNT) — calibration only, not a runtime dep
- **Path:** `C:\Users\bibleman\Dropbox\03-Biblical_Studies\Greek\discourse\Lexham-Discourse-GNT\`.
- GNT analog of LDHB. Label hierarchy: SENTENCE/PRINCIPLE/COMPLEX (top-level) ; SUPPORT/ELABORATION/SUB-POINT/BULLET (sub-relations). **Calibration finding:** the cold-eye ATU sits at LDGNT's independent-clause (SENTENCE) level and absorbs its BULLET/ELABORATION sub-splits — same relation cold-eye had to LDHB in Hebrew. Consult for comparison/calibration, never as a runtime dependency.

## PROIEL-lowfat — pilot rule-derivation source
- **Path:** `…\greek-new-testament\syntax-trees\proiel-lowfat\xml\proiel-lowfat.xml` (~31M). Dependency treebank, whole NT incl. Revelation. Used in the pilot to derive the rule catalog.
- **Gotcha:** PROIEL batches all of a sentence's verse milestones at the top before any `<w>`; naive verse-tracking dumps every word into the batch's last verse — group at sentence level.

## Also present (under `syntax-trees/`)
MorphGNT (mood/lemma, no clause syntax), nestle1904, nestle1904-lowfat, emdros-mql.

## Related
[[reference_biblical_studies_folder]] (Dropbox Greek layout) · [[reference_corpus_pipeline_map]] (per-repo ATU layer). The Greek binding-rule catalog (`atu-method/docs/binding-rules-greek.md`) is the eventual home for the per-rule Macula feature-signatures; not yet written.
