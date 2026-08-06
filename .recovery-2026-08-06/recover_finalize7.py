"""Pass 7: finalize staging.
1. Copy the last identified file-history snapshots with provenance headers
   (incl. MEMORY.md @v44, ten days newer than the sibling's @v42 stage).
2. Rename sibling-staged files to their index-canonical filenames.
3. Write marked LOST-STUB files for the 5 unrecoverable targets (index
   one-liner is all that survives; stubs say so explicitly).
"""
import os, io
from datetime import datetime

HOME = os.path.expanduser("~")
FH = os.path.join(HOME, ".claude", "file-history")
STAGE = os.path.dirname(os.path.abspath(__file__))

COPIES = {  # target -> file-history rel path
    "MEMORY.md": "87af68a0-0291-4910-962f-d0913b5722e6/5eee468b0b9a82fd@v44",
    "feedback_subagent_specs_require_receipts.md":
        "87af68a0-0291-4910-962f-d0913b5722e6/7d83c8e90b8f3b39@v2",
    "feedback_render_path_verification.md":
        "87af68a0-0291-4910-962f-d0913b5722e6/85d82fb1064cff1f@v2",
    "reference_academic_vault.md":
        "18327914-8fd6-4400-a057-2a38aaf1a09f/06a052e331367008@v2",
    "project_bom_reader.md":
        "87af68a0-0291-4910-962f-d0913b5722e6/7e754ffd8d994501@v2",
    "check_broken_pointers.py":
        "b15d8d3f-13d4-4a90-bd66-6ad57e8b4350/f3b1940b03ed6ed6@v3",
}

RENAMES = {
    "deferred-queue.md": "_deferred_queue.md",
    "project-master-blaster.md": "project_master_blaster.md",
    "bofm-substrate-quality.md": "project_bofm_substrate_quality.md",
}

STUBS = {  # target -> (type, index one-liner from MEMORY.md @v44)
    "project_session_durability.md": ("project",
        "JSONL transcripts were silently hard-deleted by Claude Code's 30-day "
        "`cleanupPeriodDays` default; FIXED 2026-06-01 (set to 36500). Tax/house "
        "convos unrecoverable. Remaining gaps: transcripts unbacked (git excludes "
        "`projects/**`), only biblical memory namespace version-controlled. "
        "Federation = per-launch-folder memory namespace; cross-history index at "
        "`~/.claude/session-index.json`."),
    "project_wallace_summaries.md": ("project",
        "Wallace summary retrofit: format spec, source mapping"),
    "feedback_canon_citation_requires_verbatim_read.md": ("feedback",
        "canon citations (framework.md §X.Y, binding-rules-*.md, §v1.x) are "
        "external-artifact state and require fresh `Read` of cited section + 30 "
        "lines downstream + verbatim quote of the firewall in the artifact. "
        "2026-06-05 anchoring failure: Alma 34:7 PP-conj rule cited "
        "framework.md:103-111 §2.2 in its comment while §2.2(ii) firewall at "
        "lines 113-117 EXPLICITLY forbids the shared-PP elision the rule "
        "restored; rule shipped + regen + +30 validator regressions before "
        "Workflow §7.3 audit caught it."),
    "feedback_preserve_formatting.md": ("feedback",
        "don't rebuild entire xlsx from scratch when only tabs changed; preserve "
        "column formatting"),
    "feedback_read_source_carefully.md": ("feedback",
        "careful source reading before changes"),
}

for target, rel in COPIES.items():
    src = os.path.join(FH, rel.replace("/", os.sep))
    text = io.open(src, encoding="utf-8", errors="replace").read()
    d = datetime.fromtimestamp(os.path.getmtime(src)).strftime("%Y-%m-%d")
    if target.endswith(".py"):
        prov = ("# PROVENANCE: recovered 2026-08-06 from Claude Code file-history "
                "(%s); state as of %s; possibly stale — re-verify before relying.\n"
                % (rel, d))
        lines = text.split("\n")
        ins = 1 if lines and lines[0].startswith("#!") else 0
        out = "\n".join(lines[:ins] + [prov.rstrip()] + lines[ins:])
    else:
        prov = ("> **PROVENANCE**: recovered 2026-08-06 from Claude Code "
                "file-history (`%s`); state as of %s (snapshot mtime); possibly "
                "stale — re-verify before relying.\n\n" % (rel, d))
        if text.startswith("---"):
            end = text.find("\n---", 3)
            end = text.find("\n", end + 1)
            out = text[: end + 1] + "\n" + prov + text[end + 1:]
        else:
            out = prov + text
    io.open(os.path.join(STAGE, target), "w", encoding="utf-8",
            newline="\n").write(out)
    print("copied  %-50s <- %s (%s)" % (target, rel, d))

for old, new in RENAMES.items():
    op, np = os.path.join(STAGE, old), os.path.join(STAGE, new)
    if os.path.exists(op):
        if os.path.exists(np):
            os.remove(np)
        os.rename(op, np)
        print("renamed %s -> %s" % (old, new))

for target, (typ, desc) in STUBS.items():
    name = target[:-3].lstrip("_").replace("_", "-")
    body = (
        "---\nname: %s\ndescription: \"%s\"\nmetadata:\n  node_type: memory\n"
        "  type: %s\n---\n\n"
        "> **LOST FILE — STUB ONLY (2026-08-06).** The full original was deleted "
        "with the `~/.claude/projects/C--Users-bibleman/memory/` namespace and "
        "was NOT recoverable from file-history, jsonl-archive Writes/Edits/Reads, "
        "or Dropbox backups. Everything below is the surviving index one-liner "
        "from the recovered `MEMORY.md` (@v44, 2026-06-15) — an inference-bearing "
        "summary, NOT the original record. Do not cite this as the warrant file.\n\n"
        "%s\n" % (name, desc.replace('"', "'")[:150], typ, desc))
    io.open(os.path.join(STAGE, target), "w", encoding="utf-8",
            newline="\n").write(body)
    print("stub    %s" % target)

mds = sorted(f for f in os.listdir(STAGE) if f.endswith(".md")
             and f != "RECOVERY-MANIFEST.md")
print("\nstaged .md files: %d" % len(mds))
