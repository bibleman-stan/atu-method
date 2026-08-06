"""Pass 2: token-overlap matching for the 24 targets pass 1 missed.

Pass 1 (recover_sweep.py) matched frontmatter name-slugs to index filenames by
normalized equality/containment; that missed files whose slug words differ from
the filename (e.g. `academic-vault-orientation` vs `reference_academic_vault.md`).
This pass scores Jaccard-style token overlap and reports best candidates per
missing target; stages high-confidence hits, prints ambiguous ones for review.
"""
import os, re, glob, io
from datetime import datetime

HOME = os.path.expanduser("~")
FH = os.path.join(HOME, ".claude", "file-history")
STAGE = os.path.dirname(os.path.abspath(__file__))

MISSING = [
    "_named_arcs.md", "user_stan.md", "project_session_durability.md",
    "project_bom_reader.md", "project_gnt_idea_unit_measurement.md",
    "project_wallace_summaries.md", "reference_academic_vault.md",
    "reference_analytics.md", "reference_corpus_pipeline_map.md",
    "reference_zotero_mcp.md", "feedback_scratch_belongs_in_repo.md",
    "feedback_stan_thinks_claude_files.md", "feedback_do_it_once.md",
    "feedback_surface_judgment_calls.md", "feedback_parallel_default.md",
    "feedback_canon_citation_requires_verbatim_read.md",
    "feedback_simplicity_bias.md", "feedback_staged_paper_scope_discipline.md",
    "feedback_atu_resolution_author_relative.md", "feedback_rhetoric_bandwagon.md",
    "feedback_stan_writes_claude_edits.md", "feedback_debug_trace_values.md",
    "feedback_preserve_formatting.md", "feedback_read_source_carefully.md",
]

STOP = {"feedback", "project", "reference", "md", "the", "a", "is", "not", "be",
        "must", "no", "in", "of", "for", "and", "to"}

def toks(s):
    return {t for t in re.split(r"[^a-z0-9]+", s.lower()) if t and t not in STOP}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)

def main():
    best = {}
    for sess in os.listdir(FH):
        sdir = os.path.join(FH, sess)
        if not os.path.isdir(sdir):
            continue
        for fn in os.listdir(sdir):
            m = re.match(r"([0-9a-f]{16})@v(\d+)$", fn)
            if not m:
                continue
            key = m.group(1)  # dedupe by content-hash ACROSS sessions
            v = int(m.group(2))
            path = os.path.join(sdir, fn)
            if key not in best or v > best[key][0]:
                best[key] = (v, path)

    cands = []
    for h, (v, path) in best.items():
        try:
            if os.path.getsize(path) > 200_000:
                continue
            text = io.open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        m = FM_RE.match(text)
        if not m:
            continue
        fm = m.group(1)
        if "node_type: memory" not in fm and not re.search(
            r"^\s*type:\s*(user|feedback|project|reference)\s*$", fm, re.MULTILINE
        ):
            continue
        nm = NAME_RE.search(fm)
        name = nm.group(1) if nm else ""
        dm = DESC_RE.search(fm)
        desc = dm.group(1) if dm else ""
        cands.append((name, desc, path, os.path.getmtime(path), text))

    print("total deduped memory-shaped candidates:", len(cands))
    for target in MISSING:
        tt = toks(target[:-3])
        scored = []
        for name, desc, path, mt, text in cands:
            ct = toks(name) | toks(desc[:80])
            inter = tt & ct
            if not inter:
                continue
            score = len(inter) / len(tt)
            scored.append((score, name, desc[:70], path, mt, text))
        scored.sort(reverse=True, key=lambda x: x[0])
        print("\n### %s" % target)
        if not scored:
            print("  NO CANDIDATES")
            continue
        for score, name, desc, path, mt, _ in scored[:3]:
            d = datetime.fromtimestamp(mt).strftime("%Y-%m-%d")
            print("  %.2f  %-45s %s  %s" % (score, name[:45], d,
                  os.path.relpath(path, FH).replace(os.sep, "/")))
        score, name, desc, path, mt, text = scored[0]
        if score >= 0.6:
            d = datetime.fromtimestamp(mt).strftime("%Y-%m-%d")
            prov = ("> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history "
                    "(`" + os.path.relpath(path, FH).replace(os.sep, "/") + "`); state as of "
                    + d + " (snapshot mtime); possibly stale — re-verify before relying.\n\n")
            m = FM_RE.match(text)
            out = text[: m.end()] + prov + text[m.end():] if m else prov + text
            io.open(os.path.join(STAGE, target), "w", encoding="utf-8",
                    newline="\n").write(out)
            print("  -> STAGED as %s" % target)
        else:
            print("  -> ambiguous, NOT staged (top score %.2f)" % score)

if __name__ == "__main__":
    main()
