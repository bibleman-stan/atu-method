---
name: feedback-check-in-regularly
description: "During long-running background work, check in with Stan at regular intervals — don't go silent until completion (\"I'll resurface when it lands\" is too passive)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/585365b0daaab9cb@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

When background agents / long jobs are running, **check in with Stan at regular intervals with a progress report** — do NOT go dark and only report on completion. Stan: "you said 'I'll resurface the moment either lands' — i expect you to check in regularly." Saying "I'll resurface when it lands" reads as passive/silent.

**Why:** Stan wants visibility into in-flight work, not a black box that surfaces only when done (or when he pings). Long agent runs (5-30 min, some lose their reports to API flakiness) leave dead air he dislikes.

**How to apply:** While agents run, proactively (a) **check their disk-state** (`git diff --stat`, scratch mtimes, the agent's persist-file) and report progress, and (b) **schedule a wakeup** (`ScheduleWakeup`, ~600-900s) to deliver a progress check-in even with no completion event — re-schedule each tick while work is outstanding; stop when the queue is clear. The harness auto-notifies on completion, but that's not enough for Stan — give intermediate progress too. Pair with [[feedback_circling_back_thread_tracking]] (hold the open-threads set) and the parallel-dispatch default.
