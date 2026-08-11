---
cssclasses:
  - wide
---

# Audit — repository architecture, git, and release engineering

> **Hostile audit of [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]]**, from a git / repo-architecture / release-engineering angle only. Run 2026-08-09. Every state claim carries a pasted receipt; every best-practice claim carries a URL. Nothing was committed or pushed. Read-only git plus live HTTP probes of the five production domains.
>
> **Verdict in one line:** the *diagnosis* survives and is in places understated; the *publish-target mechanism* is unsound as specified and would destroy irreplaceable data on at least one repo; and the plan is missing the entire release-engineering layer — there is no CI anywhere, no dependency pinning anywhere, no release versioning anywhere, and the "engine" that is supposed to force-push cannot push at all.

---

## 0. Method and limits of this audit

| | |
|---|---|
| Repos inspected | `atu-method`, `readers-tanakh`, `readers-bofm`, `readers-gnt`, `readers-lxx`, `readers-vulgate`, `readers-gnt-morph`, `readers-tanakh-morph`, `rev-reader`, `biblical-corpora` |
| Live probes | `tanakh-reader.com`, `bomreader.com`, `gnt-reader.com`, `lxx-reader.com`, `vulgate-reader.com` |
| **Could not verify** | GitHub Pages *publishing-source* API setting, per-repo Actions/Environments config, issue counts beyond one repo page. `gh` is not installed: `$ which gh` → `bash: gh: command not found`. Claims that depend on the Pages API are labelled **PLAUSIBLE**, never CONFIRMED. |
| Not in scope | Whether the ATU methodology is right; whether one engine is linguistically correct (Part 9's own first bullet). |

---

## 1. Repo inventory — reality check

**Receipt — commits, branches, tracked files:**

```
$ for r in atu-method readers-tanakh readers-bofm readers-gnt readers-lxx \
    readers-vulgate readers-gnt-morph readers-tanakh-morph rev-reader biblical-corpora; do
    d="/c/Users/bibleman/repos/$r"; ...; done

atu-method           | commits=146  | branch=main   | first=2026-05-10 | last=2026-08-09 | tracked_files=272
readers-tanakh       | commits=447  | branch=main   | first=2026-04-25 | last=2026-08-07 | tracked_files=13394
readers-bofm         | commits=1149 | branch=main   | first=2026-02-26 | last=2026-08-08 | tracked_files=1751
readers-gnt          | commits=607  | branch=main   | first=2026-04-09 | last=2026-08-07 | tracked_files=1776
readers-lxx          | commits=17   | branch=main   | first=2026-05-27 | last=2026-08-07 | tracked_files=1915
readers-vulgate      | commits=19   | branch=main   | first=2026-05-27 | last=2026-08-07 | tracked_files=610
readers-gnt-morph    | commits=53   | branch=main   | first=2026-04-17 | last=2026-06-09 | tracked_files=775
readers-tanakh-morph | commits=19   | branch=main   | first=2026-06-09 | last=2026-06-13 | tracked_files=946
rev-reader           | commits=2    | branch=master | first=2026-04-21 | last=2026-05-19 | tracked_files=11
biblical-corpora     | NOT A GIT REPO
```

**Receipt — size:**

```
$ git -C <repo> count-objects -vH
atu-method           size-pack: 0 bytes        loose: 22.69 MiB
readers-tanakh       size-pack: 222.81 MiB     loose: 26.86 MiB
readers-bofm         size-pack: 7.11 MiB       loose: 2.60 GiB
readers-gnt          size-pack: 27.38 MiB      loose: 17.38 MiB
readers-lxx          size-pack: 0 bytes        loose: 9.48 MiB
readers-vulgate      size-pack: 0 bytes        loose: 10.25 MiB
readers-gnt-morph    size-pack: 12.79 MiB      loose: 0 bytes
rev-reader           size-pack: 0 bytes        loose: 24.98 KiB
```

**Receipt — tracked bytes and composition** (`forensics.py`, run with `PYTHONIOENCODING=utf-8`):

```
===== atu-method: 272 tracked files, 100.3 MB
    75.73 MB  data/kjv-strongs/MetaV_MainIndex.csv
  .csv 5 files 89.83 MB | .md 206 files 2.10 MB | .py 42 files 0.28 MB

===== readers-tanakh: 13394 tracked files, 118.5 MB
  .txt 12150 files 52.99 MB | .html 930 files 50.47 MB | .json 72 files 9.05 MB | .py 101 files 2.14 MB

===== readers-bofm: 1751 tracked files, 1730.3 MB
    21.83 MB  audio/03-Jacob/jacob-5-samuel.mp3
  .mp3 239 files 1571.62 MB | .conllu 856 files 79.73 MB | .json 358 files 35.65 MB
  .tf 21 files 22.36 MB | .html 19 files 9.55 MB | .py 153 files 1.60 MB

===== readers-gnt: 1776 tracked files, 54.3 MB
  .txt 1590 files 41.66 MB | .html 28 files 6.00 MB | .json 7 files 4.63 MB

===== readers-lxx: 1915 tracked files, 29.5 MB   (.html 40 files 19.16 MB)
===== readers-vulgate: 610 tracked files, 29.0 MB (.tf 21 files 22.80 MB)
===== rev-reader: 11 tracked files, 0.1 MB
```

**Receipt — `.venv` / vendored deps are NOT committed anywhere** (a negative, verified not inferred):

```
$ git -C <repo> ls-files | grep -Ec "(^|/)(\.venv|venv|node_modules|site-packages)/"
atu-method 0 | readers-tanakh 0 | readers-bofm 0 | readers-gnt 0
readers-lxx 0 | readers-vulgate 0 | rev-reader 0
```

**Receipt — no submodules anywhere:** `ls <repo>/.gitmodules` → `(none)` for all eight git repos.

### Findings from inventory

| # | Finding | Severity | Status |
|---|---|---|---|
| I-1 | **`readers-bofm` tracks 1.57 GB of MP3 in plain git, no LFS.** Total tracked bytes 1730.3 MB. GitHub documents a **1 GB recommended limit for Pages source repos** and **"Published GitHub Pages sites may be no larger than 1 GB."** `bomreader.com` publishes from repo root, so the published site is already **~1.7× the documented ceiling**. | **SERIOUS** | CONFIRMED |
| I-2 | The proposal says the presentation layer is **"~92 HTML files."** Actual tracked HTML across the five live readers is **1,045** (`930 + 19 + 28 + 40 + 28`). The build output that a publish target must carry is **11× larger than the proposal's own figure**. | **SERIOUS** | CONFIRMED |
| I-3 | `biblical-corpora` — named in [[CLAUDE.md]]'s repo map as the shared vendored-clone repo — **is not a git repo at all.** It has no `.git`. It cannot be a dependency of a reproducible build. | **SERIOUS** | CONFIRMED |
| I-4 | `rev-reader` has **no git remote** (`git remote -v` → empty) and is on `master`, not `main`. It exists only on this laptop. | MINOR | CONFIRMED |
| I-5 | `readers-bofm`'s local `.git` holds **2.60 GiB of loose objects** against a 7.11 MiB pack — it has never been meaningfully gc'd. Any clone or fetch of this repo is expensive. | MINOR | CONFIRMED |
| I-6 | Tags across all repos: **1 total** (`readers-tanakh: pre-bhsa-promote`). There is no release versioning of any kind in this system today. | **SERIOUS** | CONFIRMED |

Receipt for I-6:

```
$ for r in ...; do git -C $r tag | wc -l; done
atu-method 0 | readers-tanakh 1 | readers-bofm 0 | readers-gnt 0 | readers-lxx 0 | readers-vulgate 0
$ git -C readers-tanakh tag -l -n1
pre-bhsa-promote  chore: demote CLAUDE.md to thin stub + archive directives queue (master-blaster Phase 6c)
```

Sources: [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) — *"Published GitHub Pages sites may be no larger than 1 GB"*, *"GitHub Pages source repositories have a recommended limit of 1 GB"*; [Conditions for large files](https://docs.github.com/en/enterprise/2.13/user/articles/conditions-for-large-files).

---

## 2. Claim 1 — "reader repos become publish targets, force-pushed by the engine"

Proposal, Part 5: *"Each site becomes a **publish target**: build output plus a `CNAME`, force-pushed by the engine's build. No rules, no validators, no generator, no [[CLAUDE.md]] persona, no independent history worth defending."*

### 2.1 The constraint the proposal cites is real, and its diagnosis is *understated*

**Receipt — every reader has a root `CNAME`, all five domains are live:**

```
$ cat <repo>/CNAME
readers-tanakh   tanakh-reader.com
readers-bofm     bomreader.com
readers-gnt      gnt-reader.com
readers-lxx      lxx-reader.com
readers-vulgate  vulgate-reader.com

$ curl -sIL <domain>
https://bomreader.com/         HTTP=200 size=197523
https://tanakh-reader.com/     HTTP=200 size=158237
https://gnt-reader.com/        HTTP=200 size=109871
https://lxx-reader.com/        HTTP=200 size=106615
https://vulgate-reader.com/    HTTP=200 size=106028
```

The proposal *understates* how bad the current source/publish conflation is. Because the Pages publishing source is the repo root, **the entire source tree is publicly served on the production domains**:

```
$ curl -s -o /dev/null -w "%{http_code} %{size_download}\n" -L <url>
https://tanakh-reader.com/scripts/build_books.py   200  23889
https://gnt-reader.com/scripts/build_books.py      200  17271
https://bomreader.com/CLAUDE.md                    200   5364
https://tanakh-reader.com/data/search_index.json   200
```

**Finding P-0 (CONFIRMED, SERIOUS-in-favour-of-the-proposal):** [[CLAUDE.md]], build 5-machinery/scripts, and the full corpus data directory are served to the open internet from every reader domain. Separating build output from source is not just architectural hygiene here — it closes a live exposure. **This is the strongest argument in the proposal and it is not the one the proposal makes.**

### 2.2 Force-push is the wrong mechanism, and on one repo it is destructive

| # | Finding | Severity | Status |
|---|---|---|---|
| **P-1** | **Force-pushing build output over `readers-bofm` destroys the only tracked copy of irreplaceable, non-reproducible data.** The repo tracks **856 LLM-generated CoNLL-U files (79.7 MB)** under `data/parses/llm-direct/*-batches/` plus `data/text-files/v2-adjudicated/overrides.json` (911 adjudications). Per [[CLAUDE.md]], the live BoFM parse is the *lever-2 LLM-corrected* cache — output of a non-deterministic, paid, multi-session process. It is **not** build output and **cannot** be regenerated by the engine. | **FATAL** | CONFIRMED |
| **P-2** | **The engine cannot force-push.** `readers-bofm/4-process/04-deployment-infra.md`: *"Stan pushes from his local machine (sandbox can't push — gets 403 proxy error)"*. Every deploy in this system is a manual human action through GitHub Desktop. "Force-pushed by the engine's build" describes a capability that does not exist and that the proposal never proposes building. | **FATAL** | CONFIRMED |
| **P-3** | **Force-push does not shrink the repo and does not remove the history.** `readers-tanakh` has a **222.81 MiB pack** against a 118.5 MB working tree — history is roughly 2× current content. Overwriting `main` makes old commits unreachable, not absent: GitHub's own guidance is that after a history rewrite *"the commits with sensitive data may still be accessible … directly via their SHA-1 hashes in cached views"* and that permanent removal requires contacting support. The "publish target has no history worth defending" framing is a design intention, not a git outcome. | **SERIOUS** | CONFIRMED |
| **P-4** | **`git blame` and `git log` become worthless, and the proposal treats that as free.** 447 / 1,149 / 607 commits of editorial decision history become unreachable in the UI; what replaces them is `blame` over machine-generated HTML. There is no proposal for archiving the pre-conversion history (a tag, a `legacy/*` branch, a mirror repo). One tag exists in the entire estate (I-6), so the "we'll just tag it first" reflex has no precedent here to lean on. | **SERIOUS** | CONFIRMED |
| **P-5** | **Rollback becomes strictly worse, not better.** Today a bad deploy is `git revert` on the reader repo. Under the proposal, rolling back means re-running the engine at an older engine commit — which requires (a) an engine-commit ↔ site-commit map the proposal does not specify, (b) the corpus substrate, which is **gitignored and partly a symlink into Dropbox** (§6), and (c) a pinned dependency set, which does not exist (§6). Meanwhile force-push has itself deleted the previous good build. **Mean time to recover goes from seconds to "rebuild the world and hope."** | **FATAL** | CONFIRMED |
| **P-6** | **Service-worker cache invalidation is unaddressed.** `readers-bofm/sw.js`: `const CACHE_NAME = 'bomreader-v325';` — 325 manual cache bumps. `readers-lxx/sw.js` and `readers-vulgate/sw.js` carry `* Bump CACHE_VERSION on each deploy so old caches are purged.` A generated publish target must generate the cache version deterministically or every deploy serves stale assets to returning users. The word "cache" does not appear in the proposal. | **SERIOUS** | CONFIRMED |
| **P-7** | **No `.nojekyll` anywhere, and Jekyll is demonstrably active.** Probe: `https://tanakh-reader.com/_archive/2026-05-18-.../colometry-canon.md` → **404**, while `https://tanakh-reader.com/README.md` → **200**. Jekyll is silently excluding `_`-prefixed paths. A generated publish target that ever emits `_assets/`, `_next/`, or `_app/` will 404 with no error anywhere. | **SERIOUS** | CONFIRMED |
| **P-8** | **Deploy would still be rate-limited.** Pages-from-branch has a *"soft limit of 10 builds per hour"*, and GitHub states *"This limit does not apply if you build and publish your site with a custom GitHub Actions workflow."* A one-engine build that fans out to 4–5 sites per change sits close to that ceiling on an iterative day — and the proposal's chosen mechanism is exactly the one the limit applies to. | MINOR | CONFIRMED |

Receipts for P-1, P-2, P-6, P-7:

```
$ git -C readers-bofm ls-files '*.conllu' | sed 's|/[^/]*$||' | sort | uniq -c | sort -rn | head
    200 data/parses/llm-direct/alma-batches
     84 data/parses/llm-direct/2nephi-batches
     80 data/parses/llm-direct/helaman-batches
     ... (856 files, 79.73 MB total)

$ python -c "import json; d=json.load(open('.../v2-adjudicated/overrides.json')); print(len(d))"
911     # Counter({'list': 911})  ← proposal's own claim, CONFIRMED

$ head -20 readers-bofm/4-process/04-deployment-infra.md
- **GitHub Pages** from `main` branch
- Stan pushes from his local machine (sandbox can't push — gets 403 proxy error)
- Audio files (large MP3s) are committed directly to the repo (no LFS)

$ grep -m1 CACHE readers-bofm/sw.js
const CACHE_NAME = 'bomreader-v325';

$ curl -s -o /dev/null -w "%{http_code}\n" -L https://tanakh-reader.com/_archive/.../colometry-canon.md
404
$ curl -s -o /dev/null -w "%{http_code}\n" -L https://tanakh-reader.com/README.md
200
```

### 2.3 The standard pattern the proposal reinvents badly

Force-pushing generated files into the default branch of a source repo is the pattern GitHub explicitly moved away from. The current recommended shape is **Pages-from-Actions**: `actions/upload-pages-artifact` → `actions/deploy-pages`, which *"allows publishing both versioned and transient content"* and is aimed exactly at *"transient content … which have little reason to be committed to the repository."*

Ranked alternatives for this specific shape (one engine, N corpora, N domains, one developer):

| Option | Mechanism | Fit here |
|---|---|---|
| **A. Pages-from-Actions in the engine repo, per-domain repos keep only a workflow** | Engine builds; each domain repo runs a workflow that pulls the artifact and calls `deploy-pages`. Nothing is committed. | **Best fit.** Preserves history intact, gives per-domain deployment records and one-click **Re-run/Rollback** in the Environments UI, exempts you from the 10-builds/hour limit, and the deploy artifact is retained and downloadable. |
| **B. Publish to an orphan `gh-pages` branch, `main` untouched** | `peaceiris/actions-gh-pages` or plain `git push --force origin gh-pages`. | **Acceptable and cheap.** Force-push is *safe* here because the branch is by construction disposable. Keeps `main` history, blame, and the LLM parses intact. This is the proposal's idea with the one-word fix that makes it survivable. |
| **C. Separate `site-*` repos, engine force-pushes `main`** | The proposal, applied to *new* repos. | Workable, but requires re-pointing each verified custom domain and accepts DNS/verification risk per domain (GitHub: domain verification is account-level and a domain left claimed by an old repo produces *"already taken"*). Trades a live-site outage risk for nothing that B doesn't give you. |
| **D. Force-push build output onto the existing reader `main` branches** | **The proposal as written.** | **Rejected.** Destroys P-1 data, destroys P-4 history, degrades P-5 rollback, and requires P-2 capability that doesn't exist. |

Sources: [actions/deploy-pages](https://github.com/actions/deploy-pages), [actions/upload-pages-artifact](https://github.com/actions/upload-pages-artifact), [Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), [Configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages), [Verifying your custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [Removing sensitive data from a repository](https://docs.github.com/en/enterprise-server@3.17/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

> **Bottom line on Claim 1.** The *goal* — sites stop having opinions — is right and the exposure receipt (P-0) proves it harder than the proposal does. The *mechanism* is wrong in a way that is not a detail: `--force` onto `main` is the single git operation that converts a reversible mistake into an irreversible one, and it is being aimed at the repo holding the least reproducible asset in the estate.

---

## 3. Claim 2 — "one engine repo replaces per-repo generators"

### 3.1 The coupling is already real, and worse than "shared code"

**Receipt — the engine is already imported by absolute sibling path:**

```python
# readers-gnt/scripts/build_books.py:35-37
_ATU_METHOD_ROOT = os.path.join(os.path.dirname(REPO_ROOT), "atu-method")
if _ATU_METHOD_ROOT not in sys.path:
    sys.path.insert(0, _ATU_METHOD_ROOT)
```
```python
# readers-tanakh/scripts/build_books.py:216-218
    if ATU_METHOD_ROOT not in sys.path:
        sys.path.insert(0, ATU_METHOD_ROOT)
    from atu_method.swaps import apply_swaps, load_corpus_swap_list
```

**Receipt — import counts (proposal's figures, independently CONFIRMED exactly):**

```
$ for r in ...; do grep -rl "atu_method" $r --include=*.py | wc -l; done
readers-tanakh 10 | readers-bofm 5 | readers-gnt 4 | readers-lxx 0 | readers-vulgate 0
```

| # | Finding | Severity | Status |
|---|---|---|---|
| **E-1** | The repos are **already a de facto monorepo with a filesystem-adjacency contract instead of a dependency declaration.** `atu-method` ships a `pyproject.toml` (`name = "atu-method"`, `version = "0.1.0"`) and is nonetheless consumed by `sys.path.insert` on a hardcoded sibling path. Move any repo and three readers break. Clone one repo alone and it cannot build. **This is the strongest available argument for consolidation, and the proposal does not make it.** | **SERIOUS** | CONFIRMED |
| **E-2** | `atu-method` version is `0.1.0` and has **0 tags across 146 commits**. There is no version anyone could pin to. Consolidation does not create this problem, but it removes the last excuse for not fixing it. | **SERIOUS** | CONFIRMED |
| **E-3** | The proposal's target diagram puts **RULES + CASES + ENGINE + CHECKS + APP + LOG** in `atu-method`, which already tracks **100.3 MB, 89.83 MB of it in five CSVs** (`MetaV_MainIndex.csv` alone is 75.73 MB). Adding the app and the case corpus to a repo that is already 90% lexicon-blob is a shape worth deciding deliberately, not by accretion. | MINOR | CONFIRMED |

### 3.2 Monorepo vs polyrepo — what practice actually says for *this* shape

The literature is written for organisations, and its polyrepo case is almost entirely an *organisational* case: *"Each service stayed small and comprehensible. Teams could move fast without coordinating with everyone else"*, *"different teams could use different tech stacks."* **Those benefits are worth exactly zero to a one-developer estate.** The polyrepo *costs* — *"cross-service debugging became painful… opening six different repositories, each with its own logging format and development setup"*, *"multiple CI pipelines and repeated tooling maintenance"* — are all live here and are precisely what the proposal is reacting to.

The named failure mode fits with uncomfortable precision: *"a distributed monolith — separate repositories that still have to deploy together, which gives you the coordination cost of a monorepo with none of the benefits."* Three readers `sys.path`-insert a sibling directory. That is a distributed monolith, verified at `readers-gnt/scripts/build_books.py:35`.

Google's monorepo argument is not directly transferable at this scale, but the mechanism it names is: a single repository provides *"a common source of truth"* and enables atomic cross-project change, at the cost of needing custom tooling once scale bites. **At ~2,000 tracked files of actual code across the estate, scale does not bite.** The counter-argument — *"once your monorepo hits a certain size, building everything becomes a serious infrastructure problem"* — is a real risk only for the MP3 and lexicon blobs, not for the code.

**Judgement: a monorepo for rules + engine + app + cases is correct for this shape, and the proposal is right about it.** But three caveats it does not state:

1. **The large assets must not come with.** `readers-bofm`'s 1.57 GB of MP3 and `atu-method`'s 89.83 MB of CSV must move to LFS or out-of-band storage *before* consolidation, or the monorepo inherits a clone cost that makes every future decision worse.
2. **Partial checkout is not free.** Git sparse-checkout / partial clone exist and would work, but they are one more piece of machinery for a developer who has stated he is already *"unable to process or navigate."* That cost belongs in the cost table (§5) and is absent from it.
3. **CI cost is currently zero because CI does not exist** (§6, C-1). Any comparison of monorepo vs polyrepo CI economics here is comparing two hypotheticals.

Sources: [Monorepo vs Polyrepo — Nx](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo), [Monorepos vs. Polyrepos — LogRocket](https://blog.logrocket.com/monorepos-vs-polyrepos-which-one-fits-your-use-case/), [Monorepo vs. Polyrepo — Spacelift](https://spacelift.io/blog/monorepo-vs-polyrepo), [Monorepo vs Polyrepo — Buildkite](https://buildkite.com/resources/blog/monorepo-polyrepo-choosing/), [Potvin & Levenberg, *Why Google Stores Billions of Lines of Code in a Single Repository*, CACM 59(7), 2016](https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/).

---

## 4. Claim 3 — migration one repo at a time, retire on a pre-set date

### 4.1 Is strangler fig right here?

Strangler fig is the correct *family* of pattern — Microsoft and AWS both document it as the default for incremental legacy replacement, and the alternative (big-bang against four live production domains with every validator baseline stale) is indefensible. **But the proposal invokes the pattern without invoking its one hard precondition**, and the failure mode is the documented one.

The literature is blunt about how this fails: *"Teams must stay focused and systematic; otherwise, the migration can stall indefinitely, leaving the organization with two partially modernized systems."* And more specifically: organisations *"stall once the highest-visibility features are migrated, leaving the legacy system running indefinitely in a reduced but permanent capacity, creating a worst-case outcome with double the maintenance burden … with none of the payoff of full decommissioning."* Fowler's own framing of the risk: *"lack of will and resources to finish the strangling job might lead to a bigger mess where your system now has two ways of doing everything with an awkward interface between the two."*

| # | Finding | Severity | Status |
|---|---|---|---|
| **M-1** | **The proposal's own cost table concedes the stall condition and then proposes the plan that maximises exposure to it.** It states completion's cognitive cost is *"a hybrid where some readers are sources and some are publish targets, two live models to hold at once, **for as long as migration runs**."* The documented stall mode is exactly "migration runs forever." The plan's only defence is *"retire the old path on a date decided in advance"* — a date with no owner, no forcing function, and no consequence for missing it. **In a one-developer estate, a deadline with no external stakeholder is not a control.** | **SERIOUS** | CONFIRMED (proposal text) + literature |
| **M-2** | **Migration order is unstated, and it matters enormously.** `readers-lxx` and `readers-vulgate` import `atu_method` **zero** times, have 17 and 19 commits, and 0 and 0 irreplaceable LLM artifacts. `readers-bofm` has 1,149 commits, 1.57 GB of audio, 856 LLM parses, a 325-version service worker, and a Firebase-backed annotations layer. **Convert `readers-vulgate` first; convert `readers-bofm` last or never.** The proposal says "one at a time" and stops. | **SERIOUS** | CONFIRMED |
| **M-3** | **Strangler fig requires an interception point.** The pattern works because a façade routes traffic between old and new, so cutover and rollback are a routing change. Here the "façade" is DNS + a `CNAME` file, which means **cutover per site is all-or-nothing and rollback is a DNS/Pages reconfiguration, not a config flip.** No parallel-run mechanism is proposed — no `staging.<domain>`, no `<repo>.github.io/<name>` preview, no output-diff gate between old builder and new engine on the same corpus. Without one, "keeping every live site serving" is an aspiration, not a mechanism. | **SERIOUS** | CONFIRMED |
| **M-4** | Zero repos are on anything but `main`/`master` and all five readers are currently dirty and exactly in sync with origin (`ahead/behind 0/0`, dirty 7/23/9/13/0). **There is no branching discipline to fall back on** during a migration that will need one. | MINOR | CONFIRMED |

Receipt for M-4:

```
$ for r in ...; do git -C $r status --porcelain | wc -l; git -C $r rev-list --left-right --count origin/main...HEAD; done
readers-tanakh   dirty=7   ahead/behind=0/0
readers-bofm     dirty=23  ahead/behind=0/0
readers-gnt      dirty=9   ahead/behind=0/0
readers-lxx      dirty=13  ahead/behind=0/0
readers-vulgate  dirty=0   ahead/behind=0/0
```

**The fix M-1 needs is structural, not motivational:** make the old path *impossible* rather than *deprecated*. Concretely — once a corpus is converted, delete its generator in the same commit as the conversion, so there is no second way to build it. A stalled strangler is only expensive when both systems still run.

Sources: [Strangler Fig pattern — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig), [Strangler fig pattern — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html), [Embracing the Strangler Fig pattern — Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/embracing-strangler-fig-pattern-legacy-modernization-part-one), [Strangler Fig Pattern — Swimm](https://swimm.io/learn/legacy-code/strangler-fig-pattern-modernizing-it-without-losing-it), [Strangler Fig legacy migration — AltexSoft](https://www.altexsoft.com/blog/strangler-fig-legacy-system-migration/).

---

## 5. Claim 4 — the cost table

> | Cost axis | Greenfield | Finish the abandoned direction |
> | Engineering effort | Higher | **Lower** |
> | Cognitive load on Stan | **Lower** | Higher |
> | Error discovery / rework | Bounded and visible | Unbounded and invisible |

| # | Finding | Severity | Status |
|---|---|---|---|
| **C-T1** | **"Bounded and visible" for greenfield is asserted, not argued.** The stated reason is *"everything is new, so everything is suspect and gets tested."* That is a claim about developer attention, and the estate's own record contradicts it: **75 validators exist and every one of their baselines went stale** (`4-process/improvement-loops.md:210`). Newness did not produce testing before. There is no reason encoded in the architecture that it would now. | **SERIOUS** | CONFIRMED |
| **C-T2** | **The table omits the axis a release engineer would put first: risk to four live production domains.** Greenfield's real cost is not effort — it is that the cutover is a big bang across five verified custom domains, which the proposal itself flags in Part 9 (*"Big-bang risk against four live sites"*) and then does not carry into the table it uses to decide. | **SERIOUS** | CONFIRMED |
| **C-T3** | **The table omits migration/carry-over cost of non-reproducible assets.** 1.57 GB of MP3, 856 LLM parses, 911 adjudications, 22.36 MB of TF binaries in `readers-bofm` and 22.80 MB in `readers-vulgate`. Under greenfield, every one of these must be moved by hand with no generator to re-derive it. That is not "higher engineering effort," it is *irreversible manual data migration*, which is a different risk class. | **SERIOUS** | CONFIRMED |
| **C-T4** | The one axis where the table is unambiguously right is **cognitive load**, and it is right for the reason stated. Nothing in this audit disturbs it. | — | CONCUR |

**Net:** the table is directionally honest but scored on three axes when the decision turns on five. Adding *production risk* and *non-reproducible-asset migration* pushes it further toward completion than the proposal's own conclusion allows.

---

## 6. Regression control — the behavioural snapshot

### 6.1 The stated problem is CONFIRMED and worse than stated

**Receipt — baselines dead, independently recorded in two places in this repo:**

```
$ grep -rn "baseline" 4-process/improvement-loops.md 2-evidence/PROJECT-BRIEF-2026-08-08.md

improvement-loops.md:210: every reader repo's validator baseline had gone stale against its own corpus
                          (bofm 2026-05-29 vs 2026-08-06; gnt 2026-05-21 vs 2026-06-13;
                           tanakh 2026-06-02 vs 2026-06-13)

PROJECT-BRIEF-2026-08-08.md:70: Validator baselines dead as controls … Six corpus ships landed
                                post-baseline in bofm alone ⇒ the gate was bypassed repeatedly.
PROJECT-BRIEF-2026-08-08.md:71: `--baseline-check` is counts-only; offsetting errors cancel.
                                No per-violation set-diff exists.
```

**Finding B-0 (CONFIRMED, FATAL to the current gate):** the existing regression control is *counts-only*, so **two offsetting errors read as zero regression**. This is not a stale-baseline problem that a refresh fixes; the comparison operator itself is wrong. Any snapshot design that reproduces "compare counts" inherits the defect.

### 6.2 Is the behavioural snapshot golden-master done right?

The idea — *"Run the current system across every corpus and capture every decision it makes … each rule firing, each override, each merge and split, with ref, rule, and outcome"* — **is** characterization testing, correctly identified. Feathers' definition: *"instead of trying to uncover the behavior we simply assume that whatever is happening right now is exactly what should be happening and write 5-machinery/tests that assert this."* It is the standard, correct move before refactoring untested legacy code, and **the proposal deserves credit for reaching for it unprompted.**

Two things about the *design* are right and one framing is dangerous:

**Right:** capturing at *decision* granularity (ref, rule, outcome) rather than at rendered-HTML granularity. That is the difference between a reviewable snapshot and an unreviewable one, and it is exactly the fix the snapshot-testing literature prescribes: avoid snapshots *"for large, frequently changing output where the diffs become noise nobody reviews."* A 1,045-file HTML diff would be that noise; a per-decision record is not.

**Right:** recognising it is *"missing its warrants but not its verdicts"* and therefore is a regression baseline, not a correctness oracle.

**Dangerous:** the proposal calls it *"the seed of the CASES component."* Cases are defined in Part 1 as carrying *"verdict, warrant, arbiter, date"*, and Part 7 states a validator is correct *iff it agrees with the adjudicated cases*. **If snapshot rows flow into CASES, then "what the current code did" silently becomes "what is correct," and the meta-validation of Part 7 becomes a tautology.** The proposal names this circularity risk about the *arbiter* (Part 7's honest limit) and then walks into the same trap from a different door.

### 6.3 Known failure modes, and whether this design has them

| Failure mode | Present here? |
|---|---|
| **Locks in existing bugs.** Characterization 5-machinery/tests assert current behaviour including its defects. | **YES, and unavoidable.** Mitigation is labelling, not avoidance: every snapshot row must be `status: unreviewed` and must never satisfy a CASES query until a human has adjudicated it. |
| **Rubber-stamping / snapshot blindness.** *"Developers often update snapshots without looking at them."* Jest's own ESLint rule caps snapshots at 50 lines by default. | **HIGH RISK.** ~1,045 HTML outputs, 911 overrides, and an unknown number of rule firings across five corpora. One developer, no reviewer. The `--update-baseline` reflex that killed the current gates is the same reflex. [[CLAUDE.md]] already forbids `--update-baseline`; the snapshot needs the identical prohibition written into the tool, not the docs. |
| **Nondeterminism.** Snapshots flake on unpinned inputs. | **HIGH RISK, unmeasured.** Zero lockfiles exist (§7 R-2). A Stanza or Text-Fabric version bump would diff the entire snapshot with no way to distinguish "engine changed" from "dependency changed." **Pinning must precede snapshotting or the snapshot is worthless.** |
| **Temporary-measure drift.** *"A characterization test is a temporary measure … it's just there to get you out of a bind."* | **Proposal treats it as permanent** (it becomes CASES). That is a legitimate deviation *if* rows are progressively promoted from `unreviewed` to adjudicated — but the promotion mechanism is not specified. |

**Verdict on the snapshot:** correct instinct, correct granularity, and it is the highest-value item in the whole plan because it is the only step that is *equally useful whichever path is chosen* — the proposal's own argument, and it holds. **But it has three hard prerequisites the proposal does not state:** (1) pin dependencies first; (2) snapshot rows are `unreviewed` and cannot satisfy a CASES query; (3) the diff must be a **set-diff**, never a count-diff, or it reproduces B-0.

Sources: [Characterization test — Wikipedia](https://en.wikipedia.org/wiki/Characterization_test), [Characterization 5-machinery/tests or approval 5-machinery/tests? — Understand Legacy Code](https://understandlegacycode.com/blog/characterization-tests-or-approval-tests/), [Snapshot Testing — Jest](https://jestjs.io/docs/snapshot-testing), [Effective Snapshot Testing — Kent C. Dodds](https://kentcdodds.com/blog/effective-snapshot-testing), [What's wrong with snapshot 5-machinery/tests — Sapegin](https://blog.usejournal.com/whats-wrong-with-snapshot-tests-37fbe20dfe8e).

---

## 7. What a release engineer would call mandatory and the proposal never mentions

**Receipt — keyword scan of the proposal:**

```
$ for w in version rollback secret backup CI "GitHub Action" workflow reproduc lock tag release branch restore disaster; do
    grep -ic -- "$w" 4-process/master-proposal-rebuild.md; done

version 3     ← all three are prose ("plain-language version", "versioned", "an earlier version")
rollback 1    ← refers to tx_log, not deploy rollback
secret 0      backup 0      reproduc 0
"GitHub Action" 0           workflow 0        branch 0
tag 0         restore 0     disaster 0        release 1 ("coordinated releases")
```

| # | Missing concern | Evidence it matters here | Severity |
|---|---|---|---|
| **R-1** | **No CI, anywhere.** `ls <repo>/.github/workflows` → `(no .github/workflows)` for **all eight** git repos. Every build, every validator run, and every deploy happens on one Windows laptop, by hand. The proposal's entire quality argument rests on checks that nothing automatically runs. | **FATAL** |
| **R-2** | **No dependency pinning, anywhere.** Zero `requirements.txt` / `poetry.lock` / `uv.lock` / `package-lock.json` across all five readers. `atu-method/pyproject.toml` declares `dependencies = []` while the readers consume Stanza, Text-Fabric and friends. **The build is not reproducible on any machine including this one after an upgrade.** Everything downstream — snapshot, rollback, "engine builds all sites" — depends on this and it does not exist. | **FATAL** |
| **R-3** | **No release versioning and no deploy provenance.** 1 tag across 2,400+ commits. No mapping from a deployed site to the engine commit that produced it. You cannot answer "what built this page?" today and the proposal does not add the ability. | **SERIOUS** |
| **R-4** | **Rollback is undesigned.** Covered at P-5. Note the estate already recognises the metric implicitly — [[CLAUDE.md]]'s deploy rule requires fetching the live site post-push — but "verify the deploy" without "revert the deploy" is half a control. DORA's stability pair is *change failure rate* and *failed deployment recovery time*; the proposal addresses neither. | **FATAL** |
| **R-5** | **Backup / disaster recovery is unaddressed, and the substrate is not backed up by git.** `readers-bofm/private` and `readers-gnt/private` are **symlinks into Dropbox**; `readers-tanakh/private` is a real gitignored directory. `biblical-corpora` is not a git repo (I-3). **The corpus substrate the engine needs to build anything exists in exactly one place, outside version control.** A repo-only restore rebuilds nothing. | **FATAL** |
| **R-6** | **Secrets are unaddressed and at least one is live.** `readers-bofm/4-process/04-deployment-infra.md` records an open *"GitHub secrets alert: Google API key in `annotations.js`"*. Confirmed still committed and still served: `https://bomreader.com/annotations.js` returns `apiKey: 'AIzaSyDcho…'`. Firebase web keys are semi-public by design, but (a) the alert is unresolved, (b) force-push does **not** remove it from history, and (c) the proposal has no story for how a generated publish target handles configuration that varies per environment. | **SERIOUS** |
| **R-7** | **No environment/preview tier.** No staging domain, no `*.github.io` preview, no diff-against-production gate. Every change is tested in production on a live custom domain. | **SERIOUS** |
| **R-8** | **No large-asset strategy.** 1.57 GB of MP3 in plain git with no LFS, against a documented 1 GB Pages ceiling (I-1). Any consolidation or publish-target conversion must decide this and the proposal does not know it exists. | **SERIOUS** |

Receipts for R-1, R-2, R-5, R-6:

```
$ for r in atu-method readers-tanakh readers-bofm readers-gnt readers-lxx readers-vulgate rev-reader; do
    ls "$r/.github/workflows"; done
(no .github/workflows)   ← ×7, plus readers-gnt-morph

$ for r in ...; do git -C $r ls-files | grep -Ei "requirements|pyproject|poetry.lock|uv.lock|package-lock"; done
readers-tanakh (none) | readers-bofm (none) | readers-gnt (none) | readers-lxx (none) | readers-vulgate (none)

$ readlink readers-bofm/private   →  /c/Users/bibleman/Dropbox/bom-reader-private
$ readlink readers-gnt/private    →  /c/Users/bibleman/Dropbox/gnt-reader-private
$ readlink readers-tanakh/private →  (real dir)

$ curl -s -L https://bomreader.com/annotations.js | sed -n '24,26p'
    apiKey: 'AIzaSyDcho<REDACTED>',
    authDomain: 'bofm-reader.firebaseapp.com',
```

Sources: [DORA metrics history](https://dora.dev/insights/dora-metrics-history/), [Four Keys — Google Cloud](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance), [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).

---

## 8. Findings register

| ID | Finding | Sev | Status |
|---|---|---|---|
| P-1 | Force-push over `readers-bofm` destroys 856 LLM parses + 911 adjudications; not build output, not regenerable | FATAL | CONFIRMED |
| P-2 | "Force-pushed by the engine" — the agent cannot push at all (documented 403); every deploy is manual | FATAL | CONFIRMED |
| P-5 | Rollback becomes strictly worse; previous good build is deleted by the force-push itself | FATAL | CONFIRMED |
| R-1 | Zero CI across all eight repos | FATAL | CONFIRMED |
| R-2 | Zero dependency pinning; build not reproducible; snapshot & rollback both depend on it | FATAL | CONFIRMED |
| R-4 | Deploy rollback undesigned; no change-failure or recovery-time control | FATAL | CONFIRMED |
| R-5 | Substrate is gitignored and two repos symlink it into Dropbox; `biblical-corpora` is not a repo | FATAL | CONFIRMED |
| B-0 | Existing regression gate is counts-only — offsetting errors cancel | FATAL (existing) | CONFIRMED |
| I-1 | `readers-bofm` ~1.7 GB tracked vs GitHub's 1 GB Pages ceiling, no LFS | SERIOUS | CONFIRMED |
| I-2 | Proposal says "~92 HTML files"; actual is 1,045 | SERIOUS | CONFIRMED |
| I-3 | `biblical-corpora` is not a git repo | SERIOUS | CONFIRMED |
| I-6 / R-3 | 1 tag in the estate; no release versioning, no deploy→commit provenance | SERIOUS | CONFIRMED |
| P-0 | Whole source tree incl. [[CLAUDE.md]] served publicly from all five domains | SERIOUS (argues *for* proposal) | CONFIRMED |
| P-3 | Force-push doesn't shrink repos or remove history; 222 MiB pack persists | SERIOUS | CONFIRMED |
| P-4 | `git log`/`blame` over 2,200 editorial commits lost; no archival plan | SERIOUS | CONFIRMED |
| P-6 | Service-worker cache versioning (`bomreader-v325`) unaddressed | SERIOUS | CONFIRMED |
| P-7 | No `.nojekyll`; Jekyll silently 404s `_`-prefixed paths (probe-verified) | SERIOUS | CONFIRMED |
| E-1 | Estate is already a distributed monolith via `sys.path.insert` on sibling paths | SERIOUS | CONFIRMED |
| E-2 | `atu-method` at `0.1.0`, 0 tags, consumed by path not by version | SERIOUS | CONFIRMED |
| M-1 | Strangler stall risk conceded in the cost table, controlled only by an unenforced date | SERIOUS | CONFIRMED + lit. |
| M-2 | Migration order unstated; hardest repo has 1,149 commits and all the irreplaceable data | SERIOUS | CONFIRMED |
| M-3 | No interception point / parallel run / preview tier; cutover is DNS-level all-or-nothing | SERIOUS | CONFIRMED |
| C-T1 | "Bounded and visible" contradicted by the estate's own 75-stale-baseline record | SERIOUS | CONFIRMED |
| C-T2/3 | Cost table omits production risk and non-reproducible-asset migration | SERIOUS | CONFIRMED |
| R-6 | Live Firebase key committed and served; open GitHub alert; no config-per-environment story | SERIOUS | CONFIRMED |
| R-7 | No staging/preview; every change tested in production | SERIOUS | CONFIRMED |
| R-8 | No large-asset (LFS) strategy | SERIOUS | CONFIRMED |
| E-3 | `atu-method` already 90% lexicon blobs before adding APP + CASES | MINOR | CONFIRMED |
| I-4 | `rev-reader` has no remote, on `master`, laptop-only | MINOR | CONFIRMED |
| I-5 | `readers-bofm` `.git` has 2.60 GiB loose objects, never gc'd | MINOR | CONFIRMED |
| M-4 | No branching discipline; all repos dirty, all on `main` | MINOR | CONFIRMED |
| P-8 | Pages-from-branch 10-builds/hour soft limit applies to the chosen mechanism | MINOR | CONFIRMED |

---

## 9. The minimum change that makes the plan survivable

Ordered so that each step is independently valuable and none requires the architectural decision to have been made:

1. **Pin dependencies** (`requirements.txt` or `uv.lock`, per repo, from the actual working interpreters). *Blocks R-2. Everything else depends on it.* Nothing in this plan means anything until a build is reproducible twice on the same machine.
2. **Tag every repo at current HEAD** (`pre-rebuild-2026-08-09`). Costs one command per repo, and it is the difference between P-4 being "history moved" and "history gone."
3. **Get the substrate under versioned backup** — LFS, a private repo, or a documented checksummed archive. Today it is one Dropbox folder behind two symlinks (R-5).
4. **Move `readers-bofm`'s 1.57 GB of MP3 out of plain git** before any consolidation or conversion (I-1, R-8).
5. **Fix the regression comparator before building the snapshot**: set-diff, not count-diff (B-0). A snapshot that inherits the counts-only defect is a snapshot that cannot detect offsetting errors.
6. **Build the behavioural snapshot** with `status: unreviewed` on every row and a hard wall between snapshot rows and CASES (§6.3).
7. **Replace force-push-to-`main` with orphan `gh-pages` or Pages-from-Actions.** One-word change to the proposal; removes P-1, P-3, P-4 and most of P-5 at a stroke, and unblocks P-8.
8. **Convert `readers-vulgate` first** — 19 commits, 0 engine imports, 0 irreplaceable assets. If the publish-target pattern is wrong, it is wrong there for €0.
9. **Delete each converted repo's generator in the same commit as its conversion** — the only structural defence against M-1.

---

## What survives

**Survives intact:**

- **The diagnosis.** Five of ten components absent or prose-only is the right reading, and the audit strengthened it: the estate is *already* a distributed monolith held together by `sys.path.insert(0, "../atu-method")` at `readers-gnt/scripts/build_books.py:35`, and the whole source tree — build 5-machinery/scripts, corpus data, [[CLAUDE.md]] — is served publicly on all five production domains. The proposal argues for consolidation on cleanliness grounds when it could have argued on coupling and exposure grounds and won harder.
- **"Sites should stop having opinions."** Correct, and P-0 proves it.
- **The monorepo direction.** For one engine, N datasets, N domains and **one developer**, the polyrepo case in the literature is almost entirely an organisational case worth zero here, while its documented failure mode — *"separate repositories that still have to deploy together"* — is this estate, verified.
- **The behavioural snapshot as the first move.** Correct pattern, correctly identified as characterization testing, correctly captured at decision granularity rather than rendered-output granularity, and correctly argued to be path-independent. **The single highest-value item in the plan.**
- **The cost table's cognitive-load row.** Nothing here disturbs it.
- **Part 9's self-criticism.** It names the big-bang risk and the loss of independently-authored gates honestly. The failure is that neither survives into the plan or the table.

**Survives only with amendment:**

- **The publish-target pattern** — but as an **orphan `gh-pages` branch or a Pages-from-Actions artifact deploy**, never as `--force` onto the reader repos' `main`. The goal is right; the git operation is the one that turns a reversible mistake into an irreversible one.
- **The migration** — but with an order (`readers-vulgate` first, `readers-bofm` last), an interception point, and generator-deletion-on-conversion instead of a date nobody enforces.
- **The snapshot** — but only after dependency pinning, with `unreviewed` status on every row, and with a firewall preventing snapshot rows from satisfying CASES queries. Otherwise Part 7's meta-validation becomes "the validator is correct iff it agrees with what the code already did," which is the same circularity the proposal correctly identifies about the arbiter, entering through a different door.

**Does not survive:**

- **"Force-pushed by the engine's build."** The engine cannot push — `readers-bofm/4-process/04-deployment-infra.md` records the 403 — and the target repo holds 856 LLM-generated parses and 911 adjudications that are not build output and cannot be regenerated. This clause is destructive and depends on a capability that does not exist.
- **"No independent history worth defending."** 447, 1,149 and 607 commits of editorial history, and force-push would not remove it anyway — it would only make it invisible while the 222 MiB pack stays on disk.
- **"~92 HTML files."** 1,045.
- **The cost table as a decision instrument.** It scores three axes when the decision turns on five; adding production risk and non-reproducible-asset migration moves the answer further toward completion than the proposal's own conclusion allows.
- **The premise that this is primarily an architecture problem.** Zero CI, zero lockfiles, one tag, no rollback, no backup of the substrate, a live unresolved secret alert. **Every one of these is cheaper to fix than the rebuild, and every one of them is a precondition for the rebuild being safe.** Reorganising the repos before any of them is fixed changes where the untested, unpinned, unrecoverable code lives — not whether it is untested, unpinned, or unrecoverable.
