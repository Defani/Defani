"""English is the default language of the site; Indonesian copies live in id/.

Run after build_catalog.py. The Indonesian pages written by hand (and the catalog
indexes) are copied to id/ with their relative paths fixed, then the English pages
are written at the root. Each page links to the same page in the other language."""
import os, re
from urllib.parse import quote

PAGES = ["index.md", "projects.md", "dashboard.md", "plugins.md", "geolibre.md", "webgis.md", "modul.md",
         "perpus.md", "panduan.md", "repositori.md", "tutorial.md", "expertise.md", "tools.md", "contact.md"]
BUY = "https://modul-gis-defani.myr.id/ebook/tpanduan-praktis-sql-duckdb-di-geolibre"
R = lambda f, t: f"/reader.html?file=/perpus/{f}&title={quote(t)}"
SAMPLE = R("sampel-sql-duckdb-geolibre.pdf", "Panduan Praktis SQL DuckDB di GeoLibre (sample)")

os.makedirs("id", exist_ok=True)


def to_id(md, page):
    # Paths relative to id/: shared folders are one level up; sibling pages stay as they are.
    md = re.sub(r"(\]\(|\{image\} |^!\[[^\]]*\]\()((?:assets|repos|panduan)/)", r"\1../\2", md, flags=re.M)
    md = re.sub(r"(\{image\} )(assets/)", r"\1../\2", md)
    switch = f"\n[English](../{page}) · **Bahasa Indonesia**\n"
    return re.sub(r"^(# .+\n)", r"\1" + switch, md, count=1, flags=re.M)


def fix_nesting(md):
    # A directive nested in a :::{tip} needs the outer fence to be longer.
    return md.replace(":::{tip} Buku baru", "::::{tip} Buku baru").replace(
        "· [Lihat detail](modul.md)\n:::\n", "· [Lihat detail](modul.md)\n::::\n")


# 1. Indonesian copies.
for page in PAGES:
    src = open(page, encoding="utf8").read()
    if "**Bahasa Indonesia**" in src or "· **English**" in src:
        continue  # already processed in an earlier run
    open(os.path.join("id", page), "w", encoding="utf8").write(to_id(fix_nesting(src), page))

# 2. English catalog indexes, from the Indonesian ones the catalog script wrote.
for page in ("repositori.md", "tutorial.md"):
    md = open(os.path.join("id", page), encoding="utf8").read()
    md = md.replace("\n[English](../" + page + ") · **Bahasa Indonesia**\n", "")
    md = md.replace("../repos/", "repos/")
    md = md.replace("# Repositori", "# Repositories").replace("# Tutorial", "# Tutorials")
    md = md.replace("Alat, plugin, dan aplikasi yang saya buat. Klik nama untuk membaca README-nya lengkap dengan gambar dan rumus.",
                    "Tools, plugins and apps I have built. Click a name to read its README with its images and formulas.")
    md = md.replace("Tutorial dan skrip analisis (Google Earth Engine, Python, R) yang tersambung ke repositori GitHub. Klik judul untuk membaca langkah-langkahnya lengkap dengan gambar dan rumus.",
                    "Tutorials and analysis scripts (Google Earth Engine, Python, R) linked to their GitHub repositories. Click a title to read the steps with their images and formulas.")
    md = md.replace("| Judul | Bahasa | Keterangan |", "| Title | Language | Description |").replace("## Lainnya", "## Other")
    md = md.replace("Tutorial R yang diterbitkan di [RPubs](https://rpubs.com/defanii):", "R tutorials published on [RPubs](https://rpubs.com/defanii):")
    md = re.sub(r"^(# .+\n)", r"\1\n**English** · [Bahasa Indonesia](id/" + page + ")\n", md, count=1, flags=re.M)
    open(page, "w", encoding="utf8").write(md)

sw = lambda page: f"\n**English** · [Bahasa Indonesia](id/{page})\n"

EN = {}
EN["index.md"] = f"""# Defani Arman Alfitriansyah
{sw("index.md")}
::::{{tip}} New book: Panduan Praktis SQL DuckDB di GeoLibre
:::{{image}} assets/cover-sql-duckdb.png
:alt: Cover of the book Panduan Praktis SQL DuckDB di GeoLibre
:width: 150px
:align: left
:::
I have just published a book! Learn spatial SQL from scratch in plain language, practising in GeoLibre, which is free and open source. 420 pages, 26 chapters, 147 SQL examples, real data from Kuningan and West Java. Ebook in PDF + EPUB, written in Indonesian.

**Rp85,000** · [Buy on Mayar]({BUY}) · [Read a sample]({SAMPLE}) · [Details](modul.md)
::::

:::{{image}} assets/profile.png
:alt: Foto Defani Arman Alfitriansyah
:width: 180px
:align: left
:::

I'm a Forestry graduate specializing in remote sensing, forest carbon modeling, ecological modeling, and cloud-based geospatial technology for environmental applications.

I'm now working in agroforestry, building GIS databases and WebGIS systems to support spatial data management, monitoring, and traceability. My work covers developing spatial datasets, processing and analyzing geospatial data, and producing maps and visualizations that support forest and environmental decision-making.

My research background centers on forest carbon assessment, biomass modeling, and Sentinel-2 spectral analysis, using [Google Earth Engine](https://earthengine.google.com) and an open-source [Python](https://www.python.org) ecosystem ([geemap](https://github.com/gee-community/geemap), [cartoee](https://geemap.org/cartoee/), [cartopy](https://github.com/SciTools/cartopy), [scikit-learn](https://github.com/scikit-learn/scikit-learn), [pandas](https://github.com/pandas-dev/pandas), [matplotlib](https://github.com/matplotlib/matplotlib), [Google Colab](https://colab.research.google.com)).

I also serve as a GIS & Spatial Modeling Laboratory Assistant, mentoring students in GIS, remote sensing, Google Earth Engine, and Python-based spatial analysis.

I build open-source geospatial tools: **RasterViz**, a QGIS plugin for Matplotlib-style raster visualization without coding, used by 1,300+ users worldwide, and the GeoLibre plugins Layout Composer, GBIF Data and iNaturalist Extractor.

As a content creator on Instagram ([@49s.lab](https://www.instagram.com/49s.lab), 6K+ followers), I share practical GIS, remote sensing, and open-source geospatial tutorials. I work with open-source software only, and I'm open to collaboration on forest carbon, sustainability, EUDR, and GIS-based traceability systems.

## Where I work

:::{{iframe}} /peta.html
:width: 100%
:::

## Live data

:::{{iframe}} /live-widgets.html
:width: 100%
:::

## Tree cover loss in Indonesia

:::{{iframe}} https://www.globalforestwatch.org/embed/widget/treeLoss/country/IDN
:width: 100%
:::

Source: [Global Forest Watch](https://www.globalforestwatch.org/dashboards/country/IDN/), data by Hansen/UMD/Google/USGS/NASA.

:::{{aside}}
![Cover of the SQL DuckDB in GeoLibre book](assets/cover-sql-duckdb.png)

**New book: Panduan Praktis SQL DuckDB di GeoLibre**

Rp85,000 · PDF + EPUB · 420 pages

[Buy on Mayar]({BUY}) · [Read a sample]({SAMPLE})
:::
"""

EN["projects.md"] = f"""# Featured projects
{sw("projects.md")}
Repositories and tools for remote sensing, GIS, and geospatial analysis.

## RasterViz (QGIS plugin)

Publication-quality raster rendering built with [PyQGIS](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/), [Matplotlib](https://github.com/matplotlib/matplotlib), and [PyQt5](https://riverbankcomputing.com/software/pyqt/).

[Python](https://www.python.org) · [QGIS](https://github.com/qgis/QGIS) · [Matplotlib](https://github.com/matplotlib/matplotlib)

## EE Spectral Exploration

A [Google Earth Engine](https://earthengine.google.com) app for multi-sensor vegetation index computation, thresholding, and area statistics.

[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · [Earth Engine API](https://github.com/google/earthengine-api)

## GEEDEF LULC Tools

Cloud-based, interactive land cover classification in the GEE Code Editor for supervised mapping.

[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · Random Forest

## MapBiomas ID Col 3.0 QML

A [QGIS](https://github.com/qgis/QGIS) style library that maps pixel values directly to the official MapBiomas guidelines.

[QGIS](https://github.com/qgis/QGIS) · QML · Cartography

## Simple Plots

A backend-free web chart builder for publication-ready figures, with PNG and SVG export.

HTML · CSS · [JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · [Plotly.js](https://github.com/plotly/plotly.js)

## EE CHIRPS RainMapper

A rainfall analysis WebGIS on the CHIRPS dataset (about 5 km), with a custom area of interest, trend charts, and GeoTIFF export.

[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) · Earth Engine Apps
"""

EN["dashboard.md"] = f"""# Dashboard
{sw("dashboard.md")}
Live statistics from GitHub and the GeoLibre plugin registry, refreshed every time the page opens.

## GeoLibre plugins

:::{{iframe}} /plugin-stats.html
:width: 100%
:::

## GitHub repositories

:::{{iframe}} /dashboard.html
:width: 100%
:::
"""

EN["plugins.md"] = f"""# Plugins
{sw("plugins.md")}
Plugins I have built for GeoLibre and QGIS.

## Usage

Counts come straight from the GeoLibre plugin registry every time this page opens.

:::{{iframe}} /plugin-stats.html
:width: 100%
:::

## GeoLibre plugins

### Layout Composer

![Layout Composer interface](assets/projects/layout-composer.png)

A cartographic layout designer for GeoLibre: print-ready maps with layers, grids, insets, legends, and export.

[Official page](https://plugins.geolibre.app/catalog/layout-composer/) · [Guide on the web](panduan/layout-composer.md) · [Full README](repos/alat/layout-composer.md) · [Repository](https://github.com/Defani/Layout-Composer) · [Read the guide]({R("panduan-layout-composer.pdf", "Panduan Lengkap Layout Composer")})

### GBIF Data

![GBIF occurrence points](assets/plugins/gbif-points.png)

![GBIF occurrence density](assets/plugins/gbif-density.png)

![GBIF record popup and citation](assets/plugins/gbif-popup-and-citation.png)

Fetches occurrence records from GBIF straight onto the GeoLibre map.

[Official page](https://plugins.geolibre.app/catalog/geolibre-gbif-data/) · [Guide on the web](panduan/gbif-data.md) · [Full README](repos/alat/gbif-data.md) · [Repository](https://github.com/Defani/GBIF-Data) · [Read the guide]({R("panduan-gbif-data.pdf", "GBIF Data: Complete Guide")})

### iNaturalist Extractor

Fetches iNaturalist observations and adds them to the map as a GeoJSON layer.

[Official page](https://plugins.geolibre.app/catalog/geolibre-inaturalist-extractor/) · [Full README](repos/alat/geolibre-inaturalist-extraction-plugins.md) · [Repository](https://github.com/Defani/Geolibre-Inaturalist-Extraction-Plugins)

## QGIS plugins

### RasterViz

Scientific, Matplotlib-style raster visualization in QGIS without coding, used by 1,300+ users.

[Official QGIS page](https://plugins.qgis.org/plugins/qrviz/) · [Full README](repos/alat/rasterviz.md) · [Repository](https://github.com/Defani/RasterViz) · [Documentation site](https://defani.github.io/RasterViz/)

### qthresh

Live, slider-driven threshold preview for raster layers in QGIS.

[Full README](repos/alat/qthresh.md) · [Repository](https://github.com/Defani/qthresh)
"""

EN["geolibre.md"] = f"""# GeoLibre
{sw("geolibre.md")}
GeoLibre is an open-source GIS that runs in the browser. You can run it right here, including installing my plugins from its marketplace.

:::{{iframe}} https://web.geolibre.app/
:width: 100%
:::

Open it full screen in a new tab: [web.geolibre.app](https://web.geolibre.app/).
"""

web_id = open(os.path.join("id", "webgis.md"), encoding="utf8").read()
gee_table = web_id[web_id.index("| Skrip |"):].replace("| Skrip | Buka di GEE | Tutorial |", "| Script | Open in GEE | Tutorial |").replace("../repos/", "repos/")
EN["webgis.md"] = f"""# Web apps
{sw("webgis.md")}
Apps and documentation I have built that run on GitHub Pages, with no server and no account.

## Ploots Click

A static chart builder for publication-ready figures, exporting print-quality PNG or SVG. Everything runs in the browser.

[Open Ploots Click](https://defani.github.io/Ploots-click/) · [Repository](https://github.com/Defani/Ploots-click)

:::{{iframe}} https://defani.github.io/Ploots-click/
:width: 100%
:::

## Winrock Sample Plot Calculator

A web version of the Winrock sample plot calculator, for the number of plots needed in a carbon inventory.

[Open the calculator](https://defani.github.io/winrock-sample-plot-calculator-web/) · [Repository](https://github.com/Defani/winrock-sample-plot-calculator-web)

:::{{iframe}} https://defani.github.io/winrock-sample-plot-calculator-web/
:width: 100%
:::

## GEEDEF Land Cover Classification Tools

The complete guide and tutorial for GEEDEF V3.1, an interactive land cover classification tool in Google Earth Engine.

[Open the guide](https://defani.github.io/GEEDEF-Land-Cover-Classification-Tools/) · [Repository](https://github.com/Defani/GEEDEF-Land-Cover-Classification-Tools)

## RasterViz

The documentation site for RasterViz, a QGIS plugin for scientific raster visualization in the style of Matplotlib.

[Open the RasterViz site](https://defani.github.io/RasterViz/) · [Repository](https://github.com/Defani/RasterViz)

## Threshold, reclassify, masking and clamping of rasters in R

A tutorial on four approaches to continuous rasters that are often confused, with the terra package.

[Open the tutorial](https://defani.github.io/raster-logic-terra-r/) · [Repository](https://github.com/Defani/raster-logic-terra-r)

## Google Earth Engine scripts

Scripts you can open and run in the Google Earth Engine Code Editor (an Earth Engine account is needed).

{gee_table}"""

EN["modul.md"] = f"""# GIS books and modules
{sw("modul.md")}
## Panduan Praktis SQL DuckDB di GeoLibre

:::{{image}} assets/cover-sql-duckdb.png
:alt: Cover of the book Panduan Praktis SQL DuckDB di GeoLibre
:width: 260px
:align: left
:::

Learn spatial SQL from scratch in plain language, practising in GeoLibre, which is free and open source. The book is written in Indonesian.

**Rp85,000** · Ebook PDF + EPUB · 420 pages

[Buy on Mayar]({BUY}) · [Read a sample]({SAMPLE})

A relaxed, Indonesian-language ebook that teaches vector data processing with DuckDB SQL inside GeoLibre: from installing GeoLibre and the SQL Workspace to case studies on clipping official land cover data, carbon stock in Mount Ciremai National Park, and biodiversity indices from GBIF and iNaturalist. All exercises use real data from Kuningan Regency and West Java, with sample data ready to download.

### What you will learn

- Downloading, installing and updating GeoLibre, and what its MIT licence means
- A tour of GeoLibre's menus, with their QGIS equivalents
- Preparing data: converting the official RBI topographic data (File Geodatabase) to GeoJSON and GeoParquet
- SQL basics: SELECT, WHERE, GROUP BY, HAVING, CASE, JOIN, CTE, window functions
- Spatial SQL: coordinate systems and UTM, area, length, distance, spatial join, buffer, clip, dissolve
- Cleaning vector data and reading online data without downloading it
- Case studies: land cover in Kuningan, carbon stock in Mount Ciremai National Park, biodiversity indices from GBIF and iNaturalist
- Turning results into print-ready maps

### Inside the book

- 420 pages, 4 parts, 26 chapters
- 155 figures and screenshots of the latest GeoLibre
- 147 SQL examples with syntax highlighting
- An appendix of 100 everyday SQL recipes and a linked DuckDB syntax dictionary
- Exercises, synthesis tasks and checkpoints in every chapter

Digital product, delivered automatically after payment. This is an independent guide, not officially affiliated with GeoLibre or DuckDB.

## Free module: cloud remote sensing

A remote sensing module you can open and download for free from Google Drive.

[Open the free module](https://drive.google.com/drive/folders/1NR23hEoSSn5nkFDDkqhZcHKpGfagF0t8)

The full library of books you can read on this site is on the [Library](perpus.md) page.
"""

perpus_id = open(os.path.join("id", "perpus.md"), encoding="utf8").read()
grids = perpus_id[perpus_id.index("## Buku dan panduan saya"):].replace("../assets/", "assets/")
grids = (grids.replace("## Buku dan panduan saya", "## My books and guides").replace("## Buku terbuka", "## Open books")
         .replace("Buku dengan lisensi terbuka yang boleh dibagikan ulang.", "Books with open licences that may be shared.")
         .replace("[Baca](", "[Read](").replace("[Unduh PDF](", "[Download PDF](").replace("[Beli di Mayar](", "[Buy on Mayar](")
         .replace("Sampel 15 halaman dari buku 420 halaman. Rp85.000 untuk versi lengkap (PDF + EPUB).", "A 15-page sample of the 420-page book. Rp85,000 for the full version (PDF + EPUB).")
         .replace("(sampel)", "(sample)").replace("Panduan plugin Layout Composer untuk GeoLibre, 119 halaman.", "Guide to the Layout Composer plugin for GeoLibre, 119 pages, in Indonesian.")
         .replace("Panduan plugin GBIF Data untuk GeoLibre, 55 halaman.", "Guide to the GBIF Data plugin for GeoLibre, 55 pages.")
         .replace("Sumber resmi", "Official source").replace("Dokumentasi resmi DuckDB, lisensi", "Official DuckDB documentation,").replace("(ed.)", "(eds.)"))
EN["perpus.md"] = f"""# Library
{sw("perpus.md")}
Books and guides you can read right here. Click **Read** to open the book viewer with pages you can turn, or **Download PDF** to keep the file.

{grids}"""

EN["panduan.md"] = f"""# Guides
{sw("panduan.md")}
Complete guides to my plugins, readable on the web. The PDF versions are in the [Library](perpus.md).

- [Layout Composer guide](panduan/layout-composer.md): designing print-ready map layouts in GeoLibre (in Indonesian).
- [GBIF Data guide](panduan/gbif-data.md): biodiversity occurrence data from GBIF on your GeoLibre map (in English).
"""

EN["expertise.md"] = f"""# Forestry and field expertise
{sw("expertise.md")}
- Biomass measurement, forest inventory, and wildlife inventory
- Vegetation analysis and forest biometrics
- Biodiversity survey in Mount Ciremai National Park (TNGC)
- Mangrove survey and identification
"""

tools_id = open(os.path.join("id", "tools.md"), encoding="utf8").read()
rows = tools_id[tools_id.index("| Bidang |"):]
rows = (rows.replace("| Bidang | Alat |", "| Area | Tools |").replace("GIS dan penginderaan jauh", "GIS and remote sensing").replace("| Lainnya |", "| Other |"))
EN["tools.md"] = f"""# Tools
{sw("tools.md")}
{rows}"""

EN["contact.md"] = f"""# Contact
{sw("contact.md")}
- Email: [defaniarman@gmail.com](mailto:defaniarman@gmail.com)
- LinkedIn: [defaniarmanalfitriansyah](https://linkedin.com/in/defaniarmanalfitriansyah)
- Instagram: [@49s.lab](https://www.instagram.com/49s.lab)

> Life without biodiversity is nothing. Preserve nature, preserve the future.
"""

for page, md in EN.items():
    open(page, "w", encoding="utf8").write(md)
print("English pages:", len(EN) + 2, "· Indonesian copies:", len(os.listdir("id")))
