"""Pass 6: recover the last 5 memory files from Read tool-results in archived
transcripts. A Read of a file embeds its full content in the JSONL as
toolUseResult.file.content (raw) — recoverable even when no Write survives.
Takes the LATEST Read per target across the scanned archives."""
import os, io, json, gzip, glob
from datetime import datetime

HOME = os.path.expanduser("~")
ARCH = os.path.join(HOME, ".claude", "jsonl-archive")
STAGE = os.path.dirname(os.path.abspath(__file__))

TARGETS = [
    "project_session_durability.md", "project_wallace_summaries.md",
    "feedback_canon_citation_requires_verbatim_read.md",
    "feedback_preserve_formatting.md", "feedback_read_source_carefully.md",
]

SCAN = glob.glob(os.path.join(ARCH, "**", "*.jsonl.gz"), recursive=True)

reads = {t: [] for t in TARGETS}  # (ts, sess, content)

print("scanning %d transcripts" % len(SCAN))
for fp in SCAN:
    sess = os.path.basename(fp).replace(".jsonl.gz", "")
    try:
        fh = io.TextIOWrapper(gzip.open(fp, "rb"), encoding="utf-8", errors="replace")
    except OSError:
        continue
    for line in fh:
        hit = [t for t in TARGETS if t in line]
        if not hit or "toolUseResult" not in line:
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        tr = obj.get("toolUseResult")
        if not isinstance(tr, dict):
            continue
        ts = obj.get("timestamp", "")
        path, content = "", None
        f = tr.get("file")
        if isinstance(f, dict) and f.get("content"):
            path = str(f.get("filePath", "")).replace("\\", "/")
            content = f["content"]
        elif tr.get("originalFile") and tr.get("filePath"):
            # Edit result: originalFile is PRE-edit; apply the patch for post-state
            path = str(tr["filePath"]).replace("\\", "/")
            old, new = tr.get("oldString", ""), tr.get("newString", "")
            src = tr["originalFile"]
            content = (src.replace(old, new) if old and old in src else src)
        if not content:
            continue
        for t in hit:
            if path.endswith("/" + t):
                reads[t].append((ts, sess, content))
    fh.close()

for t in TARGETS:
    rs = sorted(reads[t])
    print("\n### %s : %d reads" % (t, len(rs)))
    if not rs:
        continue
    ts, sess, content = rs[-1]
    d = ts[:10] if ts else "unknown"
    prov = ("> **PROVENANCE**: recovered 2026-08-06 from a Read tool-result in "
            "jsonl-archive (session %s, read %s); state as of that read — later "
            "edits, if any, are not captured; possibly stale — re-verify before "
            "relying.\n\n" % (sess, d))
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
    print("   -> STAGED (read %s, session %s)" % (d, sess))
