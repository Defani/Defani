"""Turn the thesis draft (pandoc Markdown in ../skripsi_raw) into a MyST book: one page per
chapter under skripsi/, numbered headings with labels, figures and tables with their own
captions, code blocks, and a landing page with the full table of contents."""
import os, re, shutil

RAW = "../skripsi_raw/skripsi.md"
OUT = "skripsi"
IMG = "assets/skripsi"

# (file, title, first line of the chapter in the raw text, chapter number for headings)
CHAPTERS = [
    ("kata-pengantar", "Persembahan dan Kata Pengantar", "**HALAMAN PERSEMBAHAN**", None),
    ("bab-1", "BAB I Pendahuluan", "# BAB I PENDAHULUAN", 1),
    ("bab-2", "BAB II Kajian Pustaka", "# BAB II KAJIAN PUSTAKA", 2),
    ("bab-3", "BAB III Metode Penelitian", "# BAB III METODE PENELITAN", 3),
    ("bab-4", "BAB IV Kondisi Umum Lokasi Penelitian", "# BAB IV KONDISI UMUM", 4),
    ("bab-5", "BAB V Hasil dan Pembahasan", "# BAB V HASIL DAN PEMBAHASAN", 5),
    ("bab-6", "BAB VI Kesimpulan dan Saran", "# BAB VI", 6),
    ("daftar-pustaka", "Daftar Pustaka", "# DAFTAR PUSTAKA", None),
    ("lampiran", "Lampiran", "# LAMPIRAN", None),
]
END = "# RIWAYAT HIDUP PENULIS"  # personal details (birth date) stay out of the web book

TITLE = "Pemodelan Simpanan Karbon Mangrove Berbasis Citra Sentinel 2A di Muara Sungai Cipunegara, Subang, Jawa Barat"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def codeblock(lines, lang=""):
    body = "\n".join(l.replace("\\'", "'").replace("\\-", "-").replace("\\*", "*").replace("\\#", "#")
                     .replace(" ", " ").rstrip() for l in lines)
    body = re.sub(r"\n{2,}", "\n", body).strip("\n")
    return f"```{lang}\n{body}\n```"


def clean(text):
    # empty pandoc headings left by page breaks, and the Word "BAB-I" style class
    text = re.sub(r"^#\s+\{#[^}]*\}\s*$", "", text, flags=re.M)
    text = re.sub(r"\s*\{#[^}]*\.BAB-I\}", "", text)
    text = text.replace("skripsi_raw/media/", f"../{IMG}/")
    text = text.replace("\\mspace{2mu}", "\\,")
    # pandoc super/subscripts (R^2^, CO~2~) -> MyST roles
    text = re.sub(r"\^([^\^\s$]{1,12})\^", r"{sup}`\1`", text)
    text = re.sub(r"(?<![~\\])~([^~\s$]{1,12})~", r"{sub}`\1`", text)

    # pandoc figures -> MyST figures that keep the thesis's own "Gambar N." caption
    def fig(m):
        src, cap = m.group(1), m.group(2).strip()
        n = re.match(r"(Gambar|Lampiran)\s+(\d+)", cap)
        return f":::{{figure}} {src}\n:width: 100%\n\n{cap}\n:::"
    text = re.sub(r"::::\s*figure\s*\n!\[[^\]]*\]\(([^)]+)\)\s*\n+:::\s*caption\s*\n(.*?)\n:::\s*\n::::", fig, text, flags=re.S)

    # pandoc table captions (": Tabel 1. ...") -> a bold caption line
    text = re.sub(r"^: (.+)$", lambda m: f"**{m.group(1).replace('..', '.').strip()}**", text, flags=re.M)

    # blank rows of the empty tally sheet
    text = re.sub(r"^(\|\s*)+\|\s*$\n", "", text, flags=re.M)
    text = re.sub(r"^\|(\s+\|)+\s*$\n", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def number_headings(text, chap, toc):
    """### -> ## n.m, #### -> ### n.m.k, each with a label the landing page links to."""
    a = b = 0
    out = []
    for line in text.split("\n"):
        m = re.match(r"^(#{3,4})\s+(.+?)\s*$", line)
        if m:
            name = m.group(2).strip()
            if len(m.group(1)) == 3:
                a, b = a + 1, 0
                num = f"{chap}.{a}" if chap else f"{a}"
                level = 2
            else:
                b += 1
                num = f"{chap}.{a}.{b}" if chap else f"{a}.{b}"
                level = 3
            label = f"s{num.replace('.', '-')}-{slug(name)}"
            toc.append((level, f"{num} {name}", label))
            out.append(f"({label})=\n{'#' * level} {num} {name}")
        else:
            out.append(line)
    return "\n".join(out)


def main():
    raw = open(RAW, encoding="utf8").read()
    raw = raw[: raw.index(END)]
    # Word's own lists of contents, figures, tables and appendices; the landing page rebuilds them with links
    raw = raw[: raw.index("# DAFTAR ISI")] + raw[raw.index("# BAB I PENDAHULUAN"):]

    # code inside the text that Word kept as plain paragraphs
    raw = re.sub(r"(#INPUT KANAL SENTINEL2A.*?)(?=\nKeterangan :)",
                 lambda m: codeblock(m.group(1).split("\n"), "python"), raw, flags=re.S)
    raw = re.sub(r"(Lampiran 4\. Output Pemodelan Scikitlearn)\n(.*?)(?=\nLampiran 5\.)",
                 lambda m: f"**{m.group(1)}**\n\n" + codeblock(m.group(2).split("\n"), "text"), raw, flags=re.S)
    raw = re.sub(r"^Akun Gcolab :.*$\n?", "", raw, flags=re.M)
    raw = re.sub(r"^(Lampiran \d\.[^\n]*)$", r"**\1**", raw, flags=re.M)

    starts = [raw.index(c[2]) for c in CHAPTERS] + [len(raw)]
    abstract = raw[raw.index("***ABSTRACT***") + len("***ABSTRACT***"): raw.index("**PEMODELAN", raw.index("***ABSTRACT***"))]

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    os.makedirs(IMG, exist_ok=True)
    for f in os.listdir("../skripsi_raw/media"):
        shutil.copy(os.path.join("../skripsi_raw/media", f), IMG)

    contents, figures, tables = [], [], []
    for i, (fn, title, _, chap) in enumerate(CHAPTERS):
        body = raw[starts[i]: starts[i + 1]]
        body = re.sub(r"\A#[^\n]*\n", "", body.lstrip()) if body.lstrip().startswith("#") else body
        body = body.replace("**HALAMAN PERSEMBAHAN**", "## Halaman Persembahan")
        body = re.sub(r"^# KATA PENGANTAR\s*$", "## Kata Pengantar", body, flags=re.M)
        body = re.sub(r"^10\.\s*$", "", body, flags=re.M)
        body = clean(body)
        toc = []
        body = number_headings(body, chap, toc)
        for cap in re.findall(r"^(Gambar \d+\..*)$", body, flags=re.M):
            figures.append((cap.strip(), fn))
        for cap in re.findall(r"^\*\*((?:Tabel \d+|Lampiran \d+)[^*]*)\*\*$", body, flags=re.M):
            (tables if cap.startswith("Tabel") else figures).append((cap.strip(), fn)) if cap.startswith("Tabel") else None
        contents.append((fn, title, toc))
        prev_next = ""
        page = (f"---\ntitle: {title}\nshort_title: {title.split(' ', 2)[0] + ' ' + title.split(' ', 2)[1] if chap else title}\n"
                f"numbering:\n  figure: false\n  table: false\n  equation: true\n---\n\n"
                f"Bagian dari skripsi *{TITLE}* · [Daftar isi](../skripsi.md)\n\n{body.strip()}\n")
        open(os.path.join(OUT, fn + ".md"), "w", encoding="utf8").write(page)

    # landing page: cover, abstract, full table of contents, list of figures and tables
    idx = ["---", "title: Skripsi", f"subtitle: {TITLE}", "short_title: Skripsi", "---", "",
           ":::{figure} " + IMG + "/image1.png", ":width: 160px", ":align: center", ":::", "",
           f"**{TITLE}**", "",
           "Defani Arman Alfitriansyah · Program Studi Kehutanan, Fakultas Kehutanan dan Lingkungan, Universitas Kuningan · 2026", "",
           "Pembimbing: Dede Kosasih, S.Hut., M.Si dan Dr. Iing Nasihin, S.Hut., M.Si", "",
           ":::{note} Draf", "Ini draf skripsi yang dibukukan di web. Isi bisa berubah sampai versi akhir disahkan.", ":::", "",
           "## Abstract", "", abstract.strip(), "", "## Daftar Isi", ""]
    for fn, title, toc in contents:
        idx.append(f"- [**{title}**](skripsi/{fn}.md)")
        for level, name, label in toc:
            idx.append(("  " if level == 2 else "    ") + f"- [{name}](#{label})")
    idx += ["", "## Daftar Gambar", ""]
    idx += [f"- [{c}](skripsi/{fn}.md)" for c, fn in figures if c.startswith("Gambar")]
    idx += ["", "## Daftar Tabel", ""]
    idx += [f"- [{c}](skripsi/{fn}.md)" for c, fn in tables]
    lamp = re.findall(r"\*\*(Lampiran \d+\.[^*]*)\*\*", raw[starts[-2]:])
    lamp += re.findall(r"^(Lampiran \d+\.[^\n]*)$", raw[starts[-2]:], flags=re.M)
    seen = []
    for l in lamp:
        l = l.replace("..", ".").strip()
        if l not in seen:
            seen.append(l)
    seen.sort(key=lambda s: int(re.search(r"\d+", s).group()))
    idx += ["", "## Daftar Lampiran", ""] + [f"- [{l}](skripsi/lampiran.md)" for l in seen]
    open("skripsi.md", "w", encoding="utf8").write(clean("\n".join(idx)).replace(f"../{IMG}", IMG) + "\n")
    print("chapters", len(contents), "figures", len(figures), "tables", len(tables), "appendices", len(seen))


main()
