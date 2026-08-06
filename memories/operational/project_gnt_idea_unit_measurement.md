---
name: gnt-idea-unit-bar-measurement-2026-05-24
description: "Genre-spread measurement of GNT v1.5 against the idea-unit bar — ~49%, over-split is 90-95% of all failures; diagnosis = no binding layer in the fabric"
metadata: 
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/2f624aa86277b8a5@v4`); state as of 2026-06-06 (snapshot mtime); possibly stale — re-verify before relying.

Genre-spread measurement of the deployed GNT edition (`readers-gnt`, `data/text-files/v1.5/grk/`) against the **idea-unit bar** (framework §1.1 bidirectional test), done 2026-05-24 as Part 2 of the GNT convergence play. 6 parallel Sonnet agents, one per genre cluster, judged every content line pass/fail and classified failures.

## Result — the bar is FAR lower than the prior 6-chapter ~72% estimate

| Cluster (chapters) | Lines | Pass rate |
|---|---|---|
| Synoptic narrative (Mark 4–5) | 259 | **64.5%** |
| Lukan narrative (Acts 2, 9) | 231 | **51.9%** |
| Pauline argument (Rom 8, Eph 1, Phil 2) | 186 | **21.0%** ← worst |
| Heb 1 / Jas 1 / Rev 1 | 169 | 50.3% (Heb 64 / Jas 50 / Rev 41) |
| **4-cluster total** | **845** | **~48.6%** |

(Matt 5/13 + John 1/6 also measured — agent outputs persisted oversized; tallies not extracted, but same over-split pattern reported. The 4-cluster ~49% is robust on 845 lines.)

**Gradient = subordination/periodic density.** Plain narrative (Mark) and elevated-but-clausal epistle (Heb) score best (~64%); dense Pauline periods (stacked ἵνα/ὅτι/relative chains + οὐ…ἀλλά antitheses) collapse to 21%; apocalyptic vision-description (Rev, participle/simile chains) 41%.

## The diagnosis (decisive and uniform)

**Over-split is 90–95% of ALL failures in every cluster.** Over-merge and anaphoric failures are negligible (a handful each; the few over-merges are amen+next-sentence run-ons in Rev). So GNT's problem is almost purely over-splitting — the opposite of BoFM's over-merge, exactly as the convergence diagnosis predicted.

The mechanism: the v1.5 fabric (`scripts/sblgnt_v1_fabric.py`) ported the **split/legality** rules (R3/R4/R7/R8/R9/R10 per the README) but **essentially no MERGE/binding layer**. So it emits raw parse-derived clause-atoms — every subordinate clause (ὅτε/ὅταν/ὅπου/ἵνα/εἰ), every ὅτι-complement, every participial phrase, every restrictive relative (ὅς/ὅστις), every bare prepositional/simile phrase, every vocative, and content-less speech verbs each get their own line, stranded from the head they belong to. Cascades of 3–6 consecutive forward-open fragments from one syntactic unit are common (e.g. Mark 4:12 six-line ἵνα chain; Phil 2:12 six-line fracture of one imperative; Heb 1:8 four-line shattering of the throne-saying; the Rev 1 Christophany).

This is precisely what Hebrew B1–B14 and the BoFM binding rules were built to prevent — unaddressed in Greek at v1.5.

## Implication for Part 3 (the port)

The fix is NOT a few targeted rules (GNT canon §3.7 antithesis / §8 prep-catenae / GNT canon §3.13 escalation were the pre-measurement guesses) — it's that **the whole binding layer must be implemented in the fabric**: bind subordinate clause→its head/apodosis, ὅτι/ἵνα-complement→governing verb, circumstantial participle→main verb (R20), restrictive relative→head noun, bare PP→its host clause, gen-abs→governing matrix (R19, already landed as spec 754609ee), vocative→its clause, speech-verb→retains content per R11. Then regenerate v1.5 + redeploy. This re-renders the live site (gnt-reader.com) → requires Stan's go-ahead before regen+push. See [[corpus-pipeline-layer-map]] (convergence decision) and the R19 canon revision as the template instance.

## RESOLVED + DEPLOYED 2026-05-24 (R9 binding)

Part 3 done. The binding layer is in `scripts/sblgnt_generate.py::merge_subordinate_clauses` (backward/forward/comparative passes, each gated by `_bind_ok` = within-verse + ≤2 finite verbs + content cap; coordinate-relative guard in `_rel_is_correlative`; quote protection via speech-frame `qflag`). Canon **GNT canon §3.4/R9 reversed** from split-default → bind (R22 subsumed), ~17-site cascade, canon **v3.3**. Engine+canon committed `b01231a9`; **full-corpus deploy (260 ch grk + eng-kjv + 27 HTML) committed `4497ee77` and pushed** → gnt-reader.com re-rendered. Net ~−4,500 lines.

**Measured outcome: uniform +~6pp across all 6 genre clusters** (post-fix re-measure). KEY HONEST CAVEAT: **absolute pass-rates are judge-noisy** (same deployed file scored 21.9% vs 49.5% by two different Sonnet judges on Matt) — only the **within-run before→after Δ is reliable**, and it was uniformly +5 to +8pp. Do NOT quote an absolute "% on the bar" as if precise.

**PARSE-DRIVEN BINDING FALSIFIED (don't re-attempt on lowfat).** Investigated binding off the SBLGNT-lowfat parse structure instead of subordinator lemma lists. The lowfat trees carry **phrase-level** roles (s/o/adv/io on np/pp/adjp) but **NO clause-level subordinate/coordinate role**; finite adverbial subordinate clauses are bare sibling `<wg class="cl">`s under a common parent, structurally indistinguishable from coordinate clauses **except by the introductory subordinator lemma**. So the lemma-keyed engine is the *correct* signal for this treebank, not a stopgap. (`is_root()` already uses the parse nesting where lowfat DOES encode dependency: participles, infinitives, relatives.) A genuine parse-driven rewrite would need a role-labeled clause dependency — not available here.

**Deferred to v2 (LLM adjudication):** intra-quote subordinate binds (quote-protection blocks them — Heb 1:13, Matt 5:26 OT quotes stay split); polysemous **ὡς** (not bound — comparative/temporal/causal); the long-period over-split tail. See [[corpus-pipeline-layer-map]].
