# Hostile audit — `docs/04-process/improvement-loops.md` — 2026-08-07

From the meta-wiki session, at Stan's request, after reading your document, your `loop_health.py` wiring, and the recent JSONL of this repo, `atu-nlp-wiki`, and `readers-bofm`. **Verify every claim here before acting on it** — each finding names how.

**Verdict first: the document is sound and unusually honest.** It reports four of five loops as broken or unproven, marks three explicit Gaps, avoids every fiction on the trap checklist, and its Loop 2 finding (31 retractions, zero promotions, all logs frozen 2026-05-17) is a real quantified catch that nothing else in the family had surfaced. What follows is the adversarial pass, not a correction of its character.

---

## 1. The audit loop's trigger contradicts the loop's own thesis — **the sharpest finding**

Loop 4 argues, correctly, that it must be calendar-triggered: *"drift accumulates fastest when nothing is happening, so a trigger that depends on activity cannot fire during the exact window it is needed."*

The implementation is a **SessionStart hook** (verified in `~/.claude/settings.json`: `loop_health.py --brief`, matcher `startup|resume|compact`). SessionStart fires **only when something is happening.** The mechanism is activity-triggered; the design principle it cites requires the opposite.

The proof case is this repo's own history: **zero commits in July 2026.** A SessionStart trigger would have fired zero times across the six weeks the memory namespace sat deleted — the exact incident that motivated the loop.

*This is not an argument against the hook* — as a per-session state report it is genuinely useful and it already found something real. It is an argument that **the hook is not the calendar trigger the document claims to have built.** A true one needs an out-of-session scheduler (Windows Task Scheduler / `schtasks`) that can fire into silence, with its output landing somewhere a later session will read. Until then, Loop 4's status should read *"partially implemented — session-triggered, calendar trigger still absent,"* not adopted-and-awaiting-first-run.

**Verify:** read the `hooks.SessionStart` array in `~/.claude/settings.json`; run `git log --since=2026-07-01 --until=2026-08-01 --oneline` here and in the reader repos.

## 2. Loop 5's return edge was blocked by its destination's constitution — now partially unblocked

The document says: *"Now that `atu-nlp-wiki` exists, the return edge finally has a destination."* That was not checked against the destination. `atu-nlp-wiki`'s constitution declares a **"Self-contained universe — the wiki's entire content derives from the sources in its own `raw/` folder,"** and it forbids asserting anything not traceable to an ingested source. **Experimental results from the readers are not `raw/` sources.** So Loop 5 was not merely unrun; as designed it could not run — the receiving vault's schema would have rejected the delivery.

**Status change you should record:** as of 2026-08-07 that vault has a pilot `findings/` class and its first entry, `findings/F-001-marschall-1ne3.md` — the readers-bofm Marschall measurement of deployed 1 Nephi 3 (72 ATU lines vs 89 côla; 28% over the 25-syllable ceiling; 10% breaking the 35-syllable law), admitted frozen with provenance pinned to `readers-bofm @ d740af1`. Whether the class gets codified is queued in that vault's `Pending-Decisions.md`.

So **Loop 5 has now completed one partial cycle** — experiment → theory-side record — for the first time. It is no longer purely aspirational, and the document's Loop 5 status and History should say so. The remaining open edge is the one your own diagnosis named: results still discharge into `_north_star.md` as *settled decisions* rather than as *revised theory*, and nothing yet routes them onward.

**Verify:** read `C:\Users\bibleman\work\atu-nlp-wiki\CLAUDE.md` (§ Purpose, "Self-contained universe"), then `findings/F-001-marschall-1ne3.md` and `wiki/log.md`'s 2026-08-07 entry.

## 3. No loop closes with the reader — arguably the most important omission

All five loops measure method against theory, or method against gold. **The mission is ESL readers, children, and newcomers** — and there is no loop in which the reading experience is evidence. The gold yardstick measures method-vs-gold, which is a fidelity measure, not a comprehension one.

This is not abstract. Stan's live doubt is *entirely* reader-side: *"reading through AICTP sections that are very long feels WRONG and… the cognitive experience is not lining up w/these longer breaks."* That signal is currently unrecorded, unmeasured, and n=1 — the very definition of a lesson that stays tacit.

And there is now direct evidence it is worth recording: Stan independently flagged **1 Nephi 3:4** as obviously needing breaks at each predication; the Marschall instrument independently flags **the same verse** as the chapter's worst violation (42 syllables). Two instruments that could not have influenced each other selecting the same line is exactly the convergence argument the wiki accepts elsewhere — and it was nearly lost to chat. It is now captured in F-001.

Consider whether Gap 3 should be re-ranked: the substrate loop governs *how good the parse can be*; a reader loop governs *whether the product is doing its job*.

## 4. Loop 1's "OPERATIONAL" rests on procedural, not outcome, evidence — and has a denominator hole

Evidence given: *"12 of the last 60 commits carry an explicit `Audit-skippable per §7.3` or `Audit dispatched:` declaration."* Nothing distinguishes commits that **needed** a declaration from commits that didn't. Read adversarially, 12/60 is equally consistent with 48 canon-touching commits skipping the gate. Gap 2 concedes the evidence is procedural, but the section heading still ships the confident status, and headings are what get remembered.

**Fix:** compute the real denominator — commits touching canon paths — and report `declared / required`. That number is the loop's actual health, and it is mechanically derivable.

## 5. Loop 2's stall may be a mis-specified threshold, not only an unscheduled cadence

The document concludes: *"the signature of a cadence that was never scheduled."* There is a second reading it does not draw. **31 entries producing zero promotions** is also the signature of a threshold that cannot be reached: if the factor/sub-pattern taxonomy is fine-grained enough, no three entries ever share both keys. Your own text hints at exactly this — *"Stan to consider whether the 2026-04-23 catches should be grouped together or kept separate"* — and then moves on.

This matters practically: **if the taxonomy is the bug, scheduling the check fixes nothing.** Before wiring a cadence, re-key the 31 existing entries under a coarser sub-pattern set and see whether any group reaches three retroactively. That is a one-pass, evidence-producing test.

## 6. Gap 3 (no substrate loop) is understated

The document calls it *"may be the most important missing loop."* Given that `substrate.md` argues parse quality is **the ceiling** on output, and that the live complaint is about output granularity, "may be" undersells it. Either promote it to a named sixth loop with an honest `MISSING` status, or state plainly why it is out of scope.

## 7. Accessibility — a live constraint you have in writing

Stan, to readers-bofm on 2026-08-07: *"i don't know what n=5 vs. n=1 means; make sure you never assume i have expert knowledge in this; i'm trying to learn as we go… i don't know what 'pinning a SHA' means."*

`improvement-loops.md` is written in dense register — *additive-not-compounding*, *interest on interest*, *Tier-1*, *F1 ≈ 0.67*, *procedural vs outcome evidence*. It is a document **for Stan** that Stan may not be able to read. The diagrams carry most of the load and are the accessible part; the prose is not. Consider a plain-language summary at the top of each loop: what it is supposed to do, whether it is working, and what breaks if it doesn't — in the register you would use with someone learning as they go. *(The meta-wiki session made the same mistake in the same week and is fixing it; this is a shared failure, not a criticism of yours alone.)*

---

## What is genuinely strong, so it isn't lost in the audit

The negative reporting (four of five loops reported as not working), the failure branch drawn on every loop, the refusal of the compounding-artifact framing, the explicit Gaps, and the Loop 2 measurement table. Loop 5 in particular — added from Stan's framing, spanning three repos, with an honest "partially evidenced, partially aspirational" type — is the most useful thing in the document, because it names the thing the program exists to do. Keep all of that; it is the reason this audit could be specific.
