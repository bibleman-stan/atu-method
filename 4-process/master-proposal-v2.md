---
cssclasses:
  - wide
---

# Master proposal v2 — propagate the pattern that already works

> **Plain-language version.** Version 1 of this proposal was withdrawn because almost every fact I asserted about our own system turned out wrong. Four audits established what is actually there. The headline: **a correct rule system already exists in one corner of the estate** — 62 YAML rule specs driven by a shared runner in `readers-tanakh` — and the thing that is genuinely broken is a set of 17 hand-run 5-machinery/scripts that edit the deployed text in place. So the move is neither "rebuild everything" nor "finish an abandoned direction." It is: **take the pattern that already works, propagate it, and delete the one that doesn't.**

**Status: PROPOSAL. Nothing adopted.** Written 2026-08-09, replacing the withdrawn [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]].

**Epistemic standing, stated up front because v1's failure was exactly this:** every factual claim below carries a source — either an audit receipt or a verification I ran this turn. I verified roughly eight of the audits' claims personally and **refuted one of them** (the USFM finding). Claims I did not verify are marked *[audit, unverified by me]*. v1 collapsed because I asserted an inventory I had not checked; v2's credibility rests on receipts, not on me.

---

## 1. Stan's reframe, which changes the decision more than any audit did

> *"we are also not certain they were correct, hence my suggestion of a greenfield; if we build on the correct architecture, we should arguably arrive at the same result — or the results we achieved were wrong."*

**This is the strongest argument made in the whole exchange, and it corrects an error running through everything I wrote before it.** I treated the deployed corpus as an asset to be preserved and the 911 lost adjudications as a cost. Both framings assume the past output was *right*. Nothing establishes that. The gold yardstick shares the bar's calibration; the Isaiah oracle turned out rule-derived; te'amim generate the very text they were proposed to judge.

Three consequences:

1. **Losing the past adjudications is not automatically a cost.** They are unvalidated claims, not banked assets. Preserving an unvalidated decision preserves whatever was wrong with it.
2. **A correct rebuild is a test, not just a migration.** Re-derive under a sound architecture and compare: agreement corroborates the old work, divergence localises exactly where the old work was wrong. Divergence becomes *informative* rather than catastrophic.
3. **It corrects my "behavioural snapshot" claim, which the audits let stand.** I called it a regression baseline. It is not — it is a **change detector**. It tells you something moved; it cannot tell you which side is right, because the deployed side has no established correctness. That distinction was blurred in v1 and Stan caught what four audits did not.

**What it does not dissolve.** The 1.5 GB of paid ElevenLabs audio and the external substrates are assets regardless of whether any segmentation decision was correct — they must survive any path.

## 2. The corrected inventory

| Fact | Source |
|---|---|
| **62 YAML rule specs** (`trigger`/`guards`/`severity`/`suggested_action`) + `validators/_shared/spec_runner.py` in `readers-tanakh` | **verified by me** — `ls validators/specs/*.y*ml` → 62 |
| **Nothing generates `index.html`** anywhere; shells are hand-maintained, 3,155–5,121 lines | **verified by me** — no write-mode open; only a comment at `build_books.py:383` |
| **789 of 23,112 deployed BoFM lines are not reproducible**; only Alma + Words of Mormon are clean | *[audit, unverified by me]* |
| Cause: **17 in-place mutators** hand-run against `data/text-files/v2/`, order recorded nowhere | *[audit, unverified by me]* |
| **GNT reproduces 100%**; `build_book.py` reproduces deployed HTML byte-for-byte | *[audit, unverified by me]* |
| **Five live sites**, not four | **verified by me** — `vulgate-reader.com` → 200 |
| **Whole source tree publicly served**, including [[CLAUDE.md]] on all four probed domains | **verified by me** — 200 on each |
| **1.5 GB of MP3** tracked in plain git, over GitHub's 1 GB Pages ceiling | **verified by me** — 239 files, 1.5 G |
| **Te'amim generate the deployed Hebrew** (`run_full_pipeline.py` step 2) | **verified by me** |
| **Cross-corpus porting already run and failed** — Jaccard 0.6958 → 0.6879 | **verified by me** — `binding-rules-lxx.md:299–302` |
| **Zero CI, zero lockfiles, one tag in ~2,400 commits** | *[audit, unverified by me]* |
| The `build_books.py` files are **HTML renderers**, not rule code | **verified by me** — their docstrings |
| lxx-reader.com renders 28,829 raw USFM markers | **REFUTED by me** — zero literal backslashes in 1,350,327 bytes |

## 3. The classification that matters — and that v1 got backwards

**Already in the right shape. Extend; do not rebuild.**

| Asset | Why it is right |
|---|---|
| `readers-tanakh/validators/specs/` + `spec_runner.py` | **This is components 3 and 6 done correctly** — a rule as one declarative artifact with an apply face and a check face. v1 scored it ❌ and proposed designing it from scratch. |
| `atu_method/` (21 modules, 3 readers import it) | The shared-engine seam, real and working |
| `atu_method/infrastructure/tx_log.py` | `{file, line, action, before, after}` with rollback — the LOG organ, half-built |
| GNT pipeline; `build_book.py` | Proof that reproducible generation is achievable here, not theoretical |

**In the wrong shape. Replace or delete.**

| Defect | Consequence |
|---|---|
| **17 in-place mutators** editing deployed text, hand-run, unordered | **The** root defect: deployed text is not any program's output, so it cannot be regenerated, tested, or migrated |
| Hand-maintained `index.html` shells, no build | Any UI change is a five-way manual cascade |
| Pages serving from repo root | Publishes source and private working documents |
| Per-repo validator sprawl on dead baselines | 75 validators; none caught a rule applied to 1 book of 15 for 65 days |
| No CI, no lockfiles, one tag | Nothing is reproducible or rollback-able |

**The LEGO answer, precisely:** the right set is already in the box — it is in `readers-tanakh/validators/specs/`. It was never propagated, and the corner of the build that most needed it (BoFM) instead grew 17 hand-run mutators.

## 4. The proposal

**Propagate the spec-driven pattern; delete the in-place mutators; make regeneration the only path to deployed text.**

Not "greenfield the core" (v1 — wrong, because the core partly exists and is sound). Not "finish the abandoned direction" (v1 — wrong, because I misidentified what had been abandoned). Instead: **a working local pattern becomes the global one.**

Concretely, a rule becomes one YAML spec with `trigger`, `guards`, `severity`, executed by a shared runner, checked by the same artifact that applies it, and **the deployed corpus becomes the output of a single deterministic regeneration** — never of a hand-run script.

### ⚠ Amendment — Stan caught an internal contradiction, and following it through flips the recommendation

The paragraph that stood here argued greenfield is wasteful because it would rebuild things already in the right shape. Stan:

> *"you basically make the same point i did above when you say: 'the assets that look expensive are mostly portable, not re-earned'"*

**He is right, and the two claims cannot both stand.** If the substrates re-import mechanically and the knowledge is prose that copies, then **the specs, `spec_runner`, `atu_method`, `build_book.py`, and the audio are files too — they copy into a greenfield.** Greenfield does not mean rewriting them; it means *carrying them into a designed contract*. My "greenfield would rebuild good work" objection was never true. It was the sunk-cost defence I had already flagged as my own likeliest bias, surviving three drafts because nobody priced it.

**So what does greenfield actually cost?** Re-establishing deploy plumbing for five domains, and re-verifying that carried code still works in a new context. Real, but small — and the migration audit independently put the architectural choice at **~20% of total cost**, with ~100 rule adjudications dominating both paths identically.

**If cost is not decisive, the decisive axis is the one Stan named first: cognitive legibility.** And on that axis greenfield wins outright — one bounded new thing with a written contract, instead of a hybrid where some repos are sources, some are targets, 17 mutators are being retired, and two models must be held at once. His ability to push back is the main error-correction mechanism this project has; a design that is harder for him to hold degrades it.

**Revised recommendation: greenfield — where "greenfield" means a new repo with a contract written first, into which the proven artifacts are COPIED, not rewritten.** Carry: the 62 YAML specs and `spec_runner`, `atu_method/`, `tx_log.py`, the GNT pipeline, `build_book.py`, the substrates, the audio, the rule catalogs and closed-route knowledge. Leave behind: the 17 in-place mutators, the hand-maintained shells, repo-root Pages serving, the dead-baseline validator sprawl.

**Cons of the flip, and one of them is about me.** I have now changed position on this question three times in one session, each time after Stan pushed. That pattern is itself a warning — but the reasoning here is chained to evidence rather than to his preference: carrying cost is low *by my own inventory*, the audit puts the architectural delta at ~20%, and cognitive load is decisive *because* his pushback is load-bearing. The substantive risks remain: a greenfield's live-site cutover is a real event with rollback needs that do not exist today; copied code can fail silently in a new context, which is exactly what Step 1's gate is for; and "contract first" is a discipline I have already failed once in this document's own ancestry.

## 4b. The baseplate — added 2026-08-09 at Stan's direction

**Audit of v2 against his asks, run before writing this section:** `lessons` 0 mentions, `lint` 0, folder layout 0, consolidation 0, `log` 4. **v2 did not meet them.** This section is the answer, and his `5-` instinct matches an existing convention — `readers-bofm` already uses `5-machinery/`.

### The consolidation, stated plainly

> *"we can then retire/delete those other repos and re-point the SITES (the real artifact we care about)"*

**That is the correct ordering of what matters, and it resolves the exposure problem structurally rather than by patching.** The sites are the artifact. The repos are scaffolding that currently leaks — publishing the whole source tree, [[CLAUDE.md]], and tracked `private/` files on four live domains. A greenfield in `atu-method` with `sites/` as pure build output ends that by construction: there is no source in the served tree to leak.

### The layout

```
atu-method/                     ← ONE repo
  CLAUDE.md                     the schema — BUDGETED; amendments name what they displace
  00-start-here.md              front door
  Current-Tasks.md · Pending-Decisions.md

  1-method/                     NORMATIVE — framework, rule catalogs (prose canon)
  2-evidence/                   MEASURED — findings · decision-log.jsonl · growth-data.csv
  3-implementation/             ARCHITECTURE — contracts, how it is built
  4-process/                    GOVERNANCE — loops, protocols, log.md, lessons.md
  5-machinery/                  CODE — the "architecture, building and maintenance bin"
      engine/                   v0 → v1 → v1.5 → v2, one implementation
      specs/                    YAML rules — one artifact, apply face + check face
      lint/                     every checker, each with calibration assertions
      app/                      one UI, per-corpus config
      build/                    corpus → site
  corpora/                      per-corpus data packages (substrates gitignored)
  sites/                        BUILD OUTPUT ONLY, one dir per domain
```

`5-machinery/` absorbs today's `atu_method/`, `5-machinery/scripts/`, and the five repos' scattered validators. **Nothing but `sites/` is ever served.**

### The three organs, and why they are three and not one

Stan asked for a log, a lessons-learned file, and a lint. They are genuinely distinct, and merging any two would force different things to be treated as one — which the two-sided simplicity criterion forbids:

| Organ | Location | Records | Cadence |
|---|---|---|---|
| **Operations log** | `4-process/log.md` | what **we** did — one line per operation, parseable `## [date] op \| title` | every operation |
| **Decision log** | `2-evidence/decision-log.jsonl` | what the **system** decided — per-verse cases with `status` | every regeneration |
| **Lessons** | `4-process/lessons.md` | **corrections** awaiting promotion into a rule or guard | captured always, **promoted only by audit** |

The operations log is what makes lint *affordable* — it scopes a pass to what changed since the last one, instead of re-reading everything. The decision log is the case record, already built as `5-machinery/scripts/decision_log.py`. Lessons is the capture buffer whose failure mode is the worry-bead pattern: collecting corrections instead of promoting them. **The promotion step is the bearing** — without a periodic audit that promotes, lessons accumulate and behaviour never changes. That is the failure this very session performed, writing seven documents about a decision record while building none.

### Lint, made structural rather than remembered

`5-machinery/lint/` holds every checker, and **the runner refuses to report unless each checker's calibration assertions pass** — a known-good it must find, a known-bad it must not. Not a convention; a precondition. Four detectors were miscalibrated in one day (wikilink checker, link-density metric, USFM regex, and the audit that reproduced it), which is the evidence that a remembered rule is an unapplied rule. `5-machinery/scripts/decision_log.py` already implements this and passes three poles.

### Nothing inherited is canonical

Per Stan's reframe, carried material enters **provisional, not authoritative**:

- `1-method/` prose canon is carried but marked provisional until re-derived under the new gate.
- Every `decision-log.jsonl` row lands `status: unreviewed`.
- The 911 `overrides.json` entries are carried as **claims**, not verdicts — they have no warrants and never did.
- Agreement between old and new corroborates; divergence localises where the old work was wrong. **Divergence is the product, not the failure.**

## 5. Sequence

**Step 0 — fix the public exposure.** Independent of everything else, cheap, and currently live. Move Pages to an orphan `gh-pages` branch or Pages-from-Actions so the repo root stops being served.

**Step 1 — the reproducibility gate. Built this turn.** `5-machinery/scripts/decision_log.py`, calibrated on three poles that must pass before it will report. Per corpus: regenerate, set-diff against deployed, emit each divergence as `status: unreviewed`. This is simultaneously the gate, the LOG organ, and the seed of CASES. **Path-independent** — greenfield, propagation, and do-nothing all need it.

**Step 2 — prove the pattern on the hardest case.** Express **one** BoFM rule as a YAML spec under `spec_runner`, retire its in-place mutator, regenerate, diff. This 5-machinery/tests the load-bearing assumption — that a Hebrew-shaped spec runner can express an English rule — on the smallest surface that can falsify it. If it cannot, the propagation plan dies here, cheaply.

**Step 3 — decide.** With Steps 1–2 reporting, greenfield versus propagation stops being a matter of opinion.

**Gate 0 has moved, not vanished.** Te'amim are disqualified, so of the three arbiter candidates only Skousen's lineation and Marschall's bands remain, both contested. Meanwhile a **weaker but available** arbiter exists: apply the §2.1 bidirectional test fresh to each divergence. That is not external ground truth, but it is a real adjudication, and it is bounded to the divergences — 789 lines in BoFM, not 23,112.

## 6. What this still gets wrong

- **I am relying on audit receipts I did not all verify.** I checked roughly eight and refuted one. The 789-line figure, the 17 mutators, and the 100% GNT reproduction are load-bearing and *[unverified by me]*.
- **`spec_runner` is Hebrew-shaped.** The 62 specs key on Hebrew morphology; BoFM rules run over a weak English parse. Step 2 exists precisely because this may not port — and the last time I assumed cross-corpus portability, the LXX experiment had already disproved it.
- **BoFM is the worst case twice over** — the unreproducible corpus *and* the outlier front-end *[audit: Jaccard 0.19–0.22 against the other four]*. The hardest case is also the one that matters most.
- **The arbiter question remains open**, and without it, divergence adjudication has no external ground. The §2.1 fallback is our own criterion judging our own output.
- **This document's ancestry is a chain of confident errors.** v1 was withdrawn for asserting an uninventoried system; before that I proposed an experiment already run and failed; before that I published a miscalibrated metric. Weight this accordingly, and prefer Steps 1–2 — which produce evidence — over any argument in Sections 3–4, which produce only reasoning.
