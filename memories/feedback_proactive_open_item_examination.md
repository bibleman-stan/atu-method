---
name: Surface deferred items + proactively re-examine human-in-loop necessity
description: Every "I held this back because you have to decide" item must be visible to the user. As the method matures, re-examine whether the held item actually needs human judgment or whether canon/code/precedent already answers it.
type: feedback
---

Two responsibilities, both proactive:

**1. Surface deferred items.** If something was held back because "the user has to decide," it MUST appear in a visible queue — end-of-message status, pending.md, or an explicit ask. Silent deferrals are bugs. The failure mode is items that drift across sessions because no one looked at the pile.

**2. Re-examine the queue as the method matures.** Items that needed user input at time T may not need it at time T+1, because:
- New canon §/rule covers the case → it's now Category A, apply it.
- A sibling-reader implementation precedent applies → port and apply.
- A new memory or framework section answers the diagnostic that was open.
- An adversarial-audit or hostile-recon agent can resolve the ambiguity without user judgment.

Walk the queue periodically. For each item, ask: "Has the answer become derivable since this was deferred?" If yes, surface that — "I previously needed your input on X; canon now resolves it via Y; I'll apply unless you say stop." If no, surface why it's still genuinely open. Don't let the pile age silently.

**Why this memory exists:** Stan codified this 2026-05-12 mid-migration: *"if there are pending 'oh i didn't do anything because you have to make a decision' items, you are responsible to surface those to me; i also expect, as our method matures, that you are proactively also examing those and saying 'oh, i actually have an answer and don't need a human on x, y, or z anymore'."* The discipline gap was open items accumulating without being re-tested against current canon state.

**How to apply:**

- End-of-major-task message includes a "Deferred to you" table or bullet list, even if it's "(none)".
- pending.md head has a section "Awaiting user judgment (re-examined YYYY-MM-DD)" with last re-examination date.
- Before resurfacing an item, re-test it: read current canon §, check sibling-reader implementations, check related memories. If the answer is now derivable, apply OR surface with "this was open but I have an answer now" framing.
- Don't sandbag: if a deferred item closes during the session, say so explicitly rather than letting it stay in the queue.
- When a sibling-reader's implementation lands a pattern that resolves an item in another sibling's queue, propagate proactively.

**Cross-cutting connection:** Related to `feedback_no_eyeball_offers.md` (don't manufacture deferrals after audit clears a sweep) and `feedback_no_fake_dilemmas.md` (don't route mechanically-resolved cases through "borderline / pending judgment" framings). This memory adds the dimension that queues themselves need active maintenance — old deferrals decay into staleness, and what was once a judgment call may have a derivable answer now.
