---
name: Don't over-engineer orchestration — prefer runbooks over scripts
description: Before building Python/TS that wraps the Anthropic SDK, check whether a markdown runbook delivers the same "consistent across sessions" property without separate API billing
type: feedback
---
When an open item says "codify the X pattern" or "build an orchestrator for Y," the first question is **"does this need to be runnable code, or would a markdown runbook / prompt template suffice?"** For one-user workstation tools that are only invoked from within Claude Code sessions, Python or TypeScript that imports the Anthropic SDK is almost always the wrong shape — it requires Stan to set `ANTHROPIC_API_KEY` from a separately-billed console.anthropic.com account, and it duplicates dispatch capability that the native Claude Code `Agent` tool already provides under his existing subscription. **Codification ≠ code.**

**Why (origin):** On 2026-04-18, the trench Claude in the `readers-gnt-morph` sibling built `src/chapter_review.py` — 408 lines of Python plumbing with `ThreadPoolExecutor`, prompt caching, structured output templates — to "codify the horde-review pattern" that had been hand-authored as 42 parallel `Agent` tool calls in prior sessions. Stan's response: *"why would I do that? is there something I can only do that way? I'm not looking to pay for another subscription."* The honest answer was no — native `Agent` tool calls from inside a Claude Code session produce the same reviews on his existing subscription. The script was reverted (`22afd7f`) and the actual codification value — the review prompt text + the data-state-vs-rendered-output instructions — was re-landed as a markdown runbook. The 408 lines of plumbing added nothing; they just routed Stan through a second paid account. Overseer propagated the lesson here (elevation propagation per `feedback_taskmaster_propagation.md` in overseer memory) because the temptation to wrap Claude in SDK code can fire in any trench.

**How to apply:** Before writing Python or TypeScript that imports `anthropic` / `@anthropic-ai/sdk`, run through this three-question check:

1. **Does Stan run this outside Claude Code sessions?** (cron, CI, other machines, headless automation) — if no, proceed to (2).
2. **Is there a native Claude Code equivalent?** (`Agent` tool, `/loop`, `CronCreate`, subagents, skills) — if yes, the native path uses Stan's existing subscription and handles parallelism / scheduling for free.
3. **Does a markdown runbook give you the consistency property?** (same prompt text, same dispatch rules, same traps documented session-to-session) — if yes, the runbook wins.

If (1) is no AND (3) is yes, **write the runbook, not the script.** Scripts that wrap the SDK are justified only when the user actually needs headless / scheduled / multi-user / cross-machine execution — not for "I want the prompt to stay consistent next session."

**Secondary signal:** if the tool you're about to build requires billing setup the user didn't ask about, pause and surface that tradeoff *before* writing the code, not after. "This will require you to set `ANTHROPIC_API_KEY` and fund an account — do you want that, or would a runbook suffice?" is a one-sentence cost that prevents 400 lines of throwaway.
