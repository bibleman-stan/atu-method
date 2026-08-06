# ⚠ WAKE-UP DIRECTIVE — 2026-08-06 — memory-loss incident + mandate. ACT, do not summarize.

You are the atu-method session. Stan directed this briefing; it was assembled by the meta-wiki session (a sibling) after a forensic pass through your repo, your CLAUDE.md, and Claude Code's file-history. **You own the fix.** The sibling found the problem and staged the recovery; everything from here — verification, restoration, hardening, the loop documents — is your responsibility, executed under your own constitution's gates (Stan promotes; you propose).

**Ground rule for this entire file: verify-don't-recall applies to THIS DIRECTIVE.** Every claim below was made by another session. Re-verify each one against disk/git before acting on it. Where a claim fails verification, stop and surface the discrepancy to Stan instead of proceeding.

---

## 1 — What happened (verify each bullet yourself)

1. **Your memory namespace is gone.** `~/.claude/projects/C--Users-bibleman/memory/` — the ~36-file store your CLAUDE.md's mandatory orientation reads #3 and #4 point at, including `_north_star.md` ("loaded every session… never optional") and `_named_arcs.md` — does not exist. The project directory itself is deleted. *Verify: `ls` the path; grep your CLAUDE.md for `_north_star`.*
2. **The deletion predates the oldest surviving backup.** `Dropbox/claude-backups/claude-2026-07-04_0600.tar.gz` covers `.claude/projects/*/memory` for other workspaces but contains no `C--Users-bibleman` dir. *Verify: `tar -tzf … | grep C--Users-bibleman`.*
3. **The migration that would have saved it was flagged and never ran.** Your own CLAUDE.md marks those files "pending migration into `repos/atu-method/memories/`" in three places (mandatory reads #3, #4, and § named arcs), dated ~2026-06-28. The files died as an untracked single copy while the tracked destination sat ready. *Verify: grep CLAUDE.md for "pending migration".*
4. **Partial recovery succeeded.** Seven files — including `_north_star.md` (state of 2026-06-01) and the `MEMORY.md` index (@v42, 2026-06-05) — were pulled from Claude Code file-history and staged at **`.recovery-2026-08-06/`** in this repo, with provenance in `RECOVERY-MANIFEST.md`. The remaining ~29 files are likely still recoverable the same way. **file-history is prunable; recovery urgency is real.** *Verify: read the manifest; spot-check a staged file's content against what your CLAUDE.md headlines say it should contain.*

## 2 — Why it happened (the diagnosis you are inheriting)

Your ops machinery is the most mature in Stan's family of workspaces — `memories/` + index, the 8 STANDING DEFAULTS each backed by a warrant file, the retraction-log protocol with its 3-recurrence promotion threshold, the closed-routes register, the §7 change-protocol. **What it lacks is any mechanism that audits the machinery itself.** The evidence, all verifiable:

- Dead mandatory-read paths sat in your constitution for weeks with nothing to flag them.
- A three-times-flagged migration stalled ~6 weeks with nothing to surface it.
- Retraction logs exist in only 3 of 7 reader repos, all frozen since 2026-05-17; this hub repo has none of its own. *Verify: `ls ../readers-*/retraction-log.md`.*
- Most damning: **a broken-pointer detection script already existed** in the lost namespace (see manifest). The tool was built; no cadence ran it. The gap was never tooling — it was that nothing scheduled the check.
- This repo has been dormant since ~mid-June — and drift accumulates fastest precisely when nothing is happening, which is why the fix below is calendar-triggered, not activity-triggered.

## 3 — The mandate (proposed way forward; Stan has endorsed the shape — execute via your own gates)

**A. Complete the recovery and finish the dead migration (first, and soon).**
Enumerate file-history for the remaining memory files (method in the manifest); land the full recovered set in **`memories/`** in this tracked repo — the migration your CLAUDE.md already prescribes. Every recovered file keeps a provenance line: `recovered 2026-08-06 from file-history; state as of <date>; possibly stale — re-verify before relying`. **Never present recovered content as current** — a retrofitted record is an inference wearing the costume of a record. Then fix the dead paths in CLAUDE.md to point at the new tracked homes, delete the staging dir, and commit.

**B. Graft an audit tier into your CLAUDE.md (propose to Stan, then adopt).**
Two tiers, **calendar/wake-triggered** (e.g., first session of any week, and any wake after >7 quiet days — dormancy is your danger mode, so the trigger must not depend on activity):
- *Mechanical lint*: every path cited in CLAUDE.md/memories resolves; every memory file is indexed and every index entry resolves; retraction-log adoption across ALL reader repos (the spokes are in scope — you are a hub, and discipline-propagation is manual by design); staleness flags on anything unedited >60 days that claims to be live; run the recovered broken-pointer script.
- *Hostile audit*: are the 8 STANDING DEFAULTS honored in recent sessions or only on paper; is the retraction 3-recurrence threshold actually being checked; is any flagged-pending item stalled; is the constitution over its salience budget (it is ~16.7KB — measure and propose a split if the layers sort that way).
Findings convert to edits or they recur.

**C. Adopt the file-back discipline (small, high-leverage).**
Your Standing Default #5 mandates consult-prior-corpora ("how did Tanakh/GNT solve this?") — but each answer is re-derived by grepping the repos and then **dies in chat**. That is re-discovery on every question, the exact failure the knowledge-compounding pattern exists to fix. The fix without restructuring: when a cross-corpus question gets answered, **file the answer back** as a synthesis page (suggested home: `docs/synthesis/`, indexed from `canon-index.md` or its own `_index`), so the next session reads instead of re-derives. Cheap; propose the one-line constitution addition to Stan.

**D. Explicitly NOT mandated: transforming this repo into an LLM-wiki.** Stan raised and settled this with the sibling session. The reasons, so you don't re-litigate: your canon is *normative and authored* (rulings validated by gates and Stan), not *compiled from sources* — there is no raw corpus awaiting compression, and the wiki's trust mechanism (cite immutable raw, lint against it) doesn't map onto canon whose ground truth is gate results and human promotion. The failures above are operational, not structural. What IS being imported from the wiki pattern is its disciplines: the audit-or-drift bearing (B) and file-back (C).

## 4 — The study-and-author assignment (after A–C are underway)

Stan wants you to understand — and then document — your own improvement loops the way the meta-wiki documents the LLM-wiki's.

1. **Read** `C:\Users\bibleman\work\meta-wiki\wiki\compounding-artifact.md` — the wiki's virtuous cycle: per-loop Mermaid frames + ASCII, an explicit failure bearing, and honest Gap-marking of unmeasured claims. Read its sibling `C:\Users\bibleman\work\meta-wiki\wiki\ops-improvement-loop.md` too — it is the analogous exercise already done once for a log/lessons system, and its **History section records the fictions that had to be audited out** (a compound-interest analogy, a manufactured four-loop symmetry, an "internalized habit" rung impossible for a stateless agent, "convergent plateau" claims assuming fixed scope). Read those failures as a checklist of traps.
2. **Author your own loop documents** (suggested: `docs/improvement-loops.md`, or split if the material demands it) — sketching and visualizing *your actual* loops, in that house style (screen-fit Mermaid per loop + plain-text fallback):
   - the **canon amendment loop** (friction → retraction/feedback → §7 change-protocol → canon → more disciplined sessions);
   - the **retraction→promotion loop** (per-repo logs → 3-recurrence threshold → promoted discipline) — including its *observed* failure mode: logs stale since May, hub log absent;
   - the **consult/file-back loop** (currently OPEN at the file-back edge — answers die in chat; C above closes it);
   - the **audit loop** (currently MISSING — this incident is its evidence; B above creates it).
3. **Rules for that authorship, learned the hard way by your siblings**: draw the loops you actually have, not a symmetric mirror of the wiki's four; type every claim (evidenced-from-your-git/logs/incident vs. designed-but-unproven); mark "does this measurably improve the system?" as an explicit **Gap** unless you can instrument it; every diagram must show its **failure branch** (a loop you can't break is a loop you can't defend); and where a loop is aspirational, label it as such rather than drawing it as operational.

## 5 — Closing protocol

- Work through your own gates: substantive proposals to Stan before constitution edits; commits per your commit discipline.
- Log every step of this recovery in a durable, tracked place as you go (persist-first — if the session dies mid-recovery, the next wake must not need archaeology).
- When A–D are executed or explicitly queued with Stan, archive this directive (e.g., into `.archive/`) with a one-line disposition note — don't leave it at root.

*Assembled 2026-08-06 by the meta-wiki session from: your CLAUDE.md + repo state, reader-repo retraction logs, Dropbox backup tarballs, and Claude Code file-history. Every path named above was live-verified at assembly time; re-verify at execution time.*
