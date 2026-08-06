---
name: surface-judgment-calls-not-silent
description: Surface non-mandated choices as labeled assumptions/questions BEFORE writing them into a deliverable; never bake them in silently
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2af06a3d-3c5c-4bb8-af2d-f02d2b7d39d1
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`18327914-8fd6-4400-a057-2a38aaf1a09f/789f7b9aa15a6241@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

When building a deliverable (docx submission, file, doc), any choice **not dictated by an explicit instruction or rubric is a judgment call** — name it as a labeled assumption or a question BEFORE writing it into the artifact, never bake it in silently and explain only if asked. Stan: "don't do stuff without being transparent and what are your judgment calls."

**Why:** Silent assumptions cause real, sometimes irreversible harm. Worked example (2026-05-26): a prior session put **unlabeled due dates** in the header of RS 6310 library-assignment submission docx. A bare date in a document header reads as *the date the paper was written/submitted* — so a deadline like `2026-08-02` on work actually turned in May made it look like Stan authored it on a future date. Five were already submitted; Canvas shows resubmission attempts, so it could not be cleanly fixed. Stan, correctly and angrily: "IF YOU DIDN'T SAY DUE DATE WHAT WOULD A HUMAN THINK… you screwed up; full stop."

**How to apply:**
- On a submission/document, **don't add a bare date** — either omit it or label it ("Due:" / actual submission date). Default to omit unless the assignment asks for one.
- Before saving formatting/structure/header choices into a file (spacing, indents, font face, header layout, title/subtitle wording, filename, dates), list them as assumptions for Stan to veto first.
- Distinguish what the **rubric/instructions actually mandate** from what is Stan's own convention vs. my invention — verify against the authoritative source (syllabus, instruction files, the actual sample docs), not just memory. See [[rs6310-amridge-course]].
- When I do take an action (e.g., editing a memory file, saving over a file Stan may be editing), say so explicitly and flag possible collisions.

Ties to [[feedback-stan-thinks-claude-files]] (execute routine moves autonomously) — the line is: routine moves dictated by durable system rules = just do; *undictated choices baked into a deliverable* = surface first.
