---
name: feedback-verify-deploy-state-never-assert
description: "Never assert deployment/architecture state from docs, memory, or an agent's claim — verify against git log of the live dir + atu-method/docs/05-status/deployment-status.md"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/0ed788a7a37f17b9@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

**Never state what is deployed/live, or a corpus's architecture, from a per-repo `CLAUDE.md`/README, a memory, or an agent's relayed claim.** Those drift stale. **Ground truth = (1) `atu-method/docs/05-status/deployment-status.md` (the single source of truth), and (2) the `git log` of the live corpus directory** (`git log -- <live-path>`). Verify BEFORE asserting.

**Why:** 2026-05-26 I asserted "BoFM v2 is hand-edited/sacred, not method output" — patently false (the pure-method edition replaced the hand-edits 2026-05-22, commit `1a980bf`; bomreader serves `bofm_generate.py` output). Then got Tanakh wrong too. It was the THIRD recurrence of the **hand-edit-as-oracle reflex** ([[feedback_hand_edit_is_a_datapoint]]) — Stan had caught it twice on 2026-05-22. Root cause: stale repo docs + post-compaction memory loss + echoing an agent that read the same stale doc. The incomplete cascade (I fixed the canon but not the orientation docs) is what left the stale line that misled me.

**The facts (as of 2026-05-26):** all three readers run **mechanical-first (v1.5 stage) LIVE**; hand-edits superseded, NOT a deploy oracle. The **source text** is sacred (words/forms/punct/refs never modified); the **ATU segmentation** is regenerable method output. Pipeline: v0 → v1 → **v1.5 (live)** → v2 (optional LLM, none run) → v3 (editorial). **No v4** (retired). Live dirs: Tanakh `v2/heb`, GNT `v1.5/grk`, BoFM `v2` — all the v1.5 stage despite the drifted names.

**How to apply:** (1) the **trigger** — the moment I'm about to treat hand-edited content as the protected/live/sacred layer, STOP and verify deploy-state. (2) Read `deployment-status.md` / `git log -- <live-path>` before any claim about what's deployed. (3) When codifying a fact, **cascade COMPLETELY** — sweep every doc stating the contradicted old fact (canon AND orientation docs AND memory index), not just the canon. (4) Deploy bar = "new AND superior by the method's own bidirectional-test yardstick," never "as good as the hand-edits."
