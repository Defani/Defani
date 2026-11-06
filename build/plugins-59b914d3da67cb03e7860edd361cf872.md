# Plugin

[English](../plugins.md) · **Bahasa Indonesia**

Plugin yang saya buat untuk [GeoLibre](https://geolibre.app) (buatan Qiusheng Wu, [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre), DOI [10.5281/zenodo.20785400](https://doi.org/10.5281/zenodo.20785400)) dan [QGIS](https://qgis.org) (QGIS Development Team, [qgis/QGIS](https://github.com/qgis/QGIS)). Platformnya milik pembuatnya; pluginnya buatan saya.

## Cara kerjanya bersama

```{mermaid}
flowchart LR
  gbif[(GBIF API)] --> p1(GBIF Data plugin)
  inat[(iNaturalist API)] --> p2(iNaturalist Extractor)
  p1 --> map[Peta GeoLibre]
  p2 --> map
  map --> lc(Layout Composer)
  lc --> out[Peta siap cetak: PNG, PDF, GeoPDF]
```

## Statistik pengguna

Data diambil langsung dari registri plugin GeoLibre setiap kali halaman ini dibuka.

:::{iframe} /plugin-stats.html
:width: 100%
:::

## Plugin GeoLibre

Coba langsung di sini: GeoLibre berjalan di dalam halaman ini.

:::{iframe} https://web.geolibre.app/
:width: 100%
:class: col-page
GeoLibre berjalan langsung di halaman ini. Buka **Plugins → Marketplace** lalu pasang Layout Composer, GBIF Data, atau iNaturalist Extractor untuk mencobanya di sini, atau [buka layar penuh](https://web.geolibre.app/).
:::

### Layout Composer

:::{figure} ../assets/projects/layout-composer.png
:label: fig-lc
Ruang kerja Layout Composer di GeoLibre.
:::

Perancang tata letak kartografi untuk GeoLibre: peta siap cetak dengan layer, grid, inset, legenda, dan ekspor.

[Halaman resmi](https://plugins.geolibre.app/catalog/layout-composer/) · [README lengkap](../repos/alat/layout-composer.md) · [Repositori](https://github.com/Defani/Layout-Composer) · [Baca panduan](/reader.html?file=/perpus/panduan-layout-composer.pdf&title=Panduan%20Lengkap%20Layout%20Composer)

### GBIF Data

:::{figure} ../assets/plugins/gbif-points.png
:label: fig-gbif-points
Kejadian GBIF sebagai titik.
:::

:::{figure} ../assets/plugins/gbif-density.png
:label: fig-gbif-density
Kejadian GBIF sebagai layer kepadatan.
:::

:::{figure} ../assets/plugins/gbif-popup-and-citation.png
:label: fig-gbif-popup
Popup rekaman beserta sitasinya.
:::

Mengambil data kejadian (occurrence) dari GBIF langsung ke peta GeoLibre.

[Halaman resmi](https://plugins.geolibre.app/catalog/geolibre-gbif-data/) · [README lengkap](../repos/alat/gbif-data.md) · [Repositori](https://github.com/Defani/GBIF-Data) · [Baca panduan](/reader.html?file=/perpus/panduan-gbif-data.pdf&title=GBIF%20Data%3A%20Complete%20Guide)

### iNaturalist Extractor

Mengambil observasi iNaturalist dan menambahkannya ke peta sebagai layer GeoJSON.

[Halaman resmi](https://plugins.geolibre.app/catalog/geolibre-inaturalist-extractor/) · [README lengkap](../repos/alat/geolibre-inaturalist-extraction-plugins.md) · [Repositori](https://github.com/Defani/Geolibre-Inaturalist-Extraction-Plugins)

### Tentang GeoLibre

[GeoLibre](https://geolibre.app) bukan buatan saya. GeoLibre dibuat dan dikelola oleh [Qiusheng Wu](https://github.com/giswqs) ([ORCID 0000-0001-5437-4073](https://orcid.org/0000-0001-5437-4073)), University of Tennessee, Knoxville, di bawah organisasi [opengeos](https://github.com/opengeos), dan dirilis dengan [Lisensi MIT](https://github.com/opengeos/GeoLibre/blob/main/LICENSE). Saya berkontribusi lewat plugin untuk ekosistemnya (plugin di halaman ini).

GeoLibre adalah GIS cloud-native gratis yang berjalan di browser, desktop, ponsel, dan notebook Jupyter, dengan 1.000+ alat geoprocessing yang berjalan di WebAssembly. Dibangun dengan [Tauri](https://github.com/tauri-apps/tauri), [React](https://github.com/facebook/react), [TypeScript](https://github.com/microsoft/TypeScript), [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js), [DuckDB-WASM](https://github.com/duckdb/duckdb-wasm), dan [deck.gl](https://github.com/visgl/deck.gl).

| | |
| --- | --- |
| Pembuat | Qiusheng Wu |
| Repositori | [github.com/opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) |
| Situs | [geolibre.app](https://geolibre.app) · [Panduan pengguna](https://geolibre.app/user-guide/interface/) · [Tutorial](https://geolibre.app/tutorials/) |
| Marketplace plugin | [plugins.geolibre.app](https://plugins.geolibre.app) ([opengeos/geolibre-plugins](https://github.com/opengeos/geolibre-plugins)) |
| Terkait | [geolibre-rust](https://github.com/opengeos/geolibre-rust) (alat WebAssembly), [geolibre-r](https://github.com/opengeos/geolibre-r) (antarmuka R), [templat plugin](https://github.com/opengeos/geolibre-plugin-template) |
| Lisensi | MIT |
| DOI | [10.5281/zenodo.20785400](https://doi.org/10.5281/zenodo.20785400) |

### Cara mengutip GeoLibre

Sesuai [CITATION.cff](https://github.com/opengeos/GeoLibre/blob/main/CITATION.cff) dan [panduan sitasi](https://github.com/opengeos/GeoLibre/blob/main/docs/citation.md) proyeknya:

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

## Plugin QGIS

### RasterViz

Visualisasi raster ilmiah bergaya Matplotlib langsung di QGIS tanpa coding, dipakai lebih dari 1.300 pengguna.

[Halaman resmi QGIS](https://plugins.qgis.org/plugins/qrviz/) · [README lengkap](../repos/alat/rasterviz.md) · [Repositori](https://github.com/Defani/RasterViz) · [Situs dokumentasi](https://defani.github.io/RasterViz/)

### qthresh

Pratinjau threshold raster secara langsung dengan slider di QGIS.

[README lengkap](../repos/alat/qthresh.md) · [Repositori](https://github.com/Defani/qthresh)
