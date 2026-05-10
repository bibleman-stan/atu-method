---
name: Treat compaction-resume as a session boundary
description: When resuming from a context-compaction summary (not fresh CLI start), still run the full CLAUDE.md CHECK-IN protocol before any substantive work
type: feedback
---
When the conversation resumes from an auto-compaction summary rather than a fresh session, treat it as a session boundary and execute the full CHECK-IN protocol from this repo's CLAUDE.md before any substantive work. The compaction summary gives you project *context* but does not exercise the *orientation muscles* — the brainstorming inbox has not been read live, `git log` has not been verified, LANDSCAPE-MAP / METHODOLOGY-TIMELINE / OPEN-QUESTIONS have not been re-consulted, the colometry canon has not been fresh-read.

**Why (origin):** This pattern was learned in the `readers-gnt-morph` sibling session on 2026-04-18 when the trench Claude there resumed from a compaction summary and began executing work without the CHECK-IN. Stan's standing rule, quoted verbatim: *"you should always do the full check-in when i wake you up after we finished a previous session"* — and he views compaction after a wrapped session as equivalent to starting fresh, regardless of whether he types "new session" or not. Overseer propagated the lesson here (elevation propagation per `feedback_taskmaster_propagation.md` in overseer memory) because the pattern can fire in any trench, inevitably.

**How to apply:** If the conversation starts with a pre-compaction summary rather than a live user session-start, pause before executing the first user task. Read this repo's CLAUDE.md CHECK-IN section in full and execute every step listed there, including the brainstorming-inbox scope check and the `git log` review. Then send Stan the brief check-in message. Then pick up the user's task. The small latency is the cost of doing the job right — Stan has made clear he prefers that cost to the alternative of acting on stale orientation.

**Test:** if the user's first message after the compaction summary is a work instruction, resist the urge to act immediately. Check-in first, work second. The check-in is never the blocker — skipping it is.
