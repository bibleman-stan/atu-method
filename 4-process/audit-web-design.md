---
cssclasses:
  - wide
---

# Audit — web and frontend architecture

> **Plain-language version.** The master proposal says the reading UI should live inside the engine as "one app, N corpora," because what differs between the four reader sites is configuration rather than code. I measured the four front-ends (plus a fifth the proposal doesn't mention). The claim is **about 75% true and 25% false, and the 25% is where all the cost is**. Four of the five sites really are near-clones — two of them are byte-for-byte the same function set — so unifying those is close to free. BoFM is not the same application by any measure, and it is the one the design docs call the reference implementation. Meanwhile the publish-target model in Part 5 would, if executed literally, destroy 1.5 GB of paid audio that no build can regenerate, and the site already exceeds GitHub's published-size limit. Separately, I found three live defects on lxx-reader.com that the audit turned up incidentally — one of which is the single best argument the proposal has.

**Status: AUDIT. Adversarial by assignment.** Written 2026-08-09 against [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]] Parts 4–5. Every file claim below carries a pasted receipt. Best-practice claims carry URLs. Findings are labelled **CONFIRMED** (I ran the check this turn) or **PLAUSIBLE** (reasoned, not measured), with severity **FATAL / SERIOUS / MINOR**.

---

## Part 0 — What I measured, and the one number that reframes everything

Five reader repos, not four. All five serve live.

```
$ for u in vulgate-reader.com lxx-reader.com tanakh-reader.com gnt-reader.com bomreader.com; do
    curl -sS -o /dev/null -w "%{http_code}  %{size_download}B  $u\n" -L "https://$u/"; done
200  106028B  https://vulgate-reader.com/
200  106615B  https://lxx-reader.com/
200  158237B  https://tanakh-reader.com/
200  109871B  https://gnt-reader.com/
200  197523B  https://bomreader.com/
```

The headline measurement. I extracted every `function NAME(...)` from each site's inline `<script>` blocks and compared the sets:

```
function-name Jaccard, all five readers:
  tanakh   vs bofm    : shared= 27 jaccard=0.19
  tanakh   vs gnt     : shared= 75 jaccard=0.74
  tanakh   vs lxx     : shared= 74 jaccard=0.73
  tanakh   vs vulgate : shared= 74 jaccard=0.73
  bofm     vs gnt     : shared= 27 jaccard=0.22
  bofm     vs lxx     : shared= 26 jaccard=0.21
  bofm     vs vulgate : shared= 26 jaccard=0.21
  gnt      vs lxx     : shared= 76 jaccard=0.97
  gnt      vs vulgate : shared= 76 jaccard=0.97
  lxx      vs vulgate : shared= 76 jaccard=1.00

vulgate unique fns: []
```

And the raw whitespace-normalised line diff between whole `index.html` files:

```
$ diff <(sed 's/[[:space:]]*$//' readers-lxx/index.html) \
       <(sed 's/[[:space:]]*$//' readers-vulgate/index.html) | grep -c '^[<>]'
315                      # of ~3,155 lines  → ~95% identical
gnt   vs lxx    :  508   # of ~3,281 lines  → ~92% identical
gnt   vs tanakh : 2299   # of ~4,322 lines  → ~70% identical
gnt   vs bofm   : 6890   # of 3,281 + 5,121 → essentially disjoint
```

**There are not five front-ends. There are two.** Codebase **A** (gnt · lxx · vulgate · tanakh-with-Hebrew-extensions) and codebase **B** (bofm). Vulgate has *zero* functions that don't appear elsewhere — it is a verbatim clone of LXX with a different corpus bolted in.

This single fact should restructure the proposal's Part 4. Unifying codebase A is nearly free and obviously correct. Folding B into it is the entire project, and the proposal never distinguishes the two.

---

## Part 1 — Claim 1: "the UI should not be its own repo, because that adds a third cross-repo cascade"

### Finding 1.1 — CONFIRMED / **SERIOUS**. The cascade already exists, is hand-executed, and Stan's own commit messages document it.

The proposal argues a UI repo *would* create a cascade. It already has one. From `git log -- index.html`:

```
readers-gnt:
  ca87a162 Search: load prebuilt index instead of runtime DOMParser walk (fixes freeze)
  4a9fa70d search: match both Greek and English layers (bilingual search, display-mode-independent)
  dd6529b2 search: add wildcard phrase-template support (port from bofm)
  4077e25b unified header: left-align location label + SBL-style abbreviations

readers-tanakh:
  0b621db7b Search: load prebuilt index (data/search_index.json)
  d546aea98 search: match both Hebrew and English layers (bilingual search, supersedes ...)
  6158572ee search: activate corpus chips + add wildcard (family-standard parity)
  a5ceccbcc chapter-grid: route through verse popover (family-standard verse nav)

readers-bofm:
  a99887c search: add corpus filter chips (Stan Option A — 7 text-structural divisions)
  41db6a2 search: standardize NEAR default to NEAR5 (family unification)
```

The phrases **"port from bofm"**, **"family-standard parity"**, **"family unification"** are the cascade, written down, by hand, one repo at a time. The proposal is right that this is a real cost. **This finding supports the proposal.**

### Finding 1.2 — CONFIRMED / **SERIOUS**. But the cascade argument does not discriminate between "in the engine" and "its own repo."

A cascade's cost is a function of *how many artifacts must move together*, not of which directory they sit in. Whether the app is `atu-method/app/` or `atu-ui/`, a UI change still has to be built and pushed to five publish targets. Putting it in the engine does not remove a hop; it removes a *repository*, which is not the same thing.

Worse: it **couples the UI release cadence to the engine release cadence**. Today a CSS fix on gnt-reader.com touches one repo and cannot possibly affect Hebrew segmentation. Under the proposal, the CSS fix ships from the same versioned artifact as the rule engine. Every UI tweak now transits whatever gate protects the rules. Stan already flagged the cognitive-load axis in the Part 2 retraction; this makes it worse, because the fastest-moving, lowest-risk layer (presentation) is now welded to the slowest-moving, highest-risk one (segmentation).

The proposal's own Part 9 concedes *"Consolidation destroys the independently-authored gates … that is genuinely weaker."* That concession applies with full force here and is not repeated in Part 4.

### Finding 1.3 — CONFIRMED / **SERIOUS**. "Part of the engine" is greenfield: the engine has no presentation layer at all.

```
$ find atu_method -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" \
      -o -name "*.jinja*" -o -name "*.j2" -o -name "*.tmpl" \) -not -path "*__pycache__*"
(no output)

$ grep -rln "<div\|<span\|<html\|render_template\|jinja" atu_method --include=*.py
atu_method/swaps/apply_swaps.py
atu_method/swaps/__init__.py
```

`atu_method` is 21 Python modules with **zero** web assets. The only HTML anywhere in it is the `<span class="swap">` wrapper emitted by `swaps/apply_swaps.py`. So "the app belongs in the engine" does not describe a relocation — it describes **building a web layer, from scratch, inside a package that has never had one**, and then migrating ~8,400 lines of hand-written HTML/CSS/JS into it.

The proposal frames Part 4 as a placement decision. It is a construction project. That mispricing is the same error the Part 2 retraction already corrected once for the engine; it recurs here uncorrected for the app.

Note also that `apply_swaps.py` already emits presentation markup into the text pipeline. Presentation is *already* leaking into the data layer, and a unified app would need to either formalise that contract or unwind it. Neither is scoped.

**Verdict on Claim 1:** the premise (a cascade exists, and it is expensive) is **CONFIRMED and well-evidenced**. The conclusion (therefore put the UI in the engine) does not follow from it, and the engine-placement option carries an unpriced coupling cost the proposal elsewhere admits is real.

---

## Part 2 — Claim 2: "one app, N corpora — what varies is configuration, not code"

The proposal's list of what varies: *"script direction (Hebrew RTL vs Greek/Latin/English LTR), fonts, transliteration toggles, apparatus layers, audio availability."*

I tested that list item by item.

### Finding 2.1 — CONFIRMED / **The claim is TRUE for four of five sites.**

Genuinely config-shaped, exactly as the proposal says:

| Axis | Receipt | Verdict |
|---|---|---|
| Font stack | `.he { font-family: 'SBL Hebrew', 'Ezra SIL', 'Taamey Frank CLM', 'Noto Serif Hebrew', 'David Libre', 'Times New Roman', serif; }` (`readers-tanakh/index.html:354`) | **config** — a string |
| `lang` on `<html>` | `he` / `el` / `grc` / `la` / *(absent on bofm)* | **config** |
| Design tokens | tanakh 22 · bofm 19 · gnt 17 · lxx 17 distinct `--vars`; 16 shared tanakh↔gnt, 16 shared bofm↔tanakh | **config** — a shared token set already exists |
| Text-layer class | `.he` / `.gk` / `.grk` / `.line-para` | **config**, and gratuitously divergent (`.gk` vs `.grk` for the same script) |
| Corpus/book list | per-repo `BOOKS` / `BOOK_KEYS` objects | **config** |

The 16-shared-design-token result is the strongest evidence *for* the proposal in this whole audit: a shared visual language already exists de facto. Extracting it is low-risk and high-value.

### Finding 2.2 — CONFIRMED / **FATAL to "one app". Routing granularity is not configuration.**

Tanakh emits **one file per chapter**. Everyone else emits **one file per book**.

```
$ for r in readers-tanakh readers-bofm readers-gnt readers-lxx readers-vulgate; do
    echo "$r: $(find $r/books -name '*.html' | wc -l) book fragments + 1 index"; done
readers-tanakh: 929 book fragments + 1 index
readers-bofm: 16 book fragments + 1 index
readers-gnt: 27 book fragments + 1 index
readers-lxx: 39 book fragments + 1 index
readers-vulgate: 27 book fragments + 1 index
```

This is not a flag. It propagates into the URL scheme, the fetch layer, the service-worker precache manifest, the search-index shape, and the scroll-restore logic. It is directly visible in the function inventory:

```
loadBook    absent in tanakh      # tanakh has no "load a book" concept
```

`loadBook` is present in bofm, gnt, lxx, vulgate and **absent in tanakh** — because Tanakh loads chapters. Any "one app" must carry both routing strategies as first-class code paths, not as config, because they imply different caching, different prefetch, and different history handling.

And Tanakh's choice is the *correct* one — see Finding 6.1. So this is not an accident to be normalised away; it is the one site that got it right, and unification would need to propagate Tanakh's shape to the others, which is a content-pipeline change, not a UI config change.

### Finding 2.3 — CONFIRMED / **FATAL to "one app". BoFM is a different application.**

Not a differently-configured one. Receipts:

```
Shared-name functions — identical or hand-diverged?
  tanakh  vs bofm : 27 same-name fns -> identical=  2  near(>0.90)=  3  DIVERGED= 22
  bofm    vs gnt  : 27 same-name fns -> identical=  3  near(>0.90)=  1  DIVERGED= 23
  bofm    vs lxx  : 26 same-name fns -> identical=  2  near(>0.90)=  1  DIVERGED= 23
  gnt     vs lxx  : 76 same-name fns -> identical= 62  near(>0.90)=  8  DIVERGED=  6

Functions present in exactly 3 of 4 readers: 51
    missing from bofm: 49
    missing from lxx:   1   (gtag)
    missing from tanakh: 1   (loadBook)
```

Of the 51 features that reached three of four sites, **49 are the ones BoFM doesn't have**. Even where BoFM shares a *name* with another reader, the body is different 22–23 times out of 27.

The search engine is a separate implementation, not a configured one:

```
function              tanakh  bofm   gnt    lxx
performSearch         4270    --     4017   4026
runSearch             --      1939   --     --
nearMatchSets         731     --     731    731
nearMatch             --      309    --     --
nearMatchMulti        --      589    --     --
buildSearchIndex      2959    --     2269   1683
```

BoFM additionally carries capabilities nobody else has:

```
$ ls readers-bofm/*.js
annotations.js  (22,629B)   narration.js  (51,842B)

$ grep -n "firebase" readers-bofm/index.html | head -3
5116:<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js" defer></script>

$ find readers-bofm/books -name "*.html" -exec grep -o 'onclick=' {} \; | wc -l
497            # tanakh: 0   gnt: 0   lxx: 0
```

Those 497 inline `onclick="showChapter('1nephi', 2); …"` handlers in *generated output* are a hard contract between BoFM's generator and BoFM's specific JS function names. No other reader has any. A unified app cannot adopt BoFM's markup without adopting its JS API, or must rewrite BoFM's generator.

**This is the finding that most damages the proposal**, because `3-implementation/apparatus.md:29` designates BoFM as canonical:

> **readers-bofm** (reference implementation). Each English ATU line standalone. … **The reference for all sibling UX behavior.**

and again at `apparatus.md:117`:

> `readers-bofm` **is the reference implementation.** Patterns in this repository were extracted from its applier patterns and methodology canon. Sibling reader editions (readers-gnt, readers-tanakh) are **calibrated against the BoFM reference.**

The reference implementation is the one that is 79–81% *un*-shared with the family. "One app, per-corpus config" is a description of the four followers, not of the reference.

### Finding 2.4 — CONFIRMED / **MINOR**. `apparatus.md` doesn't know about two of the five sites.

`3-implementation/apparatus.md:25` — *"## What the reader sees (end-state per sibling)"* — enumerates **three** siblings (bofm, gnt, tanakh). LXX and Vulgate are absent, though both are live with CNAMEs. The proposal's Part 6 diagram likewise shows four publish targets and omits `site-vulgate`.

Relatedly, `2-evidence/deployment-status.md` — which its own first line calls *"the authoritative record of what is LIVE for each reader edition"* — is headed **"## All three readers run the mechanical-first pipeline"** and has no row for LXX or Vulgate. The proposal's evidence base for "which sites exist" is a doc that is missing 40% of them.

### Finding 2.5 — CONFIRMED / **MINOR**. The proposal's "~92 HTML files" is off by ~11×.

Part 2 row 7 states: *"❌ **Duplicated.** ~92 HTML files built by separate per-repo builders."*

```
Deployed HTML actually served:
  tanakh 929 + bofm 16 + gnt 27 + lxx 39 + vulgate 27  = 1,038 fragments + 5 index = 1,043
```

The figure is wrong in the direction that *understates* the proposal's own case, so it isn't self-serving — but a load-bearing document should not be off by an order of magnitude on a countable.

**Verdict on Claim 2:** **CONFIRMED for gnt/lxx/vulgate (trivially — they are clones), largely true for tanakh, and FALSE for bofm.** The proposal states it as a universal. Stated accurately it would read: *"four of five readers are already one app with per-corpus config; BoFM is a second app and unifying it is the actual work."*

---

## Part 3 — Claim 3: "one UI change propagates to every site with a single edit plus rebuild"

### Finding 3.1 — CONFIRMED / **FATAL. There is no build. `index.html` is not generated by anything.**

This is the finding that most changes what Part 4 has to say.

```
$ for r in readers-tanakh readers-bofm readers-gnt readers-lxx; do
    grep -rn "index\.html" $r --include=*.py --exclude-dir=.git --exclude-dir=_archive \
      | grep -i "write\|open(\|Path(\|dump\|w'"; done
readers-bofm/.venv/Lib/site-packages/networkx/readwrite/json_graph/cytoscape.py:37: ...
readers-bofm/.venv/Lib/site-packages/setuptools/tests/test_dist.py:31: ...
readers-bofm/.venv/Lib/site-packages/torch/utils/tensorboard/writer.py:1143: ...
```

Every hit is third-party code inside `.venv`. **No script in any reader repo writes `index.html`.** The generators write `books/*.html` fragments only.

So the app is five hand-maintained documents, committed directly:

```
readers-tanakh/index.html   162,559 B   css= 44,049 B  js= 97,190 B  133 css classes  99 js fns
readers-bofm/index.html     202,644 B   css= 48,712 B  js=128,199 B  191 css classes  73 js fns
readers-gnt/index.html      113,152 B   css= 29,781 B  js= 65,216 B  106 css classes  78 js fns
readers-lxx/index.html      109,770 B   css= 28,965 B  js= 62,503 B  105 css classes  76 js fns
```

The proposal's phrasing — *"one cool UI idea → one edit in the app → rebuild all corpora → every site has it"* — assumes a build step that exists and merely needs re-pointing. It does not exist. "Rebuild all corpora" today rebuilds *content fragments*; it has never rebuilt the app, because the app has never been an output.

The real sequence is: **write a templating layer → decompose ~8,400 lines of hand-diverged HTML/CSS/JS into shared + per-corpus → verify five live sites are unchanged → then** the one-edit-propagates property becomes available. The proposal prices step 4 of Part 8 as *"Unify the app"* — one clause in a five-item list.

### Finding 3.2 — CONFIRMED / **SERIOUS. The hand-cascade demonstrably drops sites — and here is the live proof.**

`gnt-reader.com` fixed a search freeze on 2026-06-13. `lxx-reader.com` never got it. The GNT code says why, in a comment:

`readers-gnt/index.html:2060-2064`
```js
  // Fast path: prebuilt index (data/search_index.json, from
  // 5-machinery/scripts/build_search_index.py). Avoids fetching + DOMParser-parsing all
  // 27 interlinear book files on the main thread, which froze the UI for
  // seconds. ...
  const resp = await fetch('data/search_index.json');
```

`readers-lxx/index.html:1932ff` still does exactly the thing GNT calls out as the freeze:
```js
async function buildSearchIndex() {
  ...
  const parser = new DOMParser();
  for (const slug of BOOK_KEYS) {
      const resp = await fetch('books/' + slug + '.html');
      html = await resp.text();
      const doc = parser.parseFromString('<div>' + html + '</div>', 'text/html');
```

Confirmed live:
```
$ curl -sSo /dev/null -w "%{http_code} %{size_download}\n" -L https://lxx-reader.com/data/search_index.json
404 9379
$ ... tanakh-reader.com/data/search_index.json   → 200  8947323
$ ... gnt-reader.com/data/search_index.json      → 200  3205256
$ ... bomreader.com/data/search_index.json       → 200  1595667
```

And LXX's payload is **3.25× worse than the one GNT called unacceptable**: GNT parses 27 files / 5.6 MB; LXX parses 39 files / **18.2 MB**, including a 1,433 KB `psalms.html`. Anyone who opens search on lxx-reader.com downloads and main-thread-parses 18.2 MB of HTML.

**This is the proposal's best single piece of evidence and it should be promoted into Part 4.** It is a user-visible defect on a live site caused precisely by hand-cascading a fix across repos and missing one. It is worth more than the 31-shared-lines figure.

### Finding 3.3 — CONFIRMED / **MINOR**. A second cascade miss, same shape.

```
Functions present in exactly 3 of 4: ... missing from lxx: 1  → gtag
$ grep -o 'https://www.googletagmanager.com/gtag/js' readers-lxx/index.html | wc -l
0        # present in tanakh, bofm, gnt
```

lxx-reader.com has no analytics. Nobody decided that.

**Verdict on Claim 3:** the *goal* is **CONFIRMED as valuable** — I found two live cascade misses on one site in one afternoon. The *mechanism* as stated ("a single edit plus rebuild") is **FALSE today and requires building the thing it presupposes**. The proposal should say "build a UI build system" rather than "unify the app."

---

## Part 4 — Claim 4: "sites become build-output-only publish targets, force-pushed by the engine's build"

Part 5 says each site becomes *"build output plus a `CNAME`, force-pushed by the engine's build. No rules, no validators, no generator, no [[CLAUDE.md]] persona, **no independent history worth defending**."*

### Finding 4.1 — CONFIRMED / **FATAL. `readers-bofm` contains 1.5 GB of paid TTS audio that no build can regenerate, and it is already over GitHub's limit.**

```
$ find readers-bofm/audio -type f -name "*.mp3" -printf "%s\n" | awk '{s+=$1} END {printf "%.1f MB in %d mp3\n", s/1048576, NR}'
1498.8 MB in 239 mp3

$ git -C readers-bofm ls-files audio | wc -l
478                                    # 239 mp3 + 239 timing manifests, all tracked

$ grep -n "audio" readers-bofm/.gitignore
8:audio/*.zip
27:.audio-cache/                        # audio/ itself is NOT ignored
```

It is live:
```
$ curl -sSo /dev/null -w "%{http_code} %{size_download} %{content_type}\n" -L \
    https://bomreader.com/audio/01-1_Nephi/1nephi-1-samuel.mp3
200 5330694 audio/mp3
```

Against GitHub's published limits ([docs.github.com/pages/…/github-pages-limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)):

> "Published GitHub Pages sites may be no larger than 1 GB."
> "GitHub Pages source repositories have a recommended limit of 1 GB."
> "GitHub Pages sites have a *soft* bandwidth limit of 100 GB per month."

**bomreader.com is at ~1.5 GB — already ~50% over the published-site limit**, before books and index. At 5.3 MB per chapter MP3, the 100 GB/month bandwidth soft limit is ~19,000 chapter plays.

Now apply the proposal's model. `narration.js:1-13` documents what this audio is:

> *"Plays pre-generated MP3 chapter audio with synchronized line highlighting. **Audio files are generated offline using ElevenLabs TTS** and stored in audio/."*

This is **not build output**. It is a purchased, externally-generated asset with hand-mapped timing manifests. The engine's build cannot reproduce it. A publish target defined as "build output plus CNAME, force-pushed" either:

1. **force-pushes without the audio** → 239 MP3s and every `<audio>` URL 404 on the live site; the assets survive only in a rewritten-away git history, and
2. or the audio must be declared an input to the build, which means the engine repo (or a release channel) now carries 1.5 GB of binaries — contradicting *"thin artifact targets"* and *"no independent history worth defending."*

The phrase **"no independent history worth defending"** is the precise error. `readers-bofm`'s history is defending 1.5 GB of assets that cost real money and cannot be regenerated from source.

**Minimum required correction to Part 5:** publish targets must distinguish *generated* output from *carried* binary assets, and the audio needs a home (GitHub Releases, R2/S3, or an LFS-backed asset repo) **before** any force-push model is adopted. Note GitHub's own limits page suggests exactly this: *"including putting a third-party content distribution network (CDN) in front of your site, making use of other GitHub features such as releases."*

### Finding 4.2 — CONFIRMED / **The CNAME constraint is real and correctly stated.**

```
$ for d in readers-*/ rev-reader/; do [ -f "$d/CNAME" ] && printf "%-22s %s\n" "$d" "$(cat $d/CNAME)"; done
readers-bofm/           bomreader.com
readers-gnt/            gnt-reader.com
readers-lxx/            lxx-reader.com
readers-tanakh/         tanakh-reader.com
readers-vulgate/        vulgate-reader.com

$ git -C readers-tanakh remote get-url origin
git@github.com:bibleman-stan/readers-tanakh.git      # five separate GitHub repos
```

Five apex domains, five repos. Per [GitHub's custom-domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), a custom domain is overridden per repository: *"You can override the default custom domain by adding a custom domain to the individual repository."* The proposal's statement that five domains need five Pages-serving repos is **CONFIRMED**. No objection.

### Finding 4.3 — PLAUSIBLE / **SERIOUS**. Force-push is the wrong verb, and the proposal's own Part 9 says why.

Part 9 concedes *"Big-bang risk against four live sites, with every validator baseline already stale."* A force-push publish model makes that worse in a specific way: it destroys the ability to `git revert` a bad deploy on the target. Today, if a build ships broken HTML to gnt-reader.com, the fix is a revert commit in a repo whose history is intact. Under force-push-from-engine, the target has no history to revert *to* — recovery requires re-running the engine at an older revision, which presumes the engine is reproducible, which is exactly what the proposal says is not yet established.

An append-only publish commit (`git commit` on a `gh-pages`-style branch, not `push --force`) gets every benefit the proposal wants — thin targets, no logic, engine-owned — at zero cost, and keeps rollback. This looks like an unforced error in the wording rather than a considered design choice.

---

## Part 5 — RTL/LTR in one codebase: the real cost

The proposal lists *"script direction (Hebrew RTL vs Greek/Latin/English LTR)"* first among things that are configuration. Here is what is actually there.

### Finding 5.1 — CONFIRMED. The current bidi implementation is *better than expected*, and mostly config-shaped.

`readers-tanakh/index.html:353-368`:
```css
  .he {
    font-family: 'SBL Hebrew', 'Ezra SIL', 'Taamey Frank CLM', 'Noto Serif Hebrew', ...;
    direction: rtl;
    unicode-bidi: isolate;
    text-align: right;
    text-indent: calc(-1 * var(--wrap-indent));
    padding-inline-start: var(--wrap-indent);
```

Three things are right here. `unicode-bidi: isolate` is the correct primitive — per [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/unicode-bidi), it makes the container treat the element *"as one or several `U+FFFC Object Replacement Character`, i.e., like an image,"* which is precisely what prevents Hebrew content from reordering neighbouring English. `padding-inline-start` is a logical property. And the verse number is a **sibling** of the RTL block, not inside it:

```html
<div class="verse" id="v-1-1"><span class="verse-num">1:1</span>
  <span class="line">
    <span class="he">...</span>
    <span class="translit">...</span>
```

That sibling placement avoids the single most common Hebrew bidi bug — the [W3C's canonical example](https://www.w3.org/International/questions/qa-html-dir) of a line *"misinterpreted as being right-to-left text, since it begins with an Arabic character,"* leaving the digits stranded at the wrong edge. Whoever wrote this understood bidi.

### Finding 5.2 — CONFIRMED / **SERIOUS**. Directionality lives in CSS, not markup — against explicit W3C guidance.

```
$ for r in readers-tanakh readers-bofm readers-gnt readers-lxx; do
    printf "%-16s lang= %s   dir= %s\n" $r \
      "$(grep -o 'lang="[^"]*"' $r/index.html | wc -l)" \
      "$(grep -o 'dir="[^"]*"' $r/index.html | wc -l)"; done
readers-tanakh   lang= 1   dir= 0
readers-bofm     lang= 0   dir= 0
readers-gnt      lang= 1   dir= 0
readers-lxx      lang= 1   dir= 0

$ # and in the GENERATED fragments — where the actual Hebrew lives:
readers-tanakh   lang= 0  dir= 0   (1chronicles-01.html)
```

**Zero `dir` attributes** in any shell, and zero in any generated fragment. The only one in the entire Tanakh app is on a table-of-contents label (`index.html:3893`, `heb.setAttribute('dir','rtl')`).

[W3C i18n, "Structural markup and right-to-left text in HTML"](https://www.w3.org/International/questions/qa-html-dir):
> "Do *not* use CSS to apply base direction in HTML pages."
> "directional information can affect the semantics of your content, and so should be part of the markup"

[MDN, `dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir):
> "As the directionality of the text is semantically related to its content and not to its presentation, it is recommended that web developers use this attribute instead of the related CSS properties when possible. That way, the text will display correctly even on a browser that doesn't support CSS or has the CSS deactivated."

Practically: the Hebrew text is delivered to the accessibility tree, to copy/paste, and to any CSS-less rendering with **no declared direction**. The visual result is correct only while the stylesheet is applied.

### Finding 5.3 — CONFIRMED / **SERIOUS**. The RTL layout for two of four Hebrew layers is a *physical* hack, not a logical one.

`readers-tanakh/index.html:368-375`:
```css
  /* Translit + Interlinear: per-word spans flowed RTL via flex row-reverse
     so word 1 lands at the right under Hebrew word 1, word 2 to its left, ... */
  .translit, .en-inter {
    flex-direction: row-reverse;
```

Only **2** CSS logical properties exist across the whole Tanakh app, and **0** in the other three:

```
feature                   tanakh   bofm     gnt      lxx
CSS logical props         2        -        -        -
```

`flex-direction: row-reverse` produces RTL visual order while the DOM stays LTR. It works, but it is the physical-flip approach that [MDN's logical-properties module](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values) exists to replace — *"enable defining properties relative to the content's writing direction, rather than a physical direction."* Under a proper `direction: rtl` container the reversal is free and applies uniformly to wrapping, alignment, scroll anchoring, and caret movement; under `row-reverse` it applies only to main-axis order, and text selection across a reversed row is visually discontiguous.

**The cost estimate for "one app, both directions":** this is the part of the proposal's config claim that is *most nearly true* — but only because the current implementation is 2 logical properties away from being direction-agnostic and 0 `dir` attributes away from being correct. The work is real (audit ~44 KB of Tanakh CSS for physical `left`/`right`/`margin-*`/`padding-*`/`text-align`, convert to `inline-start`/`inline-end`, add `dir` to markup, replace `row-reverse` with a real RTL container) but it is **bounded, mechanical, and independently valuable whether or not unification happens.** Recommend doing it regardless.

Note the properties with no logical equivalents, per MDN's own related-concepts list — `float`, `clear`, `text-align`, `caption-side`, `resize` — plus `box-shadow`/`transform`/`background-position`, which do not flip. Those need manual `:dir()` or `[dir="rtl"]` overrides in any shared stylesheet. **PLAUSIBLE**: I did not enumerate how many such declarations exist in the Tanakh CSS.

---

## Part 6 — Service workers and PWA across N domains

### Finding 6.1 — CONFIRMED / **SERIOUS**. Origin scoping means unification buys *nothing* here, and the proposal implies otherwise.

Current state — three of five sites have a service worker, and they use **incompatible strategies**:

```
$ for u in bomreader.com lxx-reader.com tanakh-reader.com gnt-reader.com; do
    curl -sSo /dev/null -w "%{http_code}  $u/sw.js\n" -L "https://$u/sw.js"; done
200  bomreader.com/sw.js
200  lxx-reader.com/sw.js
404  tanakh-reader.com/sw.js
404  gnt-reader.com/sw.js
```
(verified negative — no `serviceWorker` string anywhere in readers-tanakh or readers-gnt outside `.git`/`_archive`/`research`)

```
readers-bofm/sw.js:5      const CACHE_NAME = 'bomreader-v325';
readers-lxx/sw.js:14      const CACHE_VERSION = 'lxx-reader-v1.5-2026-05-30-hebrew-projection-full-ot-landing-fix';
readers-vulgate/sw.js:14  const CACHE_VERSION = 'vulgate-v1.5-2026-05-29c';
```

Three sites, three versioning schemes: a monotonic counter at **v325**, a hand-written descriptive slug, and a date-plus-letter. All hand-edited. And the fetch strategies differ structurally — BoFM is network-first for HTML/JS + cache-first for assets + a `CACHE_ALL_BOOKS`/`FLUSH_CACHE`/`CHECK_CACHE` message API; LXX is network-first shell + stale-while-revalidate everything, no message API.

The hard constraint, which no repo layout can change ([MDN, Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)):

> "Access to data stored in the browser such as Web Storage and IndexedDB are separated by origin. Each origin gets its own separate storage, and JavaScript in one origin cannot read from or write to the storage belonging to another origin."

And ([MDN, Storage quotas and eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria)):

> "When an origin's data is evicted by the browser, all of its data, not parts of it, is deleted at the same time."

**Five domains means five service-worker registrations, five Cache Storage buckets, five quota budgets, five independent update cycles, five eviction events.** A reader who uses three of the sites downloads the shared app shell three times. Unifying the source changes none of this. The proposal does not claim otherwise — but "one app, N corpora" invites the reader to assume a shared runtime, and there isn't one.

### Finding 6.2 — CONFIRMED / **SERIOUS**. A shared app shell makes cache invalidation *worse*, not better.

Today a Hebrew-only rule fix rebuilds Tanakh's fragments and touches nothing on bomreader.com. Under one shared app, the shell is a single artifact whose hash changes on any UI edit. If the SW cache version derives from the app build — the obvious implementation, and the only one that makes "one edit propagates" safe — then **every site's entire cache invalidates on every UI change**, including bomreader.com's 1.5 GB of audio if it shares the cache name (BoFM's `sw.js` currently puts fonts, data, images and audio in the same `CACHE_NAME`, and `activate` deletes every key that isn't the current one).

That is a 1.5 GB re-download triggered by a CSS tweak on a Greek reader. The fix is straightforward — split the cache into `shell-v<appHash>` and `assets-v<corpusHash>` — but it is a design requirement the proposal has not surfaced, and BoFM's current single-cache design would have to change.

### Finding 6.3 — CONFIRMED / **SERIOUS**. Both live service workers call `skipWaiting()`, which is the documented trap.

`readers-bofm/sw.js:26` and `readers-lxx/sw.js:20` (and `readers-vulgate/sw.js:20`) all call `self.skipWaiting()` in `install`, plus `clients.claim()` in `activate`.

[web.dev, "The service worker lifecycle"](https://web.dev/articles/service-worker-lifecycle):
> "`skipWaiting()` means that your new service worker is likely controlling pages that were loaded with an older version. This means some of your page's fetches will have been handled by your old service worker, but your new service worker will be handling subsequent fetches. **If this might break things, don't use `skipWaiting()`.**"

Today this is survivable because each site's shell is one self-contained `index.html` — there are no lazily-fetched hashed JS chunks to mismatch. **Under a unified app with any code-splitting, `skipWaiting()` becomes actively dangerous**: an old page requesting an old chunk gets a new SW serving a cache that no longer has it. If unification introduces a bundler, `skipWaiting()` must be removed at the same time. That is a coupled change the migration plan doesn't mention.

Also relevant, on why stale SWs persist ([Chrome, "Fresher service workers, by default"](https://developer.chrome.com/blog/fresher-sw)):
> "if `max-age` was greater than 86400 (24 hours), it would be treated as if it were 86400, to avoid users being stuck with a particular version forever."

And the recovery path if a bad SW ships ([Workbox, "Removing buggy service workers"](https://developer.chrome.com/docs/workbox/remove-buggy-service-workers)):
> "buggy code in a `fetch` event may cause it to not respond to requests, resulting in a blank page."
> "**Caution:** when deploying a no-op service worker, be certain that the service worker URL remains unchanged!"

A no-op kill-switch SW must be part of the unified app's release plan. Nothing in the repos suggests one exists.

---

## Part 7 — Build tooling: does sharing components force a JS toolchain?

### Finding 7.1 — The proposal's implicit premise is unevidenced, and I could not find a source supporting it.

Web research turned up **no** authoritative source stating that sharing components requires a JS build system. Astro and 11ty are authoring conveniences; neither documents a capability Python templating lacks for prerendered text. Weighing the options honestly for one developer:

| Option | What it costs | What it buys | Verdict |
|---|---|---|---|
| **Jinja2 templates in `atu_method`** | ~0 new tooling; Python already required | Shared partials, per-corpus config, one edit → rebuild | **Recommended** |
| **11ty** | Node toolchain, package.json, upgrade burden | Same, plus a template ecosystem | Unjustified — adds a runtime |
| **Astro** | Node + islands + component model | Component authoring, type-safety | Overkill; docs scope it to "content-driven websites" with client interactivity |
| **Vite** | Node + bundler config | Dev-server speed on large JS apps | Solves a problem this project does not have |

[Vite's own "Why Vite"](https://vite.dev/guide/why.html) names its problem space as *"Developers working on large projects have experienced painfully slow dev server startups"* — irrelevant to a prerendered corpus. [11ty](https://www.11ty.dev/) positions itself as *"a simpler static site generator"* that *"does not require that you use a JavaScript framework—that means zero client-side JavaScript by default,"* which is the right philosophy but arrives via a runtime the project doesn't otherwise need. [Astro's own docs](https://docs.astro.build/en/concepts/why-astro/) scope it to content sites and explicitly exclude *"logged-in admin dashboards, inboxes, social networks, todo lists"* — the readers are on the right side of that line, but Astro's value is component authoring, which Jinja provides for free here.

**The lowest-complexity path that still gets shared components is Jinja2** — already a transitive dependency in this stack, same language as the engine, no new runtime, no lockfile, no upgrade treadmill. Given Stan's stated cognitive-load constraint in the Part 2 retraction, adding a Node toolchain to a Python project maintained by one person is the wrong trade.

### Finding 7.2 — On premature unification, the honest literature cuts against the proposal's confidence.

The pro-unification sources (Vercel's multi-tenant template, monorepo.tools) are advocacy with no stated tradeoffs and assume *runtime* tenant lookup by hostname — which does not apply to prerendered static output. The applicable literature is the abstraction-cost literature:

[Sandi Metz, "The Wrong Abstraction"](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction):
> "duplication is far cheaper than the wrong abstraction"
> "When the abstraction is wrong, the fastest way forward is back."

[Kent C. Dodds, "AHA Programming"](https://kentcdodds.com/blog/aha-programming):
> "Avoid Hasty Abstractions" — "prefer duplication over the wrong abstraction"

[CSS-Tricks, "From a Single Repo, to Multi-Repos, to Monorepo, to Multi-Monorepo"](https://css-tricks.com/from-a-single-repo-to-multi-repos-to-monorepo-to-multi-monorepo/):
> "the monorepo is particularly useful when all packages are coded in the same programming language, tightly coupled, and relying on the same tooling. If instead we have multiple projects based on different programming languages … composed of unrelated parts … then I don't believe the monorepo provides much of an advantage"

That last test is the useful one, and it **passes for codebase A and fails for BoFM**. Four sites: same language, tightly coupled, same tooling → unify. BoFM: different search engine, Firebase, audio subsystem, inline-handler markup contract, 1.5 GB of assets → the shared-abstraction case is not made.

This maps onto the proposal's own Part 9 self-criticism — *"the 31-shared-lines figure I used as evidence of accidental divergence may instead be evidence that the divergence is justified."* For the **web layer specifically**, I can now answer that question with data: the divergence is **accidental for gnt/lxx/vulgate/tanakh** (95%, 92%, 70% identical — nobody chose that) and **substantive for BoFM** (essentially disjoint, with capabilities nobody else has).

---

## Part 8 — Accessibility, performance, SEO: what the proposal ignores entirely

Parts 4–5 mention none of this. For a text-heavy scripture reader it is not a footnote.

### Finding 8.1 — CONFIRMED / **SERIOUS**. WCAG 3.1.2 (Language of Parts) fails on all five sites.

```
$ for r in ...; do grep -o '<html[^>]*>' $r/index.html | head -1; done
readers-tanakh    <html lang="he">
readers-bofm      <html>                 ← no lang at all: WCAG 3.1.1 (Level A) failure
readers-gnt       <html lang="el">
readers-lxx       <html lang="grc">
readers-vulgate   <html lang="la">

$ # per-element lang in generated fragments, where the actual mixed-language text lives:
readers-tanakh   lang= 0   (1chronicles-01.html)
readers-gnt      lang= 0   (1cor.html)
readers-lxx      lang= 0   (1chronicles.html)
readers-bofm     lang= 0   (1nephi.html)
```

Every site declares exactly **one** `lang`, on `<html>`, and **zero** on the elements that need it. Tanakh declares the entire document Hebrew — but the document is majority English: English UI chrome, a transliteration layer, an interlinear gloss layer, and the full KJV English layer, all inside `lang="he"`. GNT declares `el` (modern Greek) over a document containing a complete English KJV layer; it should be `grc` in any case, which LXX gets right.

[WCAG 2.2 SC 3.1.2, Level AA](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html):
> "The human language of each passage or phrase in the content can be programmatically determined…"
> "Speech synthesizers that support multiple languages will be able to speak the text in the appropriate accent with proper pronunciation. If changes are not marked, the synthesizer will try its best to speak the words in the default language it works in."
> "It allows braille translation software to follow changes in language…"

[W3C, "Declaring language in HTML"](https://www.w3.org/International/questions/qa-html-language-declarations):
> "Always use a language attribute on the `html` tag to declare the default language of the text in the page."
> "When the page contains content in another language, add a language attribute to an element surrounding that content."

Concretely: a screen-reader user on tanakh-reader.com hears the KJV read with a Hebrew speech synthesizer. This is also the *font-selection* mechanism per [W3C](https://www.w3.org/International/questions/qa-lang-why) — *"User-agents can (and do) use language information to select language-appropriate fonts"* — so the mis-declaration has visual consequences too.

**This is cheap to fix and it is a generator change, not a UI change.** `.he` → `lang="he" dir="rtl"`, `.gk`/`.grk` → `lang="grc"`, `.en`/`.en-gloss` → `lang="en"`, `.translit` → `lang="he-Latn"`. It should happen whether or not unification proceeds, and it argues mildly *for* unification, since one generator change would fix five sites.

### Finding 8.2 — CONFIRMED / **SERIOUS**. DOM sizes are 10–31× the Lighthouse error threshold — and Tanakh is the only site that got this right.

```
Largest single fragment per reader:
tanakh   psalms-119.html        219 KB  elements~  5,668   [corpus 48.0 MB / 929 fragments]
bofm     alma.html            2,665 KB  elements~ 44,223   [corpus  8.9 MB /  16 fragments]
gnt      luke.html              841 KB  elements~ 15,343   [corpus  5.6 MB /  27 fragments]
lxx      psalms.html          1,433 KB  elements~ 27,380   [corpus 18.2 MB /  39 fragments]
```

[Lighthouse, "Avoid an excessive DOM size"](https://developer.chrome.com/docs/lighthouse/performance/dom-size):
> Warning: "the body element has more than ~800 nodes". Error: "more than ~1,400 nodes."
> "A large DOM tree often includes many nodes that aren't visible when the user first loads the page, which unnecessarily increases data costs for your users and slows down load time."
> "the browser must constantly recompute the position and styling of nodes."

BoFM's `alma.html` injects **~44,223 elements** in one shot — **31× the error threshold**. Tanakh's per-chapter split caps it at 5,668.

This inverts Finding 2.2's framing. The per-chapter/per-book difference isn't arbitrary divergence to be normalised — **Tanakh's shape is correct and the other four are wrong.** Any unification must adopt Tanakh's granularity (a content-pipeline change across four corpora), or adopt [`content-visibility: auto`](https://web.dev/articles/content-visibility), which is the cheaper fix and preserves Ctrl+F and screen-reader access (unlike `display:none`, the content *"remains in the accessibility tree and is searchable"*), provided `contain-intrinsic-size` is set to stop scrollbar collapse.

Neither option is in the proposal. Both are prerequisites for "one app" to not regress performance on whichever granularity loses.

### Finding 8.3 — CONFIRMED / **SERIOUS**. SEO: chapter-level content is unreachable by fragment-only navigation.

All five apps navigate by `#`-fragment into a single `index.html` (`parseHash` / `setHash` are in the shared function set). [Google Search Central, "Pagination, incremental page loading, and Search"](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading):

> "Give each page a unique URL. For example, include a `?page=n` query parameter, as URLs in a paginated sequence are treated as separate pages by Google."
> "**Don't use URL fragment identifiers** (the text after a `#` in a URL) for page numbers in a collection. **Google ignores fragment identifiers.**"

So Genesis 1 and Isaiah 53 are not independently indexable on any of the five sites. For scripture — where essentially all organic search traffic is chapter- or verse-shaped queries — this forfeits the entire long tail. Tanakh already emits 929 per-chapter files that *could* be real URLs; they are used only as fetch targets.

**This is the single highest-leverage item in the audit that the proposal does not mention at all**, and it is another argument for unification done right: one routing fix, five sites.

### Finding 8.4 — CONFIRMED / **MINOR**, with a correction to an assumption I nearly made.

I initially suspected the Greek readers had no Greek webfont, since neither declares a `font-family` on `.gk`/`.grk` and both load only Literata. **That inference was wrong** — I checked, and Literata's Google-served CSS includes the polytonic block:

```
$ curl -sS "https://fonts.googleapis.com/css2?family=Literata:..." | grep -E "unicode-range|/\* "
/* greek-ext */   unicode-range: U+1F00-1FFF;
/* greek */       unicode-range: U+0370-0377, U+037A-037F, U+0384-038A, ...
```

Polytonic Greek is covered. Similarly I confirmed Tanakh's Hebrew webfonts are actually served (both `Noto Serif Hebrew` and `David Libre` return `@font-face` blocks covering `U+0590-05FF`, which includes te'amim at `U+0591-05AF`). Recording both as verified negatives.

The residual **MINOR** point: Tanakh's `.he` stack prefers `'SBL Hebrew', 'Ezra SIL', 'Taamey Frank CLM'` — all **local-only**, none loaded — before the webfonts. Te'amim positioning quality therefore depends on which font wins, which depends on what the user has installed. That *is* genuinely config-shaped (a font-stack string), so it supports the proposal's claim. Worth noting only because [`font-display: swap`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) — which all four sites request — is riskier for Hebrew than Latin: the fallback system font may lack te'amim coverage, so the swap period renders *visibly wrong* text rather than merely differently-shaped text.

### Finding 8.5 — CONFIRMED / **MINOR**. No dark mode anywhere; external dependencies on three third parties.

```
feature                   tanakh   bofm     gnt      lxx
theme/dark mode           -        -        -        -
```
Zero `prefers-color-scheme` across all four. For a long-form reading application this is a conspicuous gap.

External hosts per site: `fonts.googleapis.com` (all five), `googletagmanager.com` (all but lxx), `gstatic.com/firebasejs` (bofm only). BoFM's SW caches Google Fonts cache-first, so a font change never reaches returning users. Under unification these become one decision instead of five — a genuine, if small, point for the proposal.

---

## Part 9 — Three live defects found incidentally

Not part of the assignment, but they bear on it, and they should not sit undiscovered.

### 9.1 — CONFIRMED / **SERIOUS**. lxx-reader.com is shipping raw USFM markup into the English text.

```
LXX books total: 39
CLEAN (0 leaked USFM markers): 4 -> ['daniel', 'esther', 'genesis', 'ruth']
AFFECTED: 35        total markers: 28,829
worst: psalms 2,926 · 2kings 2,394 · 1kings 2,363 · isaiah 2,333 · 1samuel 1,960

marker frequency: \add 7780 · \add* 7780 · \ft 2688 · \fqa 2569 · \f 2343 ·
                  \fr 2343 · \f* 2343 · \xt 260 · \sc 154 · \sc* 154 · \x 138 ...
```

What a reader sees, from `readers-lxx/books/1chronicles.html`:
```
'\sc Adam\sc*<span class="punct">,'
'And these \add are\add* their generations<span class="punct">:'
'And these \add are\add* their kings<span class="punct">,'
```

Confirmed live (not just local):
```
$ curl -sS -L https://lxx-reader.com/books/1chronicles.html -o /tmp/lxx1c.html
$ grep -o '\\sc\|\\nd\|\\add\|\\bk\|\\wj' /tmp/lxx1c.html | wc -l
1138
```

Cross-check — this is LXX-only: `tanakh 0 · gnt 0 · vulgate 0 · bofm 2`. The four clean LXX books are exactly Genesis and Ruth (the gold keystone) plus Daniel and Esther; the 35 affected books are the Exod–Mal Hebrew-projection expansion (`b655507 LXX expand: Exod-Mal deployed via Hebrew-projection (37 new books)`). Footnote bodies (`\f…\ft…\fqa`), translator additions (`\add…\add*`) and cross-references (`\x…\xt…\x*`) are all being rendered as literal text.

**Bearing on the proposal:** this is a *content-generator* defect, not a UI defect. Unifying the web layer would not have caught it. It is a caution against treating "one app" as though it addresses the general drift problem — the worst live defect across all five sites lives in the layer Part 4 doesn't touch.

### 9.2 — CONFIRMED / **SERIOUS**. lxx-reader.com search downloads and parses 18.2 MB on the main thread. (Finding 3.2.)

### 9.3 — CONFIRMED / **MINOR**. lxx-reader.com has no analytics. (Finding 3.3.)

---

## Part 10 — The simpler option the proposal missed

The proposal presents a binary: five diverging repos, or one app in the engine with sites as force-pushed publish targets. There is a third option that captures most of the value at a fraction of the risk, and it is available now.

**Extract a shared `app/` layer into `atu_method`; keep the reader repos as repos; render the shell at build time.**

1. **`atu_method/app/`** — Jinja2 partials: `shell.html.j2`, `topbar`, `search`, `settings`, `nav`, plus `base.css.j2` and `search.js.j2`. Sourced from the gnt/lxx intersection, which is already 92–95% identical and needs no reconciliation.
2. **`atu_method/app/corpora/<slug>.toml`** — the genuinely config-shaped axes measured in Finding 2.1: `lang`, `dir`, text-layer class, font stack, layer list, feature flags (`audio`, `swaps`, `translit`, `interlinear`), book list, routing granularity.
3. **Each reader repo gains a 20-line `5-machinery/scripts/build_shell.py`** that renders `index.html` from the shared templates plus its own config. `index.html` becomes generated output for the first time — which is the actual precondition for the proposal's "one edit plus rebuild."
4. **Reader repos stay repos.** CNAME unchanged, Pages unchanged, history unchanged, BoFM's 1.5 GB of audio unchanged and un-force-pushed. Independent pre-commit gates — which Part 9 correctly calls *"the strongest argument against the whole proposal"* — survive intact.
5. **BoFM adopts the shared shell last, or never.** It gets the shared partials it can use and keeps `narration.js`, `annotations.js`, Firebase, and its own search until there is a reason to converge.

What this buys against the proposal's version:

| | Proposal (app in engine, force-pushed targets) | Shared template layer |
|---|---|---|
| One edit → all sites | ✅ | ✅ |
| Requires a build system that doesn't exist | ✅ must build it | ✅ same work, but it's the *only* work |
| BoFM's 1.5 GB audio | ⚠️ unresolved / destroyed | ✅ untouched |
| Independent per-repo gates | ❌ destroyed (Part 9 concedes) | ✅ retained |
| Rollback of a bad deploy | ❌ force-push destroys history | ✅ normal revert |
| Migration is incremental | ⚠️ "one at a time" but targets are rewritten | ✅ per-repo, reversible per-repo |
| Cognitive load (Part 2's third axis) | ❌ two live models during migration | ✅ one model; repos keep their shape |
| Blocked on Gate 0 (the arbiter question) | ✅ yes — Part 8 says nothing is built first | ❌ **independent of Gate 0** |

That last row matters most. Part 8 says *"Gate 0 — the arbiter question. Nothing is built before this is answered,"* and Part 9 concedes *"Gate 0 may fail, in which case Parts 3–8 are wasted motion."* **The web-layer work is not downstream of the arbiter question.** Whether or not an external segmentation witness exists, five live sites still need one search fix to reach all five, `lang`/`dir` on their text spans, real chapter URLs, and a bounded DOM. Sequencing the UI work behind Gate 0 delays fixes that are correct under every outcome.

**Recommended immediate actions, independent of the whole rebuild decision:**
- Fix the LXX USFM leak (28,829 markers, 35 books, live).
- Ship `data/search_index.json` to LXX (`build_search_index.py` already exists in two repos).
- Add `lang`/`dir` to text spans in all five generators; fix `<html lang>` on bofm and gnt.
- Give chapters real URLs.
- Add `content-visibility: auto` + `contain-intrinsic-size` to `.chapter`.
- Move BoFM's audio off the Pages repo before it is 50% over a hard-ish limit *and* the subject of a force-push proposal.

---

## What survives

**Survives intact:**

- **The cascade is real and expensive.** Not as an argument from principle but as measured fact: Stan's own commit messages say *"port from bofm"*, *"family-standard parity"*, *"family unification"*, and I found two live features (prebuilt search index, analytics) that reached three sites and missed the fourth. The proposal is right that this cannot continue.
- **"Configuration, not code" is correct for four of five sites** — and much more strongly than the proposal claims. Vulgate has zero unique functions; lxx↔vulgate differ by 315 lines; gnt↔lxx by 508. A shared design-token set already exists (16 vars shared across all readers). Unifying codebase A is low-risk and should happen.
- **The CNAME constraint is stated correctly.** Five apex domains, five Pages repos, verified.
- **Part 9's self-criticism was right, and applies harder than written.** *"Consolidation destroys the independently-authored gates … genuinely weaker"* and *"the divergence may be justified"* are both load-bearing for the web layer specifically. The answer is now measurable: divergence is accidental for four sites, substantive for BoFM.

**Does not survive as written:**

- **FATAL — "one edit plus rebuild"** presumes a build that does not exist. No script in any repo writes `index.html`; the app is five hand-maintained documents totalling ~8,400 lines. Part 4 describes a placement decision; it is a construction project, and Part 8 prices it as one clause.
- **FATAL — "sites are build-output-only, force-pushed, no history worth defending."** `readers-bofm` carries 1,498.8 MB of ElevenLabs-generated MP3 across 478 tracked files, live and already ~50% over GitHub's 1 GB published-site limit. It is not build output and no build regenerates it. Force-push either 404s the audio or contradicts "thin targets."
- **FATAL — "one app, N corpora" as a universal.** BoFM shares 0.19–0.22 of its function set with the family, 49 of 51 three-of-four features are the ones it lacks, it has a separate search engine, Firebase, a 1.5 GB audio subsystem, and 497 inline `onclick` handlers in generated markup binding its generator to its JS API. It is also, per `apparatus.md:29`, *"the reference for all sibling UX behavior."*
- **SERIOUS — routing granularity is not config**, and Tanakh — the outlier — is the one that's right. BoFM injects ~44,223 elements in a single fragment, 31× the Lighthouse error threshold.
- **SERIOUS — unification does not help caching and can hurt it.** Origin scoping is a browser invariant: five domains means five SW registrations and five cache buckets regardless of repo layout. A shared shell hash risks invalidating every site's cache on any UI edit, including BoFM's single-cache 1.5 GB. Both live SWs call `skipWaiting()`, which becomes dangerous the moment code-splitting appears.
- **SERIOUS — the proposal is silent on accessibility, performance, and SEO**, where the defects are systemic and cheap to fix: WCAG 3.1.2 fails on all five (zero per-element `lang`), BoFM has no `<html lang>` at all (3.1.1, Level A), directionality lives only in CSS against explicit W3C guidance, and fragment-only chapter navigation makes every chapter unindexable by Google.
- **MINOR — the evidence base is stale.** "~92 HTML files" is actually 1,043. [[3-implementation/apparatus.md|apparatus.md]] and [[2-evidence/deployment-status.md|deployment-status.md]] both describe "three readers" when five are live. Part 6's diagram omits `site-vulgate`.

**The one-sentence version.** The proposal correctly diagnoses a real and costly cascade, and correctly identifies that four of the five front-ends are the same application wearing different configs — but it mistakes a construction project for a placement decision, generalises from four followers to a reference implementation that shares almost nothing with them, and proposes a publish model that would delete 1.5 GB of unregenerable assets; a shared Jinja template layer inside `atu_method`, consumed by reader repos that keep their repos, their history, and their gates, delivers the same one-edit-propagates property with none of those three failures and — unlike the proposal — is not blocked on Gate 0.
