# atu-method — methodology canon + binding-engine + per-corpus state

Lives at `repos/atu-method/CLAUDE.md`. **Loads when cwd is `repos/atu-method/` OR any reader repo that imports atu-method conventions**, via the directory-walk cascade (each reader-repo will eventually have its own CLAUDE.md that pulls atu-method via reference). Process rules (verify-don't-recall, execute-don't-ask, etc.) live at `~/.claude/CLAUDE.md` and load in every session regardless of cwd.

**Migration note (2026-06-28):** This file was extracted from `C:\Users\bibleman\CLAUDE.md` (the former master-blaster orchestrator) as part of the repo-autonomy reorganization. The orchestrator pattern is being dismantled; each repo is going fully autonomous. Pre-split archive: `repos/atu-method/.archive/CLAUDE-orchestrator-2026-06-28-pre-split.md`.

---

## Identity

Methodology canon + shared binding-engine + per-corpus state for the biblical-reader projects. Active reader-repos that consume this methodology: `readers-tanakh`, `readers-bofm`, `readers-gnt`, `readers-gnt-morph`, `readers-lxx`, `readers-vulgate`, `rev-reader`. Cross-repo coordination NO LONGER happens via a user-home orchestrator; each reader-repo will own its own CLAUDE.md and explicitly pull atu-method conventions where needed.

---

## STANDING BEHAVIORAL DEFAULTS — ENACT, don't just store

Litmus first; full prose + dated warrants live in the linked memory files (don't re-derive, don't re-ask). User-wide rules (execute-don't-ask, verify-don't-recall, mirror-precedent, lead-with-WHAT, apologize-once, check-in-cadence) are in `~/.claude/CLAUDE.md` and layer beneath these methodology-specific defaults.

1. **Classify cascade-mode BEFORE picking a tool.** Litmus: *can one rule decide every instance?* Yes → (a) deterministic rule/fabric fix [or (b) substrate-repair if the defect clusters on bad fabric]. Judgment-per-instance AND wrong-call costly (over-merge = red line) → (c) **pipeline** (rule 2). Single instance → never fly-swat; find the class. **Second tell:** if another layer/corpus segments it right, it's almost always a missing rule (a), not a pipeline (c). State mode + 1-line reason, proceed. → `feedback_no_fly_swatting.md`

2. **Multi-agent fan-out → encode as a `Workflow` script, NOT hand-spawned `Agent` calls.** Hand-spawning ≥2 coordinated agents loses determinism, parallelism, and resumability, and dies at compaction. Canonical v2-spray: `pipeline(candidates → parallel adjudicate → ≥2 parallel audits [over-merge + atomicity]) → gate → HALT` (returns survivors; deploy is a separate gated decision). Mechanical fan-out ONLY — never workflow a methodology/judgment call, never fold deploy into the script. **Every sub-agent spec naming a file / module / function / lemma / feature MUST require pasted verification receipts** (`ls` / `wc -c` / `Grep` / TF-query output) in its StructuredOutput. **Design-space: ≥2 viable variants → simulate ALL against the anchor cases in parallel, audit only survivors** — never serial "v(N+1) after audit feedback" iteration. → `feedback_subagent_specs_require_receipts.md`, `feedback_code_path_diagnoses_require_running_the_code.md`

3. **Compaction-resume = CONTINUE the in-flight cascade.** Enumerate state from files/git/gates; never recall a pre-compaction comparative number without re-running the gate. → `feedback_verify_deploy_state_never_assert.md`

4. **Data/treebank-first for OWN reasoning.** "Cannot / impossible / needs LLM" is the STOP signal — inventory every dataset Stan gave you before asserting it. → `feedback_mechanical_first_for_own_review.md`

5. **Consult prior work before building — three granularities.** (a) Cross-corpus: "how did Tanakh/GNT/BoFM solve this?" — port, don't re-invent. (b) Same-file: before proposing a new `_is_*`/`_has_*`/`_detect_*`/`_check_*` helper, `Grep` the file for an analogous one and cite why a new one is needed. (c) **File the answer back.** When a cross-corpus consult produces a durable answer, write it to `docs/synthesis/<topic>.md` **in the same turn** and index it in `docs/00-start-here.md` — an answer that dies in chat is re-derived by grep on every future question, which is the tax (a) exists to avoid. → `feedback_check_prior_corpora.md`

6. **Verify empirically — inspection ≠ verification.** Source-parity (vs original USFM/TF/source) is the correctness gate; index-parity (vs HEAD) is regression-only. Run BOTH tactical (does this break?) and strategic (is this the right design?) audits before any pivot. Any **new mechanism / integration / env-flag / guard structure** triggers the §7.3 audit gate BEFORE code (substrate *consumption* is exempt; building a new integration shape over it is not). Any code-touching edit that **cites canon** (`framework.md` / `§2.x` / `binding-rules-*`) requires a fresh in-turn `Read` of cited-range + 30 lines downstream AND a verbatim firewall quote in the proposal. Pre-audit self-check: every cited `file:line` Read this turn, every governing helper observed firing via probe (not inferred), every analogous helper Grep-enumerated. → `feedback_never_skip_audit_gate.md`, `feedback_conformance_is_not_correctness.md`, `feedback_canon_citation_requires_verbatim_read.md`

7. **Code-path diagnoses are source-tree state-claims — bind to fresh in-turn `Read`+`Grep`+`Run`, never recall.** Before naming any `file:line` as the bug / cause / gate / integration locus: Read it this turn; Grep the file for analogous `_is_*`/`_has_*`/`_detect_*` helpers before designing a new one; for control-flow claims ("rule R fires here") run a probe that *observes* the firing, never infer from a static read. STOP signal: *"I think rule R at line N."* Live-input-path pins + full incident record → `feedback_code_path_diagnoses_require_running_the_code.md`.

8. **Stan-flagged verse → Read-canon-then-situate, NEVER fix-then-ship.** First three tool calls, in order: (a) `Read` the verse ±2 from the live source (`v2-adjudicated/` override → `v2/` baseline); (b) `Read` `framework.md` §2.1 AND §2.2 in full including the Registry-discipline firewall (~lines 113-117); (c) write a **bidirectional-test walkthrough** in chat — forward-closure + backward-containment per side, with the §2.1 allowance / §2.2 marker / firewall clause quoted verbatim. Only then does rule-design / `Edit` / audit-dispatch happen. Execute-don't-ask does NOT license skipping (a)/(b)/(c) — the situate-walkthrough IS the executing here. → `feedback_canon_citation_requires_verbatim_read.md`, `feedback_scrutinize_stan_instincts.md`

---

## Closed routes / banked-gold / settled tactical — DO NOT re-litigate

Headlines only; full record + warrants at `_north_star.md` (mandatory orientation read). If something here looks reopenable, it isn't — bring it to Stan with evidence before touching.

- **CLOSED — BoFM *parser-training* route** (training a parser on out-of-register data to *replace* baseline Stanza). PCEEC-letters-trained parser lost a blind 2-adjudicator gate to off-the-shelf Stanza **21–6** (5–0 on polysyndeton). Register gap (letters ≠ scripture); encoder strength does not close it. Do NOT reopen without genuinely new *real in-register* gold — not another letters bootstrap, not a bigger encoder over the same supervision. **LLM post-editing of baseline Stanza output to `v0-cache/` is a distinct mechanism and is NOT closed (see "BoFM forward" below).**
- **TEMPERED — "BoFM mostly correct."** Per 2026-05-28 yardstick measurement: mostly-correct on SIMPLE verses; genuine both-direction defects on COMPLEX ones. Re-measure against the gold yardstick at `readers-bofm/private/substrate/emode-substrate/bofm-atu-gold-yardstick.json` — don't recite the stale framing. Detail at `_north_star.md`.
- **PARKED — LXX clause-syntax TF, Vulgate-OT, cross-corpus convergence query.** Inherit the closed bootstrap; do NOT start without real gold or a new reason.
- **BANKED real-gold — do NOT re-prove.** Hebrew/BHSA (live, Tanakh); GNT/Macula + CenterBLC-N1904 (`readers-gnt/private/substrate/N1904`); Vulgate-NT/UD_Latin-PROIEL → TF v0.1 (`readers-vulgate/data/tf/0.1`).
- **BoFM forward = three-lever framework over baseline Stanza** (none is the closed parser-training route): (1) `§2.2`-style **binding-rule additions** in `bofm_generate.py` (substrate-first permanent reader fix — try this first for any structural class); (2) **LLM-adjudicated UD-corrections to `v0-cache/`** (silver-tier semi-automatic treebank substrate via Sonnet+Opus + `validate.py` gate; primary value is TF-query consistency); (3) **`overrides.json` v2-spray** for judgment-residuals neither rule nor UD-correction reaches. Take what each lever reaches; accept the mechanical ceiling on what none does. Full record at `_north_star.md`.
- **Settled tactical (do NOT re-ask):** SUD = derived view of UD, not a fork (one parser on UD); each project's data lives in its own repo's `private/substrate/`; **genre is NEVER an ATU criterion** (no "prophetic oracle"-type holds); private method canon untracked from public remotes (still in git history — scrub only if pre-publication scrub matters); **BoFM live parse = `data/parses/v0-cache-conllu/<book>.conllu`** (lever-2-LLM-corrected), NEVER `data/parses/ensemble/stanza/<book>.conllu` (raw Stanza ensemble — superseded reference only). Any fabric-behavior diagnosis grounded in the raw ensemble parse is MOOT before audit; the live fabric reads `v0-cache-conllu`. **GNT live Macula = `readers-gnt/research/macula-greek/SBLGNT/lowfat/`** (rich cltype/rule/role attributes), NEVER `biblical-corpora/.../sblgnt-lowfat/xml/` (lacks the rich attribute layer per 2026-06-03 Pipeline B finding).

---

## Mandatory orientation reads (every wake on atu-method-relevant cwd)

1. **This file** (`repos/atu-method/CLAUDE.md`) — methodology orientation
2. **`~/.claude/CLAUDE.md`** — user-wide process rules (already loaded by Claude Code; just be aware)
3. **`repos/atu-method/memories/operational/MEMORY.md`** — operational memory index (70 files: north-star, deferred queue, named arcs, user profile, feedback disciplines). NOTE: the former user-home namespace (`~/.claude/projects/C--Users-bibleman/memory/`) was DELETED ~mid-June 2026 and recovered 2026-08-06 into this tracked home — state as of 2026-06-15; treat entries as possibly stale until re-verified (provenance: `.archive/recovery-2026-08-06/RECOVERY-MANIFEST.md`).
4. **`repos/atu-method/memories/operational/_north_star.md`** — SETTLED decisions (banked / parked / closed-routes / standing tactical). Loaded **every session**, not just on compaction-detect — the settled-decisions layer is never optional. Recovered state 2026-06-01; same staleness caveat.
5. **`git log --oneline -10`** in `repos/atu-method/` — recent methodology commits

## Consult-on-trigger reads

| File / dir | Trigger |
|---|---|
| `repos/atu-method/docs/01-normative/framework.md` | Any methodology / rule-design / canon-touching question |
| `repos/atu-method/docs/02-registries/binding-rules-hebrew.md` | Hebrew binding-rule catalog (B1-B14) work |
| `repos/atu-method/docs/03-implementation/toolset-architecture.md` | Pipeline implementation (v0→v3 stages) |
| `repos/atu-method/docs/03-implementation/apparatus.md` | English-layer work, swap-system, 4-layer integrity |
| `repos/atu-method/memories/` | Cross-corpus methodology rules (32 files) |
| `repos/readers-tanakh/CLAUDE.md` | Tanakh-specific data + deploy details (post-Phase-6, thin stub) |
| `repos/readers-bofm/CLAUDE.md` | BoFM-specific data + deploy details (post-Phase-6, thin stub; Firestore-PWA code purged) |
| `repos/readers-gnt/CLAUDE.md` | GNT-specific data + deploy details (post-Phase-6, thin stub) |

**Self-report before first substantive response**: one line per mandatory file read; flag any pending items; surface red flags. Silent skip = orientation failure.

## Audit tier — calendar-triggered, NOT activity-triggered

**Trigger:** the first wake of any ISO week, OR any wake after >7 days with no commit in this repo. Dormancy is the danger mode — the 2026-08-06 memory-loss incident happened during a quiet stretch, and an activity-triggered check would never have fired. Run it before substantive work; it is cheap.

1. **Mechanical lint.** Run `python scripts/check_broken_pointers.py` (validates cited paths AND that every `](<file.md#Heading>)` anchor still matches a real heading — link-rot is otherwise silent). Then: every memory file indexed and every index entry resolving; retraction-log present per reader repo (spokes are in scope — this is a hub and discipline-propagation is manual); anything claiming "live" but unedited >60 days flagged.
2. **Hostile audit.** One adversarial pass, written down: are the 8 standing defaults being *enacted* in recent sessions or merely stored; is any flagged-pending item stalled (>2 weeks → surface to Stan by name); is the retraction 3-recurrence threshold actually being checked; is this file over its salience budget (~17KB) and do the layers sort for a split.

**Findings convert to edits, or they recur.** A finding that ends the turn as prose is not a finding — it lands as an edit, a `_deferred_queue.md` entry, or a Stan-facing decision. The tool being *absent* was never the failure mode here: `check_broken_pointers.py` already existed and no cadence ran it.

## Compaction-resume protocol

On compaction ("This session is being continued..." OR `isCompactSummary: true`):
1. FIRST tool call after orientation reads: PowerShell command to dump last 30-35 user/assistant exchanges from session JSONL verbatim (harness summary is degraded; JSONL is authoritative). Read command + JSONL path pattern in `feedback_compaction_resume_protocol.md`.
2. `_north_star.md` is already loaded via mandatory reads above; verify state from files/git/gates per the user-wide verify-don't-recall rule (in `~/.claude/CLAUDE.md`) and do not re-litigate any item listed in Closed routes / settled tactical. Never recall a pre-compaction comparative number without re-running the gate.
3. Named-arc resume ("continue master-blaster" etc.): pointer in `memories/operational/_named_arcs.md`; archive at `~/.claude/jsonl-archive/<namespace>/<session-id>.jsonl`.

---

## Repo map (atu-method's consumers)

| Repo | Role | Live |
|---|---|---|
| `atu-method` (this repo) | Methodology canon + shared binding-engine | — |
| `readers-tanakh` | Tanakh Hebrew + KJV | **tanakh-reader.com** |
| `readers-bofm` | Book of Mormon reader | **bomreader.com** |
| `readers-gnt` | Greek NT reader | gnt-reader.com |
| `readers-lxx` | Septuagint colometric reader (Gen+Ruth gold + Exod-Mal projection-v1) | **lxx-reader.com** |
| `readers-vulgate` | Latin Vulgate (NT gold UD_Latin-PROIEL) | vulgate-reader.com |
| `readers-gnt-morph` | GNT morph dashboard (separate from readers-gnt) | — |
| `rev-reader` | Revelation reader (separate) | TBD |
| `biblical-corpora` | Shared vendored clones: bhsa/macula-hebrew/greek-new-testament. Reader-specific substrate moved 2026-05-27 to each reader's gitignored `private/substrate/`. | — |

## Pipeline architecture

Mechanical-first per `docs/01-normative/framework.md` §3. **Live state per reader = `docs/05-status/deployment-status.md` (single source of truth).** All deployed readers run v1.5 binding-rule stage; no v4 (retired 2026-05-22). Never infer deploy state from stale per-repo docs.

Stages: v0 source → v1 treebank clause-atoms → v1.5 binding rules → v2 narrow-task LLM adjudication (optional) → v3 editorial review → deploy. Hebrew F1 85-91% boundary; 5-25% absorption per genre. **Past-ceiling levers:** (a) better *real-gold* substrate [CLOSED for BoFM via manufactured/parser-bootstrap — see Closed routes], (b) cross-corpus convergence-projection (BHSA→alignment→target for Hebrew-source LXX/Vulgate-OT — FIRST mechanical move, not v2 defer), (c) v2 LLM adjudication. Full doctrine + per-corpus state + known limits (BHSA-canon-migration arc): `docs/03-implementation/substrate.md` + `_named_arcs.md`.

## Methodology keystones (cross-corpus, load-bearing)

- **Bidirectional ATU test is SOLE arbiter** — gold is candidate-source, not verdict; genre/punctuation/external units NEVER criteria. → `feedback_external_unit_is_not_atu.md`
- **Conformance ≠ correctness** — reveal-by-reading on genre-spread sample; validator ticks are proxies, not regressions. → `feedback_conformance_is_not_correctness.md`
- **Punctuation has ZERO force ALL corpora** — never split/bind on a mark; treat parataxis ≡ ccomp; punctuation is a symptom not cause.
- **Doctrine is QUALITY CONSTRAINT, not sequencing** — ship deployed products before infrastructure for zero-user corpora.

## Default decisions (don't surface as menus)

| Decision | Standing answer |
|---|---|
| New binding rule | `docs/02-registries/binding-rules-hebrew.md` §"Adding a rule"; retest validated set; no regression = ship. |
| Adversarial audit on non-trivial work | **Encode as `Workflow` — `parallel([lens_over_merge, lens_atomicity])`.** Hand-spawning ≥2 parallel `Agent` calls is anti-pattern. Override with `# audit-skippable: <reason>` only. |
| Applying a BIND / merge | Over-merge = Stan's RED LINE; validators are BLIND to it. ≥2 parallel adversarial audits (over-merge + atomicity lenses) BEFORE applying — encode as `Workflow`; ship only survivors of BOTH; when in doubt KEEP separate. |
| Apply causes regression | Revert → root-cause → fix → re-apply with integrity gate. NEVER build recovery tools first. |
| Commit/push | Commit substantive work proactively; status claims AFTER commit + push. Failure: `git log -3` + `git status --short` BEFORE retry; HEREDOC commit messages. |
| **Deploy claim** | **After push + GitHub Pages window (~1-2 min), FETCH the live site (curl/WebFetch) and verify the user-visible change matches the commit's intent. "Commit succeeded ≠ user-visible change shipped." Required before claiming "live."** |
| Per-item corpus-scale judgment | **Encode as `Workflow` — `parallel(clusters.map(c => agent(...)))`.** Cluster set: Torah / Former Prophets / Latter Prophets / Writings prose / Sifrei Emet / Embedded Poetry. Hand-spawning is anti-pattern. |
| Agent model | Haiku=mechanical; Sonnet=per-instance-judgment-within-rule; Opus=structure-generation/adversarial-audit/novel-rule. |

---

## Identifying named multi-session arcs

To resume a named conversation arc ("continue master-blaster", "continue X"), read `memories/operational/_named_arcs.md` (recovered state 2026-06-06) — it has JSONL pointers for the relevant archived conversation under `~/.claude/jsonl-archive/`. Sessions between mid-June and the 2026-08-06 recovery are not registered there.

---

Detail in `memories/` (operational/project/feedback) + `docs/` (methodology canon).
