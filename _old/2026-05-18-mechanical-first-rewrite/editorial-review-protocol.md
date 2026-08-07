# Editorial-Review Protocol

This document specifies the Stage 3 editorial-review surface for the ATU rendering pipeline. After Stage 1 (Opus 3-pass with agreement scoring) and Stage 2 (constraint catalog audit), non-unanimous verses + constraint-violation flags surface to a structured review file. The editor adjudicates the surface; final renderings are committed only after editorial sign-off.

This protocol is consumed by per-repo pipeline scripts (`scripts/atu_pipeline/run_pipeline.py`) and by the editor's review workflow.

---

## Per-batch review file

After a batch of chapters processes through Stages 1–2, write ONE review file per batch:

**Path:** `directives/replies/<directive-slug>-batch-<book>-<NN>-<MM>.md`

E.g., `directives/replies/2026-05-17-1700-torah-batch-genesis-01-10.md` for chapters 1–10 of Genesis.

---

## File structure

```markdown
# Editorial Review — <book> chapters <NN>–<MM>

**Directive:** <slug>
**Pipeline version:** <git SHA of pipeline scripts>
**Constraint catalog version:** <SHA>
**Generated:** <YYYY-MM-DD>

## Batch summary

- Chapters processed: <N>
- Total verses: <N>
- Auto-applied (unanimous, no constraint violation): <N> (<XX%>)
- Editorial review surface: <N> (<XX%>)
  - Non-unanimous: <N>
  - Constraint-violation flagged: <N>
  - Both (overlap): <N>

## Per-chapter agreement summary

| Chapter | Verses | Unanim % | Majority % | All-disagree % | Constraint flags |
|---|---|---|---|---|---|

## Editorial review surface

For each verse needing review:

### [Verse reference]

**Source:**
```
[source lines]
```

**Pass 1 verdict:**
```
[Pass 1 ATU rendering]
```

**Pass 2 verdict:**
```
[Pass 2 ATU rendering]
```

**Pass 3 verdict:**
```
[Pass 3 ATU rendering]
```

**Agreement:** [UNANIMOUS / MAJORITY (Pass X) / ALL-DISAGREE]

**Constraint catalog audit:**
- [Constraint ID]: [BIND / SPLIT-CANDIDATE / MERGE / VIOLATION-FLAG / NO-EFFECT]
  - Encoded question: [question]
  - Audit verdict reasoning: [one sentence]
- (repeat per constraint that fired)

**Editorial decision:** [BLANK — for editor to fill in]

**Editor notes:** [BLANK]

---

[next verse...]
```

---

## Editor adjudication

The editor reviews the surface file and edits the "Editorial decision" field per verse. Allowed values:

- `Accept Pass N` — pick one of the three Stage-1 verdicts as canonical
- `Accept majority` — use the 2/3 majority verdict
- `Custom: <text>` — editor specifies a rendering different from any Stage-1 pass
- `Constraint-override` — accept the Stage-2 constraint catalog verdict over Stage-1 proposals
- `Defer` — mark verse for further investigation, do not auto-commit

The pipeline reads the editor-adjudicated file and writes final renderings to `data/text-files/v2/heb/<book>/<book>-NN.txt` (or per-corpus equivalent path).

---

## Auto-applied verses (NOT in review surface)

Verses with:
- Unanimous Stage-1 verdict AND
- No constraint catalog violations

are NOT included in the review surface. They auto-apply to the final rendering. The batch summary reports the count for transparency; the editor MAY spot-check by reading the committed v2 files, but the protocol does not require per-verse review of auto-applied content.

The empirical basis for auto-applying unanimous + clean-audit content: per `feedback_production_tier_empirical.md` (Opus 3-pass unanimous accuracy = 94% prose / 100% poetic against Stan-validated baselines).

---

## Batch granularity guidance

- **Prose chapters with ~30+ verses**: 5-chapter batches (Genesis, Numbers, Deuteronomy narrative)
- **Legal-list / formulaic chapters**: 5–10 chapters per batch (Leviticus, Numbers tribal lists)
- **Poetic chapters**: 3–5 chapters per batch (Psalms, Isaiah, Job — higher editorial bandwidth required per chapter)
- **Mixed-genre books**: 5 chapters per batch

The pipeline configures batch size per book; the editor may adjust by signaling preference (e.g., "smaller batches for Psalms").

---

## What does NOT go in the review surface

- Verses with unanimous Stage-1 verdict + zero constraint violations (auto-apply)
- Stage-1 proposals that constraint catalog cleanly affirms (verdict-family `NO-EFFECT` only)
- Boilerplate per-verse explanation when no decision is required

The discipline is: only verses that need an editorial decision appear. Reducing noise makes the editor's actual decisions faster.

---

## Constraint-violation flagging

When Stage 2 produces a verdict other than `NO-EFFECT` on a Stage-1 proposal, the verse appears in the review surface even if Stage-1 was unanimous. The editor can then:

- Accept the constraint catalog's verdict (override Stage 1)
- Override the constraint catalog (Stage 1 unanimous was right; the constraint may need refinement)
- Defer (flag for constraint-catalog review)

Constraint catalog overrides become candidate input for constraint refinement (per `change-protocol.md` §7.3 trigger #6: audit-stage signature changes under settled constraints).

---

## Cross-pipeline reuse

This protocol is corpus-agnostic. Tanakh, BoFM, and GNT pipelines all generate review surfaces in this format. The editor's review workflow is consistent across corpora — only the per-verse content (Hebrew / EME English / Koine Greek) differs.

Per-repo pipeline implementations live at:

- `readers-tanakh/scripts/atu_pipeline/run_pipeline.py`
- `readers-bofm/scripts/atu_pipeline/run_pipeline.py`
- `readers-gnt/scripts/atu_pipeline/run_pipeline.py`

Each implements the protocol; the format is defined here.
