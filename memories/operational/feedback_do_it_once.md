---
name: do-it-once-no-throwaway-passes
description: "When a task isn't urgent, do it once completely — don't split into a throwaway quick pass plus a full pass that redoes the same work"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 207b9cbe-32e7-4969-883d-9385135a663d
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`0142feeb-7d70-4e79-9add-d1ce2139d54b/03cb22adda04e494@v2`); state as of 2026-05-20 (snapshot mtime); possibly stale — re-verify before relying.

When a task isn't time-sensitive, do it **once, completely**. Don't propose a fast-but-partial intermediate step (a "quick win") when the full job will redo that same work anyway.

**Why:** While setting up lecture transcription, Claude proposed transcribing a short audio *slice* (to get one urgent-seeming answer fast) AND then transcribing the *full* lecture for analysis. Stan rejected this: the slice would just be redone by the full transcription — duplicated effort — and nothing was actually urgent. "do this once; this isn't urgent; otherwise you are duplicating effort."

**How to apply:** Before offering a quick-but-partial step, ask: will the complete job subsume this? If yes and there's no real deadline pressure, skip the partial step and just run the full job once (background it if long), then read whatever specific part you need from the complete output. Reserve the targeted/partial approach for cases that are genuinely time-critical. Relates to [[stan-user-profile]] (prefers efficient, no-padding work).
