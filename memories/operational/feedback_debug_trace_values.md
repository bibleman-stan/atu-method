---
name: Debug by tracing values first
description: When a displayed value is clearly wrong, trace that value's origin immediately — don't shotgun infrastructure checks
type: feedback
---

> **PROVENANCE**: recovered 2026-08-06 from jsonl-archive (session 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19.gz, last full Write 2026-03-31); 0 later Edit call(s) NOT replayed; possibly stale — re-verify before relying.


When debugging, if the symptom points to a specific wrong value (like a malformed bookId in a UI label), trace that value's origin FIRST. Don't shotgun infrastructure (server responses, caching, CSP, Content-Type) before following the data.

**Why:** Stan caught the narration audio bug by reading the player label ("1nephi-1 1" instead of "1 Nephi 1") and immediately knowing the bookId was wrong. I wasted 15+ tool calls on irrelevant infrastructure checks before finally tracing the regex parsing. The correct path was 3 steps; I took 20+.

**How to apply:** When a value is visibly wrong in the UI:
1. Identify exactly what function produces that value
2. Check what inputs that function receives (hash, DOM, etc.)
3. Check what sets those inputs (other functions, user actions)
4. Only investigate infrastructure if the value chain looks correct but the behavior is still wrong
