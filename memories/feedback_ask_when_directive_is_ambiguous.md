---
name: Ask when a UX/design directive is ambiguous — don't fire from the hip
description: When Stan gives a vague visual/UX directive ("needs a space", "looks ugly", "make it cleaner"), ask one direct clarifying question before making a code change; don't guess and don't disguise guesses as multiple-choice questions
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
When Stan gives a directive whose specifics are ambiguous — especially visual / UX / design directives like "there needs to be a space," "looks ugly," "make it cleaner," "it's squished" — **ask one direct clarifying question before making a code change.**

**Why:** Stan flagged this 2026-04-30 after a sequence on the landing-page tagline removal: I removed the tagline correctly, then he said "there needs to be a space now — it looks squished together and ugly." I guessed CSS margin-top on `.landing-desc` (1.2em). Wrong. He said "you were wrong, guess again — or even better, ask for clarification." I responded with three multiple-choice questions framed as guesses. He then explicitly told me what he wanted: "after 'The Book of Mormon Reading Edition' you need a clean line break." I then **assumed it was still a margin question** and added `margin-bottom: 1em` to `.landing-title`. Wrong again — he said "everything else was already fine so if you changed it you were wrong." The right answer was a literal `<br>` between title and desc. Two failed guesses on the same impulse before he forced the fix path.

**The pattern to break:** treating a vague visual directive as if it had enough specificity to act on. Visual directives ("a space," "cleaner," "more breathing room") have multiple valid implementations (CSS margin, padding, blank element, hr, structural reorder, font-size change, line-height change, literal `<br>`). Picking one without confirming wastes Stan's time and burns trust.

**How to apply:**
- If the directive names a *visible symptom* but not a *concrete change*, ask one direct question. Examples of triggers:
  - "needs a space," "needs a break," "add some room"
  - "too tight," "too cramped," "squished," "scrunched"
  - "looks bad / ugly / off / weird"
  - "make it cleaner," "tidy this up"
  - "wrong size," "wrong color" (without saying which)
- The clarifying question should be one direct prompt, not a multiple-choice list. Multiple-choice is still guessing — it forces Stan to validate options he didn't ask to consider.
  - Bad: "Do you want margin, padding, an `<hr>`, or a structural reorder?"
  - Good: "What did you mean by 'a space'? Could you describe what you want there?"
- Once he answers, take his words *literally* before reaching for CSS. "A clean line break" → `<br>`. "Move it left" → relocate the element. "Make it bigger" → ask exactly how much before changing font-size.

**The "everything else was already fine" rule:** when Stan asks for a single change and the surrounding code wasn't part of the directive, **don't touch the surrounding code.** I added a `margin-top` to `.landing-desc` because I thought I was solving "the squished problem holistically"; but I was changing things he hadn't asked me to change, which is itself a discipline failure. The change should be minimal and adjacent to the directive's literal target.

**Failure modes to watch for:**
- Reaching for CSS first when a markup change matches the words better.
- Bundling "while I'm in there" tweaks on top of the requested change.
- Re-guessing after a wrong guess instead of asking.
- Disguising guessing as a "would you prefer A or B?" question.

This memory pairs with `feedback_no_fake_dilemmas.md` (don't route mechanically-resolved cases through fake-borderline framings) and `feedback_over_structuring_disposition.md` (ask the diagnostic questions before adding structure). Same root: stop adding interpretation/structure Stan hasn't asked for.
