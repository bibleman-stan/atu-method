# Recovery manifest — 2026-08-06

Recovery of the deleted user-home memory namespace
(`~/.claude/projects/C--Users-bibleman/memory/` — entire project dir gone; deletion
predates the oldest surviving Dropbox backup `claude-2026-07-04_0600.tar.gz`,
verified to contain zero `C--Users-bibleman` entries).

**Status: COMPLETE as of 2026-08-06 (atu-method session).** Every file listed in the
recovered `MEMORY.md` index is accounted for: **52 full recoveries + 5 marked stubs**,
plus the index itself and the broken-pointer script. Target enumeration comes from
`MEMORY.md` **@v44 (2026-06-15)** — ten days newer than the @v42 first staged, and it
lists two files @v42 lacked (`feedback_subagent_specs_require_receipts.md`,
`feedback_render_path_verification.md`, both recovered).

Every staged file carries an inline `> **PROVENANCE**:` line (source + as-of date),
EXCEPT the six files first staged by the meta-wiki session (`_north_star.md`,
`_deferred_queue.md`, `project_master_blaster.md`, `project_bofm_substrate_quality.md`,
`project_bofm_discourse_voice_deploy.md`, `reference_emode_substrate.md`) — their
provenance is the table in the original manifest (file-history, newest `@vN` per hash,
states 2026-06-01 – ~June). Add headers at landing time.
**Treat ALL content as `recovered, possibly stale` until re-verified against live repos/gates.**

## Recovery tiers (method scripts are in this dir; keep with the archive)

| Tier | Script | Source | Yield |
|---|---|---|---|
| 0 (meta-wiki sibling) | — | file-history content-marker sweep | 7 (incl. `_north_star.md`, index @v42) |
| 1 | `recover_sweep.py` | file-history frontmatter scan, name-slug match, highest @vN per (session,hash) | 37 |
| 2 | `recover_sweep2.py` | token-overlap matching for slug≠filename cases | 12 |
| 3–4 | `recover_inspect3.py`, `recover_inspect4.py` | targeted content-grep leads, eyeball ID | 5 (incl. `MEMORY.md`@v44, receipts, render-path, academic-vault, bom-reader, script) |
| 5 | `recover_jsonl5.py` | jsonl-archive: latest full `Write` tool-call per target (2,524 gz transcripts) | 7 (incl. `user_stan.md`, `reference_analytics.md`) |
| 6 | `recover_jsonl6.py` | jsonl-archive: `Read`/`Edit` tool-results (`toolUseResult.file.content` / `originalFile`+patch) | 0 (probe exhausted) |
| 7 | `recover_finalize7.py` | canonical renames + LOST-stubs | 5 stubs |

## LOST — stub only (all recovery routes exhausted)

`project_session_durability.md`, `project_wallace_summaries.md`,
`feedback_canon_citation_requires_verbatim_read.md`, `feedback_preserve_formatting.md`,
`feedback_read_source_carefully.md` — no file-history snapshot (likely written once,
never harness-edited afterward) and no surviving transcript ever Read/Wrote them
(originating sessions' JSONLs died with the namespace). Stubs carry the index one-liner
and a LOST banner. Note: `canon_citation`'s discipline survives independently in
`CLAUDE.md` standing defaults #6/#8; `session_durability`'s content is richly
summarized in `MEMORY.md` @v44 line 21.

## Caveats for landing

- **Two names collide with live `memories/`**: `feedback_rhetoric_bandwagon.md` and
  `feedback_compaction_resume_protocol.md` exist in `repos/atu-method/memories/`
  (the separate cross-corpus collection). Diff before landing; live wins where current.
- `user_stan.md`: 1 later Edit call not replayed (content may lack that patch).
- `_named_arcs.md` (53KB, @v23 2026-06-06) — largest recovery; registry format intact.
- Filenames canonicalized to the index's names (`deferred-queue.md`→`_deferred_queue.md` etc.).
- `check_broken_pointers.py` — the broken-pointer detection script that existed with no
  cadence to run it; load-bearing evidence for the audit-tier mandate (directive §2/§3B).
