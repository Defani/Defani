"""Layout Composer guide as a PDF only, and more MyST features on the site, in both languages."""
import os, re, shutil
from urllib.parse import quote

BUY = "https://modul-gis-defani.myr.id/ebook/tpanduan-praktis-sql-duckdb-di-geolibre"
R = lambda f, t: f"/reader.html?file=/perpus/{f}&title={quote(t)}"
SAMPLE_EN = R("sampel-sql-duckdb-geolibre.pdf", "Panduan Praktis SQL DuckDB di GeoLibre (sample)")
SAMPLE_ID = R("sampel-sql-duckdb-geolibre.pdf", "Panduan Praktis SQL DuckDB di GeoLibre (sampel)")
LC_READ = R("panduan-layout-composer.pdf", "Panduan Lengkap Layout Composer")
GBIF_READ = R("panduan-gbif-data.pdf", "GBIF Data: Complete Guide")


def read(p):
    return open(p, encoding="utf8").read()


def write(p, s):
    open(p, "w", encoding="utf8").write(s)


def repo(slug):
    """Catalog page of a repository, whichever section it landed in."""
    for sec in ("alat", "tutorial"):
        if os.path.exists(f"repos/{sec}/{slug}.md"):
            return f"repos/{sec}/{slug}.md"
    return None


# 1. Layout Composer guide: the PDF in the reader, no Markdown copy.
if os.path.exists("panduan/layout-composer.md"):
    os.remove("panduan/layout-composer.md")
shutil.rmtree("assets/panduan/layout-composer", ignore_errors=True)

write("panduan.md", f"""# Guides

**English** · [Bahasa Indonesia](id/panduan.md)

Complete guides to my plugins.

::::{{grid}} 1 1 2 2
:::{{card}} Layout Composer guide
:link: {LC_READ}
Designing print-ready map layouts in GeoLibre. Opens in the book reader (PDF, in Indonesian).
:::
:::{{card}} GBIF Data guide
:link: panduan/gbif-data.md
Biodiversity occurrence data from GBIF on your GeoLibre map. Read it as a web page, or [as a PDF]({GBIF_READ}).
:::
::::
""")
write("id/panduan.md", f"""# Panduan

[English](../panduan.md) · **Bahasa Indonesia**

Panduan lengkap plugin saya.

::::{{grid}} 1 1 2 2
:::{{card}} Panduan Layout Composer
:link: {LC_READ}
Merancang tata letak peta siap cetak di GeoLibre. Dibuka di pembaca buku (PDF).
:::
:::{{card}} Panduan GBIF Data
:link: ../panduan/gbif-data.md
Data kejadian keanekaragaman hayati dari GBIF di peta GeoLibre. Baca sebagai halaman web, atau [sebagai PDF]({GBIF_READ}) (English).
:::
::::
""")

# 2. Plugins: no link to the removed page, numbered figures, a data-flow diagram.
FLOW_EN = """```{mermaid}
flowchart LR
  gbif[(GBIF API)] --> p1(GBIF Data plugin)
  inat[(iNaturalist API)] --> p2(iNaturalist Extractor)
  p1 --> map[GeoLibre map]
  p2 --> map
  map --> lc(Layout Composer)
  lc --> out[Print-ready map: PNG, PDF, GeoPDF]
```
"""
FLOW_ID = FLOW_EN.replace("GeoLibre map", "Peta GeoLibre").replace("Print-ready map: PNG, PDF, GeoPDF", "Peta siap cetak: PNG, PDF, GeoPDF")


def figures(md, prefix, caps):
    for img, (label, cap) in caps.items():
        md = re.sub(r"!\[[^\]]*\]\(" + re.escape(prefix + img) + r"\)",
                    f":::{{figure}} {prefix}{img}\n:label: {label}\n{cap}\n:::", md)
    return md


for path, prefix, lang in (("plugins.md", "", "en"), ("id/plugins.md", "../", "id")):
    md = read(path)
    md = re.sub(r"\[(?:Guide on the web|Panduan di web)\]\((?:\.\./)?panduan/layout-composer\.md\) · ", "", md)
    md = md.replace(f"[Baca panduan](/reader.html?file=/perpus/panduan-layout-composer.pdf", f"[Baca panduan](/reader.html?file=/perpus/panduan-layout-composer.pdf")
    if lang == "en":
        caps = {"assets/projects/layout-composer.png": ("fig-lc", "The Layout Composer workspace in GeoLibre."),
                "assets/plugins/gbif-points.png": ("fig-gbif-points", "GBIF occurrences shown as points."),
                "assets/plugins/gbif-density.png": ("fig-gbif-density", "GBIF occurrences shown as a density layer."),
                "assets/plugins/gbif-popup-and-citation.png": ("fig-gbif-popup", "A record popup with its citation.")}
        intro, flow, head = "Plugins I have built for GeoLibre and QGIS.\n", FLOW_EN, "## How they work together\n\n"
    else:
        caps = {"assets/projects/layout-composer.png": ("fig-lc", "Ruang kerja Layout Composer di GeoLibre."),
                "assets/plugins/gbif-points.png": ("fig-gbif-points", "Kejadian GBIF sebagai titik."),
                "assets/plugins/gbif-density.png": ("fig-gbif-density", "Kejadian GBIF sebagai layer kepadatan."),
                "assets/plugins/gbif-popup-and-citation.png": ("fig-gbif-popup", "Popup rekaman beserta sitasinya.")}
        intro, flow, head = "Plugin yang saya buat untuk GeoLibre dan QGIS.\n", FLOW_ID, "## Cara kerjanya bersama\n\n"
    md = figures(md, prefix, caps)
    if "{mermaid}" not in md:
        md = md.replace(intro, intro + "\n" + head + flow, 1)
    write(path, md)

# 3. Featured projects as cards.
PROJ = [
    ("RasterViz (QGIS plugin)", "rasterviz", "https://github.com/Defani/RasterViz",
     "Publication-quality raster rendering built with PyQGIS, Matplotlib and PyQt5.",
     "Rendering raster berkualitas publikasi dengan PyQGIS, Matplotlib, dan PyQt5.",
     "[Python](https://www.python.org) · [QGIS](https://github.com/qgis/QGIS) · [Matplotlib](https://github.com/matplotlib/matplotlib) · [PyQt5](https://riverbankcomputing.com/software/pyqt/)"),
    ("EE Spectral Exploration", "ee-spectral-exploration", "https://github.com/Defani/EE-SPECTRAL-EXPLORATION",
     "A Google Earth Engine app for multi-sensor vegetation indices, thresholding and area statistics.",
     "Aplikasi Google Earth Engine untuk indeks vegetasi multi-sensor, thresholding, dan statistik luas.",
     "[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · [Earth Engine API](https://github.com/google/earthengine-api)"),
    ("GEEDEF LULC Tools", "geedef-land-cover-classification-tools", "https://github.com/Defani/GEEDEF-Land-Cover-Classification-Tools",
     "Interactive, cloud-based land cover classification in the GEE Code Editor.",
     "Klasifikasi tutupan lahan interaktif berbasis cloud di GEE Code Editor.",
     "[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · Random Forest"),
    ("MapBiomas ID Col 3.0 QML", "map-biomas-land-cover-style-qgis", "https://github.com/Defani/Map-Biomas-Land-cover-Style-QGIS",
     "A QGIS style library that maps pixel values to the official MapBiomas guidelines.",
     "Pustaka style QGIS yang memetakan nilai piksel ke pedoman resmi MapBiomas.",
     "[QGIS](https://github.com/qgis/QGIS) · QML"),
    ("Simple Plots", "ploots-click", "https://github.com/Defani/Ploots-click",
     "A backend-free web chart builder for publication-ready figures, exporting PNG and SVG.",
     "Pembuat grafik web tanpa backend untuk figur siap publikasi, ekspor PNG dan SVG.",
     "[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · [Plotly.js](https://github.com/plotly/plotly.js)"),
    ("EE CHIRPS RainMapper", "ee-chirps-rainmapper-gee-apps", "https://github.com/Defani/EE-CHIRPS-RainMapper--GEE-APPS",
     "A rainfall WebGIS on CHIRPS data with a custom area, trend charts and GeoTIFF export.",
     "WebGIS curah hujan dari data CHIRPS dengan area kustom, grafik tren, dan ekspor GeoTIFF.",
     "[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · Earth Engine Apps"),
]


def cards(lang):
    out = "::::{grid} 1 1 2 2\n"
    for title, slug, gh, en, idn, tags in PROJ:
        page = repo(slug)
        link = (("" if lang == "en" else "../") + page) if page else gh
        more = "README" if lang == "en" else "README"
        out += f":::{{card}} {title}\n{en if lang == 'en' else idn}\n\n{tags}\n\n[{more}]({link}) · [GitHub]({gh})\n:::\n"
    return out + "::::\n"


write("projects.md", "# Featured projects\n\n**English** · [Bahasa Indonesia](id/projects.md)\n\nRepositories and tools for remote sensing, GIS, and geospatial analysis.\n\n" + cards("en"))
write("id/projects.md", "# Proyek unggulan\n\n[English](../projects.md) · **Bahasa Indonesia**\n\nKumpulan repositori dan alat untuk penginderaan jauh, GIS, dan analisis geospasial.\n\n" + cards("id"))

# 4. Book page: tabs and a FAQ.
TABS_EN = """::::{tab-set}
:::{tab-item} What you will learn
- Downloading, installing and updating GeoLibre, and what its MIT licence means
- A tour of GeoLibre's menus, with their QGIS equivalents
- Preparing data: converting the official RBI topographic data to GeoJSON and GeoParquet
- SQL basics: SELECT, WHERE, GROUP BY, HAVING, CASE, JOIN, CTE, window functions
- Spatial SQL: coordinate systems and UTM, area, length, distance, spatial join, buffer, clip, dissolve
- Case studies: land cover in Kuningan, carbon stock in Mount Ciremai National Park, biodiversity from GBIF and iNaturalist
:::
:::{tab-item} Inside the book
- 420 pages, 4 parts, 26 chapters
- 155 figures and screenshots of the latest GeoLibre
- 147 SQL examples with syntax highlighting
- 100 everyday SQL recipes and a linked DuckDB syntax dictionary
- Exercises and checkpoints in every chapter
:::
:::{tab-item} Formats
- Digital PDF with a clickable table of contents
- Print-ready PDF
- EPUB for phones and e-readers
- Google Drive link to the sample data (RBI Kuningan, land cover 2024 and 2025, TNGC boundary, West Java boundaries)
:::
::::

### Questions

:::{dropdown} Do I need paid software?
No. GeoLibre and DuckDB are free and open source.
:::
:::{dropdown} I have never written code. Can I follow it?
Yes. The book starts from zero, including what a query is.
:::
:::{dropdown} Where does the data come from?
RBI from the Geospatial Information Agency (BIG), official land cover, the TNGC boundary and West Java boundaries, all prepared in a Google Drive folder.
:::
:::{dropdown} Can I read it on my phone?
The EPUB reads well on a phone. For the exercises you still need a laptop.
:::
"""
TABS_ID = """::::{tab-set}
:::{tab-item} Yang akan dipelajari
- Unduh, install, dan update GeoLibre, plus arti lisensi MIT-nya
- Tur menu GeoLibre dan padanannya di QGIS
- Persiapan data: mengubah RBI dari BIG menjadi GeoJSON dan GeoParquet
- Dasar SQL: SELECT, WHERE, GROUP BY, HAVING, CASE, JOIN, CTE, window function
- SQL spasial: sistem koordinat dan UTM, luas, panjang, jarak, spatial join, buffer, clip, dissolve
- Studi kasus: tutupan lahan Kuningan, stok karbon TNGC, keanekaragaman dari GBIF dan iNaturalist
:::
:::{tab-item} Isi buku
- 420 halaman, 4 bagian, 26 bab
- 155 gambar dan screenshot GeoLibre versi terbaru
- 147 contoh kode SQL dengan pewarnaan sintaks
- 100 resep SQL sehari-hari dan kamus sintaks DuckDB yang tertaut
- Latihan dan checkpoint di tiap bab
:::
:::{tab-item} Format
- PDF digital dengan daftar isi yang bisa diklik
- PDF siap cetak
- EPUB untuk HP atau e-reader
- Tautan Google Drive data contoh (RBI Kuningan, tuplah 2024 dan 2025, batas TNGC, batas Jawa Barat)
:::
::::

### Pertanyaan

:::{dropdown} Apa harus install software berbayar?
Tidak. GeoLibre dan DuckDB gratis dan open source.
:::
:::{dropdown} Saya belum pernah ngoding sama sekali, bisa?
Bisa. Buku ini mulai dari nol, termasuk menjelaskan apa itu query.
:::
:::{dropdown} Datanya dari mana?
RBI dari Badan Informasi Geospasial, tuplah, batas TNGC, dan batas wilayah Jawa Barat. Semua sudah disiapkan di folder Google Drive.
:::
:::{dropdown} Bisa dipakai di HP?
EPUB-nya enak dibaca di HP. Untuk praktek tetap butuh laptop.
:::
"""
for path, tabs, start, stop in (
    ("modul.md", TABS_EN, "### What you will learn", "Digital product, delivered automatically"),
    ("id/modul.md", TABS_ID, "### Yang akan dipelajari", "Yang perlu disiapkan:"),
):
    md = read(path)
    if "{tab-set}" not in md:
        i, j = md.index(start), md.index(stop)
        md = md[:i] + tabs + "\n" + md[j:]
    write(path, md)

# 5. Site-wide: header navigation, a call to action, abbreviations, keywords, repository link.
y = read("myst.yml")
if "abbreviations:" not in y:
    y = y.replace("  authors:\n", """  github: https://github.com/Defani/Defani
  keywords: [forestry, remote sensing, GIS, Google Earth Engine, GeoLibre, QGIS, forest carbon, WebGIS]
  abbreviations:
    GIS: Geographic Information System
    GEE: Google Earth Engine
    SQL: Structured Query Language
    BIG: Badan Informasi Geospasial (Indonesian Geospatial Information Agency)
    KLHK: Kementerian Lingkungan Hidup dan Kehutanan (Ministry of Environment and Forestry)
    BMKG: Badan Meteorologi, Klimatologi, dan Geofisika
    TNGC: Taman Nasional Gunung Ciremai (Mount Ciremai National Park)
    RBI: Rupabumi Indonesia (official topographic base map)
    EUDR: EU Deforestation Regulation
    GBIF: Global Biodiversity Information Facility
  authors:
""", 1)
    y = y.replace("site:\n  template: book-theme\n", f"""site:
  template: book-theme
  nav:
    - title: Plugins
      url: /plugins
    - title: Library
      url: /perpus
    - title: Tutorials
      url: /tutorial
    - title: Bahasa Indonesia
      url: /id
  actions:
    - title: Buy the book
      url: {BUY}
""", 1)
    write("myst.yml", y)
print("features applied")
