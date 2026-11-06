---
title: "gayo-baseline-gis-toolkit"
---

This plugin consolidates the recurring, otherwise manual steps of a field-based baseline GIS assessment

[Repositori di GitHub](https://github.com/Defani/gayo-baseline-gis-toolkit)

<div align="left">
  <img src="https://raw.githubusercontent.com/Defani/gayo-baseline-gis-toolkit/main/assets/partners_banner.png" alt="TFCA Sumatera, Rumah Indonesia Berkelanjutan, Redelong Institute" width="260">
</div>

# Gayo Coffee Baseline GIS Toolkit

A QGIS plugin for the Gayo coffee farmer baseline assessment (Konsorsium Konservasi Kopi Gayo) in Aceh Tengah and Bener Meriah, Aceh. Every tool opens from one sidebar panel instead of separate popup windows.

<div align="left">

![QGIS](https://img.shields.io/badge/QGIS-3.16%2B-589632?logo=qgis&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![PyQt](https://img.shields.io/badge/PyQt-5-41CD52?logo=qt&logoColor=white)
![Version](https://img.shields.io/badge/version-0.11-orange)
![Status](https://img.shields.io/badge/status-experimental-yellow)
![License](https://img.shields.io/badge/license-GPLv3-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

</div>

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Feature diagrams](#feature-diagrams)
- [Tech stack](#tech-stack)
- [QGIS and engine stack reference](#qgis-and-engine-stack-reference)
- [Project structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Third-party components and licenses](#third-party-components-and-licenses)
- [License](#license)
- [Author and partners](#author-and-partners)
- [Contact](#contact)

## Overview

This plugin consolidates the recurring, otherwise manual steps of a field-based baseline GIS assessment into one QGIS sidebar panel, mapped to the stages a GIS consultant normally works through on this kind of survey:

| Workflow stage | What a GIS consultant would otherwise do manually | Toolkit feature(s) covering it |
| --- | --- | --- |
| 1. Field data ingestion | Manually export KoboToolbox submissions, geocode them, rebuild geometry from geopoint/geotrace strings | Kobo Connect |
| 2. Field evidence handling | Manually download attachment URLs one by one, resize/rotate images, link them back to the right feature | Foto di Layer, Foto Explorer |
| 3. Data QA/QC | Write ad hoc QGIS expressions to find missing coordinates, duplicates or incomplete records | Quick Query |
| 4. Base data preparation | Separately add web basemaps, WMTS/WMS/WFS services, local reference files, or set up the Earth Engine Python API and write scripts to pull imagery | Add Layer, Basemap Search (QMS), GEE Connect |
| 5. Spatial analysis | Build a spatial index, reproject to a local UTM zone, and script a nearest-neighbor distance calculation by hand | Distance Analysis |
| 6. Data delivery / integration | Export layers individually to the format each stakeholder needs, or manually run `ogr2ogr`/write SQL to push data into PostGIS | Export Data, Export to Database |
| 7. Field logistics | Manually convert layers to GPX for GPS units | Export to GPX |
| 8. Cartographic output | Manually compute grid cells and index labels for a multi-page map series/atlas | Grid Index |

In short: it is not a single-purpose tool, but a packaged set of the repetitive KoboToolbox-to-QGIS-to-deliverable steps a GIS consultant would otherwise re-implement per project, built specifically for the Gayo coffee farmer baseline survey (Konsorsium Konservasi Kopi Gayo) in Aceh Tengah and Bener Meriah, Aceh. Every tool is exposed as a `QWidget` page inside a single `QDockWidget` (see [System architecture](https://github.com/Defani/gayo-baseline-gis-toolkit/blob/main/FEATURES.md#0-system-architecture) for the full technical breakdown), and the Grid Index step is also registered as a standalone `QgsProcessingAlgorithm` so it can be scripted or batch-run from the Processing Toolbox instead of the panel.

- Author: Defani Arman, GIS Consultant
- Program: TFCA Sumatera Program
- Implementing partners: Rumah Indonesia Berkelanjutan and Redelong Institute
- Area of work: Aceh Tengah and Bener Meriah, Aceh, Indonesia

## Features

All 12 tools live in one dockable sidebar panel (toolbar icon or Plugins menu) - pick a tool from the list, it opens in place, and "Back to menu" returns to the list. The table below explains, for each tool, **why it exists in the survey workflow**, **exactly what it does step by step**, and what you get out of it, with links to the relevant QGIS documentation and the file format/standard involved.

| # | Feature | Function in the toolkit (why it exists) | How it works (step by step) | Output | References |
| --- | --- | --- | --- | --- | --- |
| 1 | **Kobo Connect** | Brings field survey data collected in KoboToolbox into QGIS, so the baseline survey can be mapped and analyzed spatially instead of staying as raw form data | Log in with the KoboToolbox API URL, username and password -> list the user's forms -> pick a form and its geometry field -> the plugin authenticates and downloads every submission (paginated) -> flattens nested/repeat-group answers and parses the geometry -> builds a feature collection and loads it as a QGIS layer | A QGIS vector layer with one feature per submission, all survey answers as attributes | [Creating vector layers](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/create_layer.html) - [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) - [KoboToolbox API](https://support.kobotoolbox.org/api.html) |
| 2 | **Foto di Layer (Kobo)** | Lets field photos taken during the survey be seen directly on the map next to the point that was surveyed, instead of digging through a folder of image files | Pick the survey layer and its photo field(s) -> the plugin detects which fields hold photo attachments and which field is the ID/title -> choose a download folder -> it downloads each photo from Kobo (authenticated), resizes it and fixes its EXIF rotation, then saves it under a predictable filename -> adds a virtual "path" field pointing to the saved file -> builds a map tip and configures the attribute form to preview the photo | Photos saved locally, a new path field on the layer, and a photo preview when hovering a point (map tip) or opening its attribute form | [Map tips](https://docs.qgis.org/latest/en/docs/user_manual/introduction/general_tools.html#identify-features-with-map-tips) - [Photo/editing widgets](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html#fields-properties) - [EXIF](https://en.wikipedia.org/wiki/Exif) |
| 3 | **Foto Explorer (Kobo)** | Gives a quick way to browse and quality-check all the photos attached to repeated question groups in a Kobo form (e.g. multiple tree photos per plot), without opening each submission one by one | Connect to the Kobo form -> the plugin detects image fields inside repeat groups -> fetches submissions and builds one browsable entry per photo -> pick a photo in the list to download it on demand and preview it full-size | An in-panel photo browser/preview for every photo in a repeat group, without pre-downloading everything | [Attribute table](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/attribute_table.html) - [KoboToolbox](https://support.kobotoolbox.org/) |
| 4 | **Quick Query** | Speeds up day-to-day data checking: finding a specific respondent, filtering by a field value, or spotting bad/incomplete records, without writing a QGIS expression by hand every time | Pick the layer -> use the search box (text/attribute search), the filter box (field + operator + value), or a ready-made QC preset (e.g. "empty geometry / no coordinates") -> the plugin builds the matching QGIS expression and applies it as a layer filter or selection | A filtered attribute table / map view showing only the matching or flagged features | [Expressions](https://docs.qgis.org/latest/en/docs/user_manual/expressions/expression.html) - [Selecting features](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_selection.html) |
| 5 | **Distance Analysis** | Answers the baseline assessment's core spatial question - how far is each surveyed coffee farm from a forest area, and what is that forest area's legal/conservation status - which is needed to flag encroachment risk | Pick the survey point layer and the forest/kawasan polygon layer plus its status field -> the plugin builds a spatial index of the forest polygons and picks a local UTM zone for accurate metric distances -> for every point it finds the nearest forest polygon, the distance to it, and its status field value -> converts the distance to m/km -> either draws a line from each point to its nearest forest (for visual QC) or writes the distance/status straight into new columns on the point layer | New distance + forest-status columns on the point layer, and/or a line layer showing each point-to-forest connection, plus a summary of the results | [Vector analysis (Processing)](https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html) - [Spatial index](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/vector.html#using-spatial-index) - [Nearest neighbor search](https://en.wikipedia.org/wiki/Nearest_neighbor_search) - [UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) |
| 6 | **Export Data** | Hands survey results to people or tools that don't use QGIS - program officers reviewing data in Excel, or another system that consumes GeoJSON/CSV | Pick the layer and a target format (Excel, GeoJSON or CSV) and an output path -> the plugin writes the layer through QGIS's own vector writer (GDAL/OGR underneath), fixing the file extension if needed | A single Excel/GeoJSON/CSV file with the layer's geometry and attributes | [Saving vector layers](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/create_layer.html#saving-vector-layers) - [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) - [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) - [XLSX/Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) |
| 7 | **Export to Database** | Moves survey data into a proper spatial database so it can be queried, shared with a team, or connected to other GIS/web tools instead of living only as local files | Pick a saved PostGIS connection (or a Supabase Postgres connection set up the same way) and a destination table name -> the plugin sanitizes the layer and its field names into safe SQL identifiers -> exports the layer via QGIS's native database exporter, no extra database driver needed | A new (or appended) spatial table inside the PostGIS/Supabase database | [Opening a database (PostGIS)](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/opening_data.html#opening-a-database) - [PostGIS](https://en.wikipedia.org/wiki/PostGIS) - [Supabase](https://supabase.com/docs) |
| 8 | **Add Layer** | One place to bring in every kind of base data the survey needs - basemap tiles, official web map services, local files handed over by partners, or Earth Engine imagery - without hunting through QGIS's several different "Add Layer" menus | Pick a source tab: for web tiles, enter an XYZ/WMTS/WMS/WFS URL (the plugin can read the service's capabilities to fill in the details automatically); for files, browse to any format QGIS/GDAL can read; for Earth Engine, pick a dataset (handled by GEE Connect, tool 10) -> the plugin builds the matching QGIS data source and adds it to the map | A new raster or vector layer on the map canvas, from whichever source was picked | [Loading data (Add data)](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/opening_data.html) - [Working with OGC data](https://docs.qgis.org/latest/en/docs/user_manual/working_with_ogc/index.html) - [WMTS](https://en.wikipedia.org/wiki/Web_Map_Tile_Service) - [WMS](https://en.wikipedia.org/wiki/Web_Map_Service) - [WFS](https://en.wikipedia.org/wiki/Web_Feature_Service) - [XYZ tiles](https://en.wikipedia.org/wiki/Tiled_web_map) |
| 9 | **Basemap Search (QMS)** | Gives a fast way to add a familiar basemap (OSM, Google, Bing, Esri, USGS, Yandex, etc.) for visual context, without opening QGIS's separate Web > QuickMapServices menu | Type a search term -> the plugin searches the basemap catalog bundled with the separately-installed QuickMapServices plugin -> pick a result -> it is added straight to the map using QuickMapServices' own "add to map" helper | A basemap raster tile layer added to the project | [XYZ tile connections](https://docs.qgis.org/latest/en/docs/user_manual/working_with_ogc/ogc_client_support.html#xyz-tile-connections) - [QuickMapServices plugin](https://plugins.qgis.org/plugins/quick_map_services/) |
| 10 | **GEE Connect** | Brings satellite imagery and other Earth Engine datasets (e.g. land cover, deforestation alerts, elevation) into the survey area, without leaving QGIS to use the Earth Engine Code Editor | Checks the Google Earth Engine Python API is installed and authenticated -> browse/search a trimmed Earth Engine dataset catalog -> pick a dataset, a date range and an area of interest -> the plugin builds the corresponding Earth Engine image (applying date/region/visualization filters) and asks Earth Engine for an XYZ tile URL (or, for vector datasets, downloads the features as GeoJSON) -> adds the result as a layer | A raster layer streamed live from Earth Engine's servers (or a vector layer for feature datasets) | [Raster layers](https://docs.qgis.org/latest/en/docs/user_manual/working_with_raster/raster_properties.html) - [Google Earth Engine](https://earthengine.google.com/) - [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets) - [geemap](https://github.com/gee-community/geemap) (catalog trimmed from geemap; see citation below) |
| 11 | **Export to GPX** | Turns survey points/lines into a track/waypoint file that can be loaded onto a handheld Garmin GPS for offline field navigation, where QGIS itself isn't available | Pick the point or line layer and a field to use as each point's name (or leave it blank to dissolve everything into one named track) -> the plugin runs it through QGIS's native Processing algorithms to fix geometries, convert polygons to lines if needed, dissolve/split features and set the name field -> writes the result using GDAL's GPX driver | A `.gpx` file with waypoints/tracks ready to copy onto a Garmin device | [Working with GPS data](https://docs.qgis.org/latest/en/docs/user_manual/working_with_gps/index.html) - [GPX (GPS Exchange Format)](https://en.wikipedia.org/wiki/GPS_Exchange_Format) |
| 12 | **Grid Index** | Produces the index grid needed to print or export the survey area as a multi-page map series/atlas (a common requirement for field teams and reports), instead of working with one unmanageably large map | Set the area extent, map scale, page size and rotation -> the plugin's Processing algorithm checks whether the layer's CRS is projected or geographic (transforming to World Mercator EPSG:3395 first if geographic, so cell sizes stay accurate) -> computes grid cells covering the extent at the chosen scale/page size and labels each one | A polygon grid layer, each cell labeled as one atlas page, ready to drive a QGIS Print Layout atlas | [Coordinate reference systems](https://docs.qgis.org/latest/en/docs/user_manual/working_with_projections/index.html) - [Atlas generation](https://docs.qgis.org/latest/en/docs/user_manual/print_composer/create_output.html#atlas-generation) - [Map series](https://en.wikipedia.org/wiki/Map_series) - [World Mercator (EPSG:3395)](https://epsg.io/3395) |


## Feature diagrams

[FEATURES.md](https://github.com/Defani/gayo-baseline-gis-toolkit/blob/main/FEATURES.md) contains the full system architecture - a component diagram of how the plugin bootstrap, the sidebar panel, each tool's UI and business-logic modules, and the external systems (KoboToolbox, Earth Engine, OGC services, PostGIS/Supabase, GDAL) connect - followed by a per-tool Mermaid flow diagram showing dialog input, processing steps and QGIS output.

## Tech stack

| Layer | Technology |
| --- | --- |
| Host application | QGIS Desktop 3.16+ |
| Plugin framework | PyQGIS (`qgis.core`, `qgis.gui`) |
| UI toolkit | PyQt5 (`qgis.PyQt.QtWidgets`, `QtGui`, `QtCore`) |
| Language | Python 3 |
| HTTP client | [`requests`](https://requests.readthedocs.io/) (KoboToolbox REST API, basic auth) |
| Survey data source | KoboToolbox API |
| Satellite imagery | [Google Earth Engine](https://earthengine.google.com/) Python API (optional, loaded only if `ee` is installed) |
| Web layers | OGC XYZ / WMTS / WMS / WFS, via QGIS's native OWS providers |
| Database export | QGIS native `QgsVectorLayerExporter` (PostGIS / Supabase, no extra DB driver required) |
| File formats | GeoJSON, CSV, Excel, GPX, generic OGR/GDAL-supported vector and raster formats |
| Concurrency | Python `concurrent.futures` / `threading` for non-blocking network calls |
| Packaging | Standard QGIS plugin layout (`metadata.txt`, `classFactory`, Processing provider) |

## QGIS and engine stack reference

A complete, class-by-class breakdown of every `qgis.core` / `qgis.gui` class, Processing algorithm, GDAL/OGR driver, Qt widget, Google Earth Engine API call, and external web service actually used in the code - each with a link to its official reference - is kept in [QGIS_ENGINE_STACK.md](https://github.com/Defani/gayo-baseline-gis-toolkit/blob/main/QGIS_ENGINE_STACK.md).

## Project structure

```text
agroforestry_gis_toolkit/
├── __init__.py                     # classFactory entry point
├── metadata.txt                    # QGIS plugin metadata
├── agroforestry_gis_toolkit_plugin.py  # plugin bootstrap, toolbar, dock widget
├── sidebar_panel.py                 # single dockable panel, menu of all tools
├── branding.py                      # plugin name, author, affiliation constants
├── icon.png                         # plugin/toolbar icon
├── add_layer_dialog.py              # XYZ / WMTS / WMS / WFS / file / GEE layer loader
├── basemap_search_dialog.py         # Quick Map Services basemap search
├── kobo_dialog.py / kobo_connector.py            # KoboToolbox connection
├── foto_layer_dialog.py / foto_layer_utils.py    # field photos on the map
├── foto_explorer_dialog.py          # Kobo repeat-group photo browser
├── quick_query_dialog.py            # search, filter, QC presets
├── distance_dialog.py / distance_processor.py    # distance-to-forest analysis
├── export_dialog.py / exporter.py                # Excel / GeoJSON / CSV export
├── db_export_dialog.py / db_exporter.py          # PostGIS / Supabase export
├── gee_dialog.py / gee_connector.py / gee_catalog.csv  # Earth Engine layers
├── gpx_dialog.py / gpx_processor.py              # GPX export for Garmin
├── grid_index_dialog.py / grid_index_algorithm.py / grid_index_provider.py  # grid/atlas index
└── ows_utils.py                     # shared OGC web service helpers
```

## Installation

1. Download the latest release ZIP of this repository.
2. In QGIS, go to **Plugins > Manage and Install Plugins > Install from ZIP**.
3. Select the downloaded ZIP and click **Install Plugin**.
4. Enable **Gayo Coffee Baseline GIS Toolkit** in the plugin list.
5. Optional: to use GEE Connect, install the Google Earth Engine Python API (`ee`) in the QGIS Python environment and authenticate it separately.

## Usage

1. Click the plugin's toolbar icon, or open it from **Plugins > Gayo Coffee Baseline GIS Toolkit**, to open the sidebar panel.
2. Pick a tool from the menu list; it opens in place inside the same panel.
3. Use **Back to menu** to return to the tool list at any time.
4. Grid Index is also available from the **Processing Toolbox** as a standalone algorithm.

## Third-party components and licenses

| Component | Source | License |
| --- | --- | --- |
| Grid Index algorithm | Adapted from a plugin by Kapildev Adhikari | GNU GPLv3 |
| GPX export pipeline | Conversion approach adapted from ["GPX Maker for GARMIN(R) devices"](https://github.com/SandaTakeru/GPX-Maker-for-Garmin-devices) by Sanda Takeru | GNU GPLv3 |
| GEE dataset catalog (`gee_catalog.csv`) | Trimmed from [geemap](https://github.com/gee-community/geemap) by Qiusheng Wu, itself derived from the Earth Engine Datasets List by Samapriya Roy | MIT |

Full attribution notice for the Earth Engine catalog is kept in `gee_catalog_NOTICE.txt`.

Survey data collection relies on [KoboToolbox](https://www.kobotoolbox.org/) (source: https://github.com/kobotoolbox) via its REST API. Satellite imagery relies on [Google Earth Engine](https://earthengine.google.com/):

> Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of Environment*, 202, 18-27. https://doi.org/10.1016/j.rse.2017.06.031
>
> Wu, Q. (2020). geemap: A Python package for interactive mapping with Google Earth Engine. *Journal of Open Source Software*, 5(51), 2305. https://doi.org/10.21105/joss.02305

The complete list of platforms, APIs and references used by every feature is in [QGIS_ENGINE_STACK.md](https://github.com/Defani/gayo-baseline-gis-toolkit/blob/main/QGIS_ENGINE_STACK.md#12-references).

## License

This plugin is distributed under the **GNU General Public License v3.0 (GPLv3)**, consistent with the license of the Grid Index code it incorporates. See [gnu.org/licenses/gpl-3.0](https://www.gnu.org/licenses/gpl-3.0.html) for the full license text.

## Author and partners

<div align="left">
  <img src="https://raw.githubusercontent.com/Defani/gayo-baseline-gis-toolkit/main/assets/partners_banner.png" alt="TFCA Sumatera, Rumah Indonesia Berkelanjutan, Redelong Institute" width="420">
</div>

- **Author**: Defani Arman - GIS Consultant
- **Program**: TFCA Sumatera Program
- **Partners**: Rumah Indonesia Berkelanjutan, Redelong Institute
- **Location**: Aceh Tengah and Bener Meriah, Aceh, Indonesia

## Contact

- Email: defaniarman@gmail.com
</div>
