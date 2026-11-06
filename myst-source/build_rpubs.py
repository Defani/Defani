"""Bring every RPubs document of defanii into the site as a full page: the R Markdown output's
text, R code, printed results and plots (saved under assets/rpubs/), and point the tutorial
index at those pages. Run after build_catalog.py and make_bilingual.py."""
import html, os, re, shutil, urllib.request
import pypandoc

USER = "defanii"
OUT = "repos/tutorial/rpubs"
ASSETS = "assets/rpubs"


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "defani-site"}), timeout=120) as r:
        return r.read().decode("utf8", "replace")


def list_docs():
    docs, page = [], 1
    while True:
        src = get(f"https://rpubs.com/{USER}?page={page}")
        new = 0
        for t in re.findall(r'<div class="pubtile">(.*?)</time>', src, flags=re.S):
            m = re.search(rf'href="https://rpubs.com/{USER}/(\d+)">([^<]+)</a></h5>', t)
            if not m or any(d[0] == m.group(1) for d in docs):
                continue
            static = re.search(r"url=(https%3A%2F%2Frstudio-pubs-static[^&\"]+)", t)
            date = re.search(r'datetime="(\d{4}-\d{2}-\d{2})', t)
            docs.append((m.group(1), html.unescape(m.group(2)).strip(),
                         urllib.request.unquote(static.group(1)) if static else None,
                         date.group(1) if date else ""))
            new += 1
        if not new:
            return docs
        page += 1


def to_markdown(doc_html, pid):
    """The R Markdown body as MyST Markdown, with embedded plots written out as image files."""
    m = re.search(r'<div class="container-fluid main-container">(.*)</div>\s*<script', doc_html, flags=re.S)
    body = m.group(1) if m else re.search(r"<body[^>]*>(.*)</body>", doc_html, flags=re.S).group(1)
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S)
    body = re.sub(r'<div id="header">.*?</div>', "", body, count=1, flags=re.S)   # title block; the page has its own
    body = re.sub(r'<div id="TOC">.*?</div>', "", body, count=1, flags=re.S)
    # R chunks are <pre class="r"><code>; results are plain <pre><code>
    body = re.sub(r'<pre class="r"><code>', '<pre class="r"><code class="language-r">', body)
    body = re.sub(r"<pre><code>", '<pre class="text"><code class="language-text">', body)
    # MathJax spans: keep the TeX and hand it back as MyST math after conversion
    maths = []
    def keep(m):
        maths.append((m.group(1) == "display", html.unescape(m.group(2)).strip()))
        return f"MATHTOKEN{len(maths) - 1}X"
    body = re.sub(r'<span class="math (display|inline)">\\[\[(](.*?)\\[\])]</span>', keep, body, flags=re.S)
    media = os.path.join(ASSETS, pid)
    shutil.rmtree(media, ignore_errors=True)
    md = pypandoc.convert_text(body, "gfm-raw_html", format="html",
                               extra_args=["--wrap=none", f"--extract-media={media}"])
    md = re.sub(r"\]\(assets/rpubs[/\\]+" + pid + r"[/\\]+", f"](../../../{ASSETS}/{pid}/", md)

    def tex(m):
        display, src = maths[int(m.group(1))]
        return f"\n\n$$\n{src}\n$$\n\n" if display else f"${src}$"
    md = re.sub(r"MATHTOKEN(\d+)X", tex, md)
    md = re.sub(r"^``` (\w+)", r"```\1", md, flags=re.M)
    md = re.sub(r"^```numberSource\S*", "```r", md, flags=re.M)   # numbered R chunks
    md = re.sub(r"\A\s*# [^\n]*\n", "", md)   # the document title, already the page title
    # result blocks without a language become text output
    md = re.sub(r"^``` *\n(## )", r"```text\n\1", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def main():
    docs = list_docs()
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    for pid, title, static, date in docs:
        md = to_markdown(get(static), pid) if static else ""
        open(os.path.join(OUT, f"{pid}.md"), "w", encoding="utf8").write(
            f"---\ntitle: {title!r}\ndate: {date}\nauthors:\n  - Defani Arman Alfitriansyah\n---\n\n"
            f"Tutorial R, terbit pertama di [RPubs](https://rpubs.com/{USER}/{pid}) ({date}).\n\n{md}\n")
        print(pid, title, len(md))

    index(docs)


def index(docs):
    """RPubs tutorials join the R table of the tutorial index, as rows like the repositories."""
    for f, prefix, note in (("tutorial.md", "", "R Markdown tutorial, first published on RPubs"),
                            ("id/tutorial.md", "../", "Tutorial R Markdown, terbit pertama di RPubs")):
        rows = "".join(f"| [{t}]({prefix}repos/tutorial/rpubs/{p}.md) | R (RPubs) | {note} ({d[:4]}) |\n"
                       for p, t, _, d in docs)
        s = open(f, encoding="utf8").read()
        s = re.sub(r"[^\n]*\[RPubs\]\(https://rpubs.com/defanii\):\n\n(?:- \[[^\n]*\n)+\n?", "", s)
        sec = s.index("\n## R\n")
        end = s.find("\n## ", sec + 1)
        part = s[sec:end if end > 0 else len(s)]
        part = re.sub(r"^\| \[[^\n]*repos/tutorial/rpubs/[^\n]*\n", "", part, flags=re.M)
        last = max(part.rfind("|\n") + 2, 0)
        part = part[:last] + rows + part[last:]
        s = s[:sec] + part + (s[end:] if end > 0 else "")
        open(f, "w", encoding="utf8").write(s)


main()
