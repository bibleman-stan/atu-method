---
name: pending.md is for carry-forward state only — decisions in chat, no redundant wrap docs
description: pending.md is the only wrap doc and contains forward-looking carry-forward state ONLY; decisions go in the chat window; transcript/session-notes/decisions narratives are redundant with JSONL
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
`pending.md` is the only wrap doc, and it is for **forward-looking carry-forward state ONLY**. Two failure modes share this root and are both prohibited:

## Section A — No redundant wrap-doc narratives

At session end, the **only** wrap-up file to produce is `pending.md`. Do NOT write `transcript.md`, `session-notes.md`, `decisions.md`, or any narrative re-summary of what happened during the session.

**Why:** Stan flagged this 2026-05-05 after observing that the four-file wrap ritual was redundant with the JSONL session log. The JSONL captures every user message, every assistant response, every tool call, every result — verbatim with timestamps. Re-summarizing that content in narrative or transcript form is duplicated work; the JSONL already did it better. Stan's directive: *"there is low utility in asking you to document each session verbatim given that it all lives in the jsonl... stop doing verbatim wrap-ups immediately we do not need to spend your bandwidth on redundant tasks."*

## Section B — No decision-deposit files

When work surfaces items that need Stan's judgment — editorial choices, scope refinements, MEDIUM-confidence classifications, REVIEW-required cases, "should I apply?" questions — **raise them in this chat window**, not in `pending.md` or any other file.

**Why:** Stan flagged this 2026-05-06 after I declared "we're good" on the M3-extension work and dropped 38 REVIEW-length cases + 4 MEDIUM theological cases into `pending.md` as "Stan-call when convenient." His correction: *"don't just put stuff in files and hope that stan goes and looks at them; decision points and recommendations all happen in this window."*

Files are passive — Stan has to read them, remember they exist, decide when to address. Chat is active — the decision is right there, Stan responds in the same context, the loop closes. Burying decisions in files breaks the active-feedback loop the working session depends on.

## What pending.md actually IS

`pending.md`'s actual role is **carry-forward STATE**: "this in-flight work hasn't shipped, here's what's left so a future session can resume." It is NOT a wrap narrative, and it is NOT a place to deposit decisions Stan needs to make.

## How to apply

- At wrap, edit/append `pending.md` only. Tight bullet list: in-flight items, HEAD pointer + cache version, fresh-session orientation cues.
- When a carry-forward closes, **delete** the bullet from `pending.md`. Don't preserve historical "completed" lists — git log + JSONL hold history.
- When work produces N items needing Stan's judgment, surface them in chat with concrete content (not abstract counts). For REVIEW-required cases: show 3-5 specific cases with merged-result preview, ask which path he wants per category. For MEDIUM-confidence editorial calls: show each case with the ambiguity and ask the binary question.
- Per-decision questions should be tight enough that Stan can answer with a one-word direction ("apply" / "drop" / "keep" / "skip"). Multi-paragraph questions force Stan to read instead of decide.

## What NOT to do (failure modes)

- Writing a session-notes "addendum" because something interesting happened mid-session. The JSONL captured it.
- Writing a decisions-style entry "for the record." The decisions live in the JSONL.
- Re-narrating a multi-day session arc to "preserve continuity." Continuity comes from `pending.md` + canon + JSONL.
- Drop "X cases routed to REVIEW — see validator output" in `pending.md` and call it done.
- Surface a scope decision ("strict-only or broad-scope?") in `pending.md` and assume Stan will discover and decide.
- Recommend a corpus edit in chat and walk away without asking whether to apply.
- Write "Stan-call" anywhere in a file as a euphemism for "I'm dropping this in your lap silently."

## Cross-project note

If tanakh-reader or readers-gnt have similar four-file wrap rituals or decision-deposit patterns, the same logic applies. Watch for the same pattern there and don't re-establish it.
