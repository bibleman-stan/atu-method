---
name: no-silent-parking
description: "An issue identified mid-session that isn't fixed in-session MUST land in _deferred_queue.md before the turn ends. Silent parking — diagnosing a problem, proposing a fix, and walking away without queueing it — evaporates at compaction and reads as 'pretending you dealt with it.' Stan's red line."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/f1cf3efdc0473cfd@v2`); state as of 2026-06-05 (snapshot mtime); possibly stale — re-verify before relying.

When I identify a defect class in mid-session work, propose a fix shape, and then DO NOT implement it before the turn ends, ONE of two things has to happen:

1. **Build it this turn.** Default for any defect on a deployed reader. Stan does not want defects that he raised to age across sessions on bomreader.com / tanakh-reader.com / lxx-reader.com / gnt-reader.com / vulgate-reader.com without forward motion.
2. **Add it to [[_deferred_queue]] BEFORE the turn ends, named explicitly.** Not in conversation prose. Not "I'll add this to the queue." An actual `Edit` against `_deferred_queue.md` in the same turn as the diagnosis. The named entry must include: (a) defect class + canonical example verse, (b) proposed fix shape, (c) why deferred (substrate gap / scope / audit-gate / Stan-pending-decision).

**Forbidden:** writing prose like "added as issue #N to the parallel audit queue" / "I'll surface this for v2 next pass" / "parked for after the four in flight return" WITHOUT either editing `_deferred_queue.md` or naming a concrete in-session next step. That prose is the silent-parking pattern. It produces the appearance of bookkeeping while doing none, and the defect evaporates on compaction.

**Why:** Stan verbatim (2026-06-05, on Alma 34:4 follow-up): *"DID WE NOT SAY THIS IS UNACCEPTABLE AND WILL NO LONGER BE TOLERATED TO 'PARK' THINGS AND PRETEND YOU HAVE DEALT WITH THEM"*. The 2026-05 prior session diagnosed Alma 34:4 as a cross-verse bare-`that`-complement forward-closure failure ("issue #5: post-emit forward-closure backstop"), proposed a fix, queued it to a "parallel audit queue" that existed only in the conversation, and then compaction dropped the queue. Alma 34:4 still renders as a single forward-closure-failing line ~10 days later. The defect didn't get worse, but Stan's trust in my surface-level acknowledgments did.

**How to apply:**
- Smell test before ending any turn: "did I diagnose anything I'm not going to build this turn?" If yes, `Edit _deferred_queue.md` BEFORE writing the response that mentions it.
- "Parallel audit queue" / "issue #N" / "for v2" are not bookkeeping — they are vapor. The queue is `_deferred_queue.md`. Nothing else counts.
- Compaction-resume audit hook: on first orientation read of `_deferred_queue.md`, cross-reference against the JSONL of the prior 2 sessions for any "issue #N parked" / "deferred for v2" prose that did NOT make it into the file. Any orphan IS a failure to surface.
- Defects raised by Stan on deployed readers get an extra-strong default toward **build-this-turn** over queue, because the deployed reader is the user-facing artifact.

## Aligns with

- [[_deferred_queue]] — the ONLY accepted parking destination
- [[feedback_circling_back_thread_tracking]] — internal continuity; the queue is the externalized form
- [[feedback_compaction_resume_protocol]] — JSONL re-acquisition is how silent-parked items can be RECOVERED, but the goal is for nothing to need recovery
- [[feedback_no_fly_swatting]] — find the CLASS, fix the class; per-instance overrides without class enumeration is a sibling of silent parking
