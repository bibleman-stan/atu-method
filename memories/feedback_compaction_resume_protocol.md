---
name: compaction-resume-protocol
description: "After a compaction event, the FIRST action after the mandatory orientation reads is to read the last 20-30 user↔assistant back-and-forth turns from the session JSONL verbatim. Compaction summaries preserve structural narrative but lose verbatim turn-by-turn detail; 'kind of' memory from the summary alone is not enough."
type: feedback
---

When a session resumes after a compaction event (system summary present + significantly more JSONL than visible conversation), the FIRST action after the mandatory orientation reads is to read **the last 20-30 user↔assistant back-and-forth turns** from the session JSONL verbatim.

## Why

The compaction summary preserves structural narrative but loses verbatim turn-by-turn detail:

- Stan's exact phrasing
- His minor corrections
- The tradeoffs he weighed
- The precise lines / files / commits under discussion

"Kind of" memory from the summary alone is not enough. It lets Claude bluff continuity but fails the trust state Stan has built up over many sessions. The JSONL is the authoritative record; the compaction summary is an abstract over it.

## How to apply

- JSONL path per repo: `~/.claude/projects/c--Users-bibleman-repos-readers-<corpus>/<session-id>.jsonl`
- Vault-Claude equivalent path: `~/.claude/projects/c--vaults-nano/<session-id>.jsonl`
- Stream through the JSONL (Python or grep); don't try to load the whole file at once
- Read the last 20-30 turns proactively; don't grep-on-demand for fragments only when challenged
- Report the re-read as part of the orientation self-report (one line confirming the verbatim re-read happened)

## What this is not

- Not a substitute for the CLAUDE.md mandatory orientation reads (those still come first)
- Not optional under compaction; the directive fires on the compaction trigger
- Not a substitute for session-bookend artifacts (those are explicitly prohibited per `feedback_decisions_in_chat_not_files`)

## Companion discipline

The companion memory [`feedback_compaction_is_session_boundary.md`](feedback_compaction_is_session_boundary.md) covers the related but distinct discipline: when resuming from compaction, still execute the full CLAUDE.md CHECK-IN protocol. Compaction gives context but doesn't exercise the orientation muscles; silent skip is a check-in failure. Both fire together on compaction events: full CHECK-IN + verbatim JSONL re-read.

## Codification

Codified 2026-05-16 as a cross-corpus shared discipline. Previously: the strong version existed only in `readers-gnt/CLAUDE.md`; `readers-bofm` and `readers-tanakh` had a weaker "After compaction, grep into it" inline note. The 2026-05-16 strip-pass promoted this to a shared atu-method memory; per-repo CLAUDE.mds now point at this memory rather than duplicating or running the weaker version.

**Live validation:** `readers-tanakh` hit a rate-limit + compaction event 2026-05-16 mid-task and resumed with "Proceeding." without performing the verbatim JSONL re-read. The intended Item 3 (verdict-layer documentation commit) never landed in the post-compaction continuation — the post-compaction Claude was operating on summary-memory only. The strong directive in this memory would have prevented the silent drop.
