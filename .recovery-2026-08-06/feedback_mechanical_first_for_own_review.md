---
name: feedback-mechanical-first-for-own-review
description: "Mechanical-first governs Claude's OWN adjudication, not just pipeline output — query the richest available treebank (Macula: that-VP/sub-CL, role, frame, referent, person) BEFORE hand-reasoning an ATU/linguistic call"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/5966dfcd5265e9a6@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

The **mechanical-first pipeline philosophy applies to Claude's own review/adjudication process, not only to the rendered output.** Before hand-reasoning a per-instance ATU or Greek-grammar decision, ask FIRST: "what does the richest treebank I already have tag mechanically?" — and look it up — rather than reading the Greek by intuition.

Stan: "i greatly fear you have been doing some of your reviews in slow and inefficient ways instead of fast and mechanical ones because you forgot you even had this stuff." This was *also* the real answer to his earlier "why is the gnt going so slowly" — not API flakiness, but the wrong method.

**The triggering failure (2026-05-26):** spent a long stretch hand-classifying 41 GNT ὅτι verses by eye, building lemma lists (`_QUOTE_INTRO`/`_CITATION_GOV`/`_DECLAR_GOV`), agonizing over "Janus" verbs (ὀμνύω causal-vs-complement), constructing morphological deixis proxies, then concluding the complement-vs-causal-vs-recitative distinction was "structurally impossible at the mechanical layer, defer to v2." **All of it is tagged mechanically in Macula Greek**, which Stan had already provided: `rule="that-VP"` (complement → bind-eligible) vs `rule="sub-CL"` (causal/subordinate → stand), clause-level `role` (`o`/`adv`), semantic `frame` (PropBank A0/A1), participant `referent`/`subjref`, and word `person`. A treebank lookup answers in seconds what hand-adjudication did slowly and less reliably.

**Why it happened:** defaulted to intuition-based Greek reasoning instead of querying provided data; forgot which datasets were on disk and what they encode. Same root as [[feedback_verify_deploy_state_never_assert]] — asserting a limit ("can't see it") without checking the resources already in hand.

**How to apply:**
1. **Inventory data sources at task start.** For GNT work the engine currently sources the *thin* `sblgnt-lowfat`; the *rich* Macula Greek lowfat (`readers-gnt/research/macula-greek/SBLGNT/lowfat/`, helper scripts `macula_clauses.py`/`macula_predication.py`/`macula_valency.py`/`macula_wordgroups.py`) carries clause role/rule/frame/referent. Lexham Discourse GNT (LDGNT) lives at `Dropbox/03-Biblical_Studies/Greek/discourse/Lexham-Discourse-GNT`. See [[reference_corpus_pipeline_map]] / the resource catalog.
2. **For any per-instance ATU judgment at scale, source the discriminating feature from the treebank, not hand-reading.** Build the rule on the tagged feature; validate mechanically against the case set (seconds), don't eyeball each verse.
3. **Never conclude "mechanically impossible / structurally can't see it" without first checking every provided dataset.** "Defer to v2" is only honest after the richest treebank has been queried and genuinely lacks the feature.

Ties to [[feedback_parallel_default]] and [[feedback_verify_deploy_state_never_assert]] (verify before asserting) and the mechanical-first canon in `~/.claude/CLAUDE.md`.
