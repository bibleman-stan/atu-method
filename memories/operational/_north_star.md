---
name: north-star-settled-decisions
description: SETTLED decisions + standing calls for the biblical-reader/TF program — RELOAD on every compaction-resume; stop re-litigating these
metadata: 
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (455e2f1f-…/918117a5ceb3cffb@v4, state 2026-06-01); possibly stale — re-verify before relying.


# North-star — SETTLED. Do not re-derive after compaction. (Stan, 2026-05-28)

The high doctrine survives compaction; this tactical/decision layer historically did NOT — Claude
kept re-litigating settled calls (run-vs-close, SUD-fork, data placement, genre holds). **This file
is the fix. Read it on every compaction-resume and treat everything here as closed unless Stan
reopens it.** Do not re-prove banked results; do not restart parked/closed work.

## KEYSTONE RESULT — banked, negative, valuable (CLOSED)

The **manufactured-gold parser route does NOT clear the bar for BoFM.** A parser trained on PCEEC
(Early-Modern *letters*) to parse BoFM *scripture* lost a blind 2-adjudicator gate to off-the-shelf
**Stanza 21–6** (5–0 on polysyndeton, the target class). Root cause = the **register gap**: the
dependency *supervision* is PCEEC letters no matter how strong the encoder, so a stronger encoder
(e.g. MacBERTh) does NOT close it. **"Can I run it" was never the question; "should we" is — and the
answer is no.** Do not conflate those again.

- **THE *PARSER-TRAINING* TRACK IS CLOSED** — specifically, training a parser on out-of-register data (e.g. PCEEC letters) to *replace* baseline Stanza. **LLM post-editing of baseline Stanza output to `v0-cache/` is a distinct mechanism and is NOT closed.** BoFM rests on Stanza (TF v0.1) + a three-lever framework (see HOW TO PROCEED): (1) binding-rule additions over the baseline UD, (2) LLM-adjudicated UD-corrections to `v0-cache/` as silver-tier substrate, (3) `overrides.json` v2-spray for judgment-residuals.
- **"Mostly correct" TEMPERED (2026-05-28 yardstick measurement).** Stan hand-segmented 33 stratified
  verses (gold = `readers-bofm/private/substrate/emode-substrate/bofm-atu-gold-yardstick.json`, the
  reusable in-register ATU regression test). Deployed v2 vs his gold on that HARD slice: **F1 ≈ 0.67**
  (agree 30 / over-split 17 / over-merge 13) — real divergence BOTH directions, genre-split (over-split
  in sermon/Isaiah, over-merge in doctrinal/narrative). So: mostly-correct on SIMPLE verses, genuine
  both-direction defects on COMPLEX ones. Root cause = weak Stanza-EModE parse (mis-segments
  coordination → over-merge; over-segments frames → over-split); binding rules propagate it. His gold
  for the 17 divergent verses + 5 audited interjection-detaches deployed 2026-05-28.
- **Do NOT reopen *the parser-training route*** without genuinely new *real gold* (a real in-register treebank) — NOT another letters-trained bootstrap, NOT a bigger encoder over the same supervision. *(This is about training/fine-tuning a parser. LLM post-editing of baseline Stanza to `v0-cache/` is a distinct mechanism — lever 2 in HOW TO PROCEED.)*
- The gate did its job: it prevented shipping a v0.2 that would have been *worse* than v0.1.

## BANKED real-gold — do NOT re-prove

- **Hebrew / BHSA** — gold TF (live, Tanakh).
- **GNT / Macula + CenterBLC-N1904** — gold TF acquired (`readers-gnt/private/substrate/N1904`).
- **Vulgate-NT / UD_Latin-PROIEL → TF v0.1** — built, validated, pushed (`readers-vulgate/data/tf/0.1`).

## PARKED — do NOT start without real gold or a new reason

LXX clause-syntax TF, Vulgate-OT, the cross-corpus convergence query. **They inherit the exact
bootstrap that just failed** (no gold treebank → manufacture via parser → register gap). Do not
repeat the failed experiment on another corpus. Gate for opening ANY new corpus front: *is there
real gold?* If no → it stays parked.

## SETTLED tactical calls — stop raising these as open questions

- **SUD is a derived view of UD, not a fork.** One parser on UD; convert to SUD as a view if ever
  needed. No decision required.
- **Each project's data lives in its own repo's `private/substrate/`.** Done; don't re-ask placement.
- **Genre is NEVER an ATU criterion — only the bidirectional test.** No "prophetic oracle"-type holds,
  ever. (A genre label is not a reason to withhold or apply a break.)
- **Private method canon is untracked from the public remotes** (bofm/gnt). Still in git *history*;
  scrub history only if pre-publication cleanliness matters — otherwise leave it.

## HOW TO PROCEED (standing)

- **BoFM forward = three-lever framework over baseline Stanza** (none is the closed parser-training route):
  1. **Binding-rule additions** in `5-machinery/scripts/bofm_generate.py` — `§2.2`-style rules that consume UD features (e.g. parallel-subordinator-stack rule shipped 2026-06-01 `9101ea9`). Substrate-first permanent fix for the *reader*; each rule subsumes a class of override workarounds. **Highest leverage when a class has a clean structural signature — try this first.**
  2. **LLM-adjudicated UD-corrections to `v0-cache/`** — Sonnet propose edit-groups (HEAD/DEPREL/lemma) → ≥2 Opus audits (over-edit + downstream-effect lenses) → `validate.py` gate → commit. Target the anomaly classes from `audit_stanza_parses.py` (PTA / PDS / LDA / BDD). **Silver-tier semi-automatic treebank substrate; primary value is TF-query consistency, reader payoff incidental once §2.2-style rules carry the structural classes.** Do NOT conflate with the closed parser-training route — this edits an existing baseline, doesn't train a new parser.
  3. **`overrides.json` v2-spray** (`_overrides()` + `data/text-files/v2-adjudicated/overrides.json`) — for judgment-residuals neither rule nor UD-correction reaches (interjections, complement-vs-quote). Token-exact, parity-safe, conservative + adversarial-audited, quality-meter gated. **Use when both upstream levers leave the case unresolved.**
  
  Take what each lever reaches; accept the mechanical ceiling on what none does.
- **Maintain the real-gold TFs.** Do not open a new corpus front without clearing the keystone logic
  first (real gold? if no → parked).
- The doctrine canon stays at `~/repos/atu-method/3-implementation/substrate.md`; this file is the *decision*
  layer that complements it. Linked: [[project_bofm_discourse_voice_deploy]],
  [[project_bofm_substrate_quality]], [[feedback_no_fly_swatting]].
