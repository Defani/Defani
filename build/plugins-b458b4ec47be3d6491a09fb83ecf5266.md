# Plugin

[English](../plugins.md) · **Bahasa Indonesia**

Plugin yang saya buat untuk [GeoLibre](geolibre.md) (buatan Qiusheng Wu, [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre), DOI [10.5281/zenodo.20785400](https://doi.org/10.5281/zenodo.20785400)) dan [QGIS](https://qgis.org) (QGIS Development Team, [qgis/QGIS](https://github.com/qgis/QGIS)). Platformnya milik pembuatnya; pluginnya buatan saya.

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

[Halaman resmi](https://plugins.geolibre.app/catalog/geolibre-gbif-data/) · [Panduan di web](../panduan/gbif-data.md) · [README lengkap](../repos/alat/gbif-data.md) · [Repositori](https://github.com/Defani/GBIF-Data) · [Baca panduan](/reader.html?file=/perpus/panduan-gbif-data.pdf&title=GBIF%20Data%3A%20Complete%20Guide)

### iNaturalist Extractor

Mengambil observasi iNaturalist dan menambahkannya ke peta sebagai layer GeoJSON.

[Halaman resmi](https://plugins.geolibre.app/catalog/geolibre-inaturalist-extractor/) · [README lengkap](../repos/alat/geolibre-inaturalist-extraction-plugins.md) · [Repositori](https://github.com/Defani/Geolibre-Inaturalist-Extraction-Plugins)

## Plugin QGIS

### RasterViz

Visualisasi raster ilmiah bergaya Matplotlib langsung di QGIS tanpa coding, dipakai lebih dari 1.300 pengguna.

[Halaman resmi QGIS](https://plugins.qgis.org/plugins/qrviz/) · [README lengkap](../repos/alat/rasterviz.md) · [Repositori](https://github.com/Defani/RasterViz) · [Situs dokumentasi](https://defani.github.io/RasterViz/)

### qthresh

Pratinjau threshold raster secara langsung dengan slider di QGIS.

[README lengkap](../repos/alat/qthresh.md) · [Repositori](https://github.com/Defani/qthresh)
