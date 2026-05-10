---
name: When you introduce a new window or flag, sweep ALL handlers that interact with it
description: A flag/window with N readers requires gating all N at once, not patching them as bugs surface; same root-cause symptoms in different code paths are not separate bugs
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
When introducing a new state window (a timeout, a "navigation in flight" flag, a "loading" state, etc.) that scroll handlers / event handlers / async readers must respect, **sweep every consumer of that signal at the moment of introduction.** Don't ship the new window with one handler gated and the rest racing.

**Why:** Stan flagged this 2026-04-30 after the third sequel of the same root-cause bug:
- Bug 1 (Jacob 4:1 → 1:1): I introduced an 800ms `_pendingVerseScroll` window during which a smooth-scroll animation runs. I gated `onScrollUpdateChapter` against the flag and shipped.
- Bug 2 (audio at Jacob 1:3): `getChapterAtViewport` in narration.js was a *second* scroll-driven reader during the same window. I patched only that one as a one-off.
- Bug 3 (Mosiah 5:1 → Mosiah 1:3): `_tryExtendBackward` and `_tryExtendForward` were a *third pair* of scroll-driven side effects. The endless-scroll prepend's `scrollBy` compensation invalidated the smooth-scroll target Y mid-animation. Stan: "why did you not find this when i pointed out the jacob problems."

The window I introduced was simple: "for ~800ms after a verse-picker navigation, the page is mid smooth-scroll." Every handler in the codebase that runs on scroll events or reads scroll position during that window can interact destructively with the animation. The same scroll listener literally has three sequential calls — `onScrollUpdateChapter()` / `_tryExtendForward()` / `_tryExtendBackward()` — all at the same indentation level in the same function. Gating one of three is the failure.

**How to apply:**

1. **At the moment you introduce a new state window**, immediately enumerate every consumer:
   - Grep for the event the window relates to (`scroll`, `resize`, `hashchange`, etc.).
   - Grep for direct readers of the related state (`scrollY`, `getBoundingClientRect`, etc.).
   - Grep for any code path that runs in the affected timeline (rAF callbacks, setTimeouts, polling intervals).
   - List them. Decide for each: gated, unaffected, or untouched-but-noted.

2. **Treat repeat symptoms as a class signal, not separate bugs.** If a fix to handler A starts producing bug reports about a symptom in handler B, **do not** patch B in isolation. Stop. Re-enumerate. Apply the gate to A, B, and any other handler that fits the same class. Ship one comprehensive fix, not three sequential ones.

3. **Audit prompts should be unprimed.** When you dispatch an audit on "why does feature X behave wrong," the prompt should ask "what *every* side effect runs during the affected timeline?", not "is this specific handler racing?" Priming the audit narrows it; an unprimed audit catches siblings.

4. **The "third strike" rule.** If you patch the same root-cause class twice in a row (handler-1, then handler-2), STOP before patching handler-3. Run an explicit sweep: `grep` for every handler that could exhibit the symptom. Ship the sweep, not the third patch. By the time you're patching the third instance, you should have done the sweep already.

**The enumeration question to ask yourself:**

> "I just introduced state window W. Code paths X, Y, Z run during W. Do all of X, Y, Z respect W? If I haven't checked all of them, I have NOT shipped a fix; I've shipped a partial fix and bug reports for the rest will come."

**Ports to other projects:** the same discipline applies to any "new flag with N readers" pattern — feature flags, loading states, animation-in-progress flags, dirty-state flags, lock flags. In the bofm codebase the trigger is `window._pendingVerseScroll`; in other codebases the analogue is whatever new flag the recent change introduced.

**Pairs with:**
- `feedback_check_existing_tooling.md` — before building new, sweep what's already there
- `feedback_application_consistency_vs_rule_coverage.md` — same-rule-applied-inconsistently is the failure mode that creates incidents
- `feedback_no_fake_dilemmas.md` — patching one of three is itself a fake-dilemma framing where the dilemma is "fix the one that's broken now"
