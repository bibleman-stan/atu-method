---
name: doc-rewrite-no-preamble
description: "When rewriting a methodology/architecture/spec doc to reflect a new state, present the current state cleanly. No 'v1.1 — this is a rewrite of...' headers. No multi-paragraph 'what it was before / why we changed it' preambles. The doc IS the current methodology; legacy detail and history belong in git log, JSONL, and memory — not in the doc itself. Verbose change-history distracts both human readers and future Claudes from the actual content."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/6e39bb92106733e7@v2`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** When rewriting a methodology, architecture, or specification document to reflect a new state of the world, **the new doc IS the doc.** Present the current methodology cleanly. Do not lead with:

- "v1.1 — this is a rewrite of v1.0" headers
- Multi-paragraph "what it used to be" sections
- "Previously we did X, but now we do Y because Z" preambles
- "This supersedes the prior architecture which had problems A, B, C" framings

Stan verbatim: *"i believe it is imperative that we don't do what you usually do, which is an extremely verbose 'version 1.1 - this is a rewrite of blah-blah and then 5 paragraphs of what it WAS' which distracts both human and robot."*

**Why:** Verbose change-history in a methodology doc:
- Forces every future reader (human or Claude) to wade through legacy detail before reaching the actual current state
- Pollutes the load-bearing content with self-referential narration
- Creates rot quickly — the "what it was" sections age poorly as the codebase evolves further
- Encourages a writing style that defends decisions rather than presenting methodology
- The legacy state and the reason for change are already captured in git log, JSONL session records, memory files, and commit messages. The doc doesn't need to duplicate them.

**How to apply:**

- Start the rewrite from a blank conceptual page. What IS the methodology? Write that.
- Acknowledge prior state only when necessary for current decisions (e.g., "the producer-style validator stack is legacy and should not be used" is one short line, not five paragraphs explaining why)
- Put change rationale in the commit message, where future archeologists can find it via `git log` or `git blame`
- If a "supersedes X" note is genuinely needed, one sentence at the top: "This supersedes [link to prior version in git history]."
- For methodology docs specifically: the reader cares about HOW TO DO THE THING NOW, not the historical journey to that knowledge

**Anti-pattern**: writing a methodology doc that reads like a research paper recapping the literature review before getting to the contribution. Strip the literature review; the contribution is the methodology.

**Pro-pattern**: a methodology doc a new collaborator (human or Claude) could read cold and immediately know how to do the thing, without needing to also internalize three prior iterations of how it was done before.

## Aligns with

- [[feedback_session_bookend_protocol]] — same family: don't write narration-of-changes when the verbatim record (git log, JSONL, memory) already captures it
- [[feedback_simplicity_bias]] — reduce noise; reader bandwidth is the scarce resource
- [[feedback_stan_writes_claude_edits]] — Stan writes substantive prose; when Claude does write a methodology doc, write it as if it were the only doc that ever existed for this thing
