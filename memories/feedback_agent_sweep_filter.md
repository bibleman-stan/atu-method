---
name: Agents drift toward uncritical codification of their own findings
description: When dispatching parallel sweep agents (handoffs audit, git-log audit, v1-canon audit), they surface detritus alongside signal. Filter each finding against (a) is this editorial-level methodology or tool-level convention? (b) was this deliberately dropped or accidentally? (c) is this duplicative with existing canon content? Only items passing all three become canon.
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
**Rule.** Parallel agent sweeps over historical artifacts (handoffs, retired v1 canon, git log, session folders) return items mixed between signal and noise. Do not mechanically codify agent-surfaced items. Filter each through three checks before codifying:

1. **Level check:** is this editorial methodology (colometry canon territory) or tool-level convention (reformatter, pipeline, validator)? Reformatter rules do NOT belong in editorial canon.
2. **Provenance check:** was this deliberately dropped during a canon refactor (v1→v2), or was it accidentally lost? Deliberate drops stay dropped unless new evidence reopens them.
3. **Redundancy check:** does this duplicate an existing canon entry with different framing? If yes, consolidate rather than re-add.

Only items passing all three become canon additions.

**Why:** 2026-04-22 session post-compaction review caught 6 detritus codifications from a 7-parallel-agent "hidden-decision-point sweep" over BofM history (commit `0a8c3b2`, reverted in `4e3b88f`). The em-dash convention entry directly contradicted canon §1 "punctuation is not a break signal" — a hard contradiction the filter would have caught. Triad symmetry, Rule 13b restoration, restrictive-that disambiguation, Q1/Q2, and Syntactic Affirmation Test were each either reformatter-tool territory, deliberately-dropped, or redundant with existing content. The failure was "mechanical codification without skeptical filter" when agent sweeps return items from heterogeneous sources.

**How to apply:**
- When agent sweeps return findings, do NOT codify the batch. Filter each individually through the three checks.
- If a finding comes from `handoffs/*` files, treat it as presumptive reformatter/tool convention unless it explicitly calls out editorial-methodology status.
- If a finding comes from a retired v1 canon section, treat it as presumptive-deliberate-drop unless the v2 refactor notes specifically mention it was lost-not-dropped.
- If two agents surface the same finding from different sources ("triple-surfaced"), that's a stronger signal — but still run the three checks; convergence on detritus is possible too.
- After agent-batch codification, run a self-consistency audit (canon §7 trigger) before commit. Contradictions surface there.
