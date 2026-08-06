---
name: User profile — Stan
description: Stan's role, expertise, and working style for the Tanakh Reader project
type: user
---

> **PROVENANCE**: recovered 2026-08-06 from jsonl-archive (session agent-a8fc91b31a4bea456.gz, last full Write 2026-04-28); 1 later Edit call(s) NOT replayed (content may be missing those patches); possibly stale — re-verify before relying.


Stan (thebibleman77@gmail.com) is a Hebrew Bible scholar / serious enthusiast working on colometric reading editions of the Tanakh (Hebrew Bible). He has deep knowledge of Biblical Hebrew grammar, te'amim (Tiberian cantillation accents), Masoretic textual tradition, and Hebrew poetry across three accent systems (prose-book accents, *Sifrei Emet* poetic accents, and embedded-poetry-routed-prose). He maintains two Obsidian vaults (my_brain for academic work, gospel for devotional) and three reader projects (readers-tanakh for Hebrew Bible, readers-gnt for Greek New Testament, readers-bofm for Book of Mormon). He uses VS Code, GitHub Desktop, and Claude Code. He makes all final editorial decisions on colometric line breaks and is the sole authority for the Tanakh project. He commits substantive work himself and pushes to GitHub. He has extensive scholar database (100+ scholars in my_brain/01_Scholars/) and Bible book notes for all 39 Tanakh books. He works with primary sources directly: STEPBible TAHOT (Leningrad MS basis), with cross-references to OSHB, UXLC, and MAM.

**Working style:** Terse, direct. No permission loops on authorized work. Parallel-by-default when tasks decompose. Expects commits after substantive work completes, not during. Provides rationale with proposals but doesn't repeat it across follow-ups. Dislikes oversized responses, filler hedging, and false-choice framings (recommend the right thing, don't list wrong options alongside). Catches methodological drift fast — he designed the three-force model (generative, subtractive, diagnostic) and the four merge-overrides. Methodological honesty matters; cutesy deflection when caught gets called out.

**Domain focus:** Hebrew syntax (cohesion, complement integrity, syntactic parallelism), te'amim as historical evidence (not authority — they inform editorial judgment, not license breaks), atomic-thought logic (one proposition per colon), single-image tiebreakers, formula integrity. Deep familiarity with William Wickes' accent treatises, Israel Yeivin's *Introduction to the Tiberian Masorah*, Adele Berlin on Biblical parallelism, James Kugel on Biblical poetry. Active research on closed-list editorial rules and the relationship between Masoretic accent structure and colometry.

**Pet peeves / failure modes to avoid:**
- Cutesy deflection ("caught me", "good catch") when Stan corrects substance — acknowledge the issue directly.
- Sequential work when parallelization works — see [Parallel horde default](feedback_parallel_horde_default.md).
- Model-size excuses ("I can't hold the whole file") — use tool boundaries properly; abstract and summarize.
- Permission loops on clearly-authorized work (Stan says "do X" + you propose X + no block = ship it; don't ask "want me to ship?").
- Oversized responses; brevity-first always.
- Breath as an editorial criterion — te'amim literally encode Masoretic breath; breath can never be the sole deciding factor (see cannon §3, memory: [No breath criterion](feedback_no_breath_criterion.md)).
- False-choice framings between methodological honesty and expediency — the right approach wins.

**Process preferences:**
- **Agent dispatch:** Haiku for mechanical work (file moves, glob/ls, single-file reference lookups). Sonnet for scanner runs, consistency checks, template-driven updates. Opus for adversarial audits, methodology synthesis, rule design — anything where reasoning quality determines output.
- **Commit cadence:** One substantive commit per completed task; uncommitted work is at risk. Status claims come after commits land.
- **Audit discipline:** Pre-commit audit triggers per canon §7 (12 mandatory-audit patterns). Audit-skippable categories: typos, cross-reference updates, corpus edits in sweeps ≥5 instances. When uncertain, dispatch the audit (false-positive cost is small). See [Pre-commit Adversarial-Audit Discipline](CLAUDE.md#pre-commit-adversarial-audit-discipline).
- **Wrap calls:** Stan decides when to wrap — don't self-declare wrap done. Report state and ask "what else?".
- **Validator findings:** Layer 1 (generic Hebrew syntax), Layer 3 (Tanakh-specific editorial methodology). STRONG findings feed work queue; REVIEW-REQUIRED items go to per-item editorial judgment. ≥80% adoption gate governs when STRONG is trusted as Category A.

**Repo layout:** `private/01-method/colometry-canon.md` (authoritative methodology), `private/03-sessions/` (session notes + handoffs), `data/text-files/` (v0 prose / v1 te'amim-baseline / v2 editorial), `scripts/` (ingest, parse, build cascade), `validators/` (Layer 1 / Layer 3 gates), `books/` (built HTML chapters). Never edit v0 or source text; all editorial work in v2/he/.

Co-Authored-By footer: `Claude Opus 4.7 (1M context) <noreply@anthropic.com>`
