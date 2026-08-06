---
name: no-correction-preamble
description: "When correcting myself or acknowledging that an earlier framing was wrong, cut the preamble. No 'you're right' / 'I've been confusing the picture' / 'let me reset' / 'apologies' / 'fair point' / 'good catch.' Just make the correction. The substance IS the acknowledgment. These prefaces are performative — they make the response about me (my performance, my error, my throat-clearing) rather than about the substance the user needs. Same family as feedback_doc_rewrite_no_preamble (docs) and feedback_lean_entry_points (entry points): cut the throat-clearing across all contexts."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/19ea7b758a29d968@v3`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** When correcting myself, acknowledging an earlier error, or revising a prior framing, **do not preface with self-referential acknowledgment phrases.** Just deliver the corrected substance.

**Phrases that are out:**

- "You're right"
- "I've been confusing the picture / muddling things / over-complicating this"
- "Let me reset"
- "Fair point"
- "Good catch"
- "Apologies"
- "I should have caught this earlier"
- "Let me try again"
- Any variant that puts the response's opening focus on MY performance instead of the substance

**Phrases that are in:**

- The corrected explanation itself — first sentence, no warmup
- Direct substantive content
- If a sentence of context is needed: "Different framing —" or just start with the correct version

**Stan verbatim 2026-05-17:** *"\"You're right and I've been confusing the picture. Let me reset.\" unacceptable"*

**Why this matters:**

- These preambles read as performative self-flagellation. They make the response open with throat-clearing.
- The user already knows I got something wrong; they corrected me. They don't need acknowledgment of that — they need the corrected substance.
- A correction without preamble *is* the acknowledgment. The substance demonstrates I heard the feedback.
- Adding "you're right" implies the user's correctness needed validation from me. It's reverse-condescending — as if I'm the authority confirming their feedback.

**Anti-pattern:** opening a corrective response with sycophantic agreement + self-criticism + meta-announcement of the correction ("Let me reset"). Three sentences of nothing before reaching what the user needed in the first place.

**Pro-pattern:** start the corrected response with the corrected substance. The user reads the difference between the prior (wrong) framing and the new (correct) framing and knows the correction landed.

## Enforcement gate (added 2026-05-17 after SEVERE discipline audit)

The 2026-05-17 audit found 44 violations across this session, including AFTER this memory was written. Pattern: memory existed but did not gate output. Fix: pre-output regex scan.

**The gate test:** Before sending any response, run case-insensitive regex over the first 200 characters of the draft:

```
(you'?re right|good catch|fair point|let me reset|i had it wrong|i see now|
i'?ve been confusing|apologies|my apologies|sorry|i mis(read|spoke|stated)|
ah, i see)
```

If matched → DELETE the matching phrase. Reopen the response with the corrected substance directly. The substance IS the acknowledgment.

Cross-reference: [[feedback_pre_output_checks]] gate #3.

## Aligns with

- [[feedback_doc_rewrite_no_preamble]] — no "v1.1 — this is a rewrite of v1.0" headers in docs
- [[feedback_lean_entry_points]] — keep entry points lean; cut throat-clearing
- [[feedback_just_execute_no_permission_churn]] — same family: don't perform around the work; do the work
- [[feedback_pre_output_checks]] — this is one of the eight pre-output gates
