"""Pass 8: land the recovered set (Mandate A remainder).
- memories/operational/  <- all 70 recovered .md (adds provenance headers to the
  six meta-wiki-staged files that lack one; banner line atop MEMORY.md)
- 5-machinery/scripts/check_broken_pointers.py  <- recovered audit tool (per
  feedback_scratch_belongs_in_repo: reusable dev 5-machinery/scripts live tracked in 5-machinery/scripts/)
- .archive/recovery-2026-08-06/  <- manifest + recover_*.py method 5-machinery/scripts
- session memory namespace gets a pointer MEMORY.md
- staging dir contents removed (dir deleted by caller after this script)
"""
import os, io, shutil

REPO = r"c:\Users\bibleman\repos\atu-method"
STAGE = os.path.join(REPO, ".recovery-2026-08-06")
OPS = os.path.join(REPO, "memories", "operational")
SCRIPTS = os.path.join(REPO, "5-machinery/scripts")
ARCH = os.path.join(REPO, ".archive", "recovery-2026-08-06")
SESSMEM = os.path.expanduser(
    r"~\.claude\projects\c--Users-bibleman-repos-atu-method\memory")

SIBLING_STAGED = {
    "_north_star.md": "455e2f1f-…/918117a5ceb3cffb@v4, state 2026-06-01",
    "_deferred_queue.md": "newest 01f7ecc9f948752f@vN, state ~2026-06",
    "project_master_blaster.md": "newest 1dc9e8f397d2c122@vN, state ~2026-06",
    "project_bofm_discourse_voice_deploy.md": "newest b8adeede15761c57@vN, state ~2026-06",
    "reference_emode_substrate.md": "newest bfef1e2a34597e82@vN, state ~2026-06",
    "project_bofm_substrate_quality.md": "newest bfd5c153475c6061@vN, state ~2026-06",
}

os.makedirs(OPS, exist_ok=True)
os.makedirs(SCRIPTS, exist_ok=True)
os.makedirs(ARCH, exist_ok=True)
os.makedirs(SESSMEM, exist_ok=True)

landed = 0
for fn in sorted(os.listdir(STAGE)):
    src = os.path.join(STAGE, fn)
    if fn == "RECOVERY-MANIFEST.md" or fn.startswith(("recover_", "land8")):
        shutil.copy2(src, os.path.join(ARCH, fn))
        continue
    if fn == "check_broken_pointers.py":
        shutil.copy2(src, os.path.join(SCRIPTS, fn))
        print("5-machinery/scripts/ <-", fn)
        continue
    if not fn.endswith(".md"):
        continue
    text = io.open(src, encoding="utf-8").read()
    if fn == "MEMORY.md":
        text = ("> **RECOVERED INDEX** (2026-08-06, state as of 2026-06-15 @v44) — "
                "namespace-deletion recovery; entries may be stale; provenance in "
                "`.archive/recovery-2026-08-06/RECOVERY-MANIFEST.md`.\n\n" + text)
    elif fn in SIBLING_STAGED and "**PROVENANCE**" not in text:
        prov = ("> **PROVENANCE**: recovered 2026-08-06 from Claude Code "
                "file-history (%s); possibly stale — re-verify before relying.\n\n"
                % SIBLING_STAGED[fn])
        if text.startswith("---"):
            end = text.find("\n---", 3)
            end = text.find("\n", end + 1)
            text = text[: end + 1] + "\n" + prov + text[end + 1:]
        else:
            text = prov + text
    io.open(os.path.join(OPS, fn), "w", encoding="utf-8", newline="\n").write(text)
    landed += 1

print("landed %d .md into memories/operational/" % landed)

pointer = """# Memory index — atu-method session namespace

This namespace's durable memory lives TRACKED IN THE REPO, not here:

- `c:/Users/bibleman/repos/atu-method/memories/` — cross-corpus methodology rules (see its `_index.md`)
- `c:/Users/bibleman/repos/atu-method/memories/operational/` — operational memory (north-star, deferred queue, named arcs, user profile, feedback disciplines; see its `MEMORY.md`)

Recovered 2026-08-06 after the user-home namespace deletion; provenance in
`repos/atu-method/.archive/recovery-2026-08-06/RECOVERY-MANIFEST.md`.
Write new durable memories to the repo dirs above (tracked, backed up), not to
this directory — this file is the pointer that survives.
"""
io.open(os.path.join(SESSMEM, "MEMORY.md"), "w", encoding="utf-8",
        newline="\n").write(pointer)
print("session-namespace pointer MEMORY.md written")
