"""Move the Medium articles (RSS export in ../medium.xml) into blog/ as MyST pages, plus a blog index."""
import email.utils, os, re, shutil
import xml.etree.ElementTree as ET
import pypandoc

NS = {"content": "http://purl.org/rss/1.0/modules/content/", "dc": "http://purl.org/dc/elements/1.1/"}
OUT = "blog"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:70]


def main():
    root = ET.parse("../medium.xml").getroot()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    rows = []
    for item in root.iter("item"):
        title = item.find("title").text.strip().lstrip("️").strip()
        title = re.sub(r"^[^\w]+", "", title)
        link = item.find("link").text.split("?")[0]
        date = email.utils.parsedate_to_datetime(item.find("pubDate").text).date()
        tags = [c.text for c in item.findall("category")]
        html = item.find("content:encoded", NS).text or ""
        # Medium's tracking pixel at the end of every post
        html = re.sub(r'<img[^>]*medium\.com/_/stat[^>]*>', "", html)
        md = pypandoc.convert_text(html, "gfm-raw_html", format="html", extra_args=["--wrap=none"])
        md = re.sub(r"\A\s*#+\s+[^\n]*\n", "", md, count=1)  # the post repeats its title
        md = re.sub(r"^#\s", "## ", md, flags=re.M)
        md = re.sub(r"\n{3,}", "\n\n", md)
        fn = f"{date.isoformat()}-{slug(title)}.md"
        fm = (f"---\ntitle: {title!r}\ndate: {date.isoformat()}\n"
              + (f"tags: [{', '.join(repr(t) for t in tags)}]\n" if tags else "")
              + "---\n\n")
        head = f"{date:%d %B %Y} · Terbit pertama di [Medium]({link}) · [Semua tulisan](../blog.md)\n\n"
        open(os.path.join(OUT, fn), "w", encoding="utf8").write(fm + head + md.strip() + "\n")
        img = re.search(r"!\[[^\]]*\]\((https://[^)\s]+)", md)
        text = re.sub(r"[#*_`>\[\]!]|\(http[^)]*\)", "", md)
        paras = [re.sub(r"\s+", " ", p).strip() for p in text.split("\n\n")]
        summary = next((p.replace("Defani Arman Alfitriansyah", "", 1).strip() for p in paras if len(p) > 120 and not p.startswith("Oleh")), "")[:220].rstrip()
        rows.append((date, title, fn, img.group(1) if img else None, summary, tags))
        print(fn)
    rows.sort(reverse=True)

    idx = ["---", "title: Blog", "subtitle: Tulisan tentang penginderaan jauh, GIS, dan kehutanan", "---", "",
           "Tulisan yang dulu saya terbitkan di [Medium](https://medium.com/@defaniarman), sekarang dipindah ke sini lengkap dengan gambar dan kodenya.", "",
           "::::{grid} 1 1 2 2"]
    for date, title, fn, img, summary, tags in rows:
        idx += [f":::{{card}}", f":link: blog/{fn}"]
        if img:
            idx += ["", f"![]({img})"]
        idx += ["", f"**{title}**", "", f"{date:%d %b %Y}" + (" · " + ", ".join(tags[:3]) if tags else ""), "",
                (summary + "…") if summary else "", ":::"]
    idx.append("::::")
    open("blog.md", "w", encoding="utf8").write("\n".join(idx) + "\n")


main()
