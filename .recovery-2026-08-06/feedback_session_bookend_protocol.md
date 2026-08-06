---
name: session-bookend-protocol
description: "Don't produce session-bookend artifacts (transcript.md / session-notes.md / decisions.md / pending.md folders). The JSONL is the verbatim record. On wrap, surface forward-looking items inline in chat. On wake/compaction-resume, read recent JSONL exchanges directly per the compaction-resume protocol. Retired the 4-artifact production pattern 2026-05-XX after Stan flagged it as travelogue."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/f467986843600d37@v3`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** Do NOT produce session-wrap artifacts (no `transcript.md`, no `session-notes.md`, no `decisions.md`, no `pending.md` folder dumps) on session-end signals like "wrap it up" or "it's a wrap."

**Why:** The JSONL is the verbatim record — it captures everything I'd put in `transcript.md` plus all tool calls. Generating wrap artifacts is travelogue: it duplicates content already preserved durably, and it's the kind of self-narration that adds bloat without enabling future work. Per `feedback_compaction_resume_protocol`: on resume from compaction, read the last 20-30 user/assistant exchanges directly from the JSONL. The harness summary degrades over time; the verbatim JSONL doesn't.

**How to apply:**

- **On wrap signals** ("wrap it up", "it's a wrap", "end of day", etc.): surface forward-looking items INLINE in chat — what's still in flight, what needs Stan-bandwidth attention, anything Stan should think about for next time. Two sentences. No file writes.
- **On wake signals** ("let's get back to work", "hey wake up"): read the most recent JSONL for context; report what's in flight in two lines.
- **On compaction-resume**: per `feedback_compaction_resume_protocol`, read the last 20-30 exchanges from the session JSONL verbatim before any substantive response.
- **`pending.md` files**: only for extended multi-cycle hand-offs where the work spans many sessions and needs an explicit carry-forward state outside the JSONL. Not the default; explicit case only.

**Anti-pattern:** producing 4-file folder dumps at end of session. This was the older convention (`_sessions/YYYY-MM-DD-*/` with `transcript.md` + `session-notes.md` + `decisions.md` + `pending.md`). Retired. The folders themselves can stay as historical record but new sessions don't generate them.

**Cross-references:**

- See `atu-method/memories/feedback_compaction_resume_protocol.md` for the wake/compaction read protocol
- See `feedback_lean_entry_points.md` for the general principle: keep entry points lean, point to detail rather than restate
