"""Build the repository catalog: one MyST page per public, non-fork repo of Defani,
made from its README, plus an index page. Relative images and links are pointed at
GitHub so the pages look the way the README does on github.com."""
import base64, json, os, re, subprocess

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
    return md


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
        page += body.strip() + "\n" if body.strip() else "Repositori ini belum punya README.\n"
        sec = section_of(r)
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
