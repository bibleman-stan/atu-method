---
name: claude-commits-and-pushes
description: "Claude handles commits AND pushes for Stan's reader/method repos (atu-method, readers-bofm, readers-gnt, readers-tanakh, rev-reader, etc.). Stan no longer manually commits/pushes Claude's work. Follow each repo's existing commit convention."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/786576eecae70983@v2`); state as of 2026-05-15 (snapshot mtime); possibly stale — re-verify before relying.

Stan's directive (verbatim, 2026-05-15): *"no - from now on, you do commits and pushes (go look at what other repos are now doing)"*

Prior pattern: Claude edited files; Stan ran `git commit` and `git push`. Stan retired that division — Claude is now responsible for both ends of the commit/push cycle on the reader-family and method repos.

## Scope

Applies to the repos under `C:\Users\bibleman\repos\`:
- `atu-method` (cross-corpus framework + change protocol)
- `readers-bofm`
- `readers-gnt`
- `readers-gnt-morph`
- `readers-tanakh`
- `rev-reader`
- any future reader-family or ATU-method repos Stan adds

Vault git operations (in `c:\vaults-nano`) are NOT yet in scope — the vault is not a tracked repo in the same way. Confirm with Stan before assuming.

## Convention discovery

Before the first commit in any repo (or whenever conventions might have drifted), inspect `git log --pretty=fuller -3` to surface:

- **Title format** — most reader repos use `<area> §X.Y: short summary` or `<file>: short summary`. atu-method recent pattern: `framework §1.2 + memories: codify "grammar constrains; atomic-thought determines"`.
- **Co-author footer** — atu-method currently uses `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`. Match what the repo's recent commits use. Do not invent a different footer; do not skip if present in recent commits.
- **Audit-evidence keyword** — atu-method enforces this via change-protocol.md §7.5. Every commit touching canon must declare `Audit-skippable per §7.3 (<reason>)` or `Audit dispatched: <evidence>`. readers-bofm has a commit-msg hook that enforces the keyword for canon-extension patterns; check `.git/hooks/commit-msg` before assuming you can skip.
- **Body style** — Stan-verbatim quotes when applicable, what changed, what motivated it, cross-refs to related commits/memories. Keep tight; don't pad.

## How to apply

1. **After Stan-approved edits land**, run `git status` and `git diff --stat` to inventory what's staged for commit.
2. **Group changes into focused commits.** Match the repo's commit granularity — recent atu-method commits cover one rule-codification + its memory + index update as a unit. Don't bundle unrelated changes.
3. **Compose the commit message** following the repo's pattern (title format, body, audit-evidence, co-author footer). For atu-method specifically, audit-evidence is mandatory per §7.5.
4. **Run pre-commit and commit-msg hooks** without `--no-verify`. If a hook fails, fix the underlying issue and create a new commit; do not bypass.
5. **Push** to `origin/<branch>` after the commit lands cleanly.
6. **Report to Stan** with the commit hash(es) and what was pushed, so he can spot-check.

## Boundary

- Stan still retains the right to amend/revise commit messages or push timing — if he wants me to wait, he'll say so.
- Hard-to-reverse git operations (`reset --hard`, `push --force`, branch deletion, rewriting published history) still require explicit per-action confirmation; this directive does NOT authorize destructive git.
- Commits to repos NOT in scope (vault, anything outside Stan's reader-family) still require explicit ask.

## Aligns with

- [[feedback_stan_thinks_claude_files]] — the complementary axis: Claude autonomous on filing/tags/moves and now also on git commits/pushes; Stan's bandwidth reserved for synthesis, prose, and judgment.
- [[feedback_stan_writes_claude_edits]] — Stan writes the substantive prose; Claude edits, fixes, suggests, and now also commits/pushes the edits.
- [[feedback_parallel_default]] — when multiple repos have pending commits, dispatch the commit work in parallel where independent.
