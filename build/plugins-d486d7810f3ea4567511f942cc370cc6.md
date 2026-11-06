# Plugins

**English** · [Bahasa Indonesia](id/plugins.md)

Plugins I have built for [GeoLibre](https://geolibre.app) (by Qiusheng Wu, [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre), DOI [10.5281/zenodo.20785400](https://doi.org/10.5281/zenodo.20785400)) and [QGIS](https://qgis.org) (QGIS Development Team, [qgis/QGIS](https://github.com/qgis/QGIS)). The platforms belong to their authors; the plugins are mine.

## How they work together

```{mermaid}
flowchart LR
  gbif[(GBIF API)] --> p1(GBIF Data plugin)
  inat[(iNaturalist API)] --> p2(iNaturalist Extractor)
  p1 --> map[GeoLibre map]
  p2 --> map
  map --> lc(Layout Composer)
  lc --> out[Print-ready map: PNG, PDF, GeoPDF]
```

## Usage

Counts come straight from the GeoLibre plugin registry every time this page opens.

:::{iframe} /plugin-stats.html
:width: 100%
:::

## GeoLibre plugins

Try them right here: GeoLibre runs inside this page.

:::{iframe} https://web.geolibre.app/
:width: 100%
:class: col-page
GeoLibre running in this page. Open **Plugins → Marketplace** and install Layout Composer, GBIF Data, or iNaturalist Extractor to try it here, or [open it full screen](https://web.geolibre.app/).
:::

### Layout Composer

:::{figure} assets/projects/layout-composer.png
:label: fig-lc
The Layout Composer workspace in GeoLibre.
:::

A cartographic layout designer for GeoLibre: print-ready maps with layers, grids, insets, legends, and export.

[Official page](https://plugins.geolibre.app/catalog/layout-composer/) · [Full README](repos/alat/layout-composer.md) · [Repository](https://github.com/Defani/Layout-Composer) · [Read the guide](/reader.html?file=/perpus/panduan-layout-composer.pdf&title=Panduan%20Lengkap%20Layout%20Composer)

### GBIF Data

:::{figure} assets/plugins/gbif-points.png
:label: fig-gbif-points
GBIF occurrences shown as points.
:::

:::{figure} assets/plugins/gbif-density.png
:label: fig-gbif-density
GBIF occurrences shown as a density layer.
:::

:::{figure} assets/plugins/gbif-popup-and-citation.png
:label: fig-gbif-popup
A record popup with its citation.
:::

Fetches occurrence records from GBIF straight onto the GeoLibre map.

[Official page](https://plugins.geolibre.app/catalog/geolibre-gbif-data/) · [Full README](repos/alat/gbif-data.md) · [Repository](https://github.com/Defani/GBIF-Data) · [Read the guide](/reader.html?file=/perpus/panduan-gbif-data.pdf&title=GBIF%20Data%3A%20Complete%20Guide)

### iNaturalist Extractor

Fetches iNaturalist observations and adds them to the map as a GeoJSON layer.

[Official page](https://plugins.geolibre.app/catalog/geolibre-inaturalist-extractor/) · [Full README](repos/alat/geolibre-inaturalist-extraction-plugins.md) · [Repository](https://github.com/Defani/Geolibre-Inaturalist-Extraction-Plugins)

### About GeoLibre

[GeoLibre](https://geolibre.app) is not my software. It is created and maintained by [Qiusheng Wu](https://github.com/giswqs) ([ORCID 0000-0001-5437-4073](https://orcid.org/0000-0001-5437-4073)), University of Tennessee, Knoxville, under the [opengeos](https://github.com/opengeos) organisation, and released under the [MIT License](https://github.com/opengeos/GeoLibre/blob/main/LICENSE). I contribute plugins to its ecosystem (the plugins on this page).

GeoLibre is a free, cloud-native GIS that runs in the browser, on the desktop, on mobile, and in Jupyter notebooks, with 1,000+ geoprocessing tools running on WebAssembly. It is built with [Tauri](https://github.com/tauri-apps/tauri), [React](https://github.com/facebook/react), [TypeScript](https://github.com/microsoft/TypeScript), [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js), [DuckDB-WASM](https://github.com/duckdb/duckdb-wasm), and [deck.gl](https://github.com/visgl/deck.gl).

| | |
| --- | --- |
| Author | Qiusheng Wu |
| Repository | [github.com/opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) |
| Website | [geolibre.app](https://geolibre.app) · [User guide](https://geolibre.app/user-guide/interface/) · [Tutorials](https://geolibre.app/tutorials/) |
| Plugin marketplace | [plugins.geolibre.app](https://plugins.geolibre.app) ([opengeos/geolibre-plugins](https://github.com/opengeos/geolibre-plugins)) |
| Related | [geolibre-rust](https://github.com/opengeos/geolibre-rust) (WebAssembly tools), [geolibre-r](https://github.com/opengeos/geolibre-r) (R interface), [plugin template](https://github.com/opengeos/geolibre-plugin-template) |
| License | MIT |
| DOI | [10.5281/zenodo.20785400](https://doi.org/10.5281/zenodo.20785400) |

### How to cite GeoLibre

From the project's [CITATION.cff](https://github.com/opengeos/GeoLibre/blob/main/CITATION.cff) and [citation guide](https://github.com/opengeos/GeoLibre/blob/main/docs/citation.md):

> Wu, Q. (2026). *GeoLibre: A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data* (Version 3.6.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.20785400

```bibtex
@software{wu_geolibre_2026,
  author    = {Wu, Qiusheng},
  title     = {GeoLibre},
  year      = {2026},
  version   = {3.6.1},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20785400},
  url       = {https://github.com/opengeos/GeoLibre}
}
```

## QGIS plugins

### RasterViz

Scientific, Matplotlib-style raster visualization in QGIS without coding, used by 1,300+ users.

[Official QGIS page](https://plugins.qgis.org/plugins/qrviz/) · [Full README](repos/alat/rasterviz.md) · [Repository](https://github.com/Defani/RasterViz) · [Documentation site](https://defani.github.io/RasterViz/)

### qthresh

Live, slider-driven threshold preview for raster layers in QGIS.

[Full README](repos/alat/qthresh.md) · [Repository](https://github.com/Defani/qthresh)
