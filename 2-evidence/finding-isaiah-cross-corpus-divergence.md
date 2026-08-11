# Finding — the same Isaiah, two editions, 34% apart

**Measured 2026-08-07.** Stan: *"I am also suspicious we have not done right by Isaiah and his bicola and tricola intentions."* This 5-machinery/tests that against the one place the program has a genuine natural experiment.

**The setup.** BoFM quotes Isaiah verbatim (2 Nephi 12–24 = Isaiah 2–14), and `readers-tanakh` publishes the Hebrew of the same chapters. So the *same text* exists in two of our editions, segmented by two different substrates: BHSA gold clause-atoms with te'amim available on the Hebrew side, Stanza EModE on the BoFM side. Any divergence is ours, not the text's.

## The measurement — MT Isaiah 9 against 2 Nephi 19

| MT / BoFM verse | Hebrew lines | BoFM lines | |
|---|---|---|---|
| 1 / 2 | 3 | 2 | differ |
| 2 / 3 | 3 | 2 | differ |
| 3 / 4 | 2 | 1 | differ |
| 4 / 5 | 3 | 1 | differ |
| 5 / 6 | 4 | 3 | differ |
| 6 / 7 | 2 | 2 | |
| 7 / 8 | 2 | 2 | |
| 8 / 9 | 1 | 1 | |
| 9 / 10 | 4 | 4 | |
| 10 / 11 | 2 | 1 | differ |
| 11 / 12 | 5 | 3 | differ |
| 12 / 13 | 3 | 2 | differ |
| 13 / 14 | 1 | 1 | |
| 14 / 15 | 3 | 1 | differ |
| 15 / 16 | 1 | 2 | differ |
| 16 / 17 | 6 | 6 | |
| 17 / 18 | 4 | 4 | |
| 18 / 19 | 4 | 2 | differ |
| 19 / 20 | 5 | 4 | differ |
| 20 / 21 | 5 | 3 | differ |
| **total** | **63** | **47** | |

**14 of 20 verses disagree, and BoFM is coarser in 13 of the 14.** The Hebrew edition breaks 34% more often on identical content. The single exception (15/16) runs the other way.

## What this means

**Stan's suspicion is supported.** BoFM's Isaiah is systematically under-broken relative to our own Hebrew edition of the same passage — consistent in direction and rough magnitude with the Skousen comparison (1.75×, 81% of verses under-broken) and with the cross-corpus word-per-line spread (BoFM 16.2 against 7–9 for every gold-substrate sibling). Three independent comparanda now agree on the direction.

**It is also a cross-corpus convergence failure, which is the program's central thesis.** [[memories/feedback_cross_corpus_convergence.md|feedback_cross_corpus_convergence.md]] holds that ATUs should reveal common patterns across corpora because thought and language share structure. Here the *same text* in two corpora diverges by a third. Either the thesis needs qualification, or one substrate is wrong — and the substrate doctrine already predicts which: Stanza-on-EModE is the weak parse, BHSA is gold.

**But the Hebrew side is not clean either, and this is the part that complicates a simple "BoFM is too coarse" story.** MT Isaiah 9:1 renders as three lines, the first of which is `הָעָם֙` — "the people," a bare noun phrase, one word, no predication. That line **fails forward closure outright** under §2.1's own test. It is there because the te'amim disjoin at that point and BHSA's clause-atoms follow. So the Hebrew edition contains a defect in the *opposite* direction, produced by exactly the accent hierarchy the framework bars as a licensor while using it as a substrate.

That is a sharper problem than either edition's granularity: **the te'amim are excluded as a criterion but enter anyway through the parse.** It is the same laundering the framework already names for punctuation-conditioned parser labels (§2.1's parse-substrate corollary) — and nobody has checked whether it applies to accent-conditioned clause-atoms.

## Limits

One chapter, twenty verses, one book. Line counts, not boundary alignment — two editions can have equal counts and disagree on where the breaks fall, so this understates disagreement. A WindowDiff or boundary-agreement score over all of Isaiah 2–14 would be the real measurement, and it is cheap now that the alignment is known to work.

## Bearing

Feeds the §1/§2 reframe under discussion (Chafe / Givón / Fields / Louw / Marschall / Nässelqvist), and the non-finite predication ruling in `../Pending-Decisions.md`. Also a candidate first entry for a substrate loop, which [[4-process/improvement-loops.md|improvement-loops.md]] Gap 3 records as missing.
