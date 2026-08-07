---
name: feedback-check-prior-corpora
description: "Before treating a new-corpus problem as novel, ask \"have we already solved this in Tanakh / another built corpus?\" — prior solutions transfer"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`ca81ff61-4510-437d-8f8c-a539e0a05296/3055339bcda4ec23@v3`); state as of 2026-05-22 (snapshot mtime); possibly stale — re-verify before relying.

Before treating a problem in a new corpus (GNT, LXX, Vulgate, BoM) as novel, ASK: **"have we already come across this in tanakh-reader (or another built corpus)?"** Tanakh is the most-built corpus; many problems — verbless/nominal clauses, treebank→v0 token reconciliation, clause-atom derivation, binding-rule design, the bidirectional test, validator-gate integrity — are ALREADY SOLVED there. Default to replicating the proven solution, not re-deriving from scratch.

**Why:** Stan's program thesis (his words, 2026-05-20) is that *ATUs reveal common cross-linguistic patterns because that is how thought and language work* — so building multiple corpora should EMPIRICALLY DEMONSTRATE the convergence, and each proven solution makes the next reader (LXX, Vulgate, rebuilt BoM) faster. But across compactions Claude loses "we already solved this" and silently re-invents, wasting effort AND missing the convergence that is itself the evidence. The Greek binding rules turned out to mirror Hebrew B1–B14 (Greek ὅτι-complement ↔ B11 ki-complement; recitative-ὅτι = B11's speech-verb inverse; restrictive ὅς-relative ↔ B3 restrictive ʾăšer; interjected vocative ↔ B1) — Claude initially mis-framed these as fuzzy "editorial residual" until Stan pointed back at the Hebrew catalog.

**How to apply:** When a new-corpus problem appears, before designing fresh — (1) name the Tanakh/Hebrew analog explicitly; (2) port the proven mechanism (e.g. PROIEL→v0 alignment ↔ `run_full_tanakh.py` `_align_words_to_v0`; verbless anchor ↔ BHSA `NmCl` handling); (3) **still run the bidirectional test on the ported rule** so the convergence is earned independent evidence, not a circular assumption (see [[feedback-derive-then-observe-convergence]] caution). Consult `~/repos/atu-method/1-method/binding-rules-hebrew.md` first. Related: [[feedback_compaction_resume_protocol]], [[feedback_do_it_once]].

## The wheel is round — do a RETROSPECTIVE at the start of each new corpus (Stan, 2026-05-22)

"Our method works, but you have to follow it." Before LXX/Vulgate (and any new corpus), **run a retrospective: "how did I handle this on Tanakh / GNT / BoFM, and what did SUCCESS look like?"** — then replicate the winning SEQUENCE, not just spot-solutions. Be *aware of what success looked like*, proactively, not only when stuck.

**The proven wheel (Tanakh → GNT → BoFM, mechanical-first):**
0. **v0** = source versification / display text.
1. **v1** = treebank/UD clause-atoms (BHSA · sblgnt-lowfat · own stanza UD-parse, CACHED). Clause-atoms keyed off clause-head deprels; **surface-order emit** so rendered text == source word order.
2. **v2** = the language's binding-rule catalog (Hebrew B1–B14 · Greek R-cat · BoFM R1–R29) applied via clause-head selection + post-passes. Catalogs mirror across languages (convergence — earn it).
3. **MEASURE by canon-conformance** (`run_all` validators), **NOT** by matching hand-edits.
4. **TIGHTEN the deterministic (Category-A) rules to ~85–90%** by running the validated appliers (build appliers for gaps). The MECHANICAL layer does the bulk; proven live this session: BoFM 1648→1061 violations from 7 appliers, no rebuild.
5. **v3 (LLM adjudication) / v4 (editorial)** polish ONLY the residual Category-B judgment (synonymy, discourse), **bounded to the flagged classes**.

**The failure mode Stan witnessed this session (= NOT following the method):**
- **Treated hand-edits as gold** despite a twice-given warning — they are criteria-drifted, NOT canonical. Yardstick = canon-conformance, never hand-edit granularity ratios.
- **Freehand v3 overshoots** (over-merged Enos 130→96 past the target). Bind only the flagged residual classes; don't merge by feel.
- **Prematurely deferred mechanizable Category-A rules** (M4, AICTP, R29-inf) to "v3→v4 tail" — deterministic rules belong in the MECHANICAL layer; don't push automatable work onto judgment stages.
