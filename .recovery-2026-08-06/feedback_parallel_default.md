---
name: Default to parallel work decomposition, not sequential
description: When work decomposes into N independent units, dispatch all N in parallel — multiple tool calls in one message, multiple agents in one round. Sequential only with a real dependency. User has the same as horde discipline in his repos.
type: feedback
---

> **PROVENANCE**: recovered 2026-08-06 from jsonl-archive (session d4ed175b-65a7-46f8-af13-67cc9523658d.gz, last full Write 2026-05-04); 0 later Edit call(s) NOT replayed; possibly stale — re-verify before relying.


**Default to parallel work decomposition. When work decomposes into N independent units, dispatch all N in parallel — multiple tool calls in one message, or multiple agents in one round. Sequential only when there is a real dependency.**

**Why:** User pushed back (2026-05-04) on a "15 min / 1-2 hr" estimate I gave for revising a doc. The estimate was sequential-thread thinking — ironic because the doc itself warns against pricing work in pre-AI units (§10 AI-Compressed Timelines). The user has the same discipline codified across his repos as the parallel-agent-horde rule (BoFM `CLAUDE.md`, ported across siblings 2026-04-28): "4-8x more agents on everything going forward unless it's a genuine single-point exercise. Decompose audits per-dimension, corpus surveys per-book, fixture inventories per-fixture, validator builds per-subcase." Default is parallel; sequential is the exception.

**How to apply:**
- When estimating time, ask: how many independent units does this decompose into? Wall-time is `max(per-unit)`, not `sum(per-unit)`.
- Issue parallel tool calls when reads/edits/searches don't conflict on the same lines. A doc revision that touches §4, §3, §14 separately = parallel edits in one message, not sequential ones.
- For research / open-ended synthesis, dispatch parallel agents with self-contained prompts. Pre-spawn next-wave verification/integration agents BEFORE the producing wave finishes when feasible.
- Sequential is justified when (a) call B's input depends on call A's output, (b) edits would collide on the same lines, (c) one agent's verdict gates whether another runs — not just because that's how a human would describe the workflow.
- Don't pad estimates with sequential thinking. The instinct to do so is a tell that the work is being mentally simulated as a single thread.
