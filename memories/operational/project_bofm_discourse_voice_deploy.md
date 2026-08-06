---
name: project_bofm_discourse_voice_deploy
description: "BoFM discourse-voice complement-vs-quote class-fix shipped to bomreader.com (frame|quote break + cognition/speech bind), gate-closed by an independent quality-meter"
metadata: 
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (newest b8adeede15761c57@vN, state ~2026-06); possibly stale — re-verify before relying.


The first two SYSTEMATIC ATU class-fixes (not per-verse swatting) shipped to bomreader.com on
2026-05-27, both from the discourse-voice / complement-vs-quote axis:

- **V1 frame|quote BREAK** (commit a8cfb05): 197 breaks (conf≥0.92) detaching a speech frame from its
  direct quote (quote has own deictic center → STAND). overrides.json 102→299.
- **V2 cognition/speech BIND** (commit 995e109): 6 over-split bare complements rejoined ("we know, /
  that he was a righteous man" → one ATU). 29 candidates → 15 proposed → **two parallel adversarial
  audits (over-merge + atomicity lenses) independently killed 8-9 over-merges** (conditionals,
  oath-formulas, fragments); only the 6 surviving BOTH audits shipped. This is the §7.3 gate working:
  it prevented 9 over-merges, Stan's red line.
- **Revert** (commit 3f256b9): 2 Ne 15:19 "That say:" — a relativizer+bare-verb fragment the break
  spray wrongly treated as a frame; caught by the quality-meter, reverted.

**The quality-meter (`readers-bofm/scripts/quality_meter.py`) is the designated independent over-merge
arbiter** — the canon validators don't detect over-merge and the bidir gate is Stanza-circular. Ran it
candidate-vs-pre-deploy-baseline → 203 changed verses → 48-verse genre-spread sample → TWO arbiters NOT
told the deploy direction → after the one revert: **47 improvement / 0 regression** = DEPLOY confirmed.
This is the gate Stan defined for autonomous deploys; run it the same way next time.

Working artifacts in `~/repos/readers-bofm/private/substrate/emode-substrate/` (gitignored; relocated 2026-05-27 from biblical-corpora/ container — "each project its own data"):
`frame-quote-verdicts.json`, `bind-candidates.json`, `bind-verdicts.json`, `bind-audit-{overmerge,
atomicity}.json`, `BUILD-PLAN.md` (STATUS), `HELD-FOR-STAN.md` (15 prophetic breaks @0.85 + audit-
overturned conditionals).

**Next BoFM class is NOT another override spray.** The remaining big validator counts (rule_19_ud 959,
rule_07_ud 599, polysyndetic_verb_chain 350) are OVER-SPLIT classes driven by Stanza-EModE parse quality
→ need the PCEEC-trained parser substrate (multi-session, [[project_bofm_substrate_quality]]), per the
substrate doctrine. See [[reference_emode_substrate]] and [[feedback_no_fly_swatting]].

## TF + substrate build — EXECUTED/underway (2026-05-27, same session)

- **Text-Fabric v0.1 BUILT + committed** (`readers-bofm/data/tf/`, `scripts/build_tf.py`): book→chapter→
  verse→**atu**→word, 302,624 slots, 16,004 ATU nodes (each spans one DEPLOYED ATU line → queryable BY
  atomic-thought-unit), BHSA-ecosystem format = the cross-corpus convergence Container. v0.1 carries the
  PROVISIONAL weak-Stanza deprel/head; layers upgrade in place.
- **PCEEC→UD conversion DONE**: `pceec_to_conllu.py` (our own PPCHE-Penn→UD converter — UDConverter is
  Icelandic-tuned + emitted 0 tokens on PCEEC). 97,169 sentences / 2.32M tokens, 0 malformed, gold
  clause-types (ccomp/xcomp/advcl/acl:relcl) flow through.
- **Parser training LOCAL on CPU** (no GPU on this box; `colab/emode_parser.ipynb` = MacBERTh-GPU alt that
  Stan would run). spaCy tagger+parser on the 2.32M-token set; LAS climbing (~69 @ step 1000). Gotchas hit +
  fixed: torch DLL broken→CPU wheel; broken urllib3/six poisoning env; shell-& bg processes die (use harness
  run_in_background); Windows file-lock on output dir (kill python + fresh dir); spaCy `patience` is in STEPS
  not epochs (patience=3 → instant early-stop; set patience=0).
- **Next**: train converges → re-parse BoFM (`bofm_toparse.conllu`, existing tokenization) → rewrite TF
  deprel/head → **v0.2** → run binding rules on good syntax → the bulk over-split classes. Canon now in
  `atu-method/docs/03-implementation/substrate.md` §7. Stan's standing ask: the TF pays off long-term (cross-corpus queries).
