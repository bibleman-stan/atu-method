---
name: project-bofm-bidirectional-rebuild
description: "BoFM pure-method edition rebuilt against the bidirectional test (2026-05-22): ~51%->~20% line failure, validated by human-judgment agents; what changed and what residuals remain"
metadata:
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/66b717437d73b01c@v5`); state as of 2026-06-06 (snapshot mtime); possibly stale — re-verify before relying.

**2026-05-22 — the BoFM pure-method edition was rebuilt against the bidirectional ATU test** (after the "98% conformant" claim was found to be canon-conformance, not correctness — see [[feedback-conformance-is-not-correctness]]). Repo `~/repos/readers-bofm`, draft at `data/text-files/v2-puremethod-draft/`, measured by `5-machinery/scripts/bofm_bidir_gate.py` (structural proxy) + periodic genre-spread agent samples (ground truth).

**Validated result (idea-unit bar, 5-genre human-judgment agents):** weighted line-failure ~51% → **~20% (≈80% pass)**. Per chapter: 1Ne1 47→15.6, Enos1 37→19.5, 2Ne8 44→21.6, Alma5 55→14.4, Moroni7 61→31.7.

**DEPLOYED LIVE 2026-05-22 (commit 1a980bf, bomreader.com).** The method edition REPLACED the hand-edited v2-mine as the source of truth: overwrote `data/text-files/v2-mine/*.txt` with the method draft (old content recoverable via git), rebuilt all 15 `books/*.html` (6604 verses, 0 nested errors), bumped sw.js cache, reset validators/.baseline.json to the method corpus, committed through the pre-commit hook (NO --no-verify), pushed. Same process Tanakh + GNT shipped on.

**The deployment decision turned on a head-to-head that I almost botched the SAME WAY again.** Stan asked "can the method edition replace the live one"; I said "no — it'd be replacing a hand-edited edition with an 80%-mechanical one" — i.e. I treated v2-mine as the gold standard to protect, the EXACT hand-edit-as-oracle reflex this session was about (see [[feedback-hand-edit-is-a-datapoint]]). Stan caught it ("why am I laughing but angry"). I had NEVER measured v2-mine on the bidirectional test. When I did (current-vs-current agent idea-unit, same 5 chapters): **method 17.2% avg line-fail vs hand-edited v2-mine 23.6%** — the LIVE edition was the inferior one; keeping it was the regression. Method wins/ties 4 of 5 (Enos 9.3 vs 28.7, 1Ne1 11.6 vs 25.3, Moroni7 25.7 vs 26.6, 2Ne8 ~tie); hand-edited wins ONLY Alma5 (carefully hand-edited sermon) narrowly (7.0 vs 9.8). NOTE: the structural-detector head-to-head (2.1% vs 28.7%) OVERSTATED the gap ~14x — it penalizes v2-mine's finer splitting; the agent idea-unit gap is the honest ~6 points.

**Lesson reinforced (twice in one session):** never answer a "is X good enough vs the hand-edited edition" question by assuming the hand-edits win — MEASURE both on the same yardstick. The proven Tanakh/GNT deploy bar is "new AND superior by the method's own yardstick," never "as good as the hand-edits."

**What changed (all committed, main):**
1. Five binding rules re-derived on the unifying principle *bind anything that can't stand alone, split only independent predications*: coordinate-verb on the **own-subject floor** (retired the BoFM canon §3.5.2 N≥3 count cliff + own_args gate — 2-lens audit confirmed Hebrew B7 binds on bareness not count); **R19 cataphoric retired** (relatives always bind); **R6/R7 break retired** (marked subordinate clauses bind, incl. advmod-tagged when/after); verbless-fragment detector precision.
2. **Archaic-morphology parse normalization** (`5-machinery/scripts/archaic_normalize.py`): stanza mis-tagged 51% of EME -eth/-est verbs as NOUN, cascading into fractures + wrong heads. Normalize archaic->modern FOR PARSING ONLY (1:1 token map, render original surface). **Sources its map from `build_book.py`'s swap lexicon** (SIMPLE_SWAPS + KNOWN_ETH — the modern-mode toggle's single source of truth) so parse-layer and display-layer can't drift.
3. **Batched parser** (tokenize per-verse for offsets, ONE pretokenized parse per book) — ~6x faster (Alma 7.5min not 46min). Parse cache committed.

**The METHODOLOGY DECISIONS that govern (Stan):**
- **Bar = idea-unit**: a line is valid if it's ONE complete idea even if grammatically dependent. Speech/discourse frames ("the Lord said unto me:", "I say unto you,") and dependent thought-units (purpose/relative/subordinate clauses) PASS. (NOT the independent-clause bar — that wrongly fails frames and inflated an earlier agent run to 27-67%.)
- **Punctuation has ZERO force** in ATU decisions (editorial overlay; same as te'amim/versification). Code decides on syntax only; punctuation is cosmetic glyph placement. Never adjudicate on commas/colons.

**Residual ~20%, named + rule-addressable (priority order):** (1) subject-clause/coordinate-arm splits (csubj/free-relative `whoso` split from predicate); (2) bare `--` em-dash artifact lines (trivial drop/merge); (3) appositive splits; (4) bare infinitive phrases (`yea, to preach`); (5) **poetry parallel cola over-merge** (2Ne8 — the one class needing MORE splits: NOUN-conj parallel-member split, port Tanakh); (6) multi-proposition over-merge (speech-content / wherefore-chains packing independents); (7) periodic-sentence participial preambles, for-coordinating, ~10 mid-phrase fractures.

**Lexicon gap to feed back to modern-mode**: ~7 EME thou-verbs absent from build_book's swap lexicon (mayest/mightest/beholdest/beheldest/knewest/deniest/commandest) — `archaic_normalize.gaps()` reports them; Stan's call whether to add (display change + HTML rebuild).

---

## 2026-05-22/23 refinement + adjudication session (extensive, ALL SHIPPED to bomreader.com)

Long verse-by-verse refinement pass driven by Stan. Rules added to `5-machinery/scripts/bofm_v1_fabric.py` (each diagnosed→sized→audited→measured→shipped):
- **Class A**: coordinator-led participial ground (having/being + leading and/yea/nevertheless) opens its own ATU; exclusions adnominal / marked-subordinate / coordinate-of-gerund. Cured 1Ne1:1.
- **M1**: EME causal **for** + own subject splits as a complete causal ATU.
- **M2**: direct-speech **ccomp under verbum dicendi RELEASES** (quote gets own line); indirect "say THAT X" binds (R17). Dropped the inverted-guard that blocked VOCATIVE speech (enos 1:5/1:7/1:10).
- **R-INV** (`5-machinery/scripts/parse_repair.py`, NEW load-time parse-repair layer): re-attaches postposed subject of inverted "thus saith the Lord" (PROPN-only).
- **AICTP "and"-form**: empty "(it) came to pass" frame binds its DISPLACED MAIN clause (first finite parataxis/conj child), not subsequent coordinates (1Ne1:6) or participial parentheticals (1Ne1:4). 533 and / 367 that — split is a KJV translation artifact (banked: vault z/data zettel + `project_fef_aictp_paper`).
- **yea-B**: a "yea"-led segment with no independent predication merges back; clause-leading "yea" stays its own ATU.

**MORPHOLOGY-FOUNDATION FIX (key lesson).** Stan caught that the binding rules ride on `archaic_normalize`, which was ASSUMED complete but wasn't: "art" (thou ART) mis-tagged NOUN ×27 broke clauses, and `gaps()` was suffix-blind (only -eth/-est). Added irregular EME map (art→are, beholdest, mightest, modal family), **re-parsed all 15 books**, built `audit_morphology.py` (finds active mis-tags, not suffix-guesses). 1Ne2:19 fixed. → Audit the parse substrate, don't assume it; detectors must catch non-suffix forms.

**v1-ensemble PARSE-ADJUDICATION arc (built this session).** `data/text-files/v2-adjudicated/overrides.json` ('book c:v'→[lines]), consulted by `generate()` with a **token-exact guard** (override re-segments only, NEVER changes a word). `detect_residuals.py` flags genuine-fragment verses; `deployed_atu_lines()` makes gate+detector **override-aware**. Scaled via 5 parallel Sonnet adjudicators using ANCHOR output (verbatim break-points → token-exact by construction). **Clear-garble class CLOSED: 91 flagged → 88 adjudicated + ether 5:4; deployed gate 422→363 fail (97.7% pass).**

**Subject-fracture class (enos 1:3/1:23 type) is NOT cleanly auto-detectable** — the severance signal is dominated by legitimate vocative-address + participial-ground structures (6 sampled = all false positives). READ-AND-FIX tail via individual overrides, never a batch sweep (would corrupt correct ATUs). Likewise the detector's remaining flags (Class-A participial beats, verbless exclamations) and the 145 stranded-subordinate (legit causal-for) must NOT be "fixed". Mechanical rules own ~97.7%; adjudication overrides the rest; both layers measured honestly.
