# Lessons

The capture buffer between a correction and a rule. Corrections land here as they
happen; **only a periodic audit promotes one into [[CLAUDE.md]] or a guard, and only
Stan ratifies.** That promotion step is the bearing — without it this file becomes
worry-beads, which is the documented failure mode of exactly this pattern.

Promoted entries move to [[CLAUDE.md]] or `5-machinery/lint/` and are struck through
here with the date and destination.

**Nothing below is promoted.** Five corrections, five candidate rules, zero
adopted.

---

## Open — captured, not yet promoted

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
`scripts/decision_log.py`; not yet general.

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
