---
name: production-tier-empirical
description: "Production tier for ATU rendering at corpus scale: Opus 3-pass with agreement scoring. Empirically validated 2026-05-17 across 5 chapters / 3 corpora / 3 languages. Sonnet 3-pass NOT production-grade (silent agreement-on-wrong-answer failure mode). Haiku off-table for biblical content (content-filter unreliability)."
metadata:
  type: feedback
---

**Production protocol (ATU rendering at scale):**

1. Three independent Opus passes per chapter, same minimal-rubric prompt, same source text
2. Per-verse verdict assignment:
   - **Unanimous (3/3 passes agree)** → auto-apply (empirically 94% accurate on prose, 100% on poetic)
   - **Majority (2/3 agree)** → surface to editorial review with majority verdict pre-filled
   - **All-disagree (3 distinct verdicts)** → surface as flagged-uncertain
3. Editor adjudicates the non-unanimous surface (~20% of verses on average)

**Empirical evidence (2026-05-17 cross-tier × cross-genre matrix):**

| Chapter | Type | Sonnet unanim accuracy | **Opus unanim accuracy** |
|---|---|---|---|
| Enos | EME narrative | 91% | **100%** |
| Lev 11 | Hebrew legal list | 74% | **93%** |
| Eph 1 | Koine Pauline | 84% | **89%** |
| Isa 53 | Hebrew poetic prophecy | 57% | **100%** |
| Rev 5 | Koine apocalyptic | 62% | **100%** |

Prose aggregate: Sonnet 81%, **Opus 94%**. Poetic aggregate: Sonnet 60%, **Opus 100%**.

**Why Sonnet is not production-grade for ATU rendering:** silent agreement-on-wrong-answer failure. Unanimous Sonnet verdicts are wrong ~20% on prose and ~40% on poetic content. Editor cannot trust them without re-verification, which negates the cost saving.

**Why Haiku is off-table for biblical content:** content-filter blocks ~67% of passes on biblical narrative containing violence, judgment, ritual purity, etc. Quality variance ~55% on the runs that complete.

**The frugal-default exception:** For non-rendering work (cluster sweeps, classification, audits, doc reads), the frugal-default model routing (Haiku/Sonnet for defined-structure tasks, Opus only for adversarial/novel-structure work) still applies. ATU rendering at production scale is the **explicit exception** that overrides frugal-default for this work class only.

**See also:** `atu-method/docs/toolset-architecture.md` Stage 1 (production tier specification in the canonical methodology doc).
