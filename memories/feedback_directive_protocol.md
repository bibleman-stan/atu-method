---
name: directive-protocol
description: "Per-repo directive queue replaces paste-prompts as the default cross-repo coordination mechanism. Vault-Claude writes directive files to each repo's directives/pending/, commits + pushes; Stan reviews + triggers each repo's Claude with minimal input; repo-Claudes process pending directives in commit order, write replies, move processed directives to archive. Stan retains editorial control at the directive-file-review step; direct engagement remains available when needed."
type: feedback
---

This protocol replaces paste-prompt copy-paste as the default mechanism for cross-repo coordination across the reader-repo family (`readers-bofm`, `readers-gnt`, `readers-tanakh`, plus future `readers-quran` / LXX / Vulgate).

## Architecture

Vault-Claude is Stan's primary (not exclusive) interlocutor. Cross-corpus synthesis, audit dispatches, and discipline maintenance happen in vault-Claude's persistent context. Per-repo work happens in per-repo Claude sessions, triggered by Stan. The connection between them is **directive files** committed to each repo's git tree, not paste-prompts.

## Per-repo directory structure

Each reader-repo (and atu-method itself if needed) carries:

```
<repo>/
  directives/
    README.md            ← brief explanation of the queue
    pending/             ← vault-Claude writes directives here
    processed/           ← repo-Claude moves directives here after acting
    replies/             ← repo-Claude writes findings/questions/status reports here
```

All four subfolders are git-tracked. `pending/`, `processed/`, `replies/` use `.gitkeep` until they have content.

## Directive file naming

Pattern: `YYYY-MM-DD-HHMM-<topic>.md`

- Date + time prefix gives natural commit-order sort
- `<topic>` is a short slug (e.g., `readiness-arc-item5`, `m4-gnt-1-followup`, `nav-readmes`)

The reply file uses the same name placed in `replies/`. Easy to pair.

## Directive file format

Self-contained — readable without external context beyond the repo's CLAUDE.md + framework + canon. Sections:

- **Directive title** (H1, repeats the filename topic)
- **Context** — one short paragraph: why this directive exists, what triggered it
- **Items** — numbered or bulleted list of specific work items, each with acceptance criteria
- **Reporting** — what the reply should contain (completed / proposed-for-Stan-review / blocked per item)
- **Audit triggers** — if any items trip §7.3 mandatory-audit triggers, the directive flags them

Length target: 30-80 lines per directive. Too long → split into multiple smaller directives.

## Processing protocol (per-repo Claude)

On wake (per CLAUDE.md orientation):

1. Complete mandatory orientation reads (CLAUDE.md, canon §0/§1/§2, git log)
2. Check `directives/pending/` for files in commit-order
3. For each pending directive:
   a. Read the directive
   b. Execute items per their reporting + audit-trigger guidance
   c. Write a reply at `directives/replies/<same-name>.md` documenting per-item status
   d. Move the directive from `pending/` to `processed/<same-name>.md`
   e. Commit the directive's work + the reply + the directive move in a coherent commit (per the repo's commit-discipline)
4. Surface in chat: which directives were processed, what's in replies/, any open Stan-decisions
5. Push to main

Multiple directives processed in one session each get their own commit unless tightly coupled.

## Reply file format

- **Header** matching the directive
- **Per-item status**: `completed (commit hash) / proposed-for-Stan-review / blocked (reason)`
- **For proposed-for-Stan-review items**: specific question + claude's recommendation + reasoning
- **For blocked items**: what blocks + what unblocks
- **Surfaced concerns**: anything the repo-Claude discovered during execution that's worth Stan-or-vault-Claude attention

## Stan's editorial control

Stan reviews directives in his editor (faster than reading drafts in chat + copy-paste). Three actions available:

- **Approve as written**: trigger the repo-Claude with the canonical trigger word (see "Triggering" below); no edit needed
- **Edit in place**: modify the directive file before triggering; Stan's edits are the directive's authoritative form
- **Reject**: delete the directive file from `pending/` before triggering; no commit needed (working-tree-only deletion)

Stan can also engage any repo-Claude directly without going through a directive — this protocol is the default flow, not the only flow. Direct engagement is appropriate when a question is specific to that repo's context and doesn't need vault-Claude synthesis.

## Triggering

Canonical trigger word: **`directive`** (single word, lowercase, no quotes, no path).

When Stan types `directive` in a repo-Claude session, the repo-Claude:

1. Looks at `directives/pending/`
2. Picks the **oldest file by filename timestamp** (filenames sort lexicographically by `YYYY-MM-DD-HHMM-` prefix → oldest first)
3. Opens it and processes per the protocol above (read → execute → reply → move to processed/ → commit → push)
4. If multiple pending directives exist, processes ONE per `directive` trigger unless the directive itself authorizes batch processing — keeps Stan's review cadence intact

Variants:

- `directive` alone → oldest pending
- `directive <slug-fragment>` → matches the pending directive whose filename contains that fragment (e.g., `directive resolve-review` picks the one with that slug). Use when skipping ahead or processing out of order
- `directive all` → process all pending in commit order, separate commits per directive

Why a single keyword: anything longer (e.g., `go`, `process`, free-form English) slots into whatever conversation context was last on the table, which has already misfired in practice. The keyword `directive` is unambiguous regardless of prior context — it's the protocol's hot key.

Anti-pattern: `go`, `proceed`, `run it`, or any phrase that depends on the last conversation turn for its referent. These are ambiguous outside the directive-queue context and have caused misfires.

## Vault-Claude protocol

Vault-Claude (Stan's primary interlocutor):

- Writes directives to each repo's `directives/pending/` and commits + pushes
- Reads replies via git log + direct read of `directives/replies/`
- Detects cross-corpus opportunities by reading reply files across repos
- Surfaces cross-cutting items by writing related directives into multiple repos at once
- Maintains the `_Dashboard – Readers.md` "pending directives" + "recent replies" sections
- Does NOT bypass Stan for substantive editorial calls; writes directives, surfaces options + recommendations + reasoning, awaits Stan's review-or-trigger

## Anti-patterns

- **Don't bundle navigability + substantive-decision items in one directive.** Stan's review burden compounds when a single file mixes "approve this 2-line cleanup" and "approve this multi-rule architecture call." Split into separate directives where reasonable.
- **Don't write directives that require synthesis Stan would have to repeat in his head.** If two items in a directive logically belong to different decisions, split. If they share a decision, group.
- **Don't auto-trigger repo-Claudes.** Stan triggers; vault-Claude proposes. Eliminating Stan from the trigger step removes editorial control.
- **Don't commit directive replies to atu-method.** Replies live in the per-repo `directives/replies/`. Cross-corpus synthesis based on replies lives in vault-Claude's context or in atu-method memory entries when codified.

## Migration from paste-prompts

Existing paste-prompts that haven't been pasted yet are converted to directive files in their respective `directives/pending/` folders as part of this protocol's rollout. Future cross-repo work uses directives by default; paste-prompts remain available for one-off Stan engagements.

## Codification

Codified 2026-05-16 as the workflow-architecture upgrade addressing the paste-prompt friction Stan named: *"you give prompts, i do the paste; you interpret; i have to make choices; you have to notice where they get out of sync."* The directive queue eliminates the copy-paste step; replies via git eliminate the manual-summarize-back step; Stan's review-or-trigger gate at the directive file preserves editorial control.

The pattern is structurally distinct from the overseer-of-trench-workers approach previously retired (per the OVERSEER files deleted 2026-05-16 in `readers-gnt/private/`). The overseer pattern attempted real-time supervision of N peer-Claudes; the directive-queue pattern uses async file-based coordination + ephemeral processing + persistent vault-Claude as synthesis layer.

## Aligns with

- [[feedback_compaction_resume_protocol]] — vault-Claude's persistent state survives compaction via JSONL re-read; the directive queue's persistent state survives via git
- [[feedback_decisions_in_chat_not_files]] — Stan-decisions live in chat (with vault-Claude). Directive files are the directive surface (vault-Claude → repo-Claude). Reply files are the result surface (repo-Claude → vault-Claude). Decisions remain in chat between Stan and vault-Claude.
- [[feedback_claude_commits_and_pushes]] — directive commits + reply commits both fall under the autonomous-commit discipline
