"""Pass 5: recover remaining memory files from jsonl-archive transcripts.

file-history has no snapshot of these 11 files (they were never edited after
file-history capture began). Session JSONLs record every Write tool call's full
content, so scan all archived transcripts for Write calls targeting each file;
keep the LATEST Write per target and count any Edit calls after it (partial
patches we'd be missing — flagged in provenance, not replayed).
"""
import os, io, json, glob, gzip
from datetime import datetime

HOME = os.path.expanduser("~")
ARCH = os.path.join(HOME, ".claude", "jsonl-archive")
STAGE = os.path.dirname(os.path.abspath(__file__))

TARGETS = [
    "user_stan.md", "project_session_durability.md", "project_wallace_summaries.md",
    "reference_analytics.md", "feedback_stan_thinks_claude_files.md",
    "feedback_parallel_default.md", "feedback_canon_citation_requires_verbatim_read.md",
    "feedback_simplicity_bias.md", "feedback_staged_paper_scope_discipline.md",
    "feedback_debug_trace_values.md", "feedback_preserve_formatting.md",
    "feedback_read_source_carefully.md",
]

writes = {t: [] for t in TARGETS}   # (ts, session, content)
edits = {t: [] for t in TARGETS}    # (ts, session)

files = glob.glob(os.path.join(ARCH, "**", "*.jsonl"), recursive=True) + \
        glob.glob(os.path.join(ARCH, "**", "*.jsonl.gz"), recursive=True)
print("scanning %d transcripts" % len(files))

for fp in files:
    sess = os.path.basename(fp)
    try:
        if fp.endswith(".gz"):
            fh = io.TextIOWrapper(gzip.open(fp, "rb"), encoding="utf-8",
                                  errors="replace")
        else:
            fh = io.open(fp, encoding="utf-8", errors="replace")
    except OSError:
        continue
    for line in fh:
        hit = [t for t in TARGETS if t in line]
        if not hit:
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        msg = obj.get("message") or {}
        content = msg.get("content")
        if not isinstance(content, list):
            continue
        ts = obj.get("timestamp", "")
        for blk in content:
            if not isinstance(blk, dict) or blk.get("type") != "tool_use":
                continue
            name = blk.get("name", "")
            inp = blk.get("input") or {}
            path = str(inp.get("file_path", ""))
            for t in hit:
                if not path.replace("\\", "/").endswith("/memory/" + t):
                    continue
                if name == "Write" and inp.get("content"):
                    writes[t].append((ts, sess, inp["content"]))
                elif name in ("Edit", "MultiEdit", "NotebookEdit"):
                    edits[t].append((ts, sess))
    fh.close()

for t in TARGETS:
    ws = sorted(writes[t])
    print("\n### %s : %d writes, %d edits" % (t, len(ws), len(edits[t])))
    if not ws:
        continue
    ts, sess, content = ws[-1]
    later = [e for e in edits[t] if e[0] > ts]
    d = ts[:10] if ts else "unknown"
    prov = ("> **PROVENANCE**: recovered 2026-08-06 from jsonl-archive (session %s, "
            "last full Write %s); %d later Edit call(s) NOT replayed%s; possibly "
            "stale — re-verify before relying.\n\n"
            % (sess.replace(".jsonl", ""), d, len(later),
               "" if not later else " (content may be missing those patches)"))
    # insert provenance after frontmatter if present
    out = content
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            end = content.find("\n", end + 1)
            out = content[: end + 1] + "\n" + prov + content[end + 1:]
        else:
            out = prov + content
    else:
        out = prov + content
    io.open(os.path.join(STAGE, t), "w", encoding="utf-8", newline="\n").write(out)
    print("   -> STAGED (write %s, %d unreplayed later edits)" % (d, len(later)))
