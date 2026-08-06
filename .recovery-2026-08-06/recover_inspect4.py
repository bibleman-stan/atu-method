"""Pass 4: identify final file-history leads surfaced by content greps."""
import os, io
from datetime import datetime

HOME = os.path.expanduser("~")
FH = os.path.join(HOME, ".claude", "file-history")

CANDS = [
    "87af68a0-0291-4910-962f-d0913b5722e6/2f5b04c27e4b19f4@v3",
    "87af68a0-0291-4910-962f-d0913b5722e6/c7e86a8b3a9d8643@v2",
    "87af68a0-0291-4910-962f-d0913b5722e6/7d83c8e90b8f3b39@v2",
    "87af68a0-0291-4910-962f-d0913b5722e6/85d82fb1064cff1f@v2",
    "a626634d-6b4d-4da9-9069-9894ffa678b4/a45545106d747b8c@v2",
    "a626634d-6b4d-4da9-9069-9894ffa678b4/f64a1efcdc515d70@v26",
    "c62fff60-202d-4161-9983-60f9dc2b11a2/10a3dc27a212c4d8@v2",
    "b15d8d3f-13d4-4a90-bd66-6ad57e8b4350/f3b1940b03ed6ed6@v3",
]

for rel in CANDS:
    p = os.path.join(FH, rel.replace("/", os.sep))
    print("=" * 78)
    if not os.path.exists(p):
        print(rel, "-> MISSING")
        continue
    mt = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d %H:%M")
    print("%s  (%dB, mtime %s)" % (rel, os.path.getsize(p), mt))
    for ln in io.open(p, encoding="utf-8", errors="replace").read().splitlines()[:12]:
        print("  |", ln[:112])
