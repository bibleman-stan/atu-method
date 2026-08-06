"""Pass 3: eyeball-identification of specific file-history candidates for the
remaining missing targets (found via content greps + pass-2 ambiguity list).
Prints header + first lines of each; also locates every snapshot of the
broken-pointer script and lineage mtimes for path-hashes of interest."""
import os, io, glob
from datetime import datetime

HOME = os.path.expanduser("~")
FH = os.path.join(HOME, ".claude", "file-history")

CANDS = [
    "87af68a0-0291-4910-962f-d0913b5722e6/5eee468b0b9a82fd@v44",
    "87af68a0-0291-4910-962f-d0913b5722e6/78033740b52bb721@v2",
    "87af68a0-0291-4910-962f-d0913b5722e6/f64a1efcdc515d70@v3",
    "87af68a0-0291-4910-962f-d0913b5722e6/b75fa66326a53cb6@v2",
    "a626634d-6b4d-4da9-9069-9894ffa678b4/4b4e0ba1f3f28adf@v61",
    "4617c323-8b80-4212-ba03-ad167063781b/18affddc92c3d7cf@v2",
    "186002fd-c94d-4554-9545-c2a304abd45b/1ba1b673536d9d76@v2",
    "186002fd-c94d-4554-9545-c2a304abd45b/0e58fbec668bfc32@v12",
    "4617c323-8b80-4212-ba03-ad167063781b/4b1947faa47dd432@v8",
    "0902bcda-3ad4-4130-8a0b-bef174fc36d7/16c242f3957d5371@v2",
    "207b9cbe-32e7-4969-883d-9385135a663d/06a052e331367008@v3",
    "18327914-8fd6-4400-a057-2a38aaf1a09f/06a052e331367008@v2",
    "2d47e65a-08dd-4c42-a648-d3bdc95174d0/6fdc26be7dc098a8@v2",
    "5e934fd5-32e0-4958-9b1e-00dd9f0e6d19/b09e47860ba46442@v4",
    "5e934fd5-32e0-4958-9b1e-00dd9f0e6d19/38663eaffdfda9bb@v3",
    "2d47e65a-08dd-4c42-a648-d3bdc95174d0/d74f4bd523f80827@v3",
    "c62fff60-202d-4161-9983-60f9dc2b11a2/3b67f1d82175ae4d@v2",
    "56f6c33e-8eca-47a4-b5ac-58609af1440d/22314e3bccd0c5c7@v1",
    "56f6c33e-8eca-47a4-b5ac-58609af1440d/d2c1133c44b469a3@v2",
]

for rel in CANDS:
    p = os.path.join(FH, rel.replace("/", os.sep))
    print("=" * 78)
    if not os.path.exists(p):
        print(rel, "-> MISSING")
        continue
    mt = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d %H:%M")
    sz = os.path.getsize(p)
    print("%s  (%dB, mtime %s)" % (rel, sz, mt))
    try:
        lines = io.open(p, encoding="utf-8", errors="replace").read().splitlines()
    except OSError as e:
        print("  read error:", e)
        continue
    for ln in lines[:14]:
        print("  |", ln[:110])

print("=" * 78)
print("ALL SNAPSHOTS of path-hashes of interest (newest mtime last):")
for h in ["f3b1940b03ed6ed6", "7e754ffd8d994501", "06a052e331367008"]:
    hits = glob.glob(os.path.join(FH, "*", h + "@v*"))
    hits.sort(key=os.path.getmtime)
    print("--- %s (%d snapshots)" % (h, len(hits)))
    for p in hits[-4:]:
        mt = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d %H:%M")
        print("   %s  %6dB  %s" % (os.path.relpath(p, FH).replace(os.sep, "/"),
                                   os.path.getsize(p), mt))
