---
name: feedback-walkthroughs-are-one-step-at-a-time
description: When walking Stan through a UI or setup procedure, give ONE step and stop — wait for acknowledgement of completion before the next. Never dump the whole sequence.
metadata:
  node_type: memory
  type: feedback
---

# Walkthroughs are one step at a time

**Stan, 2026-08-09:** *"you need to continue walking me thru step-by-step (and that means asking for acknowledgement of completion before next step)."*

Give **one step**, then stop and wait. Do not send the next step until he confirms the previous one is done.

**Why:** a six-stage procedure delivered at once is a document, not a walkthrough. He is executing in a browser while I am blind to what he sees — so each step's outcome is information I need before the next one is even correct. Twice in the `colometry-project` setup my instructions were wrong against the live UI (a workflow I said to enable ships enabled; a cross-repo capability I said was unconfirmed is demonstrated), and both were caught only because he sent a screenshot mid-sequence. Batching hides those mismatches until the end, when they are expensive to unwind.

**How to apply:**

- One step per message. Name what he should see when it worked, so the acknowledgement carries information.
- If a step has sub-parts that must all land before anything is verifiable, say so and keep them together — but that is the exception, not the default.
- Ask for a screenshot when the UI is doing the talking.
- When he confirms, correct the written procedure if the live UI differed, then send the next step.
- Do **not** re-explain the whole plan each time. He has it.

**Related:** [[feedback_no_eyeball_offers]] · [[feedback_directive_protocol]]
