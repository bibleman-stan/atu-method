---
name: feedback-time-estimate-as-diagnostic
description: When work feels like "weeks" for biblical-text engineering, that estimate is itself diagnostic — almost certainly you're treating substrate (data-already-produced-by-domain-experts) as if it were code-to-be-written. Audit before claiming the time.
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`9d9683ed-2bb3-499d-8eb7-715c2bd3a063/2b3978bf746d8609@v3`); state as of 2026-05-30 (snapshot mtime); possibly stale — re-verify before relying.

**Time-estimate as diagnostic.** When work feels like multi-day or multi-week for biblical-text engineering, the estimate is a signal you're solving the wrong problem at the wrong abstraction level — almost always treating SUBSTRATE as if it were CODE-to-be-written.

**Why:** the canonical 2026-05-30 instance — symmetric-substrate construction (KJV-to-source-word alignment for the whole NT + OT) was framed by me as "~1 week of focused engineering" then later as "~250 lines of Python, hours not days." Stan caught it: "every time I hear you say multi-day, I get suspicious you are forgetting that pipelines are available." But the deeper issue wasn't just pipelining — it was that the substrate (Macula Greek `xml:id` + `english` + `gloss` + `strong` + `lemma` per word; Macula Hebrew WLC lowfat same schema; MetaV `WordID`/`Strong's`/`vpos` per KJV word) was ALREADY ON DISK and ALREADY ENCODED THE ANSWER. The actual build was 250 lines of glue Python and 30 seconds of execution for the entire NT (99.55% cardinality match). Subsequent OT corpus build: another minute. Combined 26,014 verses validated mechanically in under 90 seconds of CPU time.

This was the same failure mode named in [[feedback_mechanical_first_for_own_review]] ("structurally impossible / defer to v2" said about features Macula tags mechanically), now applied at the time-estimate layer. The substrate doctrine ([[atu-method/3-implementation/substrate.md]] §1) says: "The ATU framework is a Container, not an Originator." Time estimates inherit this — when you're CONSUMING a substrate, hours; when you're ORIGINATING one, weeks. Confusing the two is the time-tax this memory exists to prevent.

**How to apply:**

1. **Before quoting any biblical-text engineering time estimate**, run this check:
   - Is the data I need *already on disk* in `biblical-corpora/`, `readers-*/research/`, `atu-method/data/`, `Dropbox/03-Biblical_Studies/`?
   - Is there a helper script already built (e.g., `readers-gnt/scripts/macula_*.py`, `readers-tanakh/scripts/atu_pipeline_v2/`)?
   - Is the answer encoded as substrate features (Macula `rule`/`role`/`frame`/`referent`; BHSA clause-atoms; MetaV Strong's-list)?
   - If YES to any: time is **hours, not weeks**. The code is glue.

2. **The hours-vs-weeks question collapses by an order of magnitude** when substrate is consulted first. "Multi-week" should be reserved for genuinely originating work: training a new parser (BoFM EModE), building a new gold treebank, designing a new methodology. NEVER for "use the data we have."

3. **Corollary — audit machinery scope shrinks**: complex audits + multi-round iteration become unnecessary when the substrate gives the answer directly. Audits are for genuine judgment-per-instance work (cascade-class mode (c)). When substrate solves it, the only audit is "did I read the substrate right?" — a 5-minute mechanical check, not a 25-minute parallel-Opus pipeline. Reaching for elaborate audit machinery on substrate-encoded answers is the same time-tax as treating substrate as code.

4. **Signature of the failure (when in the act of estimating)**: "We'd need to acquire X" / "Phase 0 substrate acquisition" / "Multi-week engineering" / "~$X of audit cycles." If you find yourself writing those phrases for biblical-text work, **STOP** and run the substrate-on-disk check above before committing to the estimate. The phrases are the stop signal.

**Ties:** [[feedback_mechanical_first_for_own_review]] (the per-instance-judgment analog); [[feedback_check_prior_corpora]] (port the proven solution); [[feedback_simplicity_bias]] (push back on complexity-pull); [[feedback_do_it_once]] (no throwaway quick pass before the full job); the substrate doctrine in `atu-method/3-implementation/substrate.md` §1 (Container-not-Originator). The empirical proof is the 30-second NT corpus build + 90-second full-Bible build that delivered 94.81% mechanical structural agreement with deployed ATU partitions — the work that would have been weeks if treated as code is minutes when treated as substrate consumption.

**2026-05-30 RECURRENCE — TAGNT/TAHOT** (same day this memory was committed, hours later): when Stan asked whether a KJV-side textual fabric existed to close the substrate-alignment 8% gap, I framed the response as "inventorying disk now to see what's already pulled." Stan caught it: "WE ALREADY HAVE STEPBible's TAGNT (Tagged Greek NT) and TAHOT (Tagged Hebrew OT)!!! you're killing me, smalls." Confirmed on disk in `readers-gnt/data/text-files/tagnt-source/` (TAGNT_Mat-Jhn.txt + TAGNT_Act-Rev.txt) and `readers-tanakh/research/stepbible-tahot/` (TAHOT_Gen-Deu.txt + Jos-Est + Job-Sng + Isa-Mal), with `ingest_tagnt_gaps.py` + `ingest_tahot.py` already partially wired. TAHOT's per-morpheme English column (`/`-separated, with per-morpheme Strong's tags H9009 = "the", H9002 = "and", H9003 = "in", H0853 = direct-object marker) is exactly what Stan's `ha'aretz → the(h1) | earth(h2)` example asked for — pre-encoded, not needing acquisition. **Specific stop-signal when about to recommend the symmetric-substrate path: "inventory the substrates" is the same failure as "acquire X." Search disk FIRST (find for TAGNT|TAHOT|stepbible|TBESG|TBESH; check `readers-*/research/`, `data/lexicons/`, `private/substrate/`), THEN frame the response.** Tooling: `readers-tanakh` already has TAHOT ingested; for any "we need richer per-word source-side tagging" question, check the `research/stepbible-*/` dirs and the `5-machinery/scripts/ingest_*` family before recommending net-new work.
