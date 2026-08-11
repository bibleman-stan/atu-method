# Lessons

The capture buffer between a correction and a rule. Corrections land here as they
happen; **only a periodic audit promotes one into [[CLAUDE.md]] or a guard, and only
Stan ratifies.** That promotion step is the bearing — without it this file becomes
worry-beads, which is the documented failure mode of exactly this pattern.

Promoted entries move to [[CLAUDE.md]] or `5-machinery/lint/` and are struck through
here with the date and destination.

**Promotion audit run 2026-08-09** — the first time this loop has fired in the
program's history. Five captures became **two amendments, no new numbered rules**,
per the schema-budget principle that a constitution should compound discipline
without compounding length. Stan can veto either; both are behavioural rules
about my conduct, tightening existing defaults, and neither makes a scope or
precedence claim about the methodology.

| Captured | Disposition |
|---|---|
| proxy-trust · don't propose what was tried · don't architect uninventoried | **→ Standing default #7**, scope generalised from code-paths to *any artifact claim*. Displaces the old code-path-only wording. **Three captures, one amendment, net zero new rules.** |
| a detector is a claim | **→ Standing default #6**, new clause. Displaces nothing. Reference implementation `5-machinery/scripts/decision_log.py --calibrate`. |
| write the thing, not about the thing | **NOT promoted to prose — made mechanical instead.** `loop_health.py check_lessons()` now warns when captures accumulate unpromoted, which is the specific form this failure took. A rule with no trigger is a rule nobody applies. |

---

## Promoted

- ~~**[2026-08-09] Proxy-trust — verify the artifact, never a stand-in**~~ → CLAUDE.md #7, 2026-08-09
- ~~**[2026-08-09] Do not propose what the repo has already tried**~~ → CLAUDE.md #7 (same amendment), 2026-08-09
- ~~**[2026-08-09] Do not architect from an uninventoried system**~~ → CLAUDE.md #7 (same amendment), 2026-08-09
- ~~**[2026-08-09] A detector is a claim — assert both poles in the script**~~ → CLAUDE.md #6, 2026-08-09
- ~~**[2026-08-09] Write the thing, not about the thing**~~ → `loop_health.py check_lessons()`, 2026-08-09

---

## Open — captured, not yet promoted

### [2026-08-09] A multi-path `git add` fails atomically — and the commit still succeeds

`git add .gitignore private/README.md` staged **nothing**, because the README had
already been deleted from disk and git treats an unmatched pathspec as fatal for
the whole invocation. The subsequent `git commit` then captured only what a prior
`git rm --cached` had staged, `git push` succeeded, and my own output printed
"pushed". Every signal said done; the `.gitignore` change was not in `HEAD`.

Caught by chance — I ran `git show HEAD:.gitignore` while investigating something
else. **No check would have caught it**, which is the point.

**Candidate guard:** after any commit, diff the intended file list against
`git show --stat HEAD` and fail loudly on a mismatch. This is the mechanical form
of standing default #7 — the rule already covers it in principle and did not
prevent it in practice, because nothing enforced it.

### [2026-08-09] I built a detector after promoting "calibrate detectors" — and did not calibrate it

`check_private_tracked()` was written an hour after *"a detector is itself a
claim — calibrate before sweeping"* went into standing default #6. It flagged
five files as leaks. Three were; two were `!private/README.md` **negations** —
deliberate publication decisions the check would have had Stan reverse.

The miss was structural, not careless: `git check-ignore` silently skips tracked
paths unless `--no-index` is passed, so it returned nothing for the tracked files
and that reads exactly like *"no rule matches"*.

**What actually caught it** was Stan's instruction to go repo by repo, not the
rule I had just promoted. **Candidate guard:** a new checker may not be wired
into `loop_health.py` until it carries in-file pole assertions, the way
`decision_log.py` and `build_log.py` do. Remembering the rule demonstrably does
not produce the calibration.

### [2026-08-09] The COUNTS-HEADLINE gate reads a year as a count

The `Stop` discipline hook blocked an outgoing message for *"a bare integer 2023 not contextualized as a reference."* The integer was a **year** — "a 2023 transcript" — in a sentence that led with what changed, which is exactly what the rule asks for. The gate's own examples of valid context are "verse, chapter, line, word, file"; a four-digit year is not among them and so reads as a count.

**Why this is worth capturing rather than bypassing.** It is the first live test of standing default #6's new clause — *a detector is itself a claim* — and the gate fails it: no known-bad case asserts that a year must NOT trigger. Bypassing with `<!-- counts-ok: -->` would spend an override on a defect and leave it in place for every future message.

**Candidate fix:** exempt four-digit integers in `19xx`/`20xx` range, and integers immediately preceded or followed by a date-shaped token. Then assert both poles in the hook: a genuine count-headline must trigger; "a 2023 transcript" must not.

**Blast radius: hook.** Per the sequencing rule this is the tier that can block every session, so it gets fixed carefully and tested, not patched in passing. The hook also lives in `~/.claude/hooks/` — the global bucket — so the fix does not travel with the repo, which is the same defect already flagged for Gate 10.

---

*(The five captures below were promoted 2026-08-09 and are kept as the record of what the amendments were derived from.)*

## Archive — the captures behind the 2026-08-09 promotions

### [2026-08-09] Proxy-trust — verify the artifact, never a stand-in for it

Four of five errors in one session shared one cause: trusting a proxy instead of
the artifact. A shell loop's `echo` instead of `git log`. A grep over prose
instead of the structured field sitting right there. A written command instead of
a run one. My reading of an instruction instead of naming that it had two
readings.

**Candidate rule:** any state-claim about disk, git, or a live site requires a
fresh in-turn read of the artifact itself.

### [2026-08-09] A detector is a claim — assert both poles *in* the script

Four miscalibrated detectors in one day. The wikilink checker reported 0 while
the editor flagged links. The link-density metric penalised the comparator's link
style, inverting the conclusion. A USFM scan "found" 28,829 markers that were
`\n` and `\f` regex escapes matching newlines. And an audit dispatched to enforce
this very discipline reproduced that last one.

**Candidate rule:** no checker may report unless a known-good it must find and a
known-bad it must not are asserted in the file and pass. Implemented in
`5-machinery/scripts/decision_log.py`; not yet general.

### [2026-08-09] Do not propose what the repo has already tried

I proposed cross-corpus rule porting as "the single most informative experiment
available." It was run 2026-05-30 and failed — cardinality 44.1% → 44.7%, mean
Jaccard 0.6958 → 0.6879 — and recorded in [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]], a file the
proposal cited and I had not read to the end.

**Candidate rule:** before proposing an experiment, grep the canon for its name.

### [2026-08-09] Do not architect from an uninventoried system

[[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]] was withdrawn with eight false inventory claims,
including measuring HTML renderers and calling them rule code, and proposing to
design a spec system that already exists — 62 YAML specs plus `spec_runner.py`.

**Candidate rule:** an architecture claim about a component requires opening that
component in the same turn.

### [2026-08-09] Write the thing, not about the thing

Seven documents discussed "the decision record." Zero implemented one, until Stan
pointed out he had asked for exactly that days earlier.

**Candidate rule:** when a component has been described twice without being built,
the next turn builds the smallest working version.
