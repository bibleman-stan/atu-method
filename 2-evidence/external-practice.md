---
cssclasses:
  - wide
---

# External practice — the research the audits brought back

> **Plain-language version.** Four commissioned audits went and read the outside literature — 130 distinct sources. Leaving that in four audit files would be the same accumulate-don't-integrate failure this project keeps diagnosing, so this page pulls out what actually changes a decision here, organised by the decision it changes. Sources are cited so a claim can be checked rather than trusted.

**Filed 2026-08-09** from [[4-process/audit-linguistic.md|audit-linguistic]], [[4-process/audit-repo-architecture.md|audit-repo-architecture]], [[4-process/audit-web-design.md|audit-web-design]], [[4-process/audit-migration-cost.md|audit-migration-cost]]. 130 unique URLs harvested; the ones below are those that bear on a live decision.

---

## 1. Characterization / snapshot testing — it has documented failure modes, and a better name

This bears directly on `scripts/decision_log.py` and on the whole "capture what the system currently does" idea.

| Finding | Source |
|---|---|
| The technique is standard for legacy systems whose behaviour is undocumented | Feathers, *Characterization Testing* — <https://michaelfeathers.silvrback.com/characterization-testing> |
| **Bug lock-in** — "you may commit code with a bug and a snapshot that ensures that the bug is still there" | Sapegin — <https://medium.com/@sapegin/whats-wrong-with-snapshot-tests-37fbe20dfe8e> |
| **Rubber-stamping** — "when tests fail, it is very easy to update the snapshots without fixing the code" | Gazzinelli Cruz, Rocha & Valente, *JSS* 204 (2023) 111797, D34 |
| **Nobody reads it** — "a snapshot that's over 640 lines long. Nobody reviews it" | Kent C. Dodds — <https://kentcdodds.com/blog/effective-snapshot-testing> |
| **Non-determinism** is the most frequent practical problem; mitigation is canonicalisation at capture | Fujita, Kashiwa, Lin & Iida, IEEE ICSME 2023; JSS 2023 D14 |
| **Naming changes behaviour**: "snapshot" implies no duty of care; "approval" foregrounds that a human approved it | Emily Bache, via *Understand Legacy Code* — <https://understandlegacycode.com/blog/characterization-tests-or-approval-tests/> |

**What this changes.** Bug lock-in is not a risk here — it is the *expected state*, since Stan's reframe says the deployed corpus may be wrong. So the instrument must be an **approval log, not a snapshot**: rows land `unreviewed` and require an explicit human verdict to become authoritative. `decision_log.py` already writes `status: unreviewed`; the naming and the review step should follow Bache.

## 2. A baseline is meaningless if the inputs can move — lock dependencies first

Content-hash lockfiles are the canonical mechanism (DVC's `dvc.lock` captures hashes of every dependency).

**What this changes.** **Zero lockfiles exist across five reader repos, and `use("etcbc/bhsa")` is unpinned** *[audit, unverified by me]*. So dependency pinning is a **precondition** of the reproducibility gate, not a follow-up — otherwise a clean diff proves nothing and a dirty diff cannot be attributed.

## 3. Cognitive load — the axis Stan named is empirically grounded

| Finding | Source |
|---|---|
| Developers spend ~58% of time comprehending, not writing — 78 professionals, 7 projects, **3,148 instrumented hours** | Xia, Bao, Lo, Xing, Hassan & Li, IEEE TSE 44(10), 2018 |
| Resumption after interruption is expensive — **10,000 sessions, 85 programmers**; only ~10% of sessions resume coding within a minute | Parnin & Rugaber, ICPC 2009 — <https://chrisparnin.me/pdf/parnin-icpc09.pdf> |
| **Architecture Decision Records demonstrably help — except at the hybrid boundary** | Ahmeti, Linder, Groner & Wohlrab, ECSA 2024 — <https://rebekkaa.github.io/files/2024_ECSA.pdf>; origin: Nygard — <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html> |

**What this changes.** Two things. First, it is independent support for weighting cognitive legibility over engineering effort — Stan works in interrupted sessions, which is the worst case in Parnin & Rugaber. Second, **ADRs should be adopted**, and the finding that they underperform *at the hybrid boundary* is direct evidence against a long half-migrated state — i.e. for greenfield over strangler-fig here.

## 4. Truck factor — this project is the worst case, and it is survivable

| Finding | Source |
|---|---|
| **65% of 133 popular GitHub projects have truck factor ≤ 2**; 34% have TF = 1 | Avelino, Passos, Hora & Valente, ICPC 2016 — <https://arxiv.org/pdf/1604.06766> |
| **57% of 1,932 projects have TF = 1**; 16% lost their TF developer, and **41% of those survived anyway** | Avelino, Constantinou, Valente & Serebrenik, ICSME 2019 — <https://arxiv.org/pdf/1906.08058> |
| Deprecation causes: lack of time 18, lack of interest 18, **low maintainability 7** | Coelho & Valente, ESEC/FSE 2017 — <https://arxiv.org/pdf/1707.02327> |

**What this changes.** TF = 1 is normal, not a crisis — but "low maintainability" is a named killer, which is the condition Stan reported feeling. It also makes the **substrate backup** a first-class requirement: ~1.87 GB on one disk with no offsite copy *[audit, unverified by me]* is the single point of failure that no architecture survives.

## 5. Rewrite risk — the famous numbers are unusable; one dataset is not

**The audit checked the Standish CHAOS figures and refused to use them**, which is the right call:

- Jørgensen & Moløkken-Østvold, *IST* 48(8), 2006 — CHAOS recruitment was "Standish opinion… the reader bears all risk".
- Eveleens & Verhoef, *IEEE Software* 27(1), 2010 — applied Standish's own definitions to **5,457 forecasts across 1,211 projects** and found the figures unsound: <https://www.cs.vu.nl/~x/the_rise_and_fall_of_the_chaos_report_figures.pdf>
- Jørgensen, Halkjelsvik & Kitchenham, *IJPM* 30(7), 2012 — even "bigger projects fail more" is contested.

**The one usable dataset:** Flyvbjerg & Budzier, *HBR* 2011, **n = 1,471 IT projects** — average cost overrun **27%**, with **one in six a "black swan" at ~200%** (<https://arxiv.org/pdf/1304.0265>).

**What this changes.** It supplies an honest risk budget in place of folklore: plan for ~27% overrun and accept a ~1-in-6 chance of roughly triple. It also means **no rewrite-failure-rate argument should appear in any proposal here**, in either direction.

## 6. Strangler fig — the pattern's own guidance excludes this case

Azure Architecture Center and AWS Prescriptive Guidance both document it; **Microsoft's own guidance says it is "not suitable when… you migrate a small system."** Bisbal et al. 1999 designed the Butterfly method specifically to eliminate the coexistence gateways that strangler-fig migrations depend on.

**What this changes.** The pattern I proposed in v1 is contraindicated by its own documentation at this scale. Combined with the ADR hybrid-boundary finding, it is the second independent argument against a long half-migrated state.

## 7. Deploy and repo shape

| Finding | Source |
|---|---|
| **"Published GitHub Pages sites may be no larger than 1 GB"** | <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits> |
| Artifact-based publishing is the supported modern path | `actions/deploy-pages`, `actions/upload-pages-artifact` — <https://github.com/actions/deploy-pages> |
| Treat anything committed to a public repo as compromised; removal does not undo exposure | <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository> |
| The polyrepo case is **almost entirely organisational** — worth ~nothing for one developer | Nx, LogRocket, Buildkite; Potvin & Levenberg, *CACM* 2016 |
| Deploy health has a standard measurement vocabulary | DORA — <https://dora.dev/insights/dora-metrics-history/> |

**What this changes.** Confirms `sites/` must be build output published by Actions rather than a served repo root — which simultaneously fixes the `private/` and [[CLAUDE.md]] exposure — and confirms consolidation is right for a one-developer estate. The 1.5 GB of tracked audio **already exceeds the documented ceiling** and needs its own answer (release assets, external host, or LFS) that no proposal has yet given.

## 8. Segmentation evaluation — we have no real metric

The linguistic audit found the project uses `cardinality match`, which **scores `[AB][CD]` and `[A][BCD]` as a perfect match**, and that it steered two LXX refinement rounds. The field's standard measures are WindowDiff, *P<sub>k</sub>*, boundary similarity (B), and γ, with chance correction and inter-annotator agreement — none of which appear anywhere in this project *[audit, unverified by me]*.

**What this changes.** Any rebuilt engine needs a real segmentation metric from day one, and the historical LXX/BoFM numbers should be treated as **uncalibrated** until re-measured under one.

---

## What I have NOT verified

Everything above is the auditors' sourcing. I verified the *repo-state* claims they made (see [[4-process/master-proposal-v2.md|master-proposal-v2]] §2) and **refuted one** of their findings. I have not independently re-read these external papers. They are recorded here as *reported*, with URLs so any of them can be checked before it is relied on.
