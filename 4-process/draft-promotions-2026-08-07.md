---
status: DRAFT — for Stan's review. Nothing here is applied.
---

# Draft promotions — the retraction loop's first firing

Per Stan's decision 2026-08-07: draft, do not auto-promote. Promotion writes a
permanent discipline that constrains every future session, which is a §7.1
authority question rather than a mechanical one.

**These would be the first promotions in the program's history.** Every reader
repo's log has accumulated entries since 2026-04 and not one `DISCIPLINE
PROMOTED` block exists anywhere.

---

## Correction first — I said four qualify. Two do.

On 2026-08-07 I reported that four sub-patterns had crossed the three-strike
threshold, pooling across sibling logs as [[4-process/retraction-log-protocol.md|retraction-log-protocol.md]] permits.
Extracting the actual `Sub-pattern:` fields rather than grepping for strings
shows that was wrong twice over:

| candidate | reported | actual | why |
|---|---|---|---|
| `rhetorical-figure smuggling` | 4 | **3** | one match was a block *mentioning* the phrase whose own sub-pattern is "rules that GENERATE vs AUDIT" |
| `new-rule reflex` | 4 | **3** | the 4th is the "more elaboration" variant, which is a single cascaded event |
| `whole-framework supersession` | 3 | **1** | one canon rewrite logged in three repos |
| `"more elaboration assumed = more quality"` | 3 | **1** | one retraction logged in three repos |

The two rejected candidates are the same event three times. All three
`whole-framework supersession` entries are dated 2026-05-17, share a title, and
cite **the same atu-method commits** (`f6e834a`, `82e20b8`) — differing only in
which repo's CLAUDE.md was trimmed.

## The protocol defect this exposes

[[4-process/retraction-log-protocol.md|retraction-log-protocol.md]] says: *"The 3 strikes need not all come from one
repo."* That rule was written for genuinely independent recurrences — the same
mistake made again in a different corpus, which is real evidence of a pattern.
But a **cascaded canon change is logged in every affected repo by design**, so
pooling counts *log entries* rather than *distinct events* and inflates a
single mistake up to threefold.

Left unfixed, the first serious evaluation of the threshold would have promoted
two disciplines on the strength of one mistake each — and the promotions would
have looked well-evidenced.

**Proposed protocol amendment** (needs its own ruling): strikes count **distinct
retraction events**, identified by date plus the retracted claim, not log
entries. A cascade recorded in N repos is one strike. Cross-repo pooling still
applies to genuinely independent recurrences, which is what it was for.

---

## Promotion 1 — `rhetorical-figure smuggling` (Factor A)

**Three distinct strikes, three dates, two repos:**

| date | repo | retraction | the figure smuggled |
|---|---|---|---|
| 2026-04-19 | bofm | Breath-tests retired | "breath test" as a parallel-gate diagnostic |
| 2026-04-23 | bofm | Stab-commata withdrawn | classical short-fragmentary "stab"/commata as load-bearing for J4 |
| 2026-04-25 | gnt | Three §3.7 subsections withdrawn | "bonded beats" treated as a colometric rule |

**The pattern.** A rhetorical or prosodic *figure* is observed in the text, found
salient, and then promoted into a break/merge criterion — as if noticing a
pattern licensed acting on it. Each time it was withdrawn on the same ground:
the figure constrains the candidate space, it does not determine the boundary.

**Proposed discipline.** In `memories/feedback_three_anti_default_factors.md`
under Factor A: *when a proposed rule's justification names a rhetorical or
prosodic figure — breath, colon, commata, beat, cadence, parallel member — that
naming is the warning, not the warrant. State the bidirectional-test outcome
first; if the rule survives only with the figure in the argument, it does not
survive.*

**Why it earns a promotion rather than a note.** It has already been retracted
three times across two corpora and two rule families, and it is the operative
half of the `rhetoric_bandwagon` warning — which currently tells sessions to
resist *external frameworks* but says nothing about smuggling a figure they
noticed themselves.

**Cons.** Adjacent to `feedback_rhetoric_figures_constrain_atu`, which already
says figures constrain rather than determine — a reviewer could reasonably call
this redundant. The counter-argument is that the existing memory states the
principle while this states the *detection cue*, and three retractions say the
principle alone was not enough to prevent recurrence.

---

## Promotion 2 — `new-rule reflex` (Factor B)

**Three distinct strikes, two dates, two repos:**

| date | repo | retraction | the reflex |
|---|---|---|---|
| 2026-05-14 | gnt | Bidirectional-test precedence-override withdrawn | proposed a new precedence mechanism where uniform application of R19 + J5 already covered the cases |
| 2026-05-14 | bofm | R27 extension to "so/such X that Y" withdrawn | proposed extending a rule to cover a perceived coverage gap |
| 2026-05-15 | bofm | M5 elided-predicate merge-override rejected | proposed a new §1.5 override for a five-case fragment class |

**The pattern.** Encountering cases an existing rule does not obviously cover,
the response is to propose a *new* rule rather than to check whether the
existing rule applied uniformly already covers them. All three were withdrawn
after uniform application was tested.

**Proposed discipline.** In [[memories/feedback_three_anti_default_factors.md|feedback_three_anti_default_factors.md]] under
Factor B, and as a gate refinement in [[memories/feedback_rule_proposal_gates.md|feedback_rule_proposal_gates.md]]: *before
proposing any new rule, sub-rule, override, or precedence mechanism, run the
existing rule-set uniformly over the motivating cases and report the residue. A
proposal that does not state what uniform application leaves unresolved has not
established that anything is missing.*

**Why it earns a promotion.** Factor B is already named as "new-rule reflex over
uniform-application," so the *factor* exists — what does not exist is a
mandatory pre-proposal check, and the gates are where a check becomes binding.

**Cons.** This adds real friction to every rule proposal, including the ones
where the gap is obvious, and running the rule-set uniformly is not always
cheap. It also risks the opposite failure — suppressing a genuinely needed rule
because the residue looked small — which is the over-correction that produced
the six underived §2.1 allowances from the other direction.

---

## Near-miss worth watching

`grammatical-pattern-as-rule-source` has **two** distinct strikes (2026-05-10 J6
withdrawn, 2026-05-13 compression). One short. If it recurs it promotes, and it
is the same family as Promotion 1 with grammar substituted for rhetoric.

## If approved, what happens

1. The two disciplines land in [[memories/feedback_three_anti_default_factors.md|feedback_three_anti_default_factors.md]], and
   Promotion 2 also in [[memories/feedback_rule_proposal_gates.md|feedback_rule_proposal_gates.md]].
2. A `## 2026-08-07 — DISCIPLINE PROMOTED — <name>` block goes at the top of each
   reader log, citing the triggering retractions.
3. The protocol amendment (distinct events, not log entries) gets its own ruling.
