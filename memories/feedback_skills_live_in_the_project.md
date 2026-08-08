---
name: feedback-skills-live-in-the-project
description: "Any skill created for a project lives in that project's ./.claude/skills/<name>/SKILL.md — never the global ~/.claude/skills/ bucket, never a parent .claude/, never a symlink out. Portability: the global bucket is machine state and does not travel with the folder."
metadata:
  node_type: memory
  type: feedback
---

**The rule (Stan, verbatim, 2026-08-07):** *"any skill you create for this project must live in `./.claude/skills/<skill-name>/SKILL.md` — inside THIS folder. Do NOT write it to `%USERPROFILE%\.claude\skills\` (the global bucket), and do NOT write it to a parent directory's `.claude/`. Those are machine state — they don't travel when I copy or clone this folder to another machine, and the skill silently vanishes. Never symlink a skill to a target outside this folder, for the same reason."*

**Why.** Portability, and it decides the question on its own. A skill inside the project folder is committed with the repo, or rides along with a plain folder copy. A skill in the global bucket is bound to one machine's home directory: clone the repo elsewhere and the capability is simply gone, with nothing in the project even hinting it once existed. The failure is silent, which is what makes it bad.

**Do not be persuaded by the counter-argument.** It is genuinely true that a project skill only loads when the cwd is that project, so the same skill needed in two repos must be copied into both. That duplication is the *price* of portability, not an argument against it — Stan has weighed it and ruled.

**How I got this wrong, 2026-08-07.** Stan said *"skills are skills; you move it to .claude; they can serve the project but they're only you."* I read `.claude` as the global bucket and consolidated five project skills up into `~/.claude/skills/` — the exact opposite of the instruction. He meant the project's `./.claude/`. The phrase "they're only you" means a skill is Claude's capability rather than project documentation; it says nothing about which directory holds it.

**How to apply.**
- Creating a skill while working in a repo → `./.claude/skills/<name>/SKILL.md`, plus any helper script in the same directory.
- Needed in a sibling repo too → copy it there. Do not centralise.
- Genuinely global (about how Stan works everywhere, not about any project) → **ask first.** Do not decide this unilaterally in either direction.
- Never create a symlink or junction from a project's `.claude/skills/` to anywhere outside the folder.

Related: [[feedback_scratch_belongs_in_repo]] — same principle one layer down, that durable work belongs in the repo rather than in machine-local scratch.
