---
cssclasses:
  - wide
---

# Proposal Loop 2 — hostile critique of Proposal Loop 1

> **Plain-language version.** Loop 1 proposes a shape for the whole system and asks to be attacked from two sides: what is decoration, and what did over-simplifying throw away. This is that attack. The short answer: the *diagnosis* in Loop 1 is largely sound and mostly survives; the *design* does not, because the one thing it claims makes gains spread — a single store checked against immutable sources — is not true of this project. The instrument that is supposed to supply the outside check is our own output measured against our own output on a better parse. And the headline number that justifies its top-ranked change cannot be reproduced from the file it cites.

**Status: CRITIQUE. Written 2026-08-08.** Target: [[4-process/proposal-loop-1.md|proposal-loop-1.md]] as committed at `cea9913`. Every claim below carries a pasted receipt or is labelled PLAUSIBLE.

**Labels.** CONFIRMED = I ran the command / read the line this turn. PLAUSIBLE = reasoned from confirmed facts, not directly observed.

---

## F1 — FATAL. The "checkable against sources" premise fails: the Isaiah oracle is canon-vs-canon

Loop 1's diagram labels the LINT→CANON edge **"vs RAW, never canon-vs-canon"** (line 56) and rests its whole compounding claim on segmentation being checkable against sources. Its companion states the strong form:

> `4-process/compounding-vs-additive.md:111` — "This is precisely why the Isaiah oracle matters: it is calibrated in Hebrew syntax, **outside our own judgment** — and precisely why the gold yardstick cannot referee, since it shares the bar's calibration."

**CONFIRMED — the oracle's "gold" is our own published output, not a source.**

```
$ head -60 c:/Users/bibleman/repos/readers-bofm/5-machinery/scripts/isaiah_oracle.py
TANAKH = Path(r"C:\Users\bibleman\repos\readers-tanakh\data\text-files\v2\eng-kjv")
...
We PROJECT the gold KJV-Isaiah ATU line-breaks through the diff onto the BoFM wording
```

And that directory is generated, not sourced:

```
$ head -25 c:/Users/bibleman/repos/readers-tanakh/scripts/regenerate_english.py
regenerate_english.py — KJV-verbatim English extractor (Tanakh).
This is the canonical English-layer generator.
...
For each Hebrew token in v2/heb, the universal algorithm finds the KJV words in the
same verse whose Strong's match, distributes them to the right ATU cola
```

The cola are **atu-method's own binding-rule output over `v2/heb`**. So the oracle compares atu-method-on-BoFM against atu-method-on-Tanakh. Same criterion ([[1-method/framework.md#§2.1 The bidirectional test (primary criterion)|framework.md §2.1]]), same rule family, same author — *different substrate*. What the oracle isolates is a **parse-quality differential**, which is real and useful, and is not an external arbiter.

Held against the source Loop 1 cites for the requirement:

> `meta-wiki/wiki/lint-workflow.md:37` — "Two wiki pages disagreeing tells you *that* something is wrong; only the sources tell you *which* page is wrong."

Under that rule the oracle tells us Tanakh and BoFM disagree. It does not tell us which is right. BHSA is a *syntactic treebank*, not an ATU segmentation; the ATU boundaries are normative and ours. Loop 1's own flagged worry ("Hebrew-anchored gold is not English ground truth") is *narrower* than the real problem: it is not English ground truth **and it is not ground truth in Hebrew either** — it is our own product on a better parse.

**What breaks, and when.** The moment change #2 runs. The English bidirectional filter adjudicates candidates produced by our own criterion using our own criterion. Loop 1's companion already concedes it — `2-evidence/finding-substrate-loop-diagnosis.md:75`: "The filter's judge is the same instrument whose calibration is in question." Both ends of the loop are inside the system. That is the exact structure the project rejects elsewhere ("the gold yardstick cannot detect a systematically coarse bar because the gold shares the bar's calibration").

**What this does NOT kill.** RAW is genuine for *substrate*: BHSA, Macula, the UD treebanks are external and immutable, and improving the parse is a real RAW→CANON edge. The claim that dies is the one Loop 1 needs — that **segmentation claims** are source-checkable, and therefore that LINT can arbitrate CANON. Delete the "vs RAW, never canon-vs-canon" label and the LINT organ has no arbiter.

**Severity: FATAL** to the design as argued. The correct salvage is narrower: name the oracle a *substrate-differential instrument*, admit it is canon-vs-canon with a parse gradient, and stop claiming an external arbiter the project does not have for English idea-units.

---

## F2 — FATAL. The propagation table is a restatement, not a mechanism — and its one testable row is refuted inside this repo

Loop 1 says the design "lives or dies" by §"How an improvement at any point carries through" (line 94). Read the middle column: every "because" clause is a paraphrase of the left column.

| Loop 1's claim | What it actually says |
|---|---|
| RAW propagates "because every clause atom is derived from it" | *RAW is upstream* |
| CANON propagates "because every future question starts from it" | *CANON is the store* |
| LINT propagates "because it guards the store every other organ writes to" | *LINT checks the store* |
| SCHEMA propagates "because it governs the agent performing all four operations" | *SCHEMA governs the agent* |

None of these is a mechanism. Each is the definition of the node restated as a consequence.

**CONFIRMED — the one row with data refutes it.** The CANON row claims an integrated finding propagates because future questions start from it. The same author measured the opposite yesterday, and it is *still* true today, after Loop 1 was written:

```
$ grep -in "isaiah\|0.561" 2-evidence/framework-claim-inventory.md
$ echo "exit=$?"
exit=1
$ grep -in "isaiah" 3-implementation/substrate.md
51:(Lesson: the BoFM-Isaiah oracle — Hebrew-anchored KJV breaks are a diagnostic, not a deploy template.)
```

The Isaiah divergence finding (`2-evidence/finding-isaiah-cross-corpus-divergence.md`, present on disk, 4,055 bytes) has **zero** reach into the claim inventory and one unrelated mention in [[3-implementation/substrate.md|substrate.md]]. Both files are inside the single store. **Gains get trapped inside the one store**, which is precisely what line 18 says a single store makes impossible:

> `4-process/proposal-loop-1.md:18` — "A loop with few parts and one shared store has nowhere for a gain to get trapped."

**The circularity.** Propagation does not come from the topology; it comes from change #1 (mandatory same-turn cross-page revision). But change #1 is *ranked and justified by* the propagation table. The design's virtue is supplied by an added discipline, and the discipline is justified by the design. Remove #1 and the table is false — as demonstrated above, in this repo, today.

**What breaks, and when.** Immediately, as an argument: the propagation table cannot be used to rank changes or to sort "real improvement" from "local repair" (line 103), because it does not discriminate. Every change any of us would ever propose sits somewhere in RAW/CANON/LINT/SCHEMA, so the "diagnostic this gives us for free" classifies everything as an improvement.

**A concrete non-propagating improvement at RAW** — CONFIRMED. [[CLAUDE.md]] § Repo map lists six reader repos, each with its own substrate; the standing tactical line says "each project's data lives in its own repo's `private/substrate/`". A UD correction to `readers-bofm/data/parses/v0-cache-conllu/` improves BoFM's atoms and reaches **nothing** in Tanakh, GNT, LXX, Vulgate, or Revelation — parses do not port. RAW is in fact the *most* corpus-local of the four entry points, and the table lists it first as though it were the broadest.

**Severity: FATAL** to §"How an improvement at any point carries through" as written.

---

## F3 — SERIOUS. "Sub-agents supply the independence I cannot" is false as implemented, and I am the receipt

Loop 1, line 117: "**Sub-agents — the independence I cannot supply.** … *scheduled semantic lint* (fresh context, adversarial, reading from files alone…)."

**CONFIRMED, first-person.** I was dispatched as exactly that adversarial sub-agent. My system prompt contains, verbatim, a `claudeMd` block carrying `~/.claude/CLAUDE.md`, `c:\Users\bibleman\CLAUDE.md`, **and** `c:\Users\bibleman\repos\atu-method\CLAUDE.md` in full — including the eight standing behavioural defaults and this line:

> "## Closed routes / banked-gold / settled tactical — **DO NOT re-litigate** … If something here looks reopenable, it isn't."

Fresh context is not independence when the context is re-seeded with the author's constitution and an explicit instruction not to reopen its settled conclusions. The auditor inherits the priors, the vocabulary, the red lines, and the list of questions it is told not to ask. `28,875` characters of shared prior arrive before the first file is read (F9).

**The design contains this contradiction explicitly.** The SCHEMA row of the propagation table claims schema improvements reach "*every* subsequent operation, forever." LINT is one of those operations. So the design simultaneously requires that SCHEMA govern LINT (for compounding) and that LINT not share the author's priors (for independence). Both cannot hold.

**What survives.** The *author-blindness* argument is sound and well-sourced — `meta-wiki/wiki/lint-workflow.md:30` records a fresh-context sweep finding 11 standing inconsistencies the authoring lints passed over. But that same line carries a caveat Loop 1 drops: the sweep "produced one false positive itself, so auditor findings are verified against ground truth before fixing, never applied on trust." Loop 1 says only "Both require pasted receipts," which is not the same control.

**What breaks, and when.** The first time a sub-agent lint is used as the sign-off on a canon change. It will reliably catch *cross-reference* drift (mechanical, priors-independent) and reliably miss anything the schema pre-frames — which is every settled decision, every closed route, and the whole additive/compounding taxonomy.

**Severity: SERIOUS.** Recoverable by narrowing the claim: sub-agents supply *fresh attention*, not independence. Real independence in this system is Stan, the wiki session, and external instruments — which `4-process/collapsed-maturation-loops.md:116` already said correctly and Loop 1 weakened.

---

## F4 — SERIOUS. The headline number is not in the file it cites, and the comparison is metric-incommensurable

Loop 1, line 127: "Measured: **5.54 links per page against the meta-wiki's 12.85.**"

**CONFIRMED — 5.54 appears nowhere in the recorded series.** The instrument's own committed output, from the very commit whose message quotes 5.54:

```
$ git show b44cc99:2-evidence/growth-data.csv
date,pages,words,links,links_per_page,words_per_page,targets,orphans,buffer_pages,buffer_links_per_page,schema_chars
2026-08-08,62,118130,356,5.74,1905,77,0,36,3.03,18410
```

Recorded: **62 pages, 5.74, 1,905 words/page.** Prose (both in Loop 1 and in `compounding-vs-additive.md:70-77`): **61 pages, 5.54, 1,907**. Re-run now: **63 pages, 5.79** (and one orphan — [[4-process/proposal-loop-1.md|proposal-loop-1.md]] itself).

That is a small error. The next one is not.

**CONFIRMED — the two sides of the comparison are computed by different metrics, and the sign of the result depends on which you pick.** `scripts/growth_snapshot.py:50-51,62-67` counts wikilinks **and** markdown links but only when the target ends `.md`. `meta-wiki/admin/growth-snapshot.py:17,28` counts wikilinks only, with **no** extension filter. The meta-wiki writes `[[drift]]`, not `[[drift.md]]`. Applying each metric to both corpora:

```
corpus           metric        pages  words   links  links/page  w/page
meta-wiki        MW(wikilink,any)     50   28983    642      12.84     580
meta-wiki        ATU(.md-only)        50   28983    198       3.96     580
atu-method       MW(wikilink,any)     63  120405    163       2.59    1911
atu-method       ATU(.md-only)        63  120405    365       5.79    1911

meta-wiki wikilinks total=642  ending in .md=198  (31% survive atu's .md filter)
```

Under the meta-wiki's metric, atu-method is at **20%** of it. Under atu-method's *own* metric applied symmetrically, atu-method is **46% higher** than the meta-wiki. The stated "43% of theirs" is neither; it is a ratio of two incompatible measurements.

**Calibrating my own detector, per the corpus's own rule** (`lint-workflow.md:52` — "when a scan says most of the wiki is broken, suspect the scan"): neither cross-application is fair either. A neutral metric — every internal link, both syntaxes, no extension filter, both corpora:

```
meta-wiki    pages=  50 words=  28983 links=  642 links/page=  12.84 links/1000words=22.15
atu-method   pages=  63 words= 120405 links=  415 links/page=   6.59 links/1000words= 3.45
```

**So the direction survives (51%, not 43%) and the magnitude does not.** Per 1,000 words the gap is 6×, not 2× — because links-per-page conflates density with page length, and the corpora differ enormously in page length: meta-wiki median **413.5** words/page with **24 of 50** pages under 400 words; atu-method median **1,827**, only **5 of 63** under 400. Half the meta-wiki is short ingest notes. Loop 1 concedes "some of the page-length gap is genre" and then treats the ratio as evidence anyway.

**What breaks, and when.** Change #1 is ranked first on this number. A number that moves between 20% and 146% under defensible metric choices cannot rank anything.

**Severity: SERIOUS.**

---

## F5 — SERIOUS. The metric that is supposed to falsify the compounding claim is guaranteed to rise if change #1 is adopted

`growth_snapshot.py:15-19` states predictions "so this instrument can be WRONG": compounding → links/page rises.

Change #1 mandates that filing a finding include revising the pages it touches, in the same turn. A revision that references a finding **adds a link**. The link counter is a bare regex with no weighting (`growth_snapshot.py:62-68`). Loop 1 already anticipates the degenerate case at line 145: "a mandatory cross-page edit invites cosmetic edits that satisfy a checker and integrate nothing." A cosmetic edit that adds one wikilink moves the metric by exactly as much as a genuine integration.

So: the intervention mechanically produces the signal that is supposed to test it, and the failure mode the author names produces the same signal as success. **PLAUSIBLE→CONFIRMED** (the mechanism is confirmed from the script; that it *will* be gamed is plausible).

**What breaks, and when.** Row 2 of the series. Density rises, "compounding" is declared, and nothing has been learned. The prediction is unfalsifiable in practice while presented as the project's one falsifiable claim.

**Severity: SERIOUS.** The fix is not in Loop 1: measure something the intervention cannot directly write — e.g. whether a *later* question was answered from the store without re-derivation.

---

## F6 — SERIOUS. Change #2 is scoped to a number measured against a fabric that no longer exists

Loop 1, line 128: "a `Workflow` over the ~503 Isaiah over-merge candidates."

**CONFIRMED — the number is real, and it is stale.**

```
$ grep -n "0.561" memories/operational/project_bofm_substrate_quality.md
45: … built 2026-05-27 … deployed fabric vs gold break F1 = 0.561 (prec .750 / rec .448);
    fn=503 over-merges >> fp=136
```

But the deployed fabric changed substantially *after* that measurement, in exactly the books the gold set covers (1 Nephi, 2 Nephi, Jacob, Mosiah):

```
$ cd readers-bofm && git log --format="%h %ad %s" --date=short --since=2026-05-27 -- data/text-files/v2
d9c98df 2026-06-03 BoFM book-audit final coverage — 1 Nephi + 2 Nephi + Jacob
09f2834 2026-06-03 consolidated ship — 150 lever-2 UD edits + 87 book-audit overrides
23e9b01 2026-06-02 Mosiah book-audit — 22 ATU defects fixed
ad09219 2026-06-02 Jacob book-audit — 15 ATU defects fixed
2514995 2026-06-02 2 Nephi book-audit pilot — 30 ATU defects fixed
   … 7 more
```

`finding-substrate-loop-diagnosis.md:48` documents the same waves ("482 gated edits, then waves of 334 / 327 / 216 / 131 / 42 / 37, then 150 lever-2 edits") without noticing that they invalidate the 503.

**CONFIRMED — the cheap first step is absent from Loop 1:**

```
$ grep -in "re-run\|re-measure\|rerun" 4-process/proposal-loop-1.md
exit=1
```

`isaiah_oracle.py --measure` exists and takes minutes. Loop 1 proposes ~503 units of agent adjudication before re-running it.

**A second gap in the same item.** [[CLAUDE.md]] § Default decisions: "Applying a BIND / merge — Over-merge = Stan's RED LINE … ≥2 parallel adversarial audits (over-merge + atomicity lenses) BEFORE applying"; default #2's canonical shape is `pipeline(candidates → parallel adjudicate → ≥2 parallel audits) → gate → HALT`. Loop 1 item 2 names the adjudicate stage and omits the audits and the gate. Word counts in the whole document: `audit` **1** (in an unrelated sentence at line 105), `hook` **1**, `over-merge` **1**.

**What breaks, and when.** Dispatch day: a fan-out priced against a fabric ~10 corpus-changing commits out of date, with the repo's own mandatory audit gate unmentioned.

**Severity: SERIOUS.**

---

## F7 — SERIOUS. What over-simplification threw away, part 1: the enforcement layer

This is the direct answer to the brief's second question, and it is the clearest loss.

The document Loop 1 replaces had mechanical countermeasures. `4-process/collapsed-maturation-loops.md:63,134-138`:

> "a commit-message gate that *refuses* a canon-touching commit lacking a §7.5 declaration. Mechanical, not self-reported."
> "**Post-condition verification** — after a commit, assert against `git log`/`status`. A `Stop` hook can enforce it"
> "**Documented-command execution** — a check that every fenced command in a skill or doc actually runs."
> "**Cascade enumeration without a skip list**"

**CONFIRMED — none survives into Loop 1.** All five ranked changes are text: a discipline (#1), a build (#2), a schedule (#3), a budget (#4), a measurement (#5). Not one is a gate.

The corpus Loop 1 grounds itself in says this is the wrong direction:

> `meta-wiki/wiki/schema-layer.md:21` — "'Enforcement works best at the agent boundary, not the conversation boundary' — PreToolUse hooks on the agents that actually mutate files … **'Rules-as-text fail under cognitive load; hooks don't'** … the schema layer splits in practice into instructions (cheap, advisory) and enforcement (hooks/validators, structural)."

Loop 1's change #1 is a rules-as-text intervention aimed at the failure mode the same corpus says rules-as-text cannot hold. Its own line 145 predicts the outcome ("invites cosmetic edits that satisfy a checker") and it ships anyway, ranked first, described as costing nothing.

**"Costs nothing" is also wrong on its face** (line 127). Mandatory same-turn revision of every page a finding touches is unbounded work on a store whose median page is 1,827 words. And it has not been done even once in this session: F2's grep shows the Isaiah finding still unintegrated into [[2-evidence/framework-claim-inventory.md|framework-claim-inventory.md]] after two documents diagnosed exactly that.

**Severity: SERIOUS.** The collapse removed the only parts of the prior draft that could not be forgotten.

---

## F8 — SERIOUS. What over-simplification threw away, part 2: the additive/compounding distinction, per organ

Loop 1 flags the risk itself (line 22, line 142). It is a real loss, and here is the mechanism.

`compounding-vs-additive.md:122` had established the per-loop labels: loops 1, 2, 4 **additive — "they plateau, and the plateau is success"**; loops 3, 5, 6 and the substrate loop **compounding if and only if they integrate**. Line 128 states why it matters: "an additive loop that has closed most of its error classes is *finished*, and pushing it looks like diligence while buying nothing … The two failures are indistinguishable from inside and have opposite fixes."

**Three organs have nowhere to carry that label, and the propagation table asserts the opposite of it.** Every row claims unbounded downstream lift. LINT is exactly the ops loop the source calls additive:

> `meta-wiki/wiki/ops-improvement-loop.md:55` — "each closed error-class is independent — closing one does not make the next cheaper or the agent broadly smarter, it just removes that one failure. So reliability **adds up; it does not accelerate.**"

Loop 1's LINT row asserts "every future deposit is checked; errors stop being amplified; **and its findings are generative**." Those are two organs wearing one name: the *guard* function is additive and plateaus; the *generative* function is compounding. Fusing them means you cannot tell whether more lint is investment or diligence-theatre — which is the failure `compounding-vs-additive.md:128` says is indistinguishable from inside.

**The same fusion hides the ranking question.** If LINT-as-guard is additive and near its plateau (0 broken anchors, 0 orphans before this proposal), change #3 buys reliability, not rate — and should not be ranked above change #5, the one experiment that would tell us whether *anything* here compounds.

**Severity: SERIOUS. The collapse is a genuine loss, not a tidy-up.**

---

## F9 — SERIOUS. "Three organs" does not match the document's own four entry points, and it drops the layer the corpus calls most load-bearing

| Element | Organ (line 35-39)? | Entry point (line 96-101)? | Node in the diagram? |
|---|---|---|---|
| CANON | yes | yes | yes |
| LINT | yes | yes | yes |
| **LOG** | **yes** | **no** | yes |
| **RAW** | **no** | **yes** | yes |
| **SCHEMA** | **no** | **yes** | **no** |
| EDITIONS / STAN | no | no | yes |

Three sets, three different memberships, presented as one design. SCHEMA — which Loop 1 itself calls "the interest rate, which is why practitioners rank the schema above any content page" — is not an organ and is not in either diagram.

The source has already adjudicated this exact question, and against Loop 1:

> `meta-wiki/wiki/three-layer-architecture.md:27` — "The count three is load-bearing on **one axis only: the trust/ownership gradient** … A genuine fourth layer would need a new position on that axis — a new owner or a new trust status."
> `:35` — "**Orthogonal axes — not strata at all**, and flattening them into the layer count would blur the trust gradient the model exists to carry."

LOG/LINT/CANON is a *function* axis. Loop 1 takes the number three from a trust-gradient model, applies it to a function partition, and drops the third member of the original (schema). The count is inherited decoration, not structure.

**And "three files and three verbs" (line 18) misdescribes the source.**

```
$ cd meta-wiki/wiki && grep -rn "three files" .
./source-milo-ai-os.md:13:  … The maps layer holds three files:
$ grep -rn "three verbs" . ; echo "exit=$?"
exit=1
```

The only "three files" in the corpus belongs to an unrelated adjacent source (Milo's PKM model). Karpathy's is **three layers** — a `raw/` directory, a `wiki/` directory, and one schema file — and **three operations** (`source-karpathy-02.md:21-22`). Since the entire design criterion is read off that sentence ("that is not minimalism for taste — it is why an improvement propagates"), getting it wrong matters.

**Severity: SERIOUS** for the mismatch; **MINOR** for the misquote on its own.

---

## F10 — SERIOUS. The design was already adopted in a sibling repo, uncited, and Loop 1 rests on a "verified" line that is now false on all three counts

Loop 1, lines 72 and 111, present as its own contribution: the wiki upstream and write-protected; `findings/` is a hole and closing beats legalising; a measurement of publication rigor graduates into `raw/`, "gated by Stan, needing no exception"; and this "gives the findings→canon edge an owner, which today it lacks."

**CONFIRMED — all of it is already written, adopted, and staged for ratification in the wiki:**

```
$ sed -n '1,40p' c:/Users/bibleman/work/atu-nlp-wiki/admin/maturation-loops.md
## How field-results reach the theory — the layered model (chosen over a `findings/` exception)
A `findings/` folder inside the wiki was considered and **rejected** …
- **atu-method is the workshop.** … atu-method has **read-only access** to the wiki's theory
  and is the loop-end on the measuring/modifying side.
- **`raw/` is the graduation home.** A measurement that matures to *publication rigor* can be
  admitted to `raw/` by the human as an immutable source … **no exception needed**
```

**CONFIRMED — atu-method's own record of the sibling's state is wrong on every clause.**

```
$ sed -n '19p' Pending-Decisions.md
Verified 2026-08-08: `findings/F-001-marschall-1ne3.md` is still present,
`admin/maturation-loops.md` was never created, and the wiki's `Pending-Decisions.md`
still carries only the original "codify `findings/` or leave it a pilot?" question.
```

Against ground truth this turn:

```
$ ls c:/Users/bibleman/work/atu-nlp-wiki/findings/
ls: cannot access '.../findings/': No such file or directory
$ ls c:/Users/bibleman/work/atu-nlp-wiki/admin/
conventions.md  debates.base  ingest.md  learnings.md  lint.md  maturation-loops.md  sources.base  visual-assets.md
$ sed -n '9,11p' c:/Users/bibleman/work/atu-nlp-wiki/Pending-Decisions.md
### [2026-08-08] Promote the `raw/`-graduation principle for findings into the constitution
**Status:** Approved in substance (2026-08-08). Awaiting your **hand-promotion** into `CLAUDE.md`
```

`findings/` is gone. `maturation-loops.md` exists. The wiki's pending question is the *resolved* one. Loop 1 cites neither file:

```
$ grep -n "maturation-loops\|Pending-Decisions" 4-process/proposal-loop-1.md ; echo "exit=$?"
exit=1
```

**Three consequences.**

1. A verify-don't-recall failure of exactly the class the proposal exists to fix, in the paragraph that assigns the wiki its role — the third instance today, after the two Loop 1 already confesses.
2. `improvement-loops.md:259` is now stale ("That vault now carries a pilot `findings/` class") — live cross-reference drift, uncaught, in the document that catalogues drift.
3. **It corrupts the project's independent-convergence evidence.** `collapsed-maturation-loops.md:97` treats "separate sessions reached the same conclusion with no coordination" as evidence. Restating a sibling's adopted design without citation converts a *read* into an apparent *convergence*. That is the one currency this project says it cannot manufacture.

**Severity: SERIOUS.**

---

## F11 — MINOR→SERIOUS. "Their prose can thin; their gates cannot" — the two events are unrelated, and two reader gates are already not controlling

Loop 1, line 119: "On 2026-08-08 `readers-bofm`'s pre-commit hook blocked a commit of mine while `atu-method`'s own checker reported clean with 103 citations dangling."

**CONFIRMED — the two gates check disjoint things, so the pair cannot support the inference.**

```
$ head -20 readers-bofm/.git/hooks/pre-commit
RELEVANT=$(git diff --cached --name-only | grep -E "^(data/text-files/v2/|1-method/colometry-canon\.md|1-method/pericope-canon\.md|5-machinery/validators/)" || true)
if [ -z "$RELEVANT" ]; then exit 0; fi
… python3 5-machinery/validators/run_all.py --baseline-check
```

It fires only on staged BoFM corpus/canon/validator paths and blocks only on validator-count regressions vs a baseline. It has **no** ability to see a dangling citation, and no jurisdiction in atu-method. "Gates I did not author catch me; gates I authored do not" is two unrelated events narrated as a controlled comparison.

The 103 figure itself is CONFIRMED only as a repeated self-report — `collapsed-maturation-loops.md:77,126` and `2-evidence/PROJECT-BRIEF-2026-08-08.md:90`, all the same author, no primary artifact. Treat as PLAUSIBLE.

**And the load-bearing condition is already failing.** Running the LINT organ this turn:

```
$ python scripts/loop_health.py --brief
  - readers-gnt: baseline 2026-05-21 predates newest corpus/parse commit 2026-06-13 — the gate has stopped controlling
  - readers-tanakh: baseline 2026-06-02 predates newest corpus/parse commit 2026-06-13 — the gate has stopped controlling
  - readers-lxx / readers-vulgate / readers-gnt-morph / rev-reader: no retraction-log.md
  - retraction->promotion loop has NEVER fired
  - full audit never recorded; 188 recent moves
```

Two of the three "independently authored gates" the design declares non-negotiable are **already not controlling**, and four repos have no log at all. `collapsed-maturation-loops.md:146` calls strong reader gates "the condition that decides whether this is safe." Loop 1 asserts the condition holds; the repo's own instrument says it does not.

**Severity: SERIOUS** for the unmet precondition; MINOR for the rhetorical pairing.

---

## F12 — MINOR. "One store" is false, and the schema budget is scoped to a third of the schema

**"One store."** LOG is defined (line 37) as "git history · retraction logs · `2-evidence/growth-data.csv`" — the retraction logs live in `readers-bofm`, `readers-gnt`, `readers-tanakh`; RAW spans `biblical-corpora`, six `private/substrate/` trees, and the wiki's `raw/`; EDITIONS are six repos. That is ten-plus physical stores. Only CANON is one directory, and F2 shows gains trapped inside even that. **CONFIRMED** from [[CLAUDE.md]] § Repo map + the `loop_health` output above.

**The schema budget.** `growth_snapshot.py:97` measures `REPO/CLAUDE.md` only. Three files actually load in an atu-method session:

```
4731   c:/Users/bibleman/.claude/CLAUDE.md
5734   c:/Users/bibleman/CLAUDE.md
18410  c:/Users/bibleman/repos/atu-method/CLAUDE.md
```

**28,875 chars**, not 18,410. A metric scoped to one file is gameable by moving text up a level, with no reduction in rate. The comparator is also stale and cherry-picked: the meta-wiki's constitution is **10,353** chars today (`mtime 2026-07-30`), not the 9,497 of its 2026-07-18 row, and it excludes only the user-home file (`meta-wiki/.claude/settings.json` → `claudeMdExcludes`), so its real stack is ~15,084. Honest ratio 1.91×, not 1.94× — the *conclusion* survives; the numbers cited do not.

**And the exemplar fails the same charge.** Loop 1 line 130 indicts ours as "growing monotonically." The meta-wiki's budgeted constitution: `6,647 → 7,810 → 8,879 → 9,497 → 10,353` (`meta-wiki/admin/growth-data.csv` + current size). Strictly monotonic, +56% in two weeks. Monotonic growth is not the discriminator; *what displaces what* is — which is the rule Loop 1 correctly names and then argues from the wrong evidence.

**Severity: MINOR** individually; jointly they mean change #4's evidence base is wrong in scope, in comparator, and in discriminator.

---

## F13 — MINOR. The wiki is not "upstream of RAW" — it consumes the same RAW

Loop 1, line 72: the theory wiki "sits *upstream of RAW*". Its RAW node (line 44) reads "BHSA · Macula · **Skousen · Marschall**".

```
$ ls c:/Users/bibleman/work/atu-nlp-wiki/raw/ | grep -i "skousen\|marschall\|chafe"
Chafe-1988.pdf  Chafe-1994.pdf  Marschall-2020.pdf  Marschall-2020a.pdf  Marschall-2024.pdf  Skousen-2009.pdf
```

**CONFIRMED**: Skousen, Marschall and Chafe are literally files in the wiki's `raw/`. The wiki is a *peer consumer* of part of the RAW node, not upstream of it. The diagram's one topological assertion about the wiki is wrong, and it matters for F10's graduation edge: a finding graduating into the wiki's `raw/` lands *inside* the proposal's RAW node, making the loop closed rather than open.

**Severity: MINOR** (drawing error) with a **SERIOUS** knock-on: the RAW node is not immutable-and-external if findings can be promoted into it.

---

## F14 — MINOR. Decoration

Applying Loop 1's own drop test ("removing it loses nothing but the part"):

- **The duplicate ASCII diagram (lines 63-70).** It renders the same six nodes and seven edges as the Mermaid block above it. Same in [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]], [[4-process/improvement-loops.md|improvement-loops.md]] (×7). **Drop.** *Caveat: PLAUSIBLE that it is a deliberate degraded-terminal fallback; if so, say so once in the schema rather than paying it per diagram.*
- **§"The three organs — and the RAG connection" (lines 78-88).** Three paragraphs mapping the organs onto RAG's failures. Nothing downstream depends on them; every operational claim in them is restated in the propagation table. It is motivation, not mechanism. **Drop or demote to one line.**
- **"One circulation. Three organs. One store."** Two of the three are false (F9, F12).
- **Circled edge numerals ①-⑤ with `linkStyle` colour assignments.** Referenced exactly once, at line 116 ("I perform ①②④ and dispatch ⑤"). Naming the edges in prose costs less than a colour key.
- **Its own broken links.** `python scripts/check_broken_pointers.py` → 4 broken wikilinks, all in `proposal-loop-1.md:10,27,139`, to `proposal-loop-2.md` and `proposal-loop-3.md`. Forward references to unwritten documents; -3 stays broken after this file lands.

**What is NOT decoration and should be kept:** §"What this is most likely to have wrong." Pre-registering six falsifiers is the strongest thing in the document — four of them (F1, F4, F8, F3) turned out to be the real defects. Keep that section in every future proposal.

**Severity: MINOR.**

---

## F15 — MINOR. Unfalsifiable claims

Flagged as required. Each could be true; none could be shown false as stated.

| Line | Claim | Why it cannot fail |
|---|---|---|
| 8 | "an improvement anywhere must make the whole loop better" | no defined measurement of "the whole loop" |
| 18 | "few parts and one shared store has nowhere for a gain to get trapped" | F2 exhibits a trapped gain in the one store; the claim absorbs it |
| 96-101 | the four "It propagates because" clauses | definitions restated as consequences (F2) |
| 101 | "SCHEMA … *every* subsequent operation, forever" | no instrument connects schema text to any outcome |
| 103 | "Most of what we have shipped in the last three days is local repair" | "local repair" has no test; self-deprecation is not a measurement |
| 105 | "Symmetry is the point" | asserted, not derived; the failure directions are not measured |
| 119 | "Their prose can thin; their gates cannot" | normative, and F11 shows the descriptive half already false |
| 127 | "the difference between depositing and earning" | metaphor doing the work of a criterion |
| 27 | "A design is finished when every remaining part fails the drop test" | no procedure for running the drop test; F14 had to invent one |

---

## F16 — Omissions

Ranked by what they cost.

1. **Page compaction — the direct fix for the one signature Loop 1 actually measured.** `growth-curve.md:15` names rising words-per-page as the append-only trap; ours is 1,911 and it is the largest gap in the data. `drift.md:40` gives the countermeasure: "**Compaction** — mutable-current/append-only-history page structure with line budgets." Loop 1 budgets only the schema. `grep -oi "compaction\|words per page\|words-per-page" proposal-loop-1.md` → **0, 0, 0**.
2. **Closable output — `lint-workflow.md`'s element 5.** "A lint whose findings don't convert to edits is a status report, and status reports rot" (`:41`). Loop 1's LINT produces reports with no closure mechanism. Live proof: `loop_health.py --brief` currently reports "full audit never recorded; 188 recent moves" and has been reporting the never-fired retraction loop for days.
3. **Drift variants 2, 3, 5, 6.** `drift.md:18-22`. Loop 1's LINT addresses variant 1 only. Variant 2 is the one that indicts this design directly — "health checks pass because they compare summaries against each other, never against originals" is a precise description of F1. Variant 6 (quote-smoothing) has a named countermeasure, the quote-locator; `grep -oi "quote-locator\|provenance" proposal-loop-1.md` → **0, 0**.
4. **Detector calibration by fault injection.** `lint-workflow.md:51` — "Assert both poles as executable assertions *in the script*." `compounding-vs-additive.md:105` ports this as insight (d) and Loop 1 drops it, while F4/F5 show its two instruments are miscalibrated. `grep -oi "fault.injection" proposal-loop-1.md` → **0**.
5. **The reader loop is folded back into an arrow.** `grep -oi "reader-observations\|Loop 6\|comprehension" proposal-loop-1.md` → **0, 0, 0**. `improvement-loops.md:296` calls it "the loop whose absence costs most," and `:244` records the correction Loop 1 has just undone: "**Findings are a node, not an arrow — that is the correction.** Drawn as an arrow label, the diagram could not show that a finding has *two* destinations and that only one of them is wired." Loop 1 draws reader experience as edge ③④ and it disappears — the same drawing error, one document later.
6. **A cost model.** Five changes, no estimate for any. ~503 adjudications, mandatory cross-page revision on 63 pages averaging 1,911 words, scheduled sub-agent lint. `compounding-artifact.md:125` grounds the whole pattern on maintenance being near-free; nothing here checks that this project is in that regime.
7. **`drift.md:32` — the young-vault confound.** "below those thresholds, absence of drift is expected even with NO countermeasures — so a young wiki's clean lints are weak evidence that its loops work." Loop 1 compares a one-row atu-method series against a six-row meta-wiki series (both under a month old) and reads a direction off it. The source explicitly forbids that read.

---

## What survives

Stated honestly. These I could not knock down.

- **Author-blindness is real and correctly diagnosed.** Independently sourced (`lint-workflow.md:30`, twice in that vault) and independently instantiated here: `f7b18e6` filed the substrate finding at **12:03:27**; `b44cc99` corrected the Gap it refuted at **19:37:42** — **7h34m**, and only because Stan pushed a different question. Semantic checking by the author of the edits does not work. What fails is the proposed *remedy* (F3), not the diagnosis.
- **F1 0.561 / precision .750 / recall .448 / fn=503 / fp=136 is a genuine, hard, direction-bearing measurement**, verbatim in `project_bofm_substrate_quality.md:45`. Its interpretation (F1) and its currency (F6) are both wrong; the measurement is not.
- **Over-merge is the dominant defect direction.** 503 : 136 is a 3.7:1 asymmetry replicated on a second book (Malachi, 0.591). Whatever the arbiter problem, that asymmetry is not an artifact of the KJV bridge in both directions at once.
- **The findings→canon edge genuinely has no owner and needs one.** Verified independently of F10 by the grep in F2: a finding filed in `2-evidence/` reaches nothing. Loop 1 is right that this is the break; it is not right that its topology fixes it.
- **We aggregate rather than integrate, and the direction of the link-density gap is probably real.** Under the fairest metric I could construct, 6.59 vs 12.84 — half. The number is not 43%, the comparison is genre-confounded, and the instrument is gameable (F4, F5) — but I could not make the gap disappear under any defensible metric that counts both corpora the same way.
- **Change #5 is the right experiment and is ranked too low.** Whether a ported rule is cheaper than a derived one is the only question whose answer changes what this program *is*. It is cheap, it is falsifiable, and it does not depend on any contested premise above. It should be first.
- **Pre-registering the six most likely errors was correct practice** and is why this critique had somewhere to start. Four of the six were the real defects.

**Overall verdict.** The diagnosis is good and mostly survives. The design does not: its arbiter is internal (F1), its central mechanism is a restatement refuted by its own repo (F2), its independence is supplied by an auditor that inherits the author's constitution (F3), its ranking number is unreproducible and metric-dependent (F4), its falsifier is gamed by its own top change (F5), its flagship build is priced off a stale measurement without the repo's mandatory audit gate (F6), and the collapse to three organs discarded the enforcement layer (F7) and the plateau-vs-accelerate distinction (F8) that were doing real work.

**Do not adopt as a design.** Adopt as a diagnosis, run change #5 first because it is unconditioned, re-run `isaiah_oracle.py --measure` before costing change #2, and restore the three mechanical gates the collapse deleted.

## Related

- [[4-process/proposal-loop-1.md|proposal-loop-1.md]] — the target
- [[4-process/compounding-vs-additive.md|compounding-vs-additive.md]] · [[4-process/improvement-loops.md|improvement-loops.md]] · [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]] — the context it builds on
- [[2-evidence/finding-substrate-loop-diagnosis.md|finding-substrate-loop-diagnosis.md]] — the source of the F1 0.561 chain
- `atu-nlp-wiki/admin/maturation-loops.md`, `atu-nlp-wiki/Pending-Decisions.md` — the sibling design F10 shows was already adopted
- `meta-wiki/wiki/` — `lint-workflow.md`, `drift.md`, `schema-layer.md`, `three-layer-architecture.md`, `ops-improvement-loop.md`, `growth-curve.md`, `compounding-artifact.md`
