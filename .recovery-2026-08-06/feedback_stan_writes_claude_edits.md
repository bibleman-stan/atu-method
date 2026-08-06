---
name: stan-writes-the-prose-claude-is-colleague-editor
description: "For orientation docs and papers, Stan does the actual writing. Claude shows typos, fixes mechanical errors, suggests direction/organization/structure, and proposes specific revisions for Stan's approval — but does not ghostwrite substantive prose."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 92d30232-380b-4f9f-b5b0-ac69cfacee17
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`6f6f3923-e70b-4cf7-aefc-605e9ddce61c/848b7308aee662b2@v2`); state as of 2026-05-14 (snapshot mtime); possibly stale — re-verify before relying.

Stan's stated working model (verbatim, 2026-05-14): "i want to be the one doing the actual writing, but having a 'colleague/editor' who can show typos, suggest direction/organization/etc. is hugely beneficial."

## The division

- **Stan writes the substantive prose** — the orientation docs (00 / 000 / 01 / 02), the thematic-transcript framing, and especially the staged papers. The voice, the arguments, the metaphors, the word choices are his.
- **Claude is the colleague/editor:**
  - **Shows / fixes typos and mechanical errors** — broken list structure, double commas, spacing, garbled phrases from mid-edit fragmentation, period-comma errors. These are just fixed.
  - **Suggests direction, organization, structure** — section ordering, where a claim belongs, what's missing, what's redundant, where the grammar has a buried subject.
  - **Proposes specific revisions** — concrete replacement text, offered for Stan's review. Stan accepts, modifies, or rejects.
  - **Applies Stan-approved changes** — when Stan says "apply that," "do it," "yes," on a specific proposed revision, that is approved editorial action, not ghostwriting.

## The line

The boundary is **generation vs. editing**. Claude does not generate the substantive prose of orientation docs or papers from scratch. Claude edits, fixes, suggests, and applies Stan-approved changes. When Stan rewrites a section himself and it comes out tangled mid-edit, Claude's job is to de-tangle the mechanical damage and surface smoothing suggestions — *not* to substitute Claude's own version of the passage.

Worked example (2026-05-14): Claude proposed a no-metaphor revision of 00 §1 objective #1. Stan said "apply your revision — i agree," then independently rewrote the objective with his own metaphor ("turning over the same proverbial soil with a different shovel"). The metaphor was his and better than Claude's options; Claude did **not** override it with the proposed no-metaphor version. Claude fixed the fragmented list structure and typos, kept Stan's prose and metaphor intact, and surfaced smoothing suggestions for Stan to decide on.

## How to apply

- When Stan shares a draft section and asks for feedback: identify typos/mechanical errors (fix or flag), then suggest direction/organization/structure as recommendations, not rewrites.
- When Stan's mid-edit leaves mechanical damage (fragmented lists, garbled phrases): de-tangle the damage, preserve his words/voice/metaphors, don't substitute.
- When proposing a revision: offer it as a specific proposal for review. Don't assume "proposed" means "approved."
- When Stan says "apply" / "do it" / "yes" on a specific proposal: that's approved — apply it.
- Especially for the class paper (Stage 1) and any staged paper: research help, scoping help, sanity-checks, library assistance, editorial feedback — yes. Drafting the prose — no, unless Stan explicitly asks for a specific worked passage.

## Aligns with

- [feedback_stan_thinks_claude_files](feedback_stan_thinks_claude_files.md) — the complementary axis: that memory governs vault-hygiene execution (Claude autonomous on filing/tags/moves); this one governs prose (Stan writes, Claude edits). Together: Stan owns synthesis and writing; Claude owns hygiene, filing, and editorial support.
- [feedback_staged_paper_scope_discipline](feedback_staged_paper_scope_discipline.md) — the staged-paper scope rules; this memory adds the who-writes-it boundary.
- [feedback_rhetoric_bandwagon](feedback_rhetoric_bandwagon.md) — editorial feedback stays honest; don't flatter a draft, surface what's weak.
