---
cssclasses:
  - wide
---

# Audit — migration cost, risk, and cognitive load

> **Plain-language version.** This is a hostile audit of [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]], commissioned to serve Stan's ability to push back rather than the author's convenience. It attacks five claims and answers seven questions. The headline: **the proposal's central de-risking move — "run the current system and capture every decision it makes" — cannot be executed on the corpus that needs it most, because the deployed Book of Mormon text is not the output of any program that can be run.** 789 of its 23,112 lines are not reproduced by the current generator, and the divergence has been sitting in production undetected for 65 days. Separately, the proposal proposes to build an executable-specification layer that **already exists, working, with 62 rules in it**, in `readers-tanakh`. And there is a third option the proposal never puts on the table: do almost nothing structural, and spend two days building the reproducibility gate that would have caught all of this.

**Status: AUDIT. Nothing adopted, nothing changed.** Written 2026-08-09 against [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]] @ `abdad5d`. Every state claim below carries a pasted receipt; every practice claim carries a URL. Findings are labelled **CONFIRMED** (verified this turn) or **PLAUSIBLE** (inference), with severity **FATAL / SERIOUS / MINOR**.

---

## 0. Verdict up front

| # | Finding | Label | Severity |
|---|---|---|---|
| F1 | The deployed BoFM corpus is not reproducible from any runnable program. 789 of 23,112 lines diverge. The behavioural snapshot cannot be taken there. | CONFIRMED | **FATAL** to claim 1 |
| F2 | The divergence is a live product defect, not a theory problem: one rule change was regenerated into 1 of 15 books and left unpropagated for 65 days. | CONFIRMED | **SERIOUS** |
| F3 | The executable-specification layer the proposal wants to build already exists in `readers-tanakh`: 62 uniform YAML rule specs + a 1,375-line runner + an applier + a validator. The proposal scores this component ❌. | CONFIRMED | **SERIOUS** (changes the recommendation) |
| F4 | "The behavioural snapshot" of *outputs* already exists and is called git. What is missing is rule-attribution, which requires instrumenting 19 generator files and 32 in-place mutators — i.e. the expensive part, not the cheap part. | CONFIRMED | **SERIOUS** to claim 1 |
| F5 | The snapshot is not "equally valuable" to both paths. For completion it is a change detector; for greenfield it is a 108,000-item manual adjudication queue, and the literature names this trap. | CONFIRMED | **SERIOUS** to claim 2 |
| F6 | The cost table awards greenfield two properties it does not have — absence of a hybrid state, and "everything gets tested" — against 6 test files in 464 and zero CI in six repos. | CONFIRMED | **SERIOUS** to claim 4 |
| F7 | There are **five** live sites, not four. `vulgate-reader.com` is live and absent from the target architecture. The repo's own single-source-of-truth says three. | CONFIRMED | **SERIOUS** to claim 5 |
| F8 | 1.5 GB / 478 paid, non-regenerable audio files are index-coupled to segmentation, **already desynced in production**, and appear nowhere in the proposal, the scorecard, or the migration plan. | CONFIRMED | **SERIOUS** to claim 5 |
| F9 | Gate 0 gates only the rebuild. It cannot terminate the defects that actually hurt — drift, no CI, unpinned substrate, no backup. Putting the least tractable question first is a sequencing error on cognitive-load grounds. | CONFIRMED | **SERIOUS** to claim 3 |
| F10 | No dependency manifest exists in any of the six repos. `atu-method/pyproject.toml` declares `dependencies = []` while the BoFM pipeline imports `stanza` and `torch`. BHSA is loaded with `use("etcbc/bhsa")` — no version pin. | CONFIRMED | **SERIOUS** |
| F11 | ~1.9 GB of gitignored substrate exists on exactly one disk with no offsite copy. Two of five reader repos symlink their substrate into Dropbox; three do not. | CONFIRMED | **SERIOUS** |
| F12 | Zero CI in all six repos. The only automated gate is a git hook that must be installed by hand per machine, and `atu-method` — the repo the proposal concentrates everything into — has none. | CONFIRMED | **SERIOUS** |
| F13 | The proposal's option set is {build A, build B}. Freeze, scope reduction, and fix-the-defect-leave-the-architecture are never tabled. No document in `4-process/` considers them. | CONFIRMED | **SERIOUS** |
| F14 | Neither path meets its own preconditions: a big bang has no oracle (behaviour is not known, per F1) and an incremental migration will not converge unless corpus work freezes for ~a year — which is the work Stan actually wants to do. | CONFIRMED (§7.5) | **SERIOUS** |
| F15 | The literature's standard remedy for a maintainer who cannot hold a system in his head — decision records — is measured to work on documentation culture, knowledge transfer and prioritisation, and to *stop working* at exactly the split-across-two-architectures boundary that a migration creates and holds open for a year. | CONFIRMED (§6.2d) | **SERIOUS** |
| F16 | Three of the proposal's inline receipts do not reproduce: "~92 HTML files" (actual 1,045), "imported by tanakh (10), bofm (5), gnt (4)" (actual 3/4/4 files, 4/7/7 statements), "31 identical non-trivial lines" (unreproducible; no method stated). | CONFIRMED | MINOR individually, **SERIOUS** in aggregate |

**Two things in the proposal survive intact and get stronger under audit:** the diagnosis that rule-and-check must be one artifact (Part 7 mechanism 1), and the observation that the reader UIs are one application forked — which measures true for four of the five.

---

## 1. Claim 1 — *"'What' is recoverable even though 'why' is not"*

> "Run the current system across every corpus and capture **every decision it makes** — each rule firing, each override, each merge and split, with ref, rule, and outcome. That is a mechanical extraction against code that already runs." — Part 2

### 1.1 The technique is real, is named, and its own inventor says it does not do what the proposal needs

What the proposal describes is **characterization testing** (Michael Feathers' term, 2004) — now more often called **approval testing**, and identical in mechanism to golden-master and snapshot testing.

Feathers, who coined it, is explicit about the boundary:

> "The purpose of characterization testing is to document your system's actual behavior, not check for the behavior you wish your system had."
> — Michael Feathers, *Characterization Testing*, <https://michaelfeathers.silvrback.com/characterization-testing>

The peer-reviewed statement of the same limit, from the only repository-mining study of the technique (n = 1,487 projects):

> "it **only detects differences before and after code changes, and ignores whether the current state is correct.**"
> — Fujita, Kashiwa, Lin & Iida, *An Empirical Study on the Use of Snapshot Testing*, IEEE ICSME 2023, pp. 335–340. PDF: <https://raw.githubusercontent.com/Yutaro-Kashiwa/papers/master/ICSME2023_Fujita.pdf>

And the practitioner statement of the consequence, quoted in a peer-reviewed systematic review:

> "a snapshot just tells you what the component looked like before and what it looks like now. **The decision whether you've fixed a bug, or introduced one, is entirely on you.**"
> — quoted as D5 in Gazzinelli Cruz, Rocha & Valente, *Snapshot testing in practice: Benefits and drawbacks*, *Journal of Systems & Software* 204 (2023) 111797. PDF: <https://homepages.dcc.ufmg.br/~mtov/pub/2023-jss-snapshot.pdf>

That review catalogues the drawbacks with frequencies across 50 analysed documents: fragility 28%, lack of context 22%, large snapshots 16%, manual verification 12%, flaky behaviour 6% (its Table 3). The named failure modes that land directly on this project:

- **Bug lock-in.** "you may commit code with a bug and a snapshot that ensures that the bug is still there." — Artem Sapegin, <https://medium.com/@sapegin/whats-wrong-with-snapshot-tests-37fbe20dfe8e>
- **Rubber-stamping.** "when 5-machinery/tests fail, it is very easy to update the snapshots without fixing the code and understanding the failure reason." (D34, JSS 2023). Jest's own documentation concedes the pull: it exists to "fight against the habit of regenerating snapshots when test suites fail instead of examining the root causes of their failure." <https://jestjs.io/docs/snapshot-testing>
- **Nobody reads it.** "I've personally experienced this with a snapshot that's over 640 lines long. **Nobody reviews it.**" — Kent C. Dodds, <https://kentcdodds.com/blog/effective-snapshot-testing>. The proposed snapshot here is ~108,000 ATU lines.
- **Non-determinism.** "one of the most frequent (issues) were non-deterministic JSON outputs... We were frequently facing failures." (D14, JSS 2023). The canonical mitigation is canonicalisation at capture time — "scrubbers" — not tolerance at compare time: <https://approvaltestscpp.readthedocs.io/en/latest/generated_docs/explanations/Scrubbers.html>

**Terminology matters here more than usual.** Emily Bache argues the name changes behaviour: "snapshot" "doesn't imply any duty of care towards the contents of the snapshot," while "approval" foregrounds that a human approved it and may un-approve it (<https://coding-is-like-cooking.info/2021/03/why-we-should-be-saying-approval-testing-instead-of-golden-master/>). The proposal calls its artefact a **"behavioural snapshot"** and a **"regression baseline"** and never names an approver. Under this literature that is the exact framing to avoid. The question the proposal does not ask is: *who approved these 108,000 outcomes, when, against what, and how would a wrong one be noticed?*

**Verdict on 1.1: the technique is sound and standard, but the proposal claims for it the one thing every primary source denies it — a correctness anchor. SERIOUS.**

### 1.2 FATAL — on the corpus that needs it most, the snapshot cannot be taken

The proposal calls the extraction "mechanical... against code that already runs." I ran it.

```
$ cd readers-bofm && PYTHONIOENCODING=utf-8 PYTHONPATH=../atu-method \
    .venv/Scripts/python.exe 5-machinery/scripts/bofm_generate.py <book>
```

Compared against the deployed corpus in `data/text-files/v2/`, all 15 books, `difflib.SequenceMatcher` over non-blank lines:

```
book              deployed   regen  delta  matched  %diff
1nephi                2139    2175    +36     2065   3.5%
2nephi                3002    3021    +19     2875   4.2%
jacob                  786     774    -12      739   6.0%
enos                   108     110     +2      106   1.9%
jarom                   59      61     +2       57   3.4%
omni                   115     116     +1      108   6.1%
words-of-mormon         66      66     +0       66   0.0%
mosiah                2657    2633    -24     2496   6.1%
alma                  7003    7003     +0     7003   0.0%
helaman               1685    1669    -16     1574   6.6%
3nephi                2570    2580    +10     2449   4.7%
4nephi                 158     159     +1      155   1.9%
mormon                 759     772    +13      719   5.3%
ether                 1438    1446     +8     1367   4.9%
moroni                 567     572     +5      544   4.1%
TOTAL                23112                   22323   3.4%

deployed lines not reproduced by current code: 789
```

**789 deployed lines are not produced by the current generator.** The divergence runs in both directions (+36 in 1 Nephi, −24 in Mosiah), so it is not one systematic rule.

*(Honesty note: my first pass used positional line-by-line comparison and reported 66% divergence for Enos. That number was an alignment artefact — one inserted line shifts every subsequent line. The SequenceMatcher figures above are the correct ones. Correcting my own miscalibrated detector inside an audit that criticises miscalibrated detectors seemed worth stating rather than quietly fixing.)*

**Why it cannot be reproduced.** The deployed corpus is not the output of `bofm_generate.py`. It is that output, plus an unrecorded sequence of in-place mutation 5-machinery/scripts:

```
$ ls 5-machinery/validators/apply_*.py | wc -l
17

$ grep -n "CORPUS\|--apply" 5-machinery/validators/apply_frame_merges.py
10:  python 5-machinery/validators/apply_frame_merges.py            # dry-run
11:  python 5-machinery/validators/apply_frame_merges.py --apply    # write merges
16:CORPUS = Path(__file__).resolve().parent.parent.parent / "data/text-files/v2"
```

Seventeen 5-machinery/scripts that rewrite the deployed corpus in place. And nothing sequences them:

```
$ grep -rn "apply_rule_06|apply_rule_29|apply_frame_merges" . \
    --include=*.py --include=*.md --include=*.sh --include=*.yml \
    | grep -v "/apply_"
(no output)
```

`run_all.py` — the only orchestrator in the repo — discovers `validate_*.py` only:

> "Discovers every `validate_*.py` script under `5-machinery/validators/syntax/` and `5-machinery/validators/colometry/`" — `5-machinery/validators/run_all.py` docstring

**So the deployed artefact is the product of a human-driven sequence of 17 mutators, in an order recorded nowhere.** The proposal's premise — that "what" is mechanically recoverable while only "why" is lost — is false for this corpus. The *what* is entangled with the *why*: to replay the behaviour you must first know which appliers were run, on which books, in what order, and that is precisely the lost provenance.

**CONFIRMED. FATAL to claim 1 as stated.**

### 1.3 What the divergence actually is — and why it matters more than the architecture question

Two books are reproduced exactly: **Alma (7,003 lines, 0.0%)** and **Words of Mormon (0.0%)**. Those are the last two books regenerated:

```
$ git log --format='%h %s' -1 -- data/text-files/v2/
726fa3a Alma 34: revert PP-conj amplificative rule; ship cross-verse 34:3->34:4; substrate T24 UD fix

$ git show --stat 726fa3a
 books/alma.html                                    | 6468 ++++++++++----------
 data/parses/v0-cache-conllu/alma.conllu            |    2 +-
 data/text-files/v2-adjudicated/cross-verse-merges.json |    9 +
 data/text-files/v2/09-alma-2020-sb-v2.txt          |  692 ++-
 sw.js                                              |    2 +-
```

A rule was reverted, a substrate fix shipped, and **one book of fifteen was regenerated.** The last corpus-wide regeneration was 2026-06-03. Between 2026-06-05 and 2026-08-07 there were 35 commits and **none** touched the rule layer — so this is not drift from later rule work. It is the residue of the two production methods coexisting: thirteen books still carry applier-era text, two carry pure-generator text, and **nothing in the repository distinguishes them.**

Consequence, stated plainly: **the live Book of Mormon reader currently applies a rule in Alma that it does not apply in the other fourteen books.** Nobody knew. It has been true for 65 days. No validator, no baseline, no gate, no reader observation caught it.

**This is the finding Stan should care about most, and it is completely independent of greenfield-vs-completion.** It is also detectable in ninety seconds by the script I ran above.

### 1.4 The contrast that saves the technique — GNT reproduces perfectly

The same test on `readers-gnt`, Matthew 1–10:

```
matt  1  deployed=  89 regen=  90 matched=  89  diff=  0.0%
matt  2  deployed=  78 regen=  79 matched=  78  diff=  0.0%
...
matt 10  deployed= 136 regen= 137 matched= 136  diff=  0.0%
TOTAL deployed=1147 matched=1147 diff=0.0%  unreproduced=0
```

*(The +1 per chapter is the generator's stdout banner, not content.)*

And the BoFM **publish** stage is byte-perfect:

```
$ python build_book.py helaman data/text-files/v2/10-helaman-2020-sb-v2.txt --out /c/tmp/bofm-build/
$ cmp /c/tmp/bofm-build/helaman.html books/helaman.html
BUILD REPRODUCES DEPLOYED HTML
```

And the generator is deterministic run-to-run:

```
$ python 5-machinery/scripts/bofm_generate.py 1nephi > run1.txt
$ python 5-machinery/scripts/bofm_generate.py 1nephi > run2.txt
$ cmp run1.txt run2.txt && echo IDENTICAL
RUN-TO-RUN IDENTICAL
```

**This is important and it cuts against my own headline.** The system is not globally unreproducible. GNT is clean. The publish layer is clean. Determinism is fine. The failure is localised to one corpus's segmentation stage, and it has a specific cause — in-place mutators outside the generator. That is a *bug with a known fix*, not a *reason to rebuild*.

The proposal scores Publish as ⚠ "works, but conflated with source" and Presentation as ❌. Measured, **Publish is the healthiest component in the system** — the only one that reproduces byte-for-byte.

### 1.5 SERIOUS — the substrate the snapshot would depend on is not pinned anywhere

A characterization baseline is meaningless if the inputs can move underneath it. The canonical mechanism is a lock file recording content hashes of every dependency (DVC: "`dvc.lock`... captures hashes (in most cases `md5`s) of the dependencies and values of the parameters that were used" — <https://doc.dvc.org/user-guide/pipelines/defining-pipelines>). Here:

```
$ find readers-{tanakh,bofm,gnt,lxx,vulgate} atu-method \
    -not -path '*/.git/*' -not -path '*/.venv/*' -not -path '*/private/*' \
    \( -name 'requirements*.txt' -o -name 'pyproject.toml' -o -name 'Pipfile' \
       -o -name 'poetry.lock' -o -name 'environment.yml' -o -name 'uv.lock' \)
readers-tanakh/research/macula-hebrew/pipelines/.../pyproject.toml   [vendored upstream]
...
atu-method/pyproject.toml
```

One project manifest, and it declares:

```
dependencies = []
```

while the live BoFM generator does `import stanza` and the installed environment is `stanza 1.12.0 / torch 2.12.1+cpu`, held only in a gitignored 922 MB `.venv`.

The Tanakh substrate is loaded with **no version pin at all**:

```
$ grep -n 'use(' readers-tanakh/scripts/atu_pipeline_v2/run_full_tanakh.py
378:    A = use("etcbc/bhsa", silent="deep")
```

resolving against a machine-local cache (`~/text-fabric-data`, 280 MB, holding version `2021`). And the three vendored corpora have HEADs recorded nowhere:

```
$ cd biblical-corpora && for d in bhsa greek-new-testament macula-hebrew; do
    (cd $d && git log -1 --format='%h %ci'); done
4db00e2 2026-01-18
4a76cbf 2024-09-22
47db250 2026-04-24

$ grep -rn "4db00e2" atu-method readers-tanakh --include=*.md --include=*.json --include=*.py
(no output — substrate provenance is not pinned anywhere)
```

Cross-repo wiring is by manually-set environment variable, not an installed dependency — `bofm_generate.py` fails outright without `PYTHONPATH=../atu-method`, and the parse cache directory is overridable by `BOFM_V0_CACHE_DIR`.

**Consequence:** a baseline captured today records *(rules ∘ stanza-1.12.0 ∘ torch-2.12.1 ∘ BHSA-2021 ∘ macula-47db250)* and says so nowhere. A future diff against it cannot distinguish "the code changed" from "the input changed" — which is the one ambiguity the baseline exists to remove. **CONFIRMED. SERIOUS.**

### 1.6 SERIOUS — "the behavioural snapshot" of outputs already exists, and it is called git

The proposal treats the snapshot as a missing artefact. But the deployed corpora *are* version-controlled, per-line, diffable, with history:

```
$ cd readers-bofm && git ls-files data/text-files/v2/ | wc -l
15
$ git ls-files data/parses/v0-cache | wc -l
15
```

`git diff` over `data/text-files/v2/` is already an exact, per-line regression detector for the product. For GNT, where the generator reproduces the corpus exactly, a regression gate is `regenerate && git diff --exit-code` — buildable this afternoon.

What git does *not* give you is **which rule produced each line**. Getting that requires instrumenting the rule surface:

```
$ (classification of 464 authored .py files, excluding .venv/private/research/_old/_archive/data)
RULE ENGINE / generator      files=  19  LOC=   8813
appliers (corpus mutators)   files=  32  LOC=   6529
validators                   files=  75  LOC=  31016
build/ingest                 files=  36  LOC=  13577
one-off analysis/audit       files= 127  LOC=  37821
other                        files= 175  LOC=  53323
TOTAL                        files= 464  LOC= 151079
```

19 generator files and 32 mutators would need decision-emission added, in three different languages of thought (BHSA/Text-Fabric, Stanza-over-EModE, Macula), and that instrumentation is itself new, untested code that changes the thing it measures. The `tx_log` infrastructure the proposal cites as half-built exists — but only in BoFM's appliers, never in any generator, and nowhere else at all:

```
$ grep -rln 'tx_log|TxLog' readers-tanakh readers-gnt readers-lxx readers-vulgate readers-gnt-morph --include=*.py
(no output)
```

**So the split is the opposite of what the proposal claims.** The cheap half (outputs) is already done and in git. The expensive half (rule attribution) is the half that is adjacent to the "why" the proposal concedes is unrecoverable. **CONFIRMED. SERIOUS.**

---

## 2. Claim 2 — *"Equally valuable to greenfield and to completion, so it can be built before the choice"*

**It is not equally valuable, and the asymmetry runs in the direction that hurts the option the proposal prefers.**

| | Completion | Greenfield |
|---|---|---|
| What the snapshot is | a **change detector** — any diff is a regression until adjudicated | a **work queue** — every diff must be adjudicated, and there are ~108,000 lines |
| What it costs to use | near zero; diffs are rare and local | one human decision per divergent line |
| What it risks | rubber-stamping (documented, 12–28% of practitioner reports) | **bug-for-bug compatibility** — reproducing behaviour you have already declared untrustworthy |

The bug-for-bug trap is the specific hazard here, because the proposal's own premise is that current behaviour is not trusted. Sapegin's formulation applies exactly: "you may commit code with a bug and a snapshot that ensures that the bug is still there." A greenfield engine measured against a snapshot of the system it exists to replace is being scored against the wrong oracle — and the project has already been burned by exactly this shape once, per the proposal's own Part 7: *"If cases are adjudicated by us against our own rules, this is circularity in a nicer container — which is exactly what the Isaiah oracle turned out to be."* A behavioural snapshot of our own system is that same circularity with a new name.

**Three further asymmetries, measured:**

1. **It cannot be built for BoFM at all** (§1.2) — the corpus with 911 overrides and the most judgment invested.
2. **It is free for GNT** — `regenerate && git diff` today.
3. **It does not exist for LXX or Vulgate in any form** — those two repos have zero validators, zero 5-machinery/tests, and are absent from the deployment record entirely.

So the artefact's value ranges from *impossible* to *already free* across the five corpora. "Equally valuable" is not a defensible summary of that spread. **CONFIRMED. SERIOUS.**

**What survives of claim 2:** the *sequencing instinct* is right. Something should be built before the choice, and it should be path-independent. It just isn't this artefact — see §10.

---

## 3. Claim 3 — *"Gate 0 can terminate the whole plan cheaply"*

> "Is there an external segmentation witness that our rules did not produce?... Cheap to answer, and it can terminate the whole plan." — Part 8

**Three objections, in increasing order of severity.**

**(a) It is not cheap, and the repo already has the evidence that it isn't.** Gate 0 is an open research question in Hebrew and Early-Modern-English textual scholarship, with no stated success criterion, no named evaluator, and no bar for "adequate." Questions of that shape do not resolve cheaply; they resolve into argument. And this one has already been asked once: the Isaiah oracle was run, produced F1 0.561, and then became a dispute about whether it counted as an arbiter at all — see [[4-process/compounding-vs-additive.md|compounding-vs-additive.md]] §2, which reopens a "considered judgment that a prior version of me made deliberately." **PLAUSIBLE → CONFIRMED by precedent: this question has consumed real time and produced a contested number, not a verdict.**

**(b) It cannot terminate what actually hurts.** Gate 0 gates the *rebuild*. It does not gate:

- the 789-line drift (F1/F2)
- the audio desync (F8)
- the absence of CI (F12)
- the unpinned substrate (F10)
- the absent offsite backup (F11)
- the 127 one-off 5-machinery/scripts and 37,821 LOC of dead weight

Every one of those is a defect today, is real regardless of the arbiter answer, and is fixable without answering it. Framing Gate 0 as able to "terminate the whole plan" is true only if "the plan" is exclusively about correctness-of-segmentation. But Parts 4–7 also promise to fix the record, the validators, and the presentation duplication. **Gate 0 gates none of those.** CONFIRMED. SERIOUS.

**(c) It is the wrong question to put first, on cognitive-load grounds specifically.** The brief for this audit is that Stan is "unable to process or navigate, causing me to defer to you on things I should have pushed back on." Gate 0 is the *least* Stan-decidable item in the entire document — an unbounded scholarship question with an admitted circularity problem — and the proposal places it in front of everything, including the items that are cheap, decidable, and would visibly improve the product. That inverts the correct ordering. **Put the decidable things first; they build the ability to decide the hard one.**

**What survives:** the arbiter question is real and important, and the proposal deserves credit for naming it as upstream of the rebuild's validity rather than burying it. It is a good **Gate N**. It is a bad Gate 0.

---

## 4. Claim 4 — the cost table. *Is it honest, or does it smuggle the conclusion?*

The table under audit:

| Cost axis | Greenfield | Finish the abandoned direction |
|---|---|---|
| Engineering effort | Higher | **Lower** |
| Cognitive load on Stan | **Lower** | Higher |
| Error discovery / rework | Bounded and visible | Unbounded and invisible |

**It smuggles. Row by row.**

### Row 2 is the smuggle, and it is the decisive row

> "**Lower** — one new thing, cleanly bounded; the old thing is frozen and can be ignored"

**"The old thing is frozen and can be ignored" is false.** Five live sites keep serving off the old path throughout — the proposal says so itself in Pending-Decisions step 4: *"The live sites keep serving off the old path while the spine is built."* A system that is serving users cannot be ignored. It must be maintained, patched when a reader reports an error, and kept coherent with whatever is being built next to it.

So **greenfield does not avoid the hybrid state. It produces exactly the same hybrid state as completion** — two systems, both alive, one authoritative for users and one under construction. The only difference is whether the two share code. The table awards greenfield the *absence* of a two-system period that greenfield does not actually avoid, and that absence is the entire justification for the row that the proposal then calls decisive.

If anything, sharing code makes the hybrid *more* legible, not less: one rule change visible in one place beats the same change made twice in two unrelated codebases. The row may be backwards.

### Row 3 assigns an aspiration as a property

> "Bounded and visible: everything is new, so everything is suspect and gets tested"

"Gets tested" is not a property of greenfield. It is a hope about future behaviour, and the revealed behaviour of this project contradicts it:

```
$ for r in atu-method readers-tanakh readers-bofm readers-gnt readers-lxx readers-vulgate; do
    echo -n "$r test_*.py: "; find $r -name 'test_*.py' \
      -not -path '*/.venv/*' -not -path '*/.git/*' -not -path '*/research/*' | wc -l; done
atu-method test_*.py: 2
readers-tanakh test_*.py: 4
readers-bofm test_*.py: 0
readers-gnt test_*.py: 0
readers-lxx test_*.py: 0
readers-vulgate test_*.py: 0
```

**Six test files across 464 authored Python files and 151,079 lines.** `readers-bofm` — 1,149 commits, the most complex generator, the corpus with 911 hand-adjudications — has zero. And zero CI in all six repos (§11). A design whose safety depends on "everything gets tested" is a design whose safety depends on a behaviour this project has never once exhibited over three years.

"Bounded" is also wrong in the other direction. For greenfield the error surface is the *entire product* — ~108,000 ATU lines across three live corpora — because there is no baseline to diff against. For completion the error surface is the delta. That is the opposite of the assignment.

```
bofm         files=   15 atu_lines= 16508
tanakh-heb   files=  929 atu_lines= 72147
gnt          files=  260 atu_lines= 19279
TOTAL                     107934
```

### Row 1 is wrong in both directions, which is the tell

The completion path's engineering advantage rests on inheriting the started-and-abandoned engine. Measured adoption:

```
$ grep -rl 'from atu_method|import atu_method' readers-* --include=*.py | grep -v .venv
readers-tanakh/scripts/build_books.py
readers-tanakh/scripts/propagate_editorial_layers.py
readers-tanakh/scripts/regenerate_english.py
readers-bofm/5-machinery/scripts/bofm_v1_fabric.py
readers-bofm/5-machinery/validators/parsing/conllu_query.py
readers-bofm/5-machinery/validators/parsing/line_mapping.py
readers-bofm/5-machinery/validators/tx_log.py
readers-gnt/scripts/build_books.py
readers-gnt/scripts/regenerate_english.py
readers-gnt/scripts/scan_unanchored_alignment.py
readers-gnt/validators/common.py
```

**11 files out of 464 (2.4%).** The proposal's own receipt says "tanakh (10 files), bofm (5), gnt (4)"; the measured counts are 3, 4, 4 by file and 4, 7, 7 by import statement. Neither reproduces. On the measured number, completion inherits very little — it is nearly greenfield already, which *weakens* row 1's advantage.

But row 1 also **understates** completion, badly, by missing the largest inheritable asset in the system — see §5 below. A row that is wrong in both directions at once was not measured; it was assigned by intuition and then dressed as a finding.

### The meta-finding on the retraction itself

The author disclosed a bias — *"I am not neutral, and the recommendation conveniently concentrates everything in the repo I work in"* — which points at a pro-*completion* bias. But the retraction table, written **after** Stan pushed back, scores greenfield the winner on two of three axes including the one it declares decisive. And [[Pending-Decisions.md]] already recommends *"greenfield the CORE."* So the stated bias disclosure guards the wrong flank.

More importantly: **the retraction converted Stan's objection into support for a different build, rather than into support for building less.** Stan's words were about *cost* — "not COGNITIVELY cheaper for me… nor TIME cheaper." The honest response to a cost objection includes the option of not spending. At no point does "don't restructure" appear as a row, a column, or an option (F13, §9). That is the smuggle that matters more than any individual cell.

**CONFIRMED. SERIOUS.**

### What the table is missing entirely

| Axis the table omits | Why it belongs |
|---|---|
| **Duration** | The proposal never estimates elapsed time for either path. A part-time maintainer's dominant risk is calendar, not effort (§8). |
| **Reversibility** | Which path can be abandoned halfway leaving a working system? Completion: yes, at every step. Greenfield: only if the old path stays whole — which contradicts row 2. |
| **What happens if Stan stops for a month** | Already answered empirically: the 789-line drift ran for 65 days undetected (§11). |
| **Non-code assets** | 1.5 GB of paid, non-regenerable, segmentation-coupled audio (§5.3). Absent from every row. |
| **Cost of *not* choosing** | Both paths are priced against zero. Neither is priced against "fix the four measured defects and stop." |

---

## 5. Claim 5 — *"Convert readers one at a time, keeping every live site serving"*

### 5.1 SERIOUS — the plan does not know how many sites there are

```
$ for r in readers-*; do [ -f $r/CNAME ] && echo "$r -> $(cat $r/CNAME)"; done
readers-bofm     -> bomreader.com
readers-gnt      -> gnt-reader.com
readers-lxx      -> lxx-reader.com
readers-tanakh   -> tanakh-reader.com
readers-vulgate  -> vulgate-reader.com
```

All five resolve and serve working readers (verified by fetch: `bomreader.com` "The Book of Mormon — Reading Edition"; `lxx-reader.com` "LXX Reader — Septuagint"; `vulgate-reader.com` "Vulgate Reader — Latin New Testament"; `tanakh-reader.com` "Tanakh Reader — Hebrew Bible").

Three different counts of the deliverable exist inside this repo simultaneously:

- **3** — `2-evidence/deployment-status.md`, which declares itself *"the authoritative record of what is LIVE for each reader edition"* and lists only tanakh, bofm, gnt.
- **4** — the proposal's Part 9 ("Big-bang risk against four live sites") and its Part 6 target diagram (`site-tanakh`, `site-bofm`, `site-gnt`, `site-lxx`).
- **5** — the filesystem and the live web.

**`vulgate-reader.com` is live and appears nowhere in the target architecture.** A migration plan that omits a live production system from its own diagram has an undefined scope, and "keeping every live site serving" cannot be verified against a set whose size is unknown. **CONFIRMED. SERIOUS.**

There are also **eight** reader repos on disk, not six: `readers-tanakh-morph` and `rev-reader` are absent from `atu-method/CLAUDE.md`'s repo map.

### 5.2 The UI-unification claim is measurably true for four and measurably false for the fifth

Part 4 asserts the reading UI is "a **config surface, not five applications.**" Pairwise line-similarity of the five reader shells (`index.html`, 3,155–5,121 lines each):

```
tanakh    vs bofm      ratio=0.132
tanakh    vs gnt       ratio=0.698
tanakh    vs lxx       ratio=0.703
tanakh    vs vulgate   ratio=0.702
bofm      vs gnt       ratio=0.131
bofm      vs lxx       ratio=0.132
bofm      vs vulgate   ratio=0.132
gnt       vs lxx       ratio=0.921
gnt       vs vulgate   ratio=0.948
lxx       vs vulgate   ratio=0.950
```

**tanakh/gnt/lxx/vulgate are 70–95% identical — genuinely one application, forked. BoFM is 13% similar to all four.**

This is the best-supported constructive finding in the audit. There is a cheap, high-value subset of the proposal — unify the four that are already nearly identical — and an expensive one the proposal prices at zero. BoFM is not a config variant; it is a PWA with audio narration, a service worker, a Firestore annotation layer, and 3,043 additional lines of JavaScript. And it is the flagship.

### 5.3 SERIOUS — 1.5 GB of paid, non-regenerable, segmentation-coupled audio is absent from the entire proposal

```
$ du -sh readers-bofm/audio ; find readers-bofm/audio -type f | wc -l
1.5G    readers-bofm/audio
478

$ cd readers-bofm && git ls-files audio | wc -l
478                      # all tracked; .git is 2.7 GB
```

Each MP3 has a sidecar timing manifest keyed to **ATU line boundaries**:

```json
{"book":"1nephi","chapter":1,"voice":{"provider":"elevenlabs","voice_id":"ddDFRErfhdc2asyySOG5",
 "model_id":"eleven_multilingual_v2","settings":{"stability":0.5,...}},
 "lines":[{"start":0.0,"end":3.065,"type":"line",
           "text":"I, Nephi, having been born of goodly parents,","verse":"1:1","lineIndex":1}, ...]}
```

Three consequences the proposal never addresses:

**(a) It is not build output, and it is not regenerable.** It was produced by a paid third-party TTS API at `stability: 0.5` — a stochastic setting. Re-running it would not reproduce it even given the same text. Part 5's model — a publish target is "build output plus a `CNAME`, force-pushed by the engine's build… no independent history worth defending" — would destroy it. This is history worth defending.

**(b) It is coupled to segmentation by positional index, with no text verification.** `narration.js` seeks by `lineIndex`:

```
$ grep -n 'lineIndex' readers-bofm/narration.js | head -3
236:      lineIndex: parseInt(bestEl.getAttribute('data-line-index'), 10),
336:        const entry = manifest.lines.find(l => l.lineIndex === pendingSeekIdx);
674:  const manifestIdx = manifest.lines.findIndex(l => l.lineIndex === lineIdx);
```

Any re-segmentation silently misaligns every cue after the first change. Both proposed paths re-segment.

**(c) It is already broken in production.** Helaman chapter 1:

```
audio ch1 line cues: 122, lineIndex range 1 - 126
deployed ch1 content lines: 68
built HTML ch1 elements with data-line-index: 73, range (0, 72)
```

Across the whole book, **1,498 of 2,020 audio line cues (74%) do not match any line in the deployed corpus.** Sample:

```
MISS 'And now behold, it came to pass in the commencement of the fortieth year...'
MISS 'there began to be a serious difficulty among the people of the Nephites.'
   vs deployed 1:1 = those two as ONE line
```

The audio was recorded against a third, older segmentation. So there are **three divergent versions of the BoFM line breaks in circulation right now** — the one in git, the one the code produces, and the one the narrator read — and the reader aligns them by integer index. *(The structural mismatch is CONFIRMED; that it produces a wrong seek for a user is PLAUSIBLE-high — I did not drive a browser.)*

**This is the strongest possible illustration of the audit's central point:** the system already contains an undetected, user-visible behavioural drift, coupled through an index, with no check — and neither proposed path has a step for it.

### 5.4 The availability claim is true but answers the wrong risk

"Keeping every live site serving" is technically easy — GitHub Pages serves whatever is on the branch, and there is no build step to fail. The risk is not **availability**; it is **silent content regression**. With zero CI, bare-count validator baselines, and no reproducibility gate, the sites will keep serving — possibly the wrong text, for months. That is not hypothetical. It is what the last 65 days were.

The force-push model adds a specific new hazard: `readers-bofm/.git` is 2.7 GB, and force-pushing a generated tree over it removes the rollback path that currently exists (`git revert`) for the one repo that most needs it.

---

## 6. Cognitive load — what the evidence actually says

The proposal declares this the decisive axis. It is right to, and it is also the axis on which the research most conspicuously fails to support confident design claims. Both halves matter.

### 6.1 First, the honesty check — this axis cannot bear the weight the proposal puts on it

Will Crichton, who did his Stanford PhD on cognitive load in program comprehension, on the popular "cognitive load in software" literature:

> "**We have essentially no experimental data about how to optimize programs to minimize cognitive load.**"
> "the science of working memory applied to programming is far too young to justify the kinds of claims made here."
> — <https://github.com/zakirullin/cognitive-load/issues/22>

So: **no citation exists that says "hybrid systems cost a single maintainer X% more comprehension effort than unified systems."** Anyone — including the proposal, and including me — who assigns a cognitive-load ranking to an architecture is reasoning from analogy, not from evidence. The cost table's row 2 is an intuition. That does not make it wrong; it makes it a claim Stan is as qualified to judge as the author, which is worth saying explicitly, because the whole premise of this audit is that he has been deferring on things he should push back on. **On row 2, his intuition is the better instrument, and he should use it.**

*(Two citation traps I checked and avoided: Sweller 1988 does **not** contain the intrinsic/extraneous/germane trichotomy — that is Sweller, van Merriënboer & Paas 1998, <https://link.springer.com/article/10.1023/A:1022193728205>; and the ubiquitous "23 minutes 15 seconds to recover from an interruption" is not a research finding at all — it traces to a 2006 Gallup interview with Gloria Mark, <https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx>, and appears nowhere in *The Cost of Interrupted Work*. If you see either in a future proposal, it is a citation-drift tell.)*

### 6.2 What the evidence *does* support, and it is directly relevant

**(a) Comprehension, not writing, is where the time goes.**

> "on average developers spend **~58% of their time on program comprehension activities**"
> — Xia, Bao, Lo, Xing, Hassan & Li, *Measuring Program Comprehension: A Large-Scale Field Study with Professionals*, IEEE TSE 44(10):951–976, 2018. **78 professional developers, 7 real projects, 3,148 hours** of instrumented activity. <https://ink.library.smu.edu.sg/sis_research/3779/>

The same paper reports that **senior developers spend a significantly smaller fraction of their time on comprehension than juniors** — the expert/schema effect from Sweller's original work. Its implication for this project is uncomfortable: *Stan is the senior on the domain and the junior on the machinery.* Every hour he spends is weighted toward the expensive end.

*(The widely-quoted 70% figure — Minelli, Mocci & Lanza, ICPC 2015 — is real but weaker: Xia et al. note that "only seven of the participants are professionals and more than 85% of the studied data is based on the activities of 3 participants who are PhD students." Lead with 58%.)*

**(b) For a part-time maintainer, every session is a resumption, and resumption is not free.**

> "only **10% of the programming sessions have coding activity start in less than a minute**, only 7% of the programming sessions involve no navigation to other locations prior to editing"
> "with an interrupted task, programmers are instead **re-comprehending** a program and related artifacts in order to resume work"
> — Parnin & Rugaber, *Resumption Strategies for Interrupted Programming Tasks*, ICPC 2009. **10,000 recorded sessions, 85 programmers.** <https://chrisparnin.me/pdf/parnin-icpc09.pdf>

This is the single most applicable finding in the set. At 6–10 hours a week across a six-repo system, Stan is not a developer who occasionally gets interrupted; **he is permanently in the resumption state.** The design objective that follows is not "minimise total complexity" — it is **minimise the cost of the first ten minutes of a session.** By that objective:

- A gate that outputs **five integers, all of which should be zero** (§10) is close to optimal — it re-establishes system state in one glance.
- A "behavioural snapshot" of 108,000 lines is close to worst-case.
- 106 memories, 10 [[CLAUDE.md]] files across the cascade, and 11 process documents in `4-process/` are resumption *tax*, not resumption *aid*.
- 127 one-off 5-machinery/scripts (§9-C3) are pure extraneous load: they are navigable, greppable, and irrelevant.

**(c) Single-maintainer is the ecosystem norm, not a pathology.**

| Study | Sample | Finding |
|---|---|---|
| Avelino, Passos, Hora & Valente, ICPC 2016 — <https://arxiv.org/pdf/1604.06766> | 133 popular GitHub projects | **65% have truck factor ≤ 2** (TF=1: 34%, TF=2: 31%) |
| Avelino, Constantinou, Valente & Serebrenik, ICSME 2019 — <https://arxiv.org/pdf/1906.08058> | 1,932 projects | **57% have TF = 1.** 16% suffered total TF-developer loss; **41% of those survived anyway** |
| Coelho & Valente, ESEC/FSE 2017 — <https://arxiv.org/pdf/1707.02327> | 104 deprecated popular projects | Failure causes: lack of time 18, lack of interest 18, **low maintainability 7** |

Two things follow. First, "one part-time maintainer" is not a defect to be architected away; it is the baseline condition of most successful open-source software, and 41% of projects that actually lost their sole author survived. Second — and this is the finding that argues *for* the proposal rather than against it — one respondent in Coelho & Valente attributes project death directly to architecture:

> "**The project reached an unmaintainable state due to architectural decisions made early in the project's life.**" (respondent D30)

That is a real counterweight, and I am carrying it deliberately: the case for restructuring is not empty. But note what killed projects more often — **lack of time and lack of interest, 36 mentions between them, against 7 for maintainability.** A year-long restructuring consumes exactly the two resources whose exhaustion is the leading cause of death.

**(d) The one empirical study of the standard remedy says it stops working at the hybrid boundary.**

Architecture Decision Records are the canonical prescription for exactly Stan's problem — Michael Nygard's founding statement is almost a description of this repo:

> "One of the hardest things to track during the life of a project is **the motivation behind certain decisions**."
> — <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html>

The only empirical evaluation I could find:

> "practitioners face challenges related to the documentation culture, knowledge transfer, prioritization of information to be documented, as well as handling documentation for shared and distributed components. **The first three types of challenges are well addressed by Architecture Decision Records. However, challenges arising from developing distributed systems remain open.**"
> "the decision on **where** documentation is stored has a massive influence on its perceived usefulness"
> — Ahmeti, Linder, Groner & Wohlrab, *Architecture Decision Records in Practice: An Action Research Study*, ECSA 2024. <https://rebekkaa.github.io/files/2024_ECSA.pdf>

**Read that against the migration proposal.** The documentation practice most reliably prescribed for a maintainer who cannot hold the system in his head is measured to work on culture, transfer and prioritisation — and to *stop working* precisely at the split-across-two-architectures boundary. A migration deliberately creates that boundary and holds it open for a year. **This is the closest thing to direct empirical support for Stan's own objection, and it points at the hybrid state rather than at either endpoint.**

The second quote lands too. Decision documentation in this program is spread across [[Pending-Decisions.md]] in three repos, 106 memories, 10 [[CLAUDE.md]] files and 11 documents in `4-process/`. Storage location "has a massive influence on perceived usefulness," and this one is diffuse.

### 6.3 So — how do you make either path legible to a non-full-time human?

Concrete and ordered by measured leverage:

1. **Make state readable in one glance.** Five integers, all zero (§10). Nothing else in this audit competes on resumption cost.
2. **Delete 25% of the code** (§9-C3). Extraneous load is the reducible kind; 127 one-off 5-machinery/scripts are the purest example available.
3. **Finish the decision records you already have.** [[Pending-Decisions.md]] is an ADR system in everything but name — decision, recommendation, why, cons, resolved-section. Its **Resolved section is empty**: *"(none yet — entries move here with date and outcome)"*. Six open entries, zero resolved. An ADR log that never resolves is a worry-bead. Nygard's value comes from the *Status* field moving.
4. **One page per pipeline, verified by running it** (§9-C5). This audit's four biggest findings came from doing that for two of five.
5. **Consolidate where decisions live.** Ahmeti et al.'s storage finding says the diffusion itself is costing comprehension, independent of content.
6. **If you migrate anyway: write the hybrid-state invariant down first** — one page saying, for each corpus, which system is authoritative today and how to tell. The ADR study says this is exactly the case ADRs do *not* cover automatically, so it has to be authored deliberately.

---

## 7. Incremental vs big-bang rewrite — the evidence, and it is thinner than the folklore

### 7.1 The most-cited failure data does not survive audit

Nearly every "most rewrites fail" argument traces to the Standish CHAOS reports. They should not be used.

**How respondents were recruited**, quoted from CHAOS Report v3.0 p.13 by Jørgensen & Moløkken-Østvold (*Information and Software Technology* 48(8):297–301, 2006, <https://web-backend.simula.no/sites/default/files/publications/Jorgensen.2006.4.pdf>):

> "We then called and mailed a number of confidential surveys to a random sample of top IT executives, **asking them to share failure stories**."

They also note that every independent study of the same period found average cost overrun near **30%**, against Standish's **189%**. And on method disclosure: *"This unwillingness to reveal research method and measurement definitions would have been an unacceptable response in an academic context."*

**Eveleens & Verhoef** applied Standish's own definitions to **5,457 forecasts across 1,211 real projects** (*IEEE Software* 27(1):30–36, 2010, <https://www.cs.vu.nl/~x/the_rise_and_fall_of_the_chaos_report_figures.pdf>). Landmark Graphics scores **5.8% success**; invert the sign of every identical deviation and the same error magnitudes score **94.2%**:

> "Because the underlying data has an unknown bias, any aggregation of that data is unreliable and meaningless."

And Standish's own chairman, replying to them in writing:

> "All data and information in the Chaos reports and all Standish reports should be considered **Standish opinion** and the reader bears all risk in the use of this opinion."

**Even the underlying premise — bigger projects fail more — is contested.** Jørgensen, Halkjelsvik & Kitchenham (*International Journal of Project Management* 30(7):839–849, 2012, <https://www.sciencedirect.com/science/article/abs/pii/S0263786312000099>) show the size–overrun relationship reverses depending on whether size is measured by estimated or actual cost, and that the apparent effect is partly a statistical artifact of imperfect correlation between the two. Prior observational studies "cannot be considered to provide reliable evidence."

**The one clean dataset does not generalise here.** Flyvbjerg & Budzier, *HBR* 89(9), 2011, **n = 1,471 IT projects** (<https://arxiv.org/pdf/1304.0265>): average cost overrun 27%, with **one in six a "black swan" at ~200% cost and ~70% schedule overrun.** But the average project cost **$167 million** and **92% were public agencies**. It is a study of government ERP megaprojects. Applying it to a 8,813-line rule engine maintained by one person is unwarranted, and I am not applying it.

### 7.2 "Never rewrite" is one anecdote from 2000, and its author scoped it out of this case

Joel Spolsky, *Things You Should Never Do, Part I* (<https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/>) — the source of the entire genre:

> "the single worst strategic mistake that any software company can make"
> "It's harder to read code than to write it."

**Zero data. One company. Never empirically tested in 26 years.** And Spolsky scopes it himself, in the same piece:

> "The old mantra *build one to throw away* is dangerous when applied to **large scale commercial applications**."
> "If you are writing code experimentally, you may want to rip up the function you wrote last week… That's fine."

Both of his load-bearing mechanisms — losing accumulated bug-fix knowledge, and being frozen while competitors ship — are **commercial and competitive**. Neither translates to a system with one author, no competitor, and no revenue.

The primary participant's account is more modest than the folklore. Jamie Zawinski, <https://www.jwz.org/gruntle/nomo.html> (1999):

> "this did get us more contributors. But it also constituted an almost-total rewrite of the browser, **throwing us back six to ten months**."

He attributes the outcome to several causes, not the rewrite alone — and the Gecko engine that rewrite produced became Firefox. Spolsky wrote before either happened.

**And Brooks retracted the pro-rewrite maxim from the other direction.** "Plan to throw one away; you will, anyhow" — *Mythical Man-Month*, 1975. Brooks in 2010 (<https://www.computerworld.com/article/2550685/the-grill--fred-brooks.html>): *"In the second edition, I say that **was misguided!** You ought to plan to continually iterate on it, not just build it, throw it away and start over."* **Both canonical maxims in this argument have been disowned or scoped out by their own authors.**

### 7.3 Rewrites that worked — including a big bang, from the leading authority on IT project failure

| Case | Approach | Outcome |
|---|---|---|
| **Emirates NBD** core banking (Flyvbjerg & Budzier 2011 inset, <https://arxiv.org/pdf/1304.0265> p.7) | **explicit big bang** — all components switched simultaneously | **Schedule slipped 7%, cost +18%** — despite a mid-project merger that doubled scope |
| **Dropbox** sync engine (<https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine>) | full rewrite, ~4 years | succeeded — while explicitly quoting Spolsky and doing it anyway |
| **Khan Academy** monolith→services (<https://blog.khanacademy.org/beating-the-odds-khan-academys-successful-monolith%E2%86%92services-rewrite/>) | incremental | completed **within four months of a 20-month estimate** (~20% over) |
| **Slack** desktop (<https://www.infoq.com/news/2019/07/slack-desktop-successful-rewrite/>) | incremental, strict "old cannot import new, new cannot import old" | succeeded, ~2 years |

Dropbox's post contains the sharpest statement of **when incremental is not available**:

> "**Changing the foundational nouns of a system is often impossible to do in small pieces.**"
> "we quickly ran out of effective incremental improvements."

### 7.4 The strangler fig's documented failure mode — conceded by its own custodians

The pattern's canonical page is honest about the odds:

> "We've seen this simple-sounding plan **go down in flames most of the time**."
> "Replacing a serious IT system takes a long time, and the users can't wait for new features."
> — Fowler, *StranglerFigApplication*, <https://martinfowler.com/bliki/StranglerFigApplication.html>

*(That "most of the time" refers to the big-bang plan the pattern replaces. But note the cost concession for the pattern itself: "While this may appear to be a waste, the reduced risk and earlier value from the gradual approach **outweigh its costs**." **That "outweigh" is asserted, never measured** — I could find no source quantifying it.)*

The Thoughtworks legacy-displacement series concedes the two-systems-forever outcome outright:

> "While many organizations give retirement of old systems as a key outcome for legacy modernization **it is not uncommon to find this doesn't actually happen, the legacy is still being used at the end**, with the associated business goals remaining unmet."
> — Cartwright, Horn & Lewis, <https://martinfowler.com/articles/patterns-legacy-displacement/>

> "**you _will_ have to invest in work that will be thrown away.**"
> — *Transitional Architecture*, <https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html>. The page prescribes removing the scaffolding and **cites no case where it was successfully removed.**

**Completion base rates, from the one longitudinal audit that exists.** The U.S. GAO named the 10 most critical federal legacy systems in June 2019. As of February 2025: **3 modernized, 7 not** (<https://www.gao.gov/products/gao-25-107795>). Six years. *(GAO does not attribute this to the strangler pattern; it is evidence about migration completion generally.)*

**Peer-reviewed, on how migrations actually end** — Ayas, Leitner & Hebig, *Empirical Software Engineering*, 2023, 19 interviews across 16 companies (<https://pmc.ncbi.nlm.nih.gov/articles/PMC10201508/>):

> organizations "will consider a migration **completed even if some elements of the system remain in the old form**"
> "migration project is more of an **on-going and re-occurring project rather than a one-off execution**"

**The human failure mode**, from someone who ran these at Stripe and Uber — Will Larson, <https://lethain.com/migrations/> and <https://lethain.com/migration-isnt-failing-due-to-lack-of-staffing/>:

> "**Two years later, engineers were quitting to avoid working on either side of the migration**: both the new, incomplete, services ecosystem and the old, stagnant, monolithic ecosystem."
> "If you leave one migration partially finished, folks will be exceedingly suspicious of participating in the next."

At N=1, "engineers quitting" reads as *Stan losing interest* — which is, per Coelho & Valente (§6.2c), tied for the leading cause of project death.

**And the academic ancestor reached the opposite conclusion from the modern pattern.** Bisbal, Lawless, Wu & Grimson (Trinity College Dublin, TCD-CS-1999-38, <https://publications.scss.tcd.ie/tech-reports/reports.99/TCD-CS-1999-38.pdf>) review Brodie & Stonebraker's *Chicken Little* — the strangler fig's direct intellectual forebear — and note that its coexistence gateways are so costly that a rival methodology, **Butterfly**, was designed specifically to eliminate them:

> Butterfly "assumes that while the legacy system must remain operable throughout migration, **it is not necessary for the legacy and target systems to interoperate** during this process. This assumption leads to the elimination of gateways, **avoiding the massive complexity they involve**."

**This is the strongest citation available for Stan's actual objection.** The cost of running two systems at once was examined in the peer-reviewed literature, judged prohibitive, and designed around — twenty-five years ago.

### 7.5 When each is correct — and which one this project is

**Incremental is correct when:** users cannot wait; stakeholders need visible partial value; the existing behaviour is not fully known; you cannot freeze feature work; the system is large enough that wholesale replacement is genuinely infeasible.

**Big-bang is correct when:** the "foundational nouns" change (Dropbox); the system is small enough to replace wholesale; there is no third party depending on continuity; and **you can freeze development on the old path.**

That last condition is a hard constraint, not a preference. Sam Newman:

> "**If we want to retain the ability to toggle between which implementation of the functionality is live, it's important that we shouldn't be adding new functionality or changing existing functionality until the migration is completed.**"
> — <https://www.infoq.com/articles/migrating-monoliths-to-microservices-with-decomposition/>

**And the pattern's own vendor documentation excludes this system by name.** Microsoft's reference page lists, under *"This pattern might not be suitable when"*:

> "**You migrate a small system and replacing the whole system is simple.**"
> — <https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig>

**Scoring this project against those criteria:**

| Criterion | This project | Points to |
|---|---|---|
| Users who cannot wait | Effectively none; no revenue, no competitor | **big bang** |
| Stakeholders needing visible partial value | One person, who is also the builder | **big bang** |
| System small enough to replace wholesale? | Rule engine = 19 files / 8,813 LOC. Yes by Microsoft's own carve-out | **big bang** |
| Existing behaviour fully known? | **No** — 789 lines unreproduced, 17 unsequenced mutators (§1.2) | **incremental** |
| Can you freeze work on the old path? | **No.** Corpus refinement is the work Stan actually wants to do | **incremental** |
| Are the "foundational nouns" changing? | No. Substrates, verse refs, ATU lines all stay | **neither — don't rewrite** |

**The two paths on offer each satisfy three of six criteria, and fail on the two that are hard constraints.** Behaviour is not known (so a big bang has no oracle) and development cannot be frozen (so an incremental migration will not converge, per Newman). That is not a close call between two options; **it is a signal that the precondition for either has not been met yet** — which is exactly what §10 proposes to fix, and exactly what §9-C0/C4 propose to do instead.

### 7.6 What I checked and refused to use

Rules of evidence cut both ways, so: I rejected several widely-circulated figures as unsourceable — "73% of microservices migrations fail," "68% of strangler projects stall before 90 days" (vendor marketing for modernization services), Weinberg's 20/40/60% context-switching ladder, and "50% of features are never used." I also could not verify a `parallel-run.html` page on martinfowler.com that several summaries cite — it 404s. **None of them appears above.** If a future proposal in this repo cites any of them, that is a signal, not a source.

---

## 8. Effort and duration estimate — the number the proposal never gives

**Assumptions, stated so they can be attacked:**

1. **One part-time human at ~6–10 focused hours/week**, plus an LLM agent with effectively unbounded code-production capacity.
2. **The binding constraint is Stan's review bandwidth, not code volume.** Evidence: 6 test files in 464; zero CI; validator baselines that are bare integers; retraction→promotion never fired in the program's history; a 789-line drift undetected for 65 days. Every one of those is a review-capacity failure, not a coding failure. Estimates denominated in lines of code will be wrong by an order of magnitude in the optimistic direction.
3. **Therefore the unit of estimation is *decisions Stan must make and verify*,** and the canon's own discipline (§7.3 adversarial audit, bidirectional-test walkthrough per rule) sets the per-decision cost at ≫ 10 minutes.
4. Scope: 5 live sites, ~108,000 ATU lines, 464 authored Python files / 151,079 LOC, of which the load-bearing rule surface is **19 files / 8,813 LOC**, plus 75 validators / 31,016 LOC, plus ~19,000 lines of reader-shell HTML/JS.

### The work, sized

| Work item | Sizing basis | Stan-decisions | Elapsed at 6–10 h/wk |
|---|---|---|---|
| Case schema + record | Small code, but a schema is a design commitment that must be got right once | ~10 hard | 3–6 weeks |
| Unify the rule surface into one executable spec language | ~100 rules total: 62 Tanakh YAML specs + ~20 BoFM in-code + ~15 GNT. Canon requires a bidirectional walkthrough each | **~100** | **20–40 weeks** |
| Generalise the spec engine across 3 substrates | Tanakh's `SpecRunner` is Hebrew-coupled: `morphology.py` is 3,094 LOC with a te'amim constraint baked in | ~15 | 8–16 weeks |
| Regression control (must precede everything) | §10 — the cheap version is 1–2 days; the per-violation version is weeks | ~5 | 1–4 weeks |
| Unify 4 near-identical reader shells | 70–95% similar already | ~10 | 3–6 weeks |
| Bring BoFM's shell in | 13% similar; PWA + service worker + Firestore + 3,043 LOC JS | ~25 | 8–16 weeks |
| Audio realignment | 478 files, index-coupled, already desynced, non-regenerable | **unbounded** | 4 weeks–never |
| Retire the old path per corpus | 5 sites | ~10 | 4–8 weeks |

### The two paths

| | **Path A — greenfield core** | **Path B — complete the abandoned direction** |
|---|---|---|
| Elapsed, optimistic | 9 months | 6 months |
| Elapsed, central | **14 months** | **11 months** |
| Elapsed, pessimistic | 24 months+ | never completes; hybrid becomes permanent |
| Dominant risk | no baseline ⇒ every one of ~108,000 lines is unverified | stalls at 70% and stays there |
| Can you stop halfway with a working product? | Only if the old path is kept whole — which contradicts the cost table's row 2 | **Yes, at every step** |
| What kills it | Stan's review queue saturates and the new engine ships unverified | the two-system period outlasts motivation |

**Confidence: LOW on the absolute numbers, HIGH on the ordering and the shape.** Neither is a three-month job. Both are dominated by the ~100 rule adjudications, and that term is nearly identical in both paths — which means the greenfield-vs-completion choice moves maybe 20% of the total cost. **The choice the proposal frames as architectural is not where the money is.** The money is in the rule count and Stan's hours, and neither path reduces either.

**The estimates above assume corpus work stops.** They should be read against Newman's convergence constraint (§7.5): a migration that keeps changing the functionality of the old path does not converge. Corpus refinement — new binding rules, override adjudication, deploying a better Isaiah — is the work Stan actually wants to do and the only work that produces a better reader. **Either path asks him to stop doing it for roughly a year.** If he does not stop, add 50–100% to every row above, and raise the probability of the "never completes" outcome accordingly. This is the assumption most likely to be violated, and no version of the proposal states it.

### The estimate that matters more

| Alternative | Elapsed | Stan-decisions |
|---|---|---|
| Reproducibility gate, all corpora (§10) | **1–2 days** | 1 |
| Archive the 127 one-off 5-machinery/scripts (37,821 LOC, 25% of the codebase) | 1 day | 1 |
| Pin dependencies + substrate versions | 1 day | 0 |
| Offsite backup of the 1.9 GB unbacked substrate | half a day | 1 |
| Add CI running the existing validators | 2–3 days | 1 |
| Port the Tanakh spec pattern to one more corpus (§9, option C4) | 3–6 weeks | ~15 |

**Six items, under two weeks total, that remove four of the five things a risk manager would refuse to sign off on — and none of them requires the architectural decision to be made.**

---

## 9. The third options the proposal never tabled

```
$ grep -rn -iE 'freeze|do nothing|status quo|retire (a )?corpus|shrink scope|stop building' 4-process/*.md
4-process/proposal-loop-3.md:242: [unrelated — "freeze a correct rule change"]
```

**CONFIRMED: no document in `4-process/` considers not restructuring.** The option set presented to Stan is {build A, build B}. Here are the missing ones, in increasing order of ambition.

### C0 — Freeze
Change nothing structural. Fix the 789-line drift, fix the audio, and keep shipping corpus work. **Cost: near zero. What it forfeits:** nothing that is currently earning. Four of the six defects in this audit are fixable inside a freeze. This deserves to be a row in the cost table, and its absence is the strongest evidence that the table was built to compare builds rather than to decide whether to build.

### C1 — Fix the record only, leave the architecture alone
The `Pending-Decisions` diagnosis is that *one* thing is missing — a decision record — with six symptoms. If that diagnosis is right, then **the decision record is the whole intervention**, and Parts 3–8 of the proposal are a separate project that happens to be adjacent. The proposal itself concedes this: *"we do not need a greenfield to start recording them properly."* Nothing in the case for restructuring follows from the case-record diagnosis.

### C2 — Shrink scope by retiring corpora
LXX and Vulgate have **1 validator each, 0 5-machinery/tests, 22 and 34 authored files**, are absent from the deployment record, and between them hold 1.84 GB of unbacked private substrate. Freezing them (leave the sites serving, stop developing) removes **2 of 5 sites from every future cascade** at zero cost to any current reader. That is a larger reduction in coordination surface than anything in Part 5, and it takes an afternoon.

### C3 — Delete the dead weight
127 files / 37,821 LOC — **25% of the entire codebase** — are one-off scans, audits, diagnostics and probes (`scan_*`, `audit_*`, `diag_*`, `inspect_*`, `enumerate_*`, `extract_*`). Archiving them shrinks what any future maintainer must navigate by a quarter, cannot break anything (nothing imports them into a build path), and costs a day. Cognitive load is the decisive axis by the proposal's own argument; this is the single largest cognitive-load reduction available anywhere, and it requires no architectural decision.

### C4 — Port the pattern that already works ★
**This is the option the proposal missed because it did not know the asset existed.**

```
$ ls readers-tanakh/validators/specs/*.yaml | wc -l
62

$ head -12 readers-tanakh/validators/_shared/spec_runner.py
"""Spec-driven validator engine.

Specs are YAML files in `validators/specs/` declaring trigger conditions,
guards, severity, and annotation per rule. Adding a new colometric rule =
write a new YAML spec; no Python code change.
"""

$ cat readers-tanakh/validators/specs/h13_bare_subordinator.yaml
name: h13_bare_subordinator
rule: H13
subcase: bare_subordinator
severity: STRONG-MERGE-CANDIDATE
description: |
  Bare subordinator (אֲשֶׁר alone on a line) cannot stand alone...
trigger:
  line_n_first_token: {skeleton_in: [אשר]}
  line_n_last_token:  {skeleton_in: [אשר]}
  combined_max_prosodic_words: 10
guards:
  - next_line_is_vav_coord_pp
  - next_line_is_vav_coord_np
  - next_line_is_wayyiqtol
  - next_line_is_purpose_infinitive
annotation_template: "Bare subordinator forward-merge ({pwc} prosodic words)"
suggested_action: MERGE

$ (schema uniformity across all 62)
field presence: name 62, rule 62, subcase 62, severity 62, description 62,
                trigger 62, annotation_template 62, suggested_action 62,
                guards 53, mode 7
severities: STRONG-MERGE-CANDIDATE 55, STRONG-SPLIT-CANDIDATE 7
actions:    MERGE 55, SPLIT_AT_FINITE_VERB_BOUNDARY 5, SPLIT_AT_VAV_* 2

$ grep -rn 'SpecRunner' readers-tanakh/scripts readers-tanakh/validators --include=*.py
5-machinery/scripts/apply_specs.py:306:    runner = SpecRunner(args.specs)      # applies the rules
5-machinery/scripts/run_validators.py:31:  from validators._shared.spec_runner import SpecRunner   # checks the rules
```

Read the proposal's specification of what must be built, then read that YAML again:

> "**Specification** | Rules as **executable artifacts** — one per rule, versioned, parameterised per corpus." (Part 1, component 3 — scored ❌ "Prose, re-implemented per repo")
> "**The fix is to make them two faces of one artifact.**" (Part 3, Correction B)
> "**Single source.** The check is generated from — or paired in one artifact with — the rule." (Part 7, mechanism 1)

One artifact. `suggested_action: MERGE` is the apply face; `severity: STRONG-MERGE-CANDIDATE` is the check face. 62 of them. 100% uniform schema. Applied by `apply_specs.py`, checked by `run_validators.py`, engine at `spec_runner.py` (1,375 LOC), in the largest corpus in the system.

**The proposal scores components 3 and 6 as ❌ absent and proposes to design them from first principles.** They exist. **CONFIRMED. SERIOUS — this changes the recommendation**, because porting a working, in-house, already-debugged pattern to two more corpora is a categorically cheaper and vastly more legible proposition than designing a new one — and it is legible precisely because Stan can read one YAML file and see the whole idea.

### C5 — Document-then-decide
Write down what each of the five pipelines actually does, end to end, in one page each, verified by running it. This audit did that for two of five in a session, and it produced F1, F2, F3 and F8 — four findings that change the decision. **Three more pages would probably change it again.** Deciding architecture before the pipelines are described is deciding on a map drawn from memory; §1.2, §5.1 and §9-C4 are all cases where the map was wrong.

---

## 10. The cheapest next step that produces real information

**Build the reproducibility gate. One to two days. It is path-independent, it is already half-written, and it has already found a real defect.**

```
for each corpus:
    regenerate the deployed layer from the deployed inputs, to a temp dir
    diff against what is deployed
    report: lines deployed, lines regenerated, lines not reproduced
    exit non-zero if the count is not zero, or not equal to a recorded, dated, approved allowance
```

Why this and not the behavioural snapshot:

| | Behavioural snapshot (proposal) | Reproducibility gate |
|---|---|---|
| Cost | instrument 19 generators + 32 mutators across 3 substrates | ~100 lines of Python |
| Works on BoFM? | **No** (§1.2) | Yes — and it is what *detects* that it doesn't |
| Needs a schema decision first? | Yes | No |
| Path-dependent? | Value differs 10× by path (§2) | Identical value on every path, including freeze |
| Already produced a finding? | — | **Yes: 789 lines, 14 books, 65 days** |
| Reviewable by Stan in one sitting? | 108,000 lines | one integer per corpus |

That last row is the point. The proposal's artefact produces something Stan cannot read; this one produces **five integers**, and the correct value of all five is zero. That is a gate a part-time maintainer can actually hold, and holding it is what makes every later decision safe.

**Then, in order, and each one independently useful:**

1. Pin the environment — one `requirements.txt` per repo, and record the three substrate HEADs plus the BHSA TF version in a file that the gate reads.
2. Get the 1.9 GB of unbacked substrate offsite.
3. Put the existing validators in CI, so the gates survive the machine.
4. Archive the 127 one-off 5-machinery/scripts.
5. Fix the drift: regenerate the 14 stale BoFM books, adjudicate the 789 lines, and decide the audio question.
6. *Then* — with a working gate, a pinned environment, a backup, and a quarter less code — revisit the architecture. It will be a different and much easier conversation, and several of its premises will have changed.

---

## 11. What a risk manager would refuse to sign

### Backup — FAIL

```
$ du -sh readers-*/private
 29M    readers-tanakh/private        [local only]
2.5G    readers-bofm/private   -> /c/Users/bibleman/Dropbox/bom-reader-private
343M    readers-gnt/private    -> /c/Users/bibleman/Dropbox/gnt-reader-private
438M    readers-lxx/private           [local only]
1.4G    readers-vulgate/private       [local only]

$ find readers-* atu-method -maxdepth 3 -type l
readers-bofm/private
readers-gnt/private
```

Two repos symlink their substrate into Dropbox; **three keep ~1.87 GB on one disk with no offsite copy.** The inconsistency is worse than either policy applied uniformly, because nothing tells you which repo is which. Additionally, `readers-bofm/.venv` (922 MB) is gitignored and is the *only* record of the runtime that produces the deployed corpus (§1.5). Tracked content is safe — all six repos have GitHub remotes — but tracked content is not what breaks.

Two further consequences nobody has written down: a `git clone` of `readers-bofm` or `readers-gnt` on a second machine produces a **dangling symlink** and a build that fails in a way that looks like a code bug; and `biblical-corpora/` is not a git repository at all (three independent upstream clones in a plain directory), so re-acquiring it is possible but the *versions* are not recoverable.

### CI and gates — FAIL

```
$ for r in atu-method readers-*; do echo -n "$r: "; ls $r/.github/workflows/ 2>/dev/null; echo; done
atu-method:
readers-tanakh:
readers-bofm:
readers-gnt:
readers-lxx:
readers-vulgate:
```

**Zero CI in every repo.** The only automated gate is a local pre-commit hook, present in 3 of 6. The hooks are tracked (`validators/hooks/pre-commit`, plus an `install.sh` in tanakh and bofm) — so they are recoverable — but installation is manual, per-machine, bypassable with `--no-verify`, and unenforced by anything. **`atu-method` — the repo the proposal concentrates everything into — has no hook and no tracked hooks at all.**

### "What if Stan is unavailable for a month mid-migration?"

**This question has already been answered empirically, and the answer is bad.** A rule change was regenerated into 1 of 15 books on 2026-06-05 and the other 14 were never caught up. **65 days.** Zero detections. During that window 35 commits landed, 75 validators existed, three pre-commit hooks were installed, and a "single source of truth" deployment record was maintained. None of them noticed, because none of them was capable of noticing: the validators check conformance to canon, not agreement between code and product.

A month's absence mid-migration, under either proposed path, produces the same class of outcome with a larger surface. The mitigation is not a better plan; it is **a gate that fails loudly and reads as one integer** (§10).

### Rollback — PARTIAL

Per-repo `git revert` works today for tracked content, and the publish stage is byte-reproducible (§1.4), so a bad text change can be reverted and rebuilt exactly. That is genuinely good and worth protecting. **The proposal's force-push publish-target model removes it** for the site repos, and the 1.5 GB of audio has no regeneration path at all.

### Blast radius — undocumented

5 live domains · ~108,000 ATU lines · 1,045 tracked HTML files · 478 audio files · 2.7 GB of git history in one repo. Nothing in the proposal states it.

### Dirty tree at the starting line — MINOR but telling

```
readers-bofm    23 changed files (incl. Pending-Decisions.md, retraction-log.md, build_book.py)
readers-tanakh   7 modified corpus files under data/text-files/v2-pipeline-draft/
readers-lxx     13 untracked 5-machinery/scripts
readers-gnt      9 changed
```

Uncommitted corpus and build-script edits exist in three repos right now. A migration that begins from this state cannot distinguish its own effects from work already in flight.

---

## What survives

**Of the proposal:**

1. **"A rule and its validator are two faces of one artifact."** Correct, load-bearing, and the single best idea in the document. It survives audit fully — and it survives *better* than the proposal knows, because `readers-tanakh` has already implemented it 62 times (§9-C4).
2. **The reader UIs are one application, forked.** True for four of five, measured at 70–95% similarity. Unify those four; treat BoFM separately.
3. **The arbiter question is upstream of the rebuild's validity.** Right, and honestly stated. Wrong as Gate 0 (§3).
4. **Part 9's self-criticism is the most reliable section in the document.** "The 31-shared-lines figure I used as evidence of accidental divergence may instead be evidence that the divergence is justified" is a better instinct than the argument it undercuts. Under measurement the figure does not reproduce at all, and the four-of-five UI similarity says unification is right anyway — for a different reason than the one given.
5. **Publish works.** Better than the proposal credits: it is the only component that reproduces byte-for-byte.

**Of the retraction:** the *instinct* — that engineering cost is not total cost, and that a design cheaper for the agent and harder for Stan is the wrong trade — is exactly right and should govern everything. The table built to express it does not express it (§4).

**Does not survive:**

- "'What' is recoverable" — **not on BoFM, and elsewhere it is already in git** (§1).
- "Equally valuable to both paths" — value ranges from impossible to already-free (§2).
- "Gate 0 terminates the plan cheaply" — it terminates only the rebuild, and it is the least cheap question in the document (§3).
- "Greenfield = lower cognitive load because the old thing is frozen" — the old thing serves five live sites throughout, under both paths (§4).
- "Greenfield = bounded error discovery because everything gets tested" — 6 test files in 464, 0 CI (§4).
- "Convert readers one at a time" — as specified, it deletes 1.5 GB of non-regenerable audio and omits a live site (§5).
- Components 3 and 6 scored ❌ — **they exist, working, with 62 rules in them** (§9-C4).

**And one thing survives that neither document claimed — Stan's objection is the best-evidenced position in the whole exchange.** He said the completion path might not be "COGNITIVELY cheaper for me to wrap my head around." Three independent lines of evidence support the *general* form of that worry, and none supports either proposed remedy:

- The peer-reviewed literature examined gateway-mediated coexistence in the 1990s, judged its complexity prohibitive, and designed a methodology (**Butterfly**) specifically to avoid it (§7.4).
- The only empirical study of decision records reports they address documentation culture, knowledge transfer and prioritisation — and **stop working at the distributed/hybrid boundary** (§6.2d).
- The pattern's own custodians concede that "the legacy is still being used at the end," and the one longitudinal audit found **7 of 10 systems unmodernized after six years** (§7.4).

He was right, he was right for a better reason than he gave, and the correct response to being right about a cost is not to pick the other build.

---

## If I were advising Stan in one paragraph

You are being asked to choose between two large builds, and the honest finding is that **the choice barely matters compared to what it is distracting you from.** Both paths cost roughly a year of your part-time attention, both are dominated by the same ~100 rule-by-rule adjudications that only you can make, and neither of them fixes the thing that is actually wrong right now — which is that your Book of Mormon reader has been serving 789 lines that the code no longer produces, for 65 days, because a rule change was regenerated into one book out of fifteen and nobody noticed; and separately, three-quarters of the narration cues in Helaman point at line numbers that do not exist any more. Neither of those is an architecture problem. Both would have been caught by a ninety-second script that regenerates each corpus and diffs it against what is deployed, and that script is one to two days of work, is useful under every possible future including doing nothing, and produces exactly five integers for you to look at — all of which should be zero. Build that first, pin your dependencies, get the 1.9 GB of substrate that exists on one disk backed up, put your existing validators in CI so the gates survive your machine, and delete the quarter of your codebase that is one-off 5-machinery/scripts nobody will ever run again. That is under two weeks and it removes almost every risk in this audit. Then, before you decide anything architectural, look at `readers-tanakh/validators/specs/` — because the "rules as executable artifacts, one artifact with an apply face and a check face" that the proposal says is missing and proposes to design from scratch is **already built there, running, with 62 rules in it**, and you can read one of those YAML files in ninety seconds and understand the entire idea. If that pattern is right, the next move is not a rebuild; it is porting a thing you already own to two more corpora. Be sceptical of the cost table specifically: it gives the greenfield credit for freezing the old system while your five live sites keep running on it, and credit for being well-tested against a project with six test files and no CI — so the axis you were told is decisive was scored on two properties that are not real. And know that neither path currently meets its own entry conditions — a clean-sheet rebuild has nothing to check itself against until the reproducibility gate exists, and an incremental migration is documented not to converge unless you stop doing corpus work for about a year, which is the only part of this you actually enjoy. **Your instinct that this would not be cheaper for you was correct, and it was correct for a better reason than you gave**: the one empirical study of the standard remedy for a maintainer in your position finds that it works on everything except systems split across two architectures — which is the state both proposals would put you in, deliberately, for a year. So the honest recommendation is: fix the four measured defects, keep shipping corpus work, and let the architecture question wait until you have a gate that tells you when something breaks. If in six months the gate is green every week and you still feel the machinery is unmaintainable, that is a much better-informed moment to decide, and you will have lost nothing by waiting.
