---
name: project-corpus-v1-substitutes
description: "For BoFM/LXX/Vulgate (no ready treebank), we'll build our own v1 clause-atom source — now feasible having seen how BHSA and PROIEL feed v1"
metadata: 
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`ca81ff61-4510-437d-8f8c-a539e0a05296/8e8476387697b293@v6`); state as of 2026-05-21 (snapshot mtime); possibly stale — re-verify before relying.

To extend the mechanical-first ATU pipeline to corpora that **lack a ready treebank** — Book of Mormon (English), LXX (Greek), Vulgate (Latin) — we will almost certainly have to **create our own substitute for the v1 clause-atom source** that BHSA (Tanakh) and PROIEL (GNT) provide. Stan's insight (2026-05-20): now that we've seen how both work, we should be able to build such substitutes.

**Why this is now tractable** — the pilot taught us exactly what v1 must deliver and the two shapes it can take:
- **BHSA model** — clause-atoms come *pre-packaged* in reading order with type labels; v1 is free (just read them).
- **PROIEL model** — a dependency tree (head-id + rich morphology: case, mood, role, relative-pronoun flag); clause-atoms are *derived* by segmenting the surface-sorted token stream by nearest predication head. One extra assembly step, but the dependency arrows + morphology are richer.

So a v1 substitute for a treebank-less corpus needs to emit, per clause-atom: surface text in reading order, a predication head (verb/mood or verbless-pred), the introducing particle, and enough morphology (case, role, relative/subjunction flags) for the v1.5 binding rules. A dependency parse (even an automatic one, hand-corrected) over the corpus text would suffice; BoFM English could use an English dependency parser, Vulgate has Latin treebanks (PROIEL itself includes Latin), LXX could reuse Greek tooling.

## BoFM — ACTIVE (2026-05-21), and the cleanest instance of the method

Direction locked with Stan:
- **Retire `v1-skousen-breaks`** — borrowed Skousen textual decisions, never our method. Not relevant going forward.
- **`v0` = the LDS-scriptures versification** of the Book of Mormon text (standard chapters/verses) — the display text and anchor.
- **Build our OWN UD parse + Text-Fabric as `v1`** — generate it, refine it, treat it as the clause-atom substrate. ATU = the node-layer over it.
- **Then `v2` = binding rules** (English catalog, re-derived per the convergence thesis), → final at v2 (mechanical), same depth as Tanakh/GNT.

Two ways BoFM differs from the ancient-language readers, both advantages:
1. **We can GENERATE the treebank, not hunt for one.** English UD parsing is mature off-the-shelf (Stanza/spaCy/UDPipe) — unlike Hebrew/Greek where hand-built treebanks (BHSA/lowfat) were required. So "create our UD" is realistic: parse v0 → dependency clause structure → Text-Fabric node/feature graph.
2. **No reconciler, by construction.** We parse the DISPLAY text (v0) itself, so UD tokens map 1:1 to display words (same clean property that let GNT drop the reconciler; lowfat = display text). Tanakh's reconciler debt never arises.

**The one real wrinkle: 1829 Early-Modern English** (KJV-flavored — *thee/thou*, *-eth*, wall-to-wall *"and it came to pass"* parataxis, long Isaiah quotations). Modern UD models parse most of it but throw archaic-form noise → that's the "**refine**" step: machine UD parse → clean up the EME systematics → text-fabric → binding rules. No foreign-language/interlinear layer and no eng-kjv translation layer (it's already English; KJV-parallel passages are cross-reference, not translation).

**`v2-mine` is a REFERENCE, not gold (Stan, 2026-05-21).** The hand-edits are *more comprehensive* than Tanakh/GNT got, BUT (a) they only run through **early/mid Alma** — books past that have little/no hand-editing, so the mechanical pipeline is the PRIMARY path there; and (b) **criteria have drifted** since Stan started — early books (1 Nephi, 2 Nephi) reflect OLDER criteria. So do NOT validate-to-parity against v2-mine the way GNT validated against its cold-eye. Divergence from v2-mine is a QUESTION, not an error: it may be current criteria correctly applied (pipeline right, v2-mine stale) or a pipeline bug. Anchor the English binding rules on CURRENT criteria (BoFM `private/01-method/colometry-canon.md` + a fresh current-criteria cold-eye), not on retrofitting old v2-mine. Value proposition: a consistent UD-driven pipeline can bring the early (old-criteria) books UP to standard AND extend past mid-Alma where hand-editing stopped.

**BUILD PROGRESS (2026-05-21).** The crux discovery: BoFM already has the full UD method (canon R1–R29 + `validators/apply_rule_*` appliers + `validate_rule_*` detectors + `run_all.py`), BUT the appliers read `v2_path` — they REFINE Stan's hand breaks, so every rendering inherited human inconsistency. **The missing piece was a from-scratch pure-method segmenter** — now built: `5-machinery/scripts/bofm_v1_fabric.py` (UD clause-atoms by clause-head deprel: root/advcl/acl/ccomp/csubj/parataxis/verb-conj + surface-order emit, ported from the GNT engine) and `5-machinery/scripts/bofm_generate.py` (v0-anchored: stanza parses each verse of `v0-bofm-original`, fabric segments, lines render in surface order sliced verbatim from verse text for exact punctuation; punctuation attaches backward). Stanza model is available in the repo `.venv`; run with `PYTHONPATH=../atu-method .venv/Scripts/python.exe`. **Validated on 1 Nephi: pure-method breaks (ZERO v2-mine input) recover Stan's units, and every divergence maps 1:1 to an existing canon applier** (bare `and`→R9; `know that…which…`→R17+R19). **CHOSEN PATH (Stan, "do it"): (A) reuse the existing canon appliers on the pure-method segmentation for a usable artifact now, PLUS extract the shared foundation (UD→clause-atoms→surface-order emit→gate harness) into `atu_method` so both GNT+BoFM ride one backbone; rule catalogs stay per-corpus.** NEXT: write pure-method segmentation as a v-file → run canon appliers (R9/R17/R19/R21/R27/R28/R29…) on it → `run_all.py` validates → divergence study vs v2-mine (method is arbiter, NOT parity target — Stan: hand-edits partial-through-mid-Alma + criteria-drifted).

**LXX / Vulgate resource map (verified 2026-05-21).** The "build UD → derive clause-atoms" model ports to both (UD is cross-linguistic by design; clause-atom logic is the same code). Swap per-language: parser model + binding catalog.
- **Vulgate — strongest start.** PROIEL Latin treebank *contains most of the Vulgate NT* hand-annotated (Gospels, Acts, Romans, Revelation; 112,454 Vulgate tokens) — open as `UD_Latin-PROIEL` + github.com/proiel/proiel-treebank. A partial GOLD treebank (Latin echo of the GNT pilot); parse OT-Vulgate with stanza `la`. Catalog grammar: **Plater & White, *A Grammar of the Vulgate*** (1926, PUBLIC DOMAIN — archive.org/details/AGrammarOfTheVulgateByPlaterAndWhite), Vulgate-specific clausal Latinity; + Allen & Greenough.
- **LXX — paywalled on syntax, open on morphology.** Cascadia Syntax Graphs of the Septuagint = COMMERCIAL (Logos only). MACULA does NOT cover LXX (GNT + Hebrew only). So free path = open Rahlfs morphology (github.com/eliranwong/LXX-Rahlfs-1935, openscriptures) → parse with stanza `grc` → **reuse the GNT Greek R-catalog (same language)**. Catalog grammar: **Conybeare & Stock, *Grammar of Septuagint Greek*** (1905, PUBLIC DOMAIN — archive.org/details/grammarofseptuag0000cony, CCEL). LXX is the case where ensemble+Claude parse-adjudication earns its keep (no gold parse).
- **Framing:** treebank/parser → the parse (v1); public-domain clausal grammar → the binding catalog (v2, the Wallace-analog). The grammarians pre-encoded the clausal distinctions we mechanize.

**Status: ACTIVE for BoFM.** LXX (Greek) / Vulgate (Latin) remain deferred (LXX can reuse Greek tooling; Vulgate has Latin treebanks incl. PROIEL's Latin). Related: [[feedback_check_prior_corpora]], [[corpus-pipeline-layer-map]], and the convergence thesis in atu-method `feedback_cross_corpus_convergence`.
