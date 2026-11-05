---
title: "Spectral-Value-Extractor-QGIS-Tooolbox"
---

A QGIS Processing tool that extracts raster pixel values (satellite imagery bands, vegetation indices such as NDVI, NDWI, MNDWI, SAVI, etc.) at field sample point locations automatically

[Repositori di GitHub](https://github.com/Defani/Spectral-Value-Extractor-QGIS-Tooolbox)

> **Author:** Defani Arman Alfitriansyah  
> **Date:** June 09, 2026  
> **Version:** 1.0.0  
> **GitHub:** https://github.com/Defani/Spectral-Value-Extractor-QGIS-Tooolbox

---

## Overview

A QGIS Processing tool that extracts raster pixel values (satellite imagery bands, vegetation indices such as NDVI, NDWI, MNDWI, SAVI, etc.) at field sample point locations automatically.

Key advantage over the built-in QGIS **Sample Raster Values** tool:
- Supports **multiple raster inputs** in a single run
- Directly exports results to a **CSV file**
- Supports **custom band naming**

---

## Installation & Step-by-Step Usage

### Step 1 — Add Script to Processing Toolbox

Open **Processing → Toolbox**, then click the **Python icon (⚙️)** at the top of the Toolbox panel and select **Add Script to Toolbox...**

<img width="1920" height="1080" alt="Screenshot 2026-06-09 162714" src="https://github.com/user-attachments/assets/e9001fa4-0823-45ba-a407-67ccc4224d77" />


---

### Step 2 — Browse and Select the Script File

In the file browser that opens, navigate to where you saved `SpectralValueExtractor_script.py` and select it, then click **Open**.

<img width="865" height="580" alt="Screenshot 2026-06-09 162805" src="https://github.com/user-attachments/assets/6573779f-4e2b-468e-8a67-d014ebcb89cd" />


---

### Step 3 — Find the Tool in the Toolbox

The tool will now appear under **Scripts → Remote Sensing Tools → Spectral Value Extractor** in the Processing Toolbox. Double-click it to open.
<img width="639" height="358" alt="Screenshot 2026-06-09 162824" src="https://github.com/user-attachments/assets/8ef1e9f5-358f-4977-9496-7c4ad60cecdc" />


---

### Step 4 — Fill in the Parameters

The tool dialog will open. Fill in the following:

- **Field Sample Points** — select your point layer (e.g. `field_samples`)
- **Point ID / Label Field** — select the column that identifies each point
- **Raster / Spectral Index Layers** — click `...` to select one or more rasters
- **Custom Band Names** — optional, e.g. `NDVI,SAVI`
- **Include X and Y Coordinate Columns** — check this to add coordinate columns
- **Save Output as CSV** — set a file path to save the CSV result

<img width="1200" height="758" alt="Screenshot 2026-06-09 162852" src="https://github.com/user-attachments/assets/fa86d3ab-ce85-4af7-938a-f2c27b150f7c" />


---

### Step 5 — Select Raster Layers

When you click `...` next to Raster Layers, a panel opens listing all rasters currently loaded in QGIS. Check all the layers you want to extract values from. You can also use **Add File(s)...** to load rasters directly from disk without adding them to the map first.

<img width="1229" height="789" alt="Screenshot 2026-06-09 162904" src="https://github.com/user-attachments/assets/2b020265-9ac8-43f2-95b4-96b00d0a99e4" />


---

### Step 6 — Run and Check the Log

Click **Run**. The Log tab will show the progress and results — number of points processed, bands extracted, and the CSV output path.

<img width="1224" height="775" alt="Screenshot 2026-06-09 162921" src="https://github.com/user-attachments/assets/295a7e3e-4c91-4884-b802-653ca05efbdd" />


---

### Step 7 — Output Layer Added to QGIS

Once finished, the output point layer is automatically added to the Layers panel. It contains all the original point attributes plus the new spectral value columns.

<img width="647" height="527" alt="Screenshot 2026-06-09 162941" src="https://github.com/user-attachments/assets/97d41d1f-3b6c-4eb8-b94e-2c179a9d4529" />


---

### Step 8 — View Results in Attribute Table

Open the attribute table of the output layer to see the extracted spectral values for each point — including X/Y coordinates and all selected band/index values.

<img width="802" height="580" alt="Screenshot 2026-06-09 162958" src="https://github.com/user-attachments/assets/2af2a2fc-0480-4d05-811b-43d155a3d419" />


---

## Parameters Reference

| Parameter | Description |
|-----------|-------------|
| **Field Sample Points** | Point vector layer (.shp / .gpkg / etc.) containing field sample locations |
| **Point ID / Label Field** | Select the column that uniquely identifies each point (e.g. `Sample_ID`, `No`, `Name`) |
| **Raster / Spectral Index Layers** | Select one or more raster layers — different CRS and resolutions are handled automatically |
| **Custom Band Names** | Optional. Example: `B2_Blue,B3_Green,B4_Red,NDVI` — if left empty, column names are taken from the raster file names |
| **Include X and Y Coordinate Columns** | Check to append X and Y coordinate columns to the output |
| **Save Output as CSV** | File path for the CSV output |
| **Output Layer** | New point layer in QGIS with spectral values as attributes |

---

## Notes

- If the point layer and raster layers have **different CRS**, the tool reprojects automatically — no manual reprojection needed.
- For **multi-band rasters** (Sentinel-2, Landsat, etc.), all bands are extracted in a single run.
- Shapefile attribute column names are limited to **10 characters** — use the CSV output for full-length band names.
- If a point falls outside the raster extent, the column value will be `NULL`.

---

## Requirements

- QGIS 3.16 or later
- Python 3.x (included with standard QGIS installation)
- Libraries: `gdal`, `numpy` (included with standard QGIS installation)
