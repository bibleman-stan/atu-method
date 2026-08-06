---
name: ship-independent-not-coupled
description: "ship each repo's change the moment it's gated; don't couple independent readers into one atomic push, and parallelize independent tracks"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`9d9683ed-2bb3-499d-8eb7-715c2bd3a063/308db35beb646c18@v2`); state as of 2026-05-29 (snapshot mtime); possibly stale — re-verify before relying.

Ship independent work AS EACH PIECE IS READY, and run independent tracks IN PARALLEL — don't hold a gated, done reader waiting for a sibling, and don't gate/build/adjudicate one repo at a time when they're independent.

**Why:** twice in one session (2026-05-29) Stan pushed back on over-serialization — "if vulgate and bofm are good to go, why aren't they updating/shipping out? there's no reason all three have to be done before you do pushes" and "why can't you do these in parallel … parallel not sequential unless there's a good reason." I had (a) bundled Vulgate + BoFM + GNT into one "atomic push" and (b) gated/built the readers sequentially.

**How to apply:** the **cross-repo push atomicity** rule in `~/.claude/CLAUDE.md` applies ONLY to a *shared-canon cascade* — an `atu-method` methodology change that must land together with the corpus rebuild that renders it (don't leave canon ahead of rendering). It does NOT apply to independent reader corpora: bomreader.com / gnt-reader.com / vulgate-reader.com / tanakh-reader.com are separate sites in separate repos with no cross-dependency, so each ships the instant its own change is regenerated + gated. Likewise, gate/build/adjudicate independent tracks via parallel agents (one per repo/lens), not one after another. Ties to [[feedback_parallel_default]] and [[feedback_no_fly_swatting]] (cascade autonomously).
