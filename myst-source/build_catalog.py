"""Build the repository catalog: one MyST page per public, non-fork repo of Defani,
made from its README, plus an index page. Relative images and links are pointed at
GitHub so the pages look the way the README does on github.com."""
import nb_tidy
import base64, json, os, re, shutil, subprocess, urllib.parse, urllib.request

OWNER = "Defani"
SKIP = {"Defani"}  # the site itself
OUT = "repos"


def gh(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf8")
    if r.returncode != 0:
        return None
    return json.loads(r.stdout)


def list_repos():
    repos, page = [], 1
    while True:
        batch = gh(f"users/{OWNER}/repos?per_page=100&page={page}&sort=updated")
        if not batch:
            break
        repos += batch
        page += 1
    return [r for r in repos if not r["fork"] and not r["private"] and r["name"] not in SKIP]


def absolutize(md, repo, branch):
    raw = f"https://raw.githubusercontent.com/{OWNER}/{repo}/{branch}/"
    blob = f"https://github.com/{OWNER}/{repo}/blob/{branch}/"

    def fix(url, is_image):
        if re.match(r"^(https?:|mailto:|#|data:|//)", url):
            return url
        url = url.lstrip("./").lstrip("/")
        return (raw if is_image else blob) + url

    # Markdown images and links
    md = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)([^)]*)\)", lambda m: f"![{m.group(1)}]({fix(m.group(2), True)}{m.group(3)})", md)
    md = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)([^)]*)\)", lambda m: f"[{m.group(1)}]({fix(m.group(2), False)}{m.group(3)})", md)
    # HTML <img src="...">
    md = re.sub(r'(<img[^>]*\ssrc=")([^"]+)(")', lambda m: m.group(1) + fix(m.group(2), True) + m.group(3), md)
    # A fixed height next to a width capped by the page squashes the image; keep only the width.
    md = re.sub(r'(<img[^>]*?)\s+height="?\d+(px)?"?', r"\1", md)
    return md


IMG_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp")
CODE_EXT = {".js": "javascript", ".r": "r", ".rmd": "r", ".py": "python"}


def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "defani-site"}), timeout=60) as r:
            return r.read()
    except Exception:
        return None


def repo_tree(repo, branch):
    tree = gh(f"repos/{OWNER}/{repo}/git/trees/{branch}?recursive=1") or {}
    return [t for t in tree.get("tree", []) if t["type"] == "blob" and not t["path"].startswith(".")]


def notebooks(repo, branch, sec, blobs):
    """Copy the repo's notebooks next to its page; MyST renders each one as a notebook page
    (code cells, saved outputs, plots) without running it. Returns the links section."""
    raw = f"https://raw.githubusercontent.com/{OWNER}/{repo}/{branch}/"
    links = []
    for t in blobs:
        if not t["path"].lower().endswith(".ipynb") or t["size"] > 15_000_000:
            continue
        data = fetch(raw + urllib.parse.quote(t["path"]))
        try:
            nb = json.loads(data)
        except Exception:
            continue
        name = os.path.basename(t["path"])
        fn = f"{slug(repo)}--{slug(os.path.splitext(name)[0])}.ipynb"
        nb.setdefault("metadata", {})["title"] = f"{repo}: {name}"
        nb["metadata"].pop("widgets", None)
        os.makedirs(os.path.join(OUT, sec, "nb"), exist_ok=True)
        json.dump(nb, open(os.path.join(OUT, sec, "nb", fn), "w", encoding="utf8"), ensure_ascii=False)
        nb_tidy.tidy(os.path.join(OUT, sec, "nb", fn), nb["metadata"]["title"])
        q = urllib.parse.quote(t["path"])
        links.append(f"- [{name}](nb/{fn}) · [GitHub](https://github.com/{OWNER}/{repo}/blob/{branch}/{q}) · "
                     f"[Colab](https://colab.research.google.com/github/{OWNER}/{repo}/blob/{branch}/{q})")
    return ("## Notebook\n\nNotebook dari repositori ini, tampil lengkap dengan sel kode dan hasilnya:\n\n"
            + "\n".join(links)) if links else ""


def files_body(repo, branch, has_pages, blobs):
    """For a repo without a README: show its scripts and images instead."""
    raw = f"https://raw.githubusercontent.com/{OWNER}/{repo}/{branch}/"
    parts = []
    for t in blobs:
        ext = os.path.splitext(t["path"])[1].lower()
        if ext in CODE_EXT and t["size"] < 80_000:
            code = fetch(raw + urllib.parse.quote(t["path"]))
            if code:
                parts.append(f"## Kode: {t['path']}\n\n````{CODE_EXT[ext]}\n{code.decode('utf8', 'replace').rstrip()}\n````")
    imgs = [t for t in blobs if t["path"].lower().endswith(IMG_EXT) and t["size"] < 10_000_000]
    if imgs:
        parts.append("## Gambar\n\n" + "\n\n".join(
            f":::{{figure}} {raw}{urllib.parse.quote(t['path'])}\n:width: 100%\n\n{t['path']}\n:::" for t in imgs))
    pages = [t["path"] for t in blobs if t["path"].lower().endswith(".html")]
    if pages:
        base = f"https://{OWNER.lower()}.github.io/{repo}/" if has_pages else f"https://github.com/{OWNER}/{repo}/blob/{branch}/"
        parts.append("## Halaman web\n\n" + "\n".join(f"- [{p}]({base}{urllib.parse.quote(p)})" for p in pages))
    return "\n\n".join(parts)


# GeoLibre plugins get GeoLibre itself embedded at the top of their page, to try them right away.
GEOLIBRE_PLUGINS = {"Layout-Composer": "Layout Composer", "GBIF-Data": "GBIF Data",
                    "Geolibre-Inaturalist-Extraction-Plugins": "iNaturalist Extractor"}


def geolibre_embed(plugin):
    return (":::{iframe} https://web.geolibre.app/\n:width: 100%\n:class: col-page\n"
            f"Coba langsung: GeoLibre ([Qiusheng Wu](https://github.com/opengeos/GeoLibre)) berjalan di halaman ini. "
            f"Buka **Plugins → Marketplace**, pasang **{plugin}**, atau [buka layar penuh](https://web.geolibre.app/).\n:::\n\n")


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


TOOL_WORDS = ("plugin", "toolbox", "tool", "rasterviz", "qthresh", "ploots", "plotstudio", "plotbench",
              "layout", "geolibre", "gbif", "inaturalist", "calculator", "skill", "diagram", "ipynbprint",
              "terrain", "simbology", "symbology", "style", "remove-black", "extractor", "viewer")


def section_of(repo):
    """Tools and plugins go under Repositori; notebooks, scripts and analyses under Tutorial."""
    text = f"{repo['name']} {repo.get('description') or ''}".lower()
    return "alat" if any(w in text for w in TOOL_WORDS) else "tutorial"


APP_ORDER = ["Google Earth Engine", "Python", "R", "QGIS", "Lainnya"]
RPUBS = [
    ("Analisis Perubahan Luasan Tutupan dan Penggunaan Lahan dengan R dan MapBiomas Indonesia", "https://rpubs.com/defanii/1421395"),
    ("Animasi Peta Tutupan Lahan IKN Menggunakan R", "https://rpubs.com/defanii/1421387"),
    ("BuiltUp Mapping Using Sentinel 2A and Terra Package", "https://rpubs.com/defanii/1350501"),
    ("Pemetaan mangrove", "https://rpubs.com/defanii/1343104"),
]


def app_of(name, desc, fn, lang):
    """The app a tutorial is written for, from its name, description and main language."""
    text = f"{name} {desc}".lower()
    if "gee" in text or "earth engine" in text or "earth-engine" in text:
        return "Google Earth Engine"
    if "qgis" in text:
        return "QGIS"
    if lang == "R" or "terra" in text or re.search(r"(^|[\s-])r($|[\s-])", name.lower()) or "menggunakan-r" in name.lower():
        return "R"
    if lang in ("Python", "Jupyter Notebook") or "python" in text or "geemap" in text:
        return "Python"
    return "Lainnya"


SECTIONS = {
    "alat": ("repositori.md", "Repositori",
             "Alat, plugin, dan aplikasi yang saya buat. Klik nama untuk membaca README-nya lengkap dengan gambar dan rumus."),
    "tutorial": ("tutorial.md", "Tutorial",
                 "Tutorial dan skrip analisis (Google Earth Engine, Python, R) yang tersambung ke repositori GitHub. Klik judul untuk membaca langkah-langkahnya lengkap dengan gambar dan rumus."),
}


def main():
    for sec in SECTIONS:
        d = os.path.join(OUT, sec)
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):
            if f.endswith(".md"):
                os.remove(os.path.join(d, f))
        shutil.rmtree(os.path.join(d, "nb"), ignore_errors=True)
    for f in os.listdir(OUT):
        if f.endswith(".md"):
            os.remove(os.path.join(OUT, f))
    repos = list_repos()
    rows = {sec: [] for sec in SECTIONS}
    for r in repos:
        name, branch = r["name"], r["default_branch"]
        desc = (r.get("description") or "").strip()
        readme = gh(f"repos/{OWNER}/{name}/readme")
        body = ""
        if readme and readme.get("content"):
            body = base64.b64decode(readme["content"]).decode("utf8", "replace")
            body = absolutize(body, name, branch)
            # drop the README's own first H1; the page gets a consistent one
            body = re.sub(r"\A\s*#\s+[^\n]*\n", "", body, count=1)
        links = f"[Repositori di GitHub]({r['html_url']})"
        if r.get("has_pages"):
            links += f" · [Halaman web](https://{OWNER.lower()}.github.io/{name}/)"
        page = f"---\ntitle: {json.dumps(name)}\n---\n\n"
        if desc:
            page += f"{desc}\n\n"
        page += f"{links}\n\n"
        if name in GEOLIBRE_PLUGINS:
            page += geolibre_embed(GEOLIBRE_PLUGINS[name])
        sec = section_of(r)
        blobs = repo_tree(name, branch)
        if not body.strip():
            body = files_body(name, branch, r.get("has_pages"), blobs)
        nbs = notebooks(name, branch, sec, blobs)
        if nbs:
            body = body.rstrip() + "\n\n" + nbs
        page += body.strip() + "\n" if body.strip() else "Repositori ini belum punya README.\n"
        fn = f"{slug(name)}.md"
        open(os.path.join(OUT, sec, fn), "w", encoding="utf8").write(page)
        rows[sec].append((name, desc, fn, r.get("language") or ""))
        print(sec, fn)

    def row(name, desc, fn, lang, sec):
        d = desc.replace("|", "\\|").replace("\n", " ")
        if len(d) > 140:
            d = d[:137].rstrip() + "…"
        return f"| [{name}]({OUT}/{sec}/{fn}) | {lang} | {d} |\n"

    head = "| Judul | Bahasa | Keterangan |\n| --- | --- | --- |\n"
    for sec, (index_file, title, intro) in SECTIONS.items():
        index = f"# {title}\n\n{intro}\n\n"
        if sec == "tutorial":
            # One group per app the tutorial is written for.
            groups = {}
            for r_ in rows[sec]:
                groups.setdefault(app_of(*r_), []).append(r_)
            for app in APP_ORDER:
                items = groups.get(app, [])
                extra = RPUBS if app == "R" else []
                if not items and not extra:
                    continue
                index += f"## {app}\n\n"
                if items:
                    index += head + "".join(row(*r_, sec) for r_ in items) + "\n"
                if extra:
                    index += "Tutorial R yang diterbitkan di [RPubs](https://rpubs.com/defanii):\n\n"
                    index += "".join(f"- [{t}]({u})\n" for t, u in extra) + "\n"
        else:
            index += head + "".join(row(*r_, sec) for r_ in rows[sec])
        open(index_file, "w", encoding="utf8").write(index)
        print(f"{title}: {len(rows[sec])}")
    if os.path.exists("katalog.md"):
        os.remove("katalog.md")


main()
