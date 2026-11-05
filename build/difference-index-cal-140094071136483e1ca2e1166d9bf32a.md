---
title: "Difference-Index-Calculator-QGIS-Toolbox"
---

A QGIS Processing toolbox script that calculates any normalized difference spectral index from one or two raster layers using the  normalized Difference Index

[Repositori di GitHub](https://github.com/Defani/Difference-Index-Calculator-QGIS-Toolbox)

> **Author:** Defani Arman Alfitriansyah
> **Date:** June 11, 2026
> **Version:** 1.0.0
> **GitHub:** https://github.com/Defani/Difference-Index-Calculator-QGIS-Toolbox
> **Compatible:** QGIS 3.16+

---

## Overview

A QGIS Processing toolbox script that calculates **any normalized difference spectral index** from one or two raster layers using the universal formula:

$$\text{NDI} = \frac{\text{Band A} - \text{Band B}}{\text{Band A} + \text{Band B}}$$

Common indices you can calculate:

| Index | Band A | Band B | Typical Use |
|-------|--------|--------|-------------|
| **NDVI** | NIR | Red | Vegetation health |
| **NDWI** | Green | NIR | Water body mapping |
| **MNDWI** | Green | SWIR | Modified water index |
| **NDBI** | SWIR | NIR | Built-up area mapping |
| **NBR** | NIR | SWIR | Burn severity |
| **NDSI** | Green | SWIR | Snow mapping |
| **Custom** | Any | Any | Any user-defined index |

> This tool is part of the **Remote Sensing Tools** group in the QGIS Processing Toolbox — alongside the [Spectral Value Extractor](https://github.com/Defani/Spectral-Value-Extractor-QGIS-Tooolbox).

---

## Key Features

- **Flexible band selection** — Band A and Band B can come from different raster files or from the same multi-band raster
- **Auto-resample** — if the two bands have different spatial resolutions, the coarser one is automatically resampled (bilinear) to match the finer resolution
- **Auto-reproject** — if the two rasters have different CRS, the secondary one is reprojected to match
- **Custom index name** — the name you enter becomes the QGIS layer name and the band description in the output GeoTIFF
- **Output range clipped to [−1, 1]** with NoData set to −9999
- **Quick statistics** printed to the log (min, max, mean)
- **Output added to QGIS automatically** after processing

---

## Installation

### Step 1 — Download the Script

Download `NormalizedDifferenceIndexCalculator_script.py` from this repository (click **Code → Download ZIP** or clone with git).

```bash
git clone https://github.com/Defani/Difference-Index-Calculator-QGIS-Toolbox.git
```

---

### Step 2 — Add Script to Processing Toolbox

Open **Processing → Toolbox**, click the **Python icon (⚙️)** at the top of the Toolbox panel, and select **Add Script to Toolbox...**

---

### Step 3 — Browse and Select the Script File

Navigate to where you saved `NormalizedDifferenceIndexCalculator_script.py` and click **Open**.

---

### Step 4 — Find the Tool in the Toolbox

The tool will appear under:

```
Processing Toolbox
└── Scripts
    └── Remote Sensing Tools
        └── Normalized Difference Index Calculator
```

Double-click to open the dialog.

---

## Usage

### Step 5 — Fill in the Parameters

| Parameter | Description |
|-----------|-------------|
| **Preset Index** | Optional dropdown — select an index to see a hint about which band should go in Band A and which in Band B. Does not auto-fill the band numbers. |
| **Raster for Band A** | Select the raster layer containing Band A (e.g. a NIR band) |
| **Band A** | Band number within Raster A (default: 1) |
| **Raster for Band B** | Select the raster layer containing Band B — can be the same file as Band A |
| **Band B** | Band number within Raster B (default: 1) |
| **Output Index Name** | Name for the output, e.g. `NDVI`, `NDWI`, `CustomIndex` |
| **Output Raster** | File path for the output GeoTIFF |

---

### Step 6 — Understanding the Preset Dropdown

The **Preset Index** dropdown is a **guidance tool** — it shows a hint in the processing log telling you which band should go in Band A and which in Band B. You still assign the band numbers manually, which gives you full flexibility with any satellite sensor.

Example presets:

| Preset | Band A | Band B |
|--------|--------|--------|
| NDVI | NIR band | Red band |
| NDWI | Green band | NIR band |
| MNDWI | Green band | SWIR band |
| NDBI | SWIR band | NIR band |
| NBR | NIR band | SWIR band |

---

### Step 7 — Auto-Resample Behavior

If Band A and Band B come from rasters with **different pixel resolutions** (e.g. 10 m vs 20 m), the tool will:

1. Detect which raster has the **finer** (smaller pixel) resolution
2. Resample the **coarser** raster to match the finer grid using **bilinear interpolation**
3. Compute the index on the harmonized grid
4. The output resolution matches the **finest input resolution**

This is reported in the processing log:

```
Pixel area A: 100.000000  |  Pixel area B: 400.000000
Raster B has coarser resolution (or different CRS). Resampling Band B → Band A grid (bilinear).
```

---

### Step 8 — Run and Check the Log

Click **Run**. The log will show:

```
Preset hint: NIR band → Band A  |  Red band → Band B
Index name  : NDVI
Band A      : band 4 from 'Sentinel2_10m'
Band B      : band 3 from 'Sentinel2_10m'
Same resolution and CRS — no resampling needed.
Result  min : -0.312500
Result  max :  0.891200
Result mean :  0.423700
✔ Layer 'NDVI' added to QGIS.
✔ Done! 'NDVI' saved to: C:/output/NDVI.tif
```

---

### Step 9 — Output Layer

Once finished, the output raster is automatically added to the QGIS Layers panel with the name you specified (e.g. `NDVI`). The output is a single-band Float32 GeoTIFF compressed with LZW.

---

## Parameters Reference

| Parameter | Type | Description |
|-----------|------|-------------|
| **Preset Index** | Enum (optional) | Guidance hint — shows band assignment in the log |
| **Raster for Band A** | Raster Layer | Input raster containing Band A |
| **Band A** | Band Number | Band index in Raster A |
| **Raster for Band B** | Raster Layer | Input raster containing Band B (can equal Raster A) |
| **Band B** | Band Number | Band index in Raster B |
| **Output Index Name** | String | Name used for the QGIS layer and GeoTIFF band description |
| **Output Raster** | Raster Destination | Output GeoTIFF file path |

### Outputs

| Output | Description |
|--------|-------------|
| **Output Raster** | Float32 GeoTIFF, values in [−1, 1], NoData = −9999 |
| **Minimum value** | Minimum valid pixel value |
| **Maximum value** | Maximum valid pixel value |
| **Mean value** | Mean valid pixel value |

---

## Technical Notes

- Output values are **clipped to [−1, 1]** — pixels where Band A + Band B = 0 are set to NoData
- NoData value in the output is **−9999**
- If both bands have the same raster source and resolution, no resampling is performed
- If CRS differ, the secondary raster is **reprojected** to the reference CRS using GDAL `ReprojectImage` with bilinear resampling
- Output GeoTIFF is written with **LZW compression** and tiling for efficient performance on large rasters

---

## Requirements

- QGIS 3.16 or later
- Python 3.x (included with QGIS)
- Libraries: `gdal`, `numpy` (included with QGIS)

---

## Related Tool

| Tool | Description |
|------|-------------|
| [Spectral Value Extractor](https://github.com/Defani/Spectral-Value-Extractor-QGIS-Tooolbox) | Extracts raster pixel values at field sample point locations, exports to CSV and new point layer |

---

## License

MIT License — free to use, modify, and distribute.
