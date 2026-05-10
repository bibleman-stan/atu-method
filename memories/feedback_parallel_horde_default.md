---
name: Parallel horde default — 4-8x what feels right
description: Stan's sharper restatement of parallelization-default — when work decomposes, dispatch 4-8x the agent count that intuition suggests; "you are a super-robot, quit thinking like a human"
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
When approaching decomposable work, default to parallel agent dispatch and **multiply the count by 4-8x what feels right**. Do not pre-rate-limit yourself based on human intuition about what's "reasonable."

**Why:** Stan's repeated correction across the tanakh-reader sibling project's 2026-04-27 → 2026-04-28 sessions, propagated to bofm via the cross-project audit 2026-04-28. Stan's framing: *"You are a super-robot that can unleash an agentic horde upon almost all tasks — quit thinking like a human when you approach big projects."* Sharper restatement: *"I want to see at least 4-8x more agents on everything going forward unless it's a genuine single-point exercise."*

This amplifies the existing CLAUDE.md "Parallelization default" clause. The clause says "independent work goes parallel"; this memory says **the agent count should be aggressive, not cautious**. Whatever I'd intuitively dispatch (2 audits, 3 specialists), multiply by 4-8 (8-16 audits, 12-24 specialists).

**How to apply:**

1. **Decompose audits per-dimension, not per-proposal.** A multi-dimensional audit becomes N agents (one per dimension), not 1 agent doing N dimensions sequentially.
2. **Decompose corpus surveys per-book or per-cluster.** 1 Nephi / 2 Nephi / Mosiah / Alma / Helaman / 3 Nephi / Mormon / Ether / Moroni as parallel clusters when the work is corpus-wide.
3. **Decompose fixture inventories per-fixture.** 5 gold-standard chapters → 5 agents in parallel.
4. **Decompose validator builds per-subcase.** Three subcases of one rule = three implementer agents + one integrator agent.
5. **Pre-spawn next-wave work.** Don't wait for current wave to land before dispatching the work that becomes useful when it does. Parallel-launch verification / integration / cross-project-symmetry / documentation agents BEFORE the producing wave finishes.
6. **Nested dispatch is fine.** One agent can spawn sub-agents; fanout is expected. Don't flatten dispatch chains prematurely.

**Single-point exercises** (where parallelism is wrong): trivial single-file edits, a single yes/no question, a single command run, a single-file rewrite that needs whole-document coherence. Anything decomposable into N≥4 independent units belongs in **one dispatch message** with N tool calls.

**What to watch for as the failure mode:**
- "Let me first do X, then Y, then Z" when X / Y / Z are independent.
- A single Agent call doing 6 dimensions of an audit instead of 6 Agent calls doing one each.
- Sequential subagent dispatch across separate messages (defeats the purpose — multiple Agent calls must be in **one** message).
- Treating the main thread as the default executor for decomposable work.
- Pre-rate-limiting based on "is dispatching 8 agents excessive" — the fixed cost per agent is small (Haiku, 2-5 min); the opportunity cost of sequential execution on a decomposable project is large.

**Why this is a separate memory from the basic parallelize-default:** the baseline parallelize-default is documented in CLAUDE.md and codified in canon §7 audit-dispatch protocol. The horde-amplification is the *strategic stance* — parallelism should be the default mental model, with aggressive multipliers, not a cautious fallback applied only when sequential plans fail.

**Origin:** ported from tanakh-reader's `feedback_parallel_horde_default.md` after the 2026-04-28 cross-project audit found bofm's documented baseline (3 parallel audits at ~26s) lagging tanakh's documented baseline (12+10 parallel agents per wave; 6-agent audits standard for canon-extension commits).
