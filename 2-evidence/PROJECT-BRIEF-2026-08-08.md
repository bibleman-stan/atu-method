# ATU PROGRAM — SYSTEM BRIEF (2026-08-08)

Audience: an LLM asked to critique loops, structure, and alternative models/tools. Dense by intent. Claims marked [V]=verified on disk this session, [R]=reported by a sibling session, [U]=unverified/asserted.

## 1. GOAL

Produce colometric reading editions of canonical texts: each rendered line = one **atomic thought unit (ATU)**, "a span a reader can take in as a single complete unit before needing the next." Target readers: ESL, children, newcomers. Live sites: bomreader.com, tanakh-reader.com, lxx-reader.com, gnt-reader.com, vulgate-reader.com.

## 2. FOUR ORGANS

| organ | location | role | VCS |
|---|---|---|---|
| THEORY | `work/atu-nlp-wiki` | 73 raw PDFs → 275 synthesized pages; constitution: "self-contained universe… derives solely from raw/" | **none** (Obsidian Sync only) [V] |
| CANON/SPEC | `repos/atu-method` (public GitHub) | framework + rule registries + evidence + process | git [V] |
| EDITION | `repos/readers-{bofm,gnt,tanakh,lxx,vulgate,gnt-morph}`, `rev-reader` (public) | corpus, pipeline, validators, deploy | git [V] |
| HUMAN | Stan | sole promoting authority (§7.1) | — |

atu-method layout (reorganized 2026-08-07): `1-method/` (framework.md, cross-corpus-principles.md, glossary.md, binding-rules-hebrew.md, binding-rules-lxx.md), `2-evidence/` (scholarship/ per-rule rationale, framework-claim-inventory.md, deployment-status.md, findings), `3-implementation/`, `4-process/`, `_old/`, `canon-index.md` (264 lines, 119 file:line receipts), `Pending-Decisions.md`. [V]

## 3. METHOD

- **§1 Purpose** NOT-list: apparatus does NOT adjudicate variants / produce typography or oral-delivery markup / reveal rhetorical parallelism / alter words. [V]
- **§2 criterion**: a line is an ATU if EITHER (A) §2.1 bidirectional test OR (B) §2.2 explicit-marker license.
- **§2.1 bidirectional test** = forward grammatical closure AND backward referential self-containment. Break licensed iff BOTH adjacent lines independently satisfy both. Asymmetry: anaphoric fails, cataphoric passes. Discriminator for speech/cognition = complement-vs-quote, not verb class; operationalized on Macula features (`rule=that-VP`/`role=o` bind vs `sub-CL`/`role=adv` stand) + deixis test (shared deictic centre binds; own centre stands).
- **§2.2 marker license**: the only *productive* (break-generating) licensor; quarantined by (i) single discrete author lexeme, (ii) colon closure-eligible under (A) — restoration permitted for **a gapped finite verb ONLY, NOT shared subject/object/PP**, (iii) not already licensed by (A). Default: **KEEP-AS-IS**.
- **Firewall (§2.2:116)**: cognitive-unity gates, parallelism-class adjudication, te'amim hierarchy, genre anchors are NOT licensors.
- **Punctuation has zero force**, including parser labels conditioned on punctuation (parse-substrate corollary; `ccomp`≡`parataxis`).
- **§7 change protocol**: §7.0 Categories A/B/C + scope/precedence diagnostic; §7.3 twelve mandatory-audit triggers; §7.4 audit-skippable; §7.5 commit must declare audit status. [V]

## 4. PIPELINE

`v0 source → parse → v1 clause atoms → v1.5 binding rules → v2 deployed ← overrides.json → build → site`

Three levers, preference order: (1) binding rules in the fabric; (2) UD corrections to `v0-cache-conllu` (**781 full-class candidates outstanding** [V]); (3) `overrides.json` (**911 entries** [V]). Per-corpus parses: BHSA (Hebrew, gold), Macula (Greek, gold), UD_Latin-PROIEL (Latin, gold), **Stanza EModE (BoFM, weak)**.

## 5. MEASUREMENTS (the empirical core)

| measure | value | note |
|---|---|---|
| BoFM vs Skousen lineation | 16,481 vs **28,828** lines over 6,593 word-identical verses = **1.75×**; we break fewer in **81%** of verses | [R] strongest non-circular comparandum |
| cross-corpus words/line | BoFM **16.2** vs 7–9 all gold-substrate siblings | [R] |
| Marschall bands, 1 Nephi | **16%** of deployed lines exceed her 35-syllable **Law**; 1 Ne 3: 72 lines, 28% over 25-syll ceiling, 10% over the Law | [V] |
| Isaiah cross-corpus (MT Isa 9 vs 2 Ne 19, same text) | Hebrew **63** lines vs BoFM **47**; 14/20 verses differ, BoFM coarser in 13 | [V] |
| gold yardstick | F1 ≈ **0.67**, 33 stratified verses, 2026-05-28, **never re-run** | over-split in sermon/Isaiah, over-merge in doctrinal/narrative |
| (A)/(B) split | 96.4% / 3.6% | [R] |
| theory vs scholarship audit | ATU thesis **holds** vs de Marneffe / Matthiessen-Thompson / Shopen / Quirk; grain intact | [R] run in wiki 2026-08-07 |

**Convergent direction**: four independent instruments (Skousen manuscript tradition; Marschall ancient rhetorical criteriology; our own Masoretic-substrate Hebrew edition; Stan's reading) agree the BoFM edition is **systematically too coarse**. Counter-discipline from the wiki: *"a single chapter is not grounds to move a corpus-state."*

## 6. LOOPS AND STATUS

| # | loop | status |
|---|---|---|
| 1 | canon amendment (friction→proposal→§7 gate→canon) | RUNS; but **50 of last 60 commits touch canon, only 12 declare audit status = 24%** [V] |
| 2 | retraction→promotion (3 strikes → discipline) | **NEVER FIRED.** 31 log entries, 0 promotions, logs frozen 2026-05-17 [V] |
| 3 | consult→file-back | RUNS since 2026-08-07 (2 entries in `2-evidence/`); return edge open — nothing consumes a filed answer |
| 4 | audit | PARTIAL. `loop_health.py` runs at SessionStart; trigger = 20 moves or 7 days + dormancy stamp; **hostile half never run** |
| 5 | theory ↔ experiment (wiki↔canon↔edition) | findings→theory fired **once** (F-001); **findings→canon has NO channel** |
| 6 | reader experience | capture edge opened 2026-08-07 (`reader-observations.md`); return edge absent |
| — | substrate improvement | **MISSING entirely** |

**The two live breaks**: (a) theory was never audited against scholarship *from the canon side* — the wiki ran it, the result has not returned; (b) a measurement in `2-evidence/` never becomes a rule proposal; nobody carries it.

## 7. GATES, AND WHAT THEY CANNOT SEE

Gates: §7.3 adversarial audit (2 parallel lenses: over-merge + atomicity, survivors of BOTH); text-parity check; pre-commit colometry validators vs `.baseline.json`; `quality_meter.py` (deploy gate: "candidate measurably BEATS baseline", never "is different"); live-DOM verification.

Blind spots [V]:
- **No validator detects over-merge** — the stated red line.
- **Validator baselines dead as controls**: bofm 2026-05-29 vs corpus 2026-08-06; gnt 2026-05-21 vs 06-13; tanakh 2026-06-02 vs 06-13. Six corpus ships landed post-baseline in bofm alone ⇒ the gate was bypassed repeatedly.
- `--baseline-check` is **counts-only**; offsetting errors cancel. No per-violation set-diff exists.
- ~15 validators ignore `BOFM_V2_DIR` and silently score the old corpus.
- `--update-baseline` on a regressed run is forbidden.
- Gates see only what tooling walks (see §9).

## 8. KNOWN CANON DEFECTS

- **§2.1 is 18,828 bytes elaborating a 1,352-byte criterion (~14:1)**; six named allowances landed in ONE day (2026-06-02) [V].
- **Two phantom carve-outs**: "the participial-predication allowance" and "the existing legal-casuistic protasis carve-out" are cited as settled canon and **defined nowhere** (grepped: framework, cross-corpus-principles, binding-rules, `_old/`, BoFM+GNT per-corpus canons) [V]. Three allowances rest on them.
- Deconstruction verdict: of six allowances, **2 derive** (relative-clause-embedded speech-frame, discourse-particle attribution — both from the deixis test), **3 do not**, **1 collides with the §2.2(ii) firewall** (discourse-particle amplification restores shared subject + PP).
- **Claim inventory**: 37 load-bearing assertions typed; ~¾ are `[OURS]`. The hinge — *"grammatical closure is a proxy for thought"* — is one unsupported clause and is what licenses a syntactic test to answer a cognitive question.
- Framework §1's NOT-list excludes the aural and rhetorical lenses that Stan now says are the point.
- §3 honours petucha/setuma while §2.1 bars te'amim; both Masoretic; distinction never argued. Related: te'amim enter anyway **through the substrate** (BHSA clause-atoms follow accents; MT Isa 9:1 renders a bare 1-word NP line that fails forward closure outright) [V].
- **Retraction-protocol defect**: pooling says "3 strikes need not come from one repo," but cascaded canon changes are logged in every repo by design ⇒ counts log entries, not distinct events, inflating one mistake 3×. Corrected count: only **2** sub-patterns truly qualify (`rhetorical-figure smuggling` 3, `new-rule reflex` 3) [V].
- **Both proposed promotions are contaminated by the theory question**: "rhetorical-figure smuggling" retracted *breath-tests* (2026-04-19) and *breath as a 4th criterion* (2026-04-20, on a 260-chapter sweep finding breath never *solely* deciding). Under the proposed breath-unit reframe, breath is near-definitional. Promoting would entrench rejection of the evidence class the new theory centres. **Both denied 2026-08-07.**

## 9. INCIDENTS (generalizable failure modes)

1. **2026-08-06 memory loss**: user-home memory namespace (57 files incl. `_north_star.md`, declared "never optional") deleted ~mid-June, unnoticed ~6 weeks. Recovered from file-history + jsonl-archive: 52 full + 5 stubs. Signals ignored: dead mandatory-read paths; a migration flagged pending in 3 places since 2026-06-28; **a broken-pointer detector that already existed and no cadence ran**.
2. **Shared blind spot**: a cross-repo path rewrite skipped `private/`; the integrity checker could not see what the rewriter refused to walk. Both reported clean while **103 canon citations dangled**. Fix pattern now used: independent enumeration with no skip list (surfaced a 9th repo the tool's hardcoded list omitted) + **verification by set-difference against a pre-move snapshot, never counts**.
3. **Zero commits in July 2026** across all active repos ⇒ any activity-triggered audit fires zero times in the exact window it is needed.
4. **Duplicate tooling**: two sessions independently shipped the same JSONL reader on the same day, unaware.
5. **Report-vs-reality**: a shell loop echoed "committed 9 files" while a pre-commit hook had blocked the commit.

## 10. CONSTRAINTS

- Stan's own work may be public. **Third-party licensed material may not.** `parry_index.json` (Parry's arrangement, 2.1 MB) was tracked in a public repo and publicly fetchable; untracked 2026-08-07, overlay removed from build and live pages. Skousen line data stays gitignored. **A list of break positions + public-domain text losslessly reconstructs a copyrighted arrangement** — counts are safe, offsets are not.
- `atu-nlp-wiki/raw/` = 3.2 GB, 73 PDFs, published scholarship, reacquirable; `wiki/` = 2.8 MB irreplaceable synthesis. Neither under version control.

## 11. OPEN DECISIONS (Stan's)

1. Framework §1 NOT-list — separate *revealing* from *licensing*?
2. Non-finite predication — **RULED 2026-08-07: allow restoring shared subject + modal**, not only a gapped finite verb. Execution gated on §7.3 audit + yardstick measurement. Not yet executed.
3. Retraction-protocol amendment: count distinct events, not log entries.
4. Ratify `findings/` into the wiki constitution (currently an undocumented carve-out to self-containment).
5. Routing among three evidence stores (`readers-*/2-evidence`, `atu-method/2-evidence`, wiki `findings/`).

## 12. QUESTIONS A REVIEWER SHOULD PRESS

- Is a single necessary-and-sufficient criterion ("sole arbiter") defensible, versus Marschall's **8 binding Laws + 13 defeasible Tendencies** with convergence deciding? Stan favours the latter.
- If the target is a breath-approximable chunk (Chafe IU ≈ 4 words / ~1 clause; Marschall côlon 7–25 syllables, Law ≤35; Skousen 9.24 w/l), is 16.2 w/l a *rule* failure or a *criterion* failure?
- Does adopting the Chafe–Givón–Fields–Louw–Marschall–Nässelqvist grounding convert the hinge claim from unsupported to sourced — or import rhetorical criteria as determinants (the "bandwagon" failure the canon has retracted repeatedly)?
- Rules were derived under "syntactic closure is sole arbiter." **Which rules are artifacts of the criterion rather than of the text?** No rule-set-vs-theory audit has ever been run.
- Is triple-store evidence with no routing a structural defect or acceptable federation?
- Everything is prose + Python + git. What tooling (annotation store, IAA scoring, WindowDiff/boundary metrics, treebank query layer, provenance graph) is missing?
