---
cssclasses:
  - wide
---

# Master proposal v3 — greenfield in atu-method, sites as the artifact

> **Plain-language version.** This is the third version, and the first one written *after* going and reading what the outside world knows. Four audits brought back 130 sources; the ones that change a decision here are logged in [[2-evidence/external-practice.md|external-practice.md]]. The recommendation is now **greenfield inside `atu-method`**: one repo, a designed baseplate, proven pieces copied in rather than rewritten, the reader repos retired, and the five live sites re-pointed as pure build output. Nothing carried over is treated as correct until it is re-derived.

**Status: PROPOSAL. Nothing adopted.** 2026-08-09. Supersedes [[4-process/master-proposal-v2.md|v2]]; [[4-process/master-proposal-rebuild.md|v1 is withdrawn]].

**What is new in v3, and it is the point:** v1 and v2 argued from my reasoning. v3 argues from **evidence the audits went and got**. Where the literature contradicts what I proposed, the literature wins and I say so.

> ## ⚠ AMENDED 2026-08-09 — two inputs that reorder this document
>
> ### A. Stan's reframe: this is an SDLC problem, and we have been running two phases of four
>
> > *"i am intrigued that i have not really thought of this as a software development problem, but it seems that it matches the software development cycle paradigm? to rebuild we need requirements → design → implementation → deployment?"*
>
> **Yes — and naming it exposes the actual defect more precisely than anything in the four audits.** This project has been running **implementation → deployment** for three years, with no requirements phase and no design phase. Everything diagnosed since 2026-08-06 is a symptom of those two absences:
>
> | Symptom | Missing phase |
> |---|---|
> | 75 validators and "no guarantee they are correct" | **Requirements** — a validator is only correct *relative to a stated requirement*, and none was ever written |
> | 17 in-place mutators, order recorded nowhere | **Design** |
> | Rules as prose, re-implemented per repo | **Design** — no specification artifact |
> | No acceptance criterion for "is this segmentation right" | **Requirements** |
> | Loops written up *after* the machinery accreted | Both — "assembled and then described" |
>
> **The V-model makes the validator problem exact.** Each development phase pairs with a verification level: requirements ↔ acceptance 5-machinery/tests, design ↔ integration 5-machinery/tests, implementation ↔ unit 5-machinery/tests. We built the bottom-right (75 validators) with nothing on the left for them to verify *against*. **That is why they cannot be trusted, and why adding more would not help.**
>
> **And it reframes Gate 0 usefully.** "Is there an external arbiter?" has been treated as an epistemology problem. It is a **requirements** problem: *what does correct output look like, and who says so?* That is the first requirement of the system, it has never been written down, and it is Stan's to answer rather than mine to discover.
>
> **One honest qualification.** This is not an argument for waterfall — the audits' own evidence (Flyvbjerg's overrun distribution; ADRs failing at the hybrid boundary) favours iterating with gates. And research software has genuinely evolving requirements, since the correctness criterion here is contested. **But that is an argument for writing requirements down and versioning them, not for continuing without them.**
>
> ### B. The workflow consult: v3 is machinery Stan cannot debug
>
> From `~/Downloads/Claude-Streamlining reader project development workflow-20260809-1802.md`, logged at [[2-evidence/external-practice.md|external-practice.md §9]]. That session knew Stan is not a coder and walked back its own advice:
>
> > *"Automation you can't diagnose isn't leverage — it's a new failure mode that stops your work cold."*
>
> **v3 proposes Actions deploys, content-hash lockfiles, a spec engine, a calibrating lint runner, an approval workflow, ADRs, DORA metrics and WindowDiff — and never asks whether Stan can operate any of it.** That is a real design defect.
>
> **The fix is a sequencing rule: phase by BLAST RADIUS, not by dependency.** A bad skill makes an ignorable suggestion; a bad hook fires at every session start and can block every repo at once. So: **skills that suggest → hooks that enforce → autonomous workflows last.** §4's sequence below is ordered by dependency and should be re-ordered by blast radius.
>
> **Mechanisms adopted into the plan** (detail in §9 of external-practice): `save`/`undo` as the entire git interface · GitHub Desktop for visual diffs, which is the missing check against *my* error rate · tags on known-good states · **deploy previews**, the cheapest guardrail we lack · **version-stamping chapters with the rules version**, which turns staleness into a computed fact and is a better answer to the BoFM drift than regenerate-everything · touch-tax + ratchet so debt can shrink but never grow · `forward-only` rules · rules carrying their own reach (`applies-to: bom, gnt`).
>
> **A better headline metric than the one I built:** *"you re-explain your conventions to Claude less often each month."* That measures the return leg directly; link density only measures prose integration.
>
> **And one conflict I will not resolve silently:** the consult recommends `claude plugin init`, which scaffolds into the **global** `~/.claude/skills/`. Stan's standing rule is that project skills live in `./.claude/skills/` and never the global bucket, because machine state does not travel. **Flagged for him.**

---

## 1. The decision

**Greenfield inside `atu-method`. One repo. The five sites become build output.**

Stan: *"we can then retire/delete those other repos and re-point the SITES (the real artifact we care about)."* That is the right ordering of what matters, and it dissolves three problems at once rather than patching them:

- **The exposure ends by construction.** Serving `sites/` — build output only — means there is no source tree, no [[CLAUDE.md]], and no tracked `private/` file in the served path. Verified live today: four `private/` files and [[CLAUDE.md]] on four domains return 200.
- **The five-way cascade ends**, because there is one implementation.
- **The unreproducible corpus is confronted rather than inherited**, because regeneration becomes the only path to deployed text.

### Three independent findings now point the same way

1. **Strangler-fig is contraindicated by its own documentation at this scale** — Microsoft's guidance says it is "not suitable when… you migrate a small system." My v1 proposed exactly that pattern.
2. **ADRs help everywhere except the hybrid boundary** (Ahmeti et al., ECSA 2024) — direct evidence against a long half-migrated state.
3. **The polyrepo case is almost entirely organisational** (Nx, LogRocket, Buildkite; Potvin & Levenberg, CACM 2016) — worth approximately nothing for one developer.

None of these came from me. All three argue against the position I held through two drafts.

## 2. The baseplate

```
atu-method/                     ← ONE repo
  CLAUDE.md                     the schema — BUDGETED; amendments name what they displace
  00-start-here.md · Current-Tasks.md · Pending-Decisions.md

  1-method/                     NORMATIVE — framework, rule catalogs (prose canon)
  2-evidence/                   MEASURED — findings · approval-log.jsonl · growth-data.csv
  3-implementation/             ARCHITECTURE — contracts + decisions/ (ADRs)
  4-process/                    GOVERNANCE — loops, protocols, log.md, lessons.md
  5-machinery/                  CODE — the architecture / building / maintenance bin
      engine/                   v0 → v1 → v1.5 → v2, one implementation
      specs/                    YAML rules — one artifact, apply face + check face
      lint/                     every checker, each carrying calibration assertions
      app/                      one UI, per-corpus config
      build/                    corpus → site
  corpora/                      per-corpus data packages (substrates gitignored, hash-locked)
  sites/                        BUILD OUTPUT ONLY — published by GitHub Actions
```

`5-machinery/` absorbs today's `atu_method/`, `5-machinery/scripts/`, and the five repos' scattered validators — Stan's "architecture, building and maintenance bin", and the name `readers-bofm` already uses.

### The three organs, kept distinct because merging them merges different things

| Organ | Location | Records | Cadence |
|---|---|---|---|
| **Operations log** | `4-process/log.md` | what **we** did — `## [date] op \| title`, parseable | every operation |
| **Approval log** | `2-evidence/approval-log.jsonl` | what the **system** decided, per verse | every regeneration |
| **Lessons** | `4-process/lessons.md` | **corrections** awaiting promotion to a rule or guard | captured always, **promoted only by audit** |

The operations log is what makes lint affordable — it scopes a pass to what changed. Lessons' failure mode is the worry-bead pattern: collecting corrections instead of promoting them, which is what this session did by writing seven documents about a decision record while building none.

**Renamed from "decision log" to APPROVAL LOG, on the literature's advice.** Emily Bache's argument is that "snapshot" implies no duty of care while "approval" foregrounds that a human approved the content. Given Stan's reframe — the deployed corpus may be wrong — **bug lock-in is not a risk here, it is the expected state**, so rows must land `unreviewed` and require an explicit verdict. `5-machinery/scripts/decision_log.py` already writes `status: unreviewed`; it gets renamed and gains a review path.

### Lint as a precondition, not a habit

`5-machinery/lint/` holds every checker, and the runner **refuses to report unless each checker's calibration assertions pass** — a known-good it must find, a known-bad it must not. Four detectors were miscalibrated in a single day, including one inside an audit dispatched to enforce discipline. A remembered rule is an unapplied rule. `decision_log.py` implements this and passes three poles.

**And we need a real segmentation metric.** The project currently uses `cardinality match`, which scores `[AB][CD]` and `[A][BCD]` as a perfect match — and it steered two LXX refinement rounds. WindowDiff, *P<sub>k</sub>*, boundary similarity and γ exist for exactly this. **Every historical segmentation number should be treated as uncalibrated until re-measured.**

## 3. What is carried, what is left, and what is authoritative

**Carried — copied, not rewritten:** the 62 YAML specs and `spec_runner.py`; `atu_method/`; `tx_log.py`; the GNT pipeline and `build_book.py` (both reproduce today); substrates; the 1.5 GB of audio; rule catalogs; closed-route knowledge.

**Left behind:** the 17 in-place mutators; hand-maintained `index.html` shells; repo-root Pages serving; dead-baseline validator sprawl; per-repo [[CLAUDE.md]] personas.

**Nothing inherited is canonical.** Prose canon enters provisional. Every approval-log row lands `unreviewed`. The 911 `overrides.json` entries are carried as **claims, not verdicts** — they never had warrants. Agreement between old and new corroborates; **divergence localises where the old work was wrong, and is the product rather than the failure.**

## 4. Sequence

**Step 0 — lock the inputs.** Pin every dependency by content hash; back up the ~1.87 GB substrate offsite. **This is a precondition, not a follow-up**: a baseline whose inputs can move proves nothing, and a clean diff would be meaningless. Zero lockfiles exist today and `use("etcbc/bhsa")` is unpinned.

**Step 1 — stop the live exposure.** `git rm --cached` the five tracked `private/` files. Independent of everything else, and currently leaking.

**Step 2 — the approval log across every corpus.** Built and calibrated. Emits per-verse divergence at `status: unreviewed`. GNT should read zero; BoFM will not.

**Step 3 — prove the spec pattern on the hardest case.** Express **one** BoFM rule as a YAML spec under `spec_runner`, retire its mutator, regenerate, diff. Tests whether a Hebrew-shaped runner can carry an English rule, on the smallest surface that can falsify it. If it cannot, this plan dies here, cheaply.

**Step 4 — build `sites/` and cut over one domain.** `vulgate-reader.com` first: 19 commits, no engine imports, nothing irreplaceable. Publish via `actions/deploy-pages`. **The 1.5 GB of audio needs its own answer** — it already exceeds GitHub's documented 1 GB Pages ceiling, so release assets, an external host, or LFS, decided before BoFM cuts over.

**Step 5 — the rest, one corpus at a time**, each with its approval log at zero-or-approved before cutover.

**Gate 0 has not gone away.** Te'amim are disqualified — they generate the deployed Hebrew. Of the three candidate arbiters only Skousen's lineation and Marschall's bands remain, both contested. The available fallback is the §2.1 bidirectional test applied fresh to each divergence: not external ground truth, but a real adjudication, bounded to the divergences.

## 5. The honest risk budget

The famous rewrite-failure statistics are unusable — the Standish CHAOS figures were demolished by Eveleens & Verhoef across 5,457 forecasts, and the audit correctly refused to cite them. **The one sound dataset** is Flyvbjerg & Budzier (n = 1,471 IT projects): **average 27% cost overrun, and one in six a "black swan" at roughly 200%.**

So: plan for ~27% over, accept a real ~1-in-6 chance of roughly triple, and **make Step 3 the falsification point** so the expensive part is never entered on faith.

**Truck factor.** This project is TF = 1, which the literature says is *normal* — 57% of 1,932 projects (Avelino et al., ICSME 2019) — and 41% of projects that lost their TF developer survived anyway. But "low maintainability" is a named cause of project death (Coelho & Valente), and that is precisely the condition Stan reported. The offsite substrate backup in Step 0 is the single highest-value insurance available.

## 6. What this still gets wrong

- **I have changed position three times in this session**, each after Stan pushed. The reasoning is now chained to external evidence rather than to my preference — but the pattern warrants suspicion, and v3 should be audited as adversarially as v1 was.
- **`spec_runner` is Hebrew-shaped.** Step 3 exists because it may not port; the last time I assumed cross-corpus portability, the LXX experiment had already disproved it.
- **The audio problem has no answer yet**, only a deadline.
- **I have not re-read the external papers** — they are the auditors' sourcing, recorded with URLs so any can be checked before it is relied on. One audit finding I *did* check turned out false.
- **The arbiter question is unresolved**, so some divergences may be unadjudicable. If that is common rather than rare, the whole compounding premise fails and this becomes a reliability project, which is a smaller and more honest thing.
