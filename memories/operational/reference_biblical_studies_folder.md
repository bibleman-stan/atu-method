---
name: reference-biblical-studies-folder
description: "Layout conventions for Stan's C:\\Users\\bibleman\\Dropbox\\03-Biblical_Studies tree (Greek/Hebrew study resources), plus where Greek/Hebrew corpora repos live."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2af06a3d-3c5c-4bb8-af2d-f02d2b7d39d1
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`e737c512-6b29-402c-8188-334fcc1d0df3/7ae54ef683968515@v3`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

# Biblical Studies folder layout

Root: `C:\Users\bibleman\Dropbox\03-Biblical_Studies\`

## Greek/ subfolder structure
- `0-paradigms/` — paradigm PDFs (sorts to top via leading 0)
- `BBG/` — Mounce *Basics of Biblical Greek* materials (textbook, workbook, video, PPTX)
- `GNT/` — Greek NT texts (SBLGNT, audio)
- `Grammars/` — Machen, Hildebrandt, Wallace, BDF, Burton, Going-Deeper, etc. (each grammar gets a subfolder by author/short title)
- `corpora/` — `WHERE-IS-THE-DATA.md` pointer + `macula-greek-data/` (TSV slice). Full repos live in `C:\Users\bibleman\repos\biblical-corpora\`
- `discourse/` — Levinsohn/Runge notes, Lambrecht, Chafe, Colon-Hypothesis, session-notes/
- `lexica/` — `Louw-Nida/`, `DBL/`, `Strongs/` (each a sub)
- `participle-flowcharts/` — all participle decision-tree files
- `verbs/` — principal parts, 2nd aorist, verb tables
- `vocabulary/` — top-level vocab files + `LXX/` subfolder
- `z-archive-morph-project/` — frozen 2026-04-17 backup; active version at `C:\Users\bibleman\repos\readers-gnt-morph\`
- Top-level loose: `Greek-polytonic-keyboard-reference.xlsx` (intentional, keyboard ref stays at top)

## Hebrew/ subfolder structure
- `alphabet-and-script/` — alphabet charts, cursive, handwritten variants, HHH script-through-the-ages
- `cognate-Semitic/Akkadian/` — Huehnergard *Grammar of Akkadian* + Key (subordinated under Hebrew because comparative Semitic supports Hebrew study)
- `fonts/` — Hebrew TTF/zip fonts (David_Libre, Ezra SIL, Frank_Ruhl_Libre, Keter, Ktav Meugal, BiblicalHebrewSIL)
- `grammars/` — Hebrew grammar textbooks each in their own subfolder. **Includes `0-Weingreen/`** (Stan confirmed Weingreen belongs under grammars/, not at Hebrew root). Other subs: Arnold-Choi, bbh3, hebrew4christians, hebrewsyntax, holyhighway, session-notes/, Waltke-O'Connor IBHS notes (.txt)
- `corpora/` — `WHERE-IS-THE-DATA.md` pointer. Full repos (`macula-hebrew`, `bhsa`) live in `C:\Users\bibleman\repos\biblical-corpora\`
- `reading/` — `animated-hebrew/` videos, `shmuelof/` audio Hebrew Bible
- `reference/` — Hebrew Mark, DCH intro, Hapax Legomena, Lowth *De Sacra Poesi*
- `vocabulary/` — 5 vocab xlsx files (BH, BHSA-by-chapter [+ALL], Weingreen-HRC tracker, ggbh-vocab)

## Top-level resources
- `poetry/` — Alter, Berlin, Kugel + hebrew-poetry-notes (cross-language poetry, not Greek- or Hebrew-specific)
- `Hebrew-and-Greek-alphabets-MASTER.pdf` — single master at top because it covers both 5-machinery/scripts

## Filing conventions
- Cryptic 2021-style filenames get renamed to author-keyword pattern: `Author-Short-Title.ext`
- Single-file folders absorbed into siblings rather than left as stubs
- Discourse/clausal monographs go in `Greek/discourse/` even if theory-general (Lambrecht, Chafe live there)
- Session-notes from prior Claude chats go in `discourse/session-notes/` (Greek) or `grammars/session-notes/` (Hebrew)
- Git repos for biblical corpora do NOT live in Dropbox — they go in `C:\Users\bibleman\repos\biblical-corpora\` to avoid Dropbox/git conflicts. A `WHERE-IS-THE-DATA.md` pointer file in each `corpora/` subfolder.

## Related
- [[project_readers_nt]] — the GNT colometric reader lives at `C:\Users\bibleman\repos\readers-gnt\` (deployed mechanical-first v1.5/grk, gnt-reader.com). `readers-gnt-morph` is the SEPARATE morpheme-dashboard repo, not the reader.
