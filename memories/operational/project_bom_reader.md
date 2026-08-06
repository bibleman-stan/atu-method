---
name: bom-reader-project-context
description: Key facts about the bomreader.com project for fast orientation
metadata: 
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/7e754ffd8d994501@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.


Web reading app for the Book of Mormon at bomreader.com. Repo at C:\Users\bibleman\repos\readers-bofm.

**Why:** ESL readers, children, newcomers. Sense-line (cola) format for read-aloud delivery.
**Stack:** Vanilla HTML/CSS/JS SPA, Python 3 build scripts, GitHub Pages.
**How to apply:** Always read CLAUDE.md and handoffs/ before any substantive work. The handoffs are the authoritative state of the project.

Key constraints:
- The v0 SOURCE TEXT is sacred (never alter words/punctuation/verse-refs). The `v2` ATU **segmentation** is now the deployed **mechanical-first method output** (`bofm_generate.py`; it replaced the old hand-edits 2026-05-22, commit `1a980bf`) — regenerable, NOT a hand-edit to protect. *(This whole memory is 60+ days stale; for live state see `atu-method/docs/05-status/deployment-status.md`.)*
- Stan pushes to GitHub; Claude cannot push (403 proxy error)
- Service worker cache version must be bumped with every CSS/JS/HTML change
- All colometry decisions: propose only, Stan approves
- After line-break edits: commit source → rebuild HTML (py -3 build_book.py --all) → bump sw.js cache → commit HTML → ready to push

Repo structure (as of 2026-03-21):
- Root: 13 files (index.html, build_book.py, narration.js, annotations.js, sw.js, CLAUDE.md, etc.)
- handoffs/: 14 documentation files (00-13)
- scripts/: 15 utility scripts (colometric_analysis.py, senseline_reformat_v8.py, build_* scripts)
- data/: production assets only (indexes, glosses, source texts)
- research/: SYMLINK to C:\vaults-nano\my_brain\10_Projects\BOM-Reader-Research\ — gitignored, not on public repo
- books/: generated HTML (15 files, rebuilt from v2 sources)
- colab/: samuel_pipeline.ipynb only
- archive-studying-edition/: shelved features

Research/paper context:
- FEF paper in development — annotated bibliography (40 sources), strategy notes, and colometric metrics CSV in research/
- Target venue: JBMS first, then potentially DH venue
- Full-corpus mechanical scrub complete (178 fixes, 0.25% error rate, rubric validated)
- Quantitative voice marker data computed (AICTP rates, "I say unto you" density, "caused that" frequency, etc.)
- Five distinct colometric voice types identified from data
- Connection to Stan's OTC dissertation: paper establishes the empirical foundation
