# New-Lens Onboarding — `lenses/_template/README.md`

> **Read this before adding any new lens to a reader.** The substrate is the apparatus; ATU is one lens, not the only one. This doc is the contract every lens must satisfy.

---

## 0. Why this exists

A mature reader-substrate (Text-Fabric or equivalent) decouples **what-is-there** (rich per-token / per-clause features: morph, dependency, frame, referent, te'amim, Wackernagel position, parenthetical bracketing, etc.) from **how-it-is-segmented** for reading.

Once the substrate is optimized for ATU revelation, the same enrichment *theoretically* lets us expose **other** segmentation truths — colometric, prosodic, rhetorical, diagrammatic — by running a different deterministic function over the same features. Each such function is a **lens**.

Pill-button UX on the reader lets the user toggle lenses on the same passage. Side-by-side compare is deprioritized.

**The load-bearing risk this doc mitigates:** losing the lens-catalog insights and the substrate-as-apparatus framing to compaction or repo drift. If a future lens idea isn't in `lenses/_catalog.md` with a stub manifest, it doesn't exist.

---

## 1. What a lens IS

A lens is a **deterministic function** of the form:

```
f_lens : substrate × passage_range → ordered list of segment boundaries
                                   → rendered text file (one segment per line/block)
```

Properties every lens must have:

- **Pure over substrate.** Same substrate version + same lens code → byte-identical output. No hand edits in the rendered file. Hand edits go *into the substrate* (as a feature, override, or correction) and the lens re-renders.
- **Deterministic, mechanical-first.** The lens consumes substrate features (te'amim disjunctive rank, dependency edge, Wackernagel position, parenthetical-signal flag, etc.). If a judgment call is unavoidable, it is encoded as a v2 LLM-adjudication pass writing back to the substrate, *not* as freehand in the renderer.
- **Single-purpose.** One lens exposes one segmentation theory. Mixed-criteria lenses ("ATU but also break on te'amim") are forbidden; ship them as two lenses and let the user toggle.
- **Reversible.** Lens output is a view, not the source. Deleting `lenses/<name>/` and re-running the renderer must reproduce it exactly.

A lens is **not**:

- A hand-edited text file. (That's a *gold yardstick*, see §2.3.)
- A mixed-genre canon. (Genre is never an ATU criterion; it is never a lens criterion either.)
- A punctuation overlay. (Punctuation has zero force across all corpora — see Skousen lens note in §3.)

---

## 2. The lens contract — checklist

Every lens that ships must have all seven artifacts. Missing any one = not shippable.

### 2.1 `manifest.json`

Machine-readable identity card. Required fields:

```json
{
  "lens_id": "atu",
  "display_name": "ATU (Atomic Translatable Unit)",
  "pill_button_label": "ATU",
  "corpus_applicability": ["tanakh", "bofm", "gnt", "lxx", "vulgate"],
  "substrate_version_min": "v0.1",
  "substrate_features_required": ["clause_atom_id", "dependency", "binding_rule_applied"],
  "segmenter_entrypoint": "lenses/atu/segment.py::segment",
  "gold_yardstick": "lenses/atu/gold/yardstick.json",
  "validation_oracles": ["lenses/atu/oracles/bidirectional_test.py"],
  "production_status": "deployed",
  "deployment_status_md_row": "atu-method/docs/deployment-status.md#atu"
}
```

`production_status` ∈ `{draft, gated, deployed, retired}`. Only `deployed` lenses appear on the live pill-button bar.

### 2.2 Segmenter

A pure function in the lens's own subdirectory:

```
lenses/<lens_id>/segment.py
    def segment(substrate, passage_range) -> List[Segment]: ...
```

Must:
- Take substrate + range; return ordered segments.
- Have zero side effects (no network, no writes outside its own render dir).
- Be re-runnable against any past substrate version named in `substrate_version_min`.

### 2.3 Gold yardstick

A small, hand-curated reference rendering against which the lens is measured. Genre-spread sample, NEVER one passage. Format:

```
lenses/<lens_id>/gold/yardstick.json
    {
      "samples": [
        {"ref": "Gen 1:1-5", "expected_segments": [...]},
        {"ref": "Alma 36:1-30", "expected_segments": [...]},
        ...
      ],
      "rationale": "<paragraph: why this sample, what it stresses>"
    }
```

The yardstick is **candidate-source**, not verdict (cf. `feedback_external_unit_is_not_atu.md`). Bidirectional test (§2.6) is the arbiter; the yardstick supplies the candidates.

### 2.4 Rendering rules

Plain markdown spec in `lenses/<lens_id>/RENDERING.md`. Covers:

- One segment per line vs per block.
- Whitespace, indentation, hanging-indent for continuation.
- Whether segment IDs are emitted alongside text.
- How embedded structures (quoted speech, parentheticals) are visualized.
- What the lens does NOT do (explicit non-goals).

### 2.5 Pill-button label

Short, distinctive, ≤ 5 chars preferred (fits the toggle bar). Exemplars: `ATU`, `Cola`, `Period`, `Skn`, `Wal`, `KJV`. Registered in `manifest.json::pill_button_label`. No emoji.

### 2.6 Validation oracles

At minimum, **bidirectional test** adapted to the lens's claim:
- For ATU: §2.1 framework bidirectional test.
- For Korpel-colometric: te'amim-disjunctive-rank closure under Korpel's hierarchy.
- For Wackernagel: every P2 enclitic lands in segment-position 2.
- For Marschall: 100% match against the hand-segmented gold for 2 Cor 10–13.
- For Wallace-diagrammatic: every main clause is a top-level segment; every dependent clause indents one level.

Oracles live in `lenses/<lens_id>/oracles/` and run in CI.

### 2.7 Pre-rendered text-file convention (§4)

Spelled out below. A lens without rendered text on disk is not shippable.

---

## 3. Per-corpus applicability

| Lens | Tanakh (Hebrew) | BoFM (EModE) | GNT (Greek) | LXX (Greek) | Vulgate (Latin) |
|---|---|---|---|---|---|
| **ATU** | ✓ deployed | ✓ deployed | ✓ deployed | ✓ deployed | ✓ gated |
| **Korpel / Masoretic-colometric** (te'amim disjunctive hierarchy) | ✓ candidate — substrate has te'amim live | — | — | — | — |
| **Cantillation-prosody** (te'amim melodic units, distinct from Korpel) | ✓ candidate | — | — | — | — |
| **Wackernagel periods** (P1/P2 postpositive position) | — | — | ✓ candidate — Macula has dep-edges + clitic flags | ✓ candidate | — |
| **Marschall hand-segmented periods** (2 Cor 10–13 gold) | — | — | ✓ candidate, scope-limited | — | — |
| **Wallace diagrammatic** (didactic clause-structure) | — | — | ✓ candidate — needs Wallace summary retrofit | — | — |
| **Skousen parenthetical structure** (structural-signal layer; NOT em-dash overlay — see `feedback_em_dashes_illustrative_not_text.md`) | — | ✓ candidate — needs parenthetical-open/close substrate feature | — | — | — |
| **Croft / Scheppers full-grammatical-unit** (FEF/AICTP cross-corpus) | ✓ candidate | ✓ candidate | ✓ candidate | ✓ candidate | ✓ candidate |
| **KJV verse boundaries** (legacy comparison only) | ✓ trivial | ✓ trivial | ✓ trivial | ✓ trivial | ✓ trivial |

"Candidate" = substrate features exist (or are within one converter of existing) but the lens isn't yet drafted. Update this table when a lens promotes.

**Cross-corpus note.** Croft/Scheppers full-grammatical-unit is the cross-corpus FEF/AICTP convergence target — a single lens applicable to every corpus is itself evidence for the convergence thesis. Don't ship per-corpus variants under one `lens_id`; if Hebrew and Greek FGU diverge mechanically, they are two lenses.

---

## 4. Pre-rendered text-file convention

Every deployed lens emits **plain text files on disk**, parallel to the canonical text directory. Renderers are deterministic; outputs are committed (or built at deploy time from a pinned substrate hash). Readers read the rendered files; they do not run segmenters in the browser.

### Directory layout (per-reader)

```
<reader-repo>/
  data/
    text-files/
      v2/                       # canonical substrate-aligned text (corpus-specific stage name)
        heb/                    # Tanakh example; analogs: grk/, eng-emode/, lat/
          Gen.1.txt             # source text, one verse per line (or canonical unit)
    lenses/
      atu/                      # one subdirectory per lens (recommended during design phase)
        heb/
          Gen.1.txt             # ATU-rendered: one ATU per line
        manifest.json
        segment.py
        RENDERING.md
        gold/yardstick.json
        oracles/bidirectional_test.py
      korpel/
        heb/
          Gen.1.txt
        manifest.json
        ...
      wackernagel/
        grk/
          Rom.1.txt
        ...
```

**Per-lens subdirectory is the design-phase recommendation** — it keeps each lens's contract artifacts (manifest, segmenter, oracles, gold, rendered text) co-located. Promotion to a flat `lenses/<lang>/<lens_id>/Book.ch.txt` layout is allowed once the lens has shipped and stabilized, but the contract artifacts stay co-located with the lens, not scattered.

### File-format invariants

- UTF-8, LF line endings, no BOM.
- One segment per line **unless** the lens's `RENDERING.md` declares block-mode.
- No trailing whitespace.
- Stable ordering: canonical passage order; ties broken by substrate node-id.
- File header (commented per corpus convention) records: `lens_id`, substrate version, segmenter git-sha, render timestamp. Reproducibility evidence.

### What goes in git

- `manifest.json`, `segment.py`, `RENDERING.md`, `gold/`, `oracles/` — always.
- Rendered text files — **yes**, committed. Stan's readers ship as static sites; the rendered files ARE the deployable artifact. Re-rendering is part of the regen step (cf. atomic-ship doctrine: rule + regen + HTML + sw.js as ONE).

---

## 5. Required §7.3 audit before a lens ships

A new lens is a **new mechanism + new code-integration shape over substrate**. Per Standing Behavioral Default #7, that triggers the §7.3 audit gate **before code, not after**.

Gate sequence:

1. **Pre-code adversarial-audit fan-out.** Encode as a `Workflow` script (Default #2), `parallel([lens_over_merge_audit, lens_atomicity_audit, lens_corpus_fit_audit])`. Each lens-class audit asks:
   - **over-merge lens:** does this segmenter ever collapse two distinct authorial units into one? (Stan's red line.)
   - **atomicity lens:** does this segmenter ever split an indivisible unit? (Bidirectional test failure mode.)
   - **corpus-fit lens:** are the substrate features it consumes actually present in the live data, or are we projecting from a related corpus and calling it gold?
2. **Halt at gate.** Workflow returns survivors. Deploy is a separate gated decision (NEVER folded into the workflow).
3. **Gold-yardstick run.** Lens must pass its own yardstick (§2.3) on the genre-spread sample.
4. **Bidirectional-test (or lens-equivalent) oracle run.** Pass in CI.
5. **Reveal-by-reading.** Stan reads a genre-spread sample of rendered output. Conformance ticks are proxies, not regressions (cf. `feedback_conformance_is_not_correctness.md`).
6. **§7.3 audit override.** Bypass only with `# audit-skippable: <reason>` and only for substrate consumption that is genuinely read-only. New code-integration is never audit-skippable.

No lens ships to production without all six.

---

## 6. Registering a new lens in `deployment-status.md`

The single source of truth for live state is `atu-method/docs/deployment-status.md`. With lenses, that doc gains a **per-lens dimension** orthogonal to per-reader rows.

Add the lens by editing the doc with this shape (suggested — adapt to current doc structure on read):

```markdown
## Lenses

| lens_id | display_name | pill | status   | corpora deployed                | substrate_min | last_audit |
|---------|--------------|------|----------|--------------------------------|---------------|------------|
| atu     | ATU          | ATU  | deployed | tanakh, bofm, gnt, lxx          | v0.1          | 2026-05-27 |
| korpel  | Korpel cola  | Cola | draft    | (tanakh candidate)              | v0.1          | —          |
| ...     |              |      |          |                                |               |            |

## Reader × Lens matrix

| Reader   | ATU      | Korpel | Wackernagel | Marschall | Wallace | Skousen | Croft-FGU | KJV-verses |
|----------|----------|--------|-------------|-----------|---------|---------|-----------|------------|
| tanakh   | deployed | draft  | —           | —         | —       | —       | candidate | deployed   |
| bofm     | deployed | —      | —           | —         | —       | candidate | candidate | deployed   |
| gnt      | deployed | —      | candidate   | candidate | candidate | —     | candidate | deployed   |
| lxx      | deployed | —      | candidate   | —         | —       | —       | candidate | deployed   |
| vulgate  | gated    | —      | —           | —         | —       | —       | candidate | deployed   |
```

Update both tables in the same commit that flips `manifest.json::production_status`. Stale `deployment-status.md` after a flip = orientation failure (Default #4 / `feedback_verify_deploy_state_never_assert.md`).

---

## 7. Sample structure — `lenses/atu/` as the exemplar

ATU is the deployed canon and serves as the contract exemplar. New lenses copy its shape.

```
lenses/atu/
  manifest.json                 # lens_id=atu, pill=ATU, status=deployed
  segment.py                    # consumes substrate clause-atoms + binding-rule output (v1.5 stage)
  RENDERING.md                  # one ATU per line; binding-rule marks NOT shown; hanging-indent on continuation
  gold/
    yardstick.json              # genre-spread sample per corpus (Torah / Former Prophets / Latter Prophets /
                                #   Writings prose / Sifrei Emet / Embedded Poetry for Hebrew;
                                #   Narrative / Sermon / Vision / Letter / Quoted-letter for BoFM; etc.)
  oracles/
    bidirectional_test.py       # framework §2.1 — sole arbiter
    over_merge_audit.py         # over-merge is Stan's red line; checked in CI
    atomicity_audit.py
  README.md                     # this file is the template; atu/README.md is its instantiation
```

The substrate this lens reads (live, per corpus):
- Tanakh: BHSA + binding-rule v1.5 stage at `data/text-files/v2/heb/`.
- BoFM: Stanza TF v0.1 + binding-rule v1.5 + v2-spray overrides at `data/text-files/v2/`.
- GNT: Macula / N1904 + binding-rule v1.5 at `data/text-files/v1.5/grk/`.
- LXX: BHSA→alignment projection-v1 (Gen + Ruth gold) at `readers-lxx/data/...`.
- Vulgate: UD_Latin-PROIEL TF v0.1 at `readers-vulgate/data/tf/0.1/`.

**Copy `lenses/atu/` to `lenses/_template/` and edit. Do not invent a new shape.**

---

## 8. Quick-start checklist for a new lens

- [ ] Idea registered in `lenses/_catalog.md` with a one-paragraph rationale (this is the anti-loss step — do it the moment the idea surfaces, before any code).
- [ ] `lenses/<lens_id>/` created from the `_template/` skeleton.
- [ ] `manifest.json` filled out; `production_status: draft`.
- [ ] Substrate features the lens depends on are confirmed present in live substrate (NOT projected, NOT promised).
- [ ] Gold yardstick drafted — genre-spread, with rationale paragraph.
- [ ] `segment.py` written; pure function over substrate; zero side effects.
- [ ] `RENDERING.md` written.
- [ ] Oracles written and passing locally.
- [ ] §7.3 pre-code adversarial-audit Workflow run (over-merge + atomicity + corpus-fit, parallel); survivors only.
- [ ] Yardstick run passes.
- [ ] Reveal-by-reading on the genre-spread sample, with Stan in the loop.
- [ ] `deployment-status.md` Lens table + Reader×Lens matrix updated in the same commit that flips status.
- [ ] Pill-button registered in reader UI; toggle wired to swap the rendered text file source.
- [ ] Live-site fetch verification post-deploy (cf. default-decisions: "Commit succeeded ≠ user-visible change shipped").

---

## 9. Anti-patterns

- **Mixed-criteria lens.** "ATU but with Korpel breaks." Ship two lenses.
- **Hand-edits in rendered text files.** Edits go into substrate; lens re-renders.
- **Punctuation as criterion.** Zero force across all corpora. Always.
- **Genre as criterion.** Never. ATU rule; lens rule too.
- **Side-by-side compare as the primary UX.** Deprioritized. Pill-button toggle on the same view is the target.
- **Lens that requires a substrate feature not yet on disk.** Build the substrate feature first; then the lens is a one-day job (cf. `feedback_time_estimate_as_diagnostic.md` — multi-week lens estimates are the stop signal that substrate, not lens, is the real work).
- **Hand-spawning parallel audit agents.** Encode the audit fan-out as a `Workflow` script (Default #2). Never freehand N parallel `Agent` calls in a turn.

---

## 10. Where this idea is anchored

- **In-conversation reframe:** 2026-06-03 (Stan) — "the substrate IS the apparatus; ATU is one lens; pill-button toggle UX; don't lose this."
- **Memory pointer:** add `project_lens_architecture.md` to `~/.claude/projects/C--Users-bibleman/memory/` indexing this doc + the catalog.
- **Methodology canon:** `atu-method/docs/framework.md` §2 (ATU definition) remains canon for the ATU lens specifically. The lens-architecture layer sits one level above and treats ATU as one instantiation of the lens contract.
- **Catalog of unimplemented lens ideas:** `lenses/_catalog.md` (create on first use). Every lens idea that surfaces in conversation lands there immediately, with a one-paragraph rationale and pointers to substrate features it would need. This is the load-bearing anti-loss artifact.