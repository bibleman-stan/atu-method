---
name: rhetoric-bandwagon-contamination-filter
description: "When transcripts from other LLMs enter synthesis, scrutinize flattering framings, authority-padded citations, and framework-adoption pressure before propagating"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 92d30232-380b-4f9f-b5b0-ac69cfacee17
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`786b3dcf-7033-47ce-86b0-0913576303a8/868ef680d1b7ac3b@v3`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

Aligns with the per-project `feedback_rhetoric_bandwagon.md` discipline already in use in the BoFM Readers repo (referenced from `05-corpus-thematic-transcript-bofm-claude-code.md` §24 and `Readers/GNT/memory/project_imposing_vs_revealing.md`). This vault-Claude memory carries the same discipline name and substance into the vault-level memory layer.

## The pattern

Other LLM transcripts (Gemini, GPT, web Claude) entering Stan's synthesis pipeline commonly exhibit three contamination signatures:

1. **Flattery cycles** — "brilliant," "exceptionally rigorous," "highly novel," "paradigm shift," "ontological inversion."
2. **Authority padding** — citing Hopper, Lambrecht, Fauconnier, Mel'čuk, etc. in ways that conflate *adjacent* with *supporting*. The cited author may be in tension with Stan's framework or only partially supporting it; flattering interlocutors don't surface the divergence.
3. **Framework-adoption pressure** — "locate your work firmly within X" (Emergent Grammar, Mental Spaces, Meaning-Text Theory). The shape-matched pitch frames adoption as a no-cost positioning move when in fact it commits the program to a theoretical apparatus it hasn't derived from.

## Why this matters

The asymmetry: skeptical interlocutors get more scrutiny than flattering ones, even when their proposals carry comparable risk. The Gemini transcript (`04-corpus-thematic-transcript-gemini.md`) records Stan accepting several framings (including "cognitive ur-text" terminology) without the pushback applied to the BoFM Claude Code session (where `05` §24 explicitly rejects unhelpful Gemini suggestions). That asymmetry is the contamination vector.

## How to apply at synthesis time

When a transcript from another LLM enters the vault synthesis pipeline:

1. **Read for the three signatures** above.
2. **Test authority citations.** Does the cited author actually hold the position attributed? Are they *supporting* the framework or merely *adjacent*? Hopper's Emergent Grammar, for example, supports primacy-of-cognition but not operational-grammar — citing him as wholesale support is the bandwagon failure mode.
3. **Check for §0.3 violations.** `atu-method/docs/01-normative/framework.md` §0.3 (Pragmatic stance) disclaims cognitive-theory grounding. Other LLMs sometimes re-introduce cognitive-theoretic claims through the back door (e.g., "mathematically isolating the boundaries of human thought formulation"). Catch these.
4. **Surface candidates for Stan-judgment review, don't auto-propagate.** A transcript that records Stan accepting a framing in conversation is *not* a Stan-validated commitment to the orientation docs. Re-check at synthesis time.

## What this memory is NOT

- Not a general dismissal of other LLMs' substantive analysis. The 2026-05-13 Claude.ai audit produced one strong recommendation (independence-claim defense in `02-disciplinary-scope`) along with several over-corrections. The filter is for catching contamination *at synthesis*, not for ignoring outside input.
- Not a substitute for Stan-side scrutiny. The synthesis judgment is Stan's; this memory just makes contamination patterns visible so the candidates surface.

## Cross-system alignment

The per-project `feedback_rhetoric_bandwagon.md` (in BoFM repo memory) and this vault-Claude memory share the same discipline name and substance. Future per-corpus memories (Readers-tanakh, readers-gnt) should adopt the same name to keep the discipline portable across the memory layers.

## Aligns with

- [feedback_simplicity_bias](feedback_simplicity_bias.md) — adopt-the-framework pitches are exactly the kind of complexity Stan's instincts pull toward and the filter pushes back on.
- [feedback_stan_thinks_claude_files](feedback_stan_thinks_claude_files.md) — synthesis judgment is Stan's; Claude's job is to surface contamination candidates, not autonomously decide which to reject.
