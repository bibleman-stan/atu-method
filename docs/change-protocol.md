# Change Protocol — §7 (Operational)

**This document is the canonical statement of the change protocol for ATU canons.** It supersedes per-repo §7 sections (which become one-line pointers to this document).

The protocol governs: when a canon change requires hostile audit; what audit-evidence must appear in the commit message; how the commit-msg gate enforces compliance.

---

**Status: SCAFFOLD** — to be populated by extraction from `readers-bofm/private/01-method/colometry-canon.md` §7 + the BoFM-Reader CLAUDE.md "Pre-commit adversarial-audit discipline" section.

Target subsections:

## §7.1 Authority of the framework

- The framework (§0/§1/§2) and the change protocol (§7) are the SHARED specification authority.
- Per-corpus rule detail (§5) is per-repo specialization.

## §7.2 Versioning and amendment

- atu-method semantic versioning (major / minor / patch).
- Per-repo canon revision tracking.
- Cross-project provenance preserved in git, not in canon body.

## §7.3 Mandatory-audit triggers for canon changes

- **Trigger #1**: Closed-list extension (new lemma in a rule's closed list).
- **Trigger #2**: Scope claim ("rule X applies to / does not apply to Y").
- **Trigger #3**: Precedence claim ("rule A trumps rule B").
- **Trigger #4**: Named-category carve-out (introducing a new gating category).
- **Trigger #5**: Retirement / replacement of a previously-active rule.
- **Trigger #6**: New §5 rule subsection (new rule).
- **Trigger #7**: New merge-override or structural justification.
- **Trigger #8**: New named pattern under an existing rule.
- **Trigger #9**: SCOPE-exclusion bullet under any rule.
- **Trigger #10**: Catch-all H3 principle headings (Hebrew-corpus canon specific).
- **Trigger #11**: Recovery from retired canon (audit required before reintroduction).
- **Trigger #12**: Post-codification corpus-fit sweep (mechanically newly-codified rule needs goal-fit validation).

## §7.4 Audit-evidence requirements in commit messages

- Mandatory keywords or phrases in commit body when canon files are staged.
- Skip-safe declarations for non-trigger changes.
- The mechanical gate (`atu_method.hooks.check_canon_extensions`) enforces these requirements.

## §7.5 Audit-skippable categories

- Typo fixes, cross-reference updates, defensibility-capture additions to settled rules without scope changes.
- Category A mechanical corpus edits not part of a ≥5-instance sweep.

## §7.6 Hostile-audit dispatch pattern

- When in doubt, dispatch parallel Opus agents.
- Cost of false-positive audit < cost of false-negative audit.

## §7.7 Self-test before commit

- Five questions an editor asks before committing canon changes.

---

**This scaffold will be replaced with the full change protocol in version 0.2.0.**
