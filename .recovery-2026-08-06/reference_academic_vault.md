---
name: academic-vault-orientation
description: "Stan's my_brain Obsidian vault — structure, conventions, and connections to BOM Reader work"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2af06a3d-3c5c-4bb8-af2d-f02d2b7d39d1
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`18327914-8fd6-4400-a057-2a38aaf1a09f/06a052e331367008@v2`); state as of 2026-05-25 (snapshot mtime); possibly stale — re-verify before relying.


Stan's academic Obsidian vault lives at C:\vaults-nano\my_brain\. It uses Obsidian Sync. The BOM Reader research folder is symlinked into it at 10_Projects/BOM-Reader-Research/.

## Vault Structure
- 00_Inbox/ — unprocessed captures (~60 items)
- 01_Scholars/ — ~230 scholar hub notes (Lastname_FI.md, Dataview-powered)
- 02_Sources/ — 332 bibliographic records (Author-Year.md, Zotero-linked)
- 03_Notes/ — Summaries/ (literature + lectures), Topics/ (thematic MOCs)
- 04_Zettels/ — 838 atomic notes in 7 types: Arguments, Data, Debates, Definitions (393), Grammar (252), Observations, Synthesis (2)
- 05-Bible/ — Bible books, exegesis (Galatians, Mark ch.1)
- 08_Bibliographies/ — reference collections
- 10_Projects/ — Thesis-0 (OTC dissertation), Article Ideas, BOM-Reader-Research (symlink), BofM Critical Text, Papers, Proposals

## Tag System (11 layers + z/)
- 0/ admin (moc, source, scholar) | 1/ source type | 2/ author | 3/ conversation/discipline
- 4/ biblical text (SBL abbrevs) | 5/ era | 6/ method | 7/ literary corpus
- 8/ textual tradition | 9/ manuscript | 10/ ms type | z/ zettel type

Key tags for our work: 3/colometry, 3/book_of_mormon, 6/oral-criticism, 6/performance-criticism

## Conventions (never violate)
- Sources: Author-Year.md in 02_Sources/, must have 0/source + 1/type tags
- Zettels: descriptive filename in 04_Zettels/[type]/, z/ tag required, NEVER Layer 1 tags
- Scholars: Lastname_FI.md in 01_Scholars/, 0/scholar + 2/lastname_fi tags
- Tags filter; wikilinks connect. Status: seed → draft → stable
- NEVER create/modify vault files without Stan's explicit instruction

## Connections to BOM Reader
- 10_Projects/Thesis-0/ — OTC dissertation (FEF paper is empirical foundation)
- 10_Projects/BofM Critical Text/ — Skousen's critical apparatus reference
- 10_Projects/Article Ideas/ — "Re-Examining Restoration Texts" proposal
- 04_Zettels/Definitions/Mormon as Editor - Grant R. Hardy.md — directly relevant to FEF
- Welch-1969.md (Inbox), Marschall-2024.md, Korpel-2002.md — colometry sources (stubs)
- Hebrew poetry zettels exist but are seeds

## Zotero 9 integration + "notes not collection" (realized 2026-05-22, PKM v9)
`07_Misc/PKM/My PKM Organizing System v9.md` — REWRITTEN to the realized model (v8's tags/folders/zettels stand). Two principles: **(1) the notebook holds notes Stan took, NOT a collection** — auto-generated metadata stubs are "the illusion of busyness"; a cited-but-unwritten source is an *unresolved link*, not a fake note; generate on demand, never pre-generate. **(2) Two databases bridged by the citekey** — Zotero 9 = reference layer (metadata/PDFs/annotations/citekeys, MCP-queryable), vault = thinking layer. Test: fact-about-source→Zotero, thought-about-it→vault.
**Source note = working HUB** (not thin anchor): highlights + synthesis accumulate in `02_Sources/{{citekey}}.md`, built incrementally. **Engine built + verified**: Zotero Integration plugin "Source Note" import → `_Templates/zotero-source-hub.md` (frontmatter + Synthesis persist block + 3-color highlight buckets); incremental via `{% persist %}` + `filterby(date,dateafter,lastImportDate)` (adds new highlights, preserves edits). CRITICAL gotcha: exclude `02_Sources` AND `_Templates` from Filename Heading Sync (Ignore Regex `(_Templates|02_Sources)/.*`) or it renames hubs off their citekey and breaks re-import. Citations plugin retired; one bridge = Zotero Integration.
**Cleanup done**: `02_Sources` 373→73, B-Literature 220→193 (hollow stubs archived to `07_Misc/Archived/orphaned-source-stubs/` + `empty-summary-stubs/`, recoverable/regenerable). SBL pipeline built — see [[zotero-mcp-integration]]. Parked: strip retired `TOC-`/`Glossary-` companion dead-links.
**Logos-source variant (2026-05-25)**: Logos-locked works (a large slice of Stan's library — IBHS, Niccacci, LDHB/LDGNT, Robertson, Porter, Brant-John, etc.) have NO PDF in Zotero, so the "highlight in Zotero → import buckets" step is structurally unavailable; the 3-color buckets come back empty. Recipe for these: still run "Zotero Integration: Source Note" (scaffolds citekey-correct frontmatter + `{% persist %}` Synthesis block so Pandoc/re-import behave) → **paste quotes by hand** from Logos → synthesis sentence. Only difference from the standard flow is skipping the highlight step. When turning a Logos extraction into a source note, do NOT suggest the highlight pipeline. For quotes already captured as a Zotero child note (e.g. Brant `RIBC9WET`), copy from there rather than re-opening Logos.

## How to apply
Read vault content for context when relevant to BOM Reader work. Flag connections between vault content and repo work. Never create or modify vault files without explicit instruction. The vault's CLAUDE.md has detailed orientation.
