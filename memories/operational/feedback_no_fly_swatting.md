---
name: feedback-no-fly-swatting
description: "Once the mechanical edition is deployed, don't hand-patch individual verse-level splits; the residual tail is resolved systematically by progressing v2->v4, not by accreting more v1.5 rules one flag at a time"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`9d9683ed-2bb3-499d-8eb7-715c2bd3a063/2b089e65deb27ad5@v3`); state as of 2026-05-28 (snapshot mtime); possibly stale — re-verify before relying.

When Stan flags a few verse-level rendering issues on a *deployed* mechanical edition (e.g. GNT Matt 2:4 indirect-question split, 2:6 verbless-vocative split, 2:16 cognition-participle-ὅτι split), do **NOT** immediately diagnose-and-patch each one with a new v1.5 binding rule. That is "swatting individual flies" — Stan named it as **not a smart approach** (2026-05-21).

**Why:** the mechanical layer (v1.5 → v4) is a *baseline*, deliberately imperfect. Its residual long tail of heterogeneous edge cases — and there will be one in GNT, Tanakh, and every corpus — is meant to be cleaned up **systematically by progressing the pipeline v2 → v4** (the v2 LLM-adjudication and v3 editorial-refinement stages), in due course. Per-verse rule-patching at this stage has diminishing returns, risks over-fitting the catalog to whatever verse is on screen, and re-opens the deploy/validate/redeploy loop for marginal gain.

**How to apply:**
- **Big systematic root-causes are still worth fixing in v1.5** — e.g. the postpositive-δέ bind and the fronted-participle finite-head fix were single root causes that healed *hundreds* of lines corpus-wide. That is not fly-swatting.
- **A handful of heterogeneous verse-level edge cases is fly-swatting.** Note the *pattern/class* for the future v2/v3 pass if useful, but don't patch each. Let the systematic refinement stages absorb them.
- The discriminator: does the fix have **one root cause healing a broad class corpus-wide** (fix it) or is it **N distinct small rules for N flagged verses** (defer to v2→v4)?
- **ENACTMENT (Stan, 2026-05-28) — the gap that keeps recurring: once a class is identified, RUN the corpus-wide cascade *automatically*; do NOT deploy the gold verse/chapter and then ASK "want me to run the spray?"** Deploying the gold instance alone *is* fly-swatting — the gold verse is merely *where the class was discovered*; the corpus-wide class-fix is the point. So the DEFAULT next action after a hand-gold validates a rule (e.g. Stan's Alma 32 gold → the clause-initial heightening **"yea"-increment** split, ~384 candidate verses corpus-wide) is to execute the v2-spray pipeline end-to-end — candidates → parallel adjudicate (Sonnet) → ≥2 adversarial audits (Opus) → gate → deploy — **executed, not offered.** Asking permission to do the thing the SOP already prescribes is the failure mode; "we are beyond just swatting bugs" (Stan). The principle survives compaction; this *enactment* default historically did not — treat it as standing.

Ties to [[feedback_do_it_once]] (don't add throwaway passes) and the deploy-then-refine stance in [[corpus-pipeline-layer-map]].
