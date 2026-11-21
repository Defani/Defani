---
title: "qthresh"
---

Live, slider-driven threshold preview for raster layers in QGIS

[Repositori di GitHub](https://github.com/Defani/qthresh)

![QGIS](https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=flat-square&logo=qt&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)![Dependencies](https://img.shields.io/badge/Dependencies-ZERO-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-GPLv2%2B-lightgrey?style=flat-square)

Live, slider-driven threshold preview for raster layers in QGIS — built for
exploratory analysis of vegetation/water indices (NDVI, NDWI, EVI, etc.)
derived from Sentinel-2, Landsat, or any single/multi-band raster.

## Features (v0.1.0)

- **Live threshold preview**: min/max sliders (with paired numeric spin
  boxes for precision) update the layer's symbology in near real time,
  debounced to stay responsive on larger rasters.
- **Histogram overlay**: shows the sampled band's value distribution with
  the current threshold range shaded, so you can see where the slider is
  cutting the data.
- **Otsu auto-suggestion**: one-click threshold suggestion using Otsu's
  (1979) between-class variance maximization, implemented in pure numpy.
- **Live statistics**: pixel count and approximate area (ha) within the
  current range, computed on the sampled preview grid.
- **Presets**: save/load named min–max threshold combinations (per QGIS
  profile, via `QSettings`).
- **Export to vector**: converts the current threshold mask to polygons
  (`gdal:polygonize` under the hood) and adds it to the project.

## Installation (development)

1. Clone this repo into your QGIS plugins directory:
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - Windows: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
2. In QGIS, open **Plugins → Manage and Install Plugins → Installed**, and
   enable **QThresh**.
3. The plugin icon appears on the toolbar and under **Raster → QThresh**.

## Known limitations / assumptions

- Preview statistics (histogram, Otsu suggestion, pixel/area counts) are
  computed on a **downsampled** version of the raster (capped at ~400×400
  px by default, see `raster_utils.sample_band_as_array`) for
  responsiveness. For values used in a paper or report, recompute on the
  full-resolution raster.
- Area statistics assume a **projected CRS with metre units**; for a
  geographic CRS the panel flags this instead of reporting a (misleading)
  hectare value.
- The live symbology uses a single semi-transparent highlight colour for
  "in range" values; multi-class breaks are not yet supported (see
  Roadmap).

## Roadmap / ideas not yet implemented

- Multi-band index computation on the fly (e.g. build NDVI from red/NIR
  bands before thresholding, rather than requiring a precomputed index
  raster).
- Multi-class (>2) threshold breaks with more than one slider pair.
- Time-series batch apply (same threshold across a raster stack).

## License

GPL-2.0 — see `LICENSE`.
