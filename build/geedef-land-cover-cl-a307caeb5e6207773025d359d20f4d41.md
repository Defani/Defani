---
title: "GEEDEF-Land-Cover-Classification-Tools"
---

GEEDEF is a cloud-based, interactive land cover classification tool built entirely within the Google Earth Engine (GEE) Code Editor using the GEE JavaScript API. It is designed to accelerate supervised land cover mapping workflow with full GUI panel

[Repositori di GitHub](https://github.com/Defani/GEEDEF-Land-Cover-Classification-Tools) · [Halaman web](https://defani.github.io/GEEDEF-Land-Cover-Classification-Tools/)

> **Platform:** Google Earth Engine (JavaScript API) | **Data:** Sentinel-2A SR Harmonized | **Version:** V3.1

[![Open in GEE](https://img.shields.io/badge/Open%20in-Google%20Earth%20Engine-4285F4?logo=google&logoColor=white)](https://code.earthengine.google.com/328e48a66c1f2b0a9268cbce3327b9df?hl=id)
![Sentinel-2](https://img.shields.io/badge/Data-Sentinel--2A%20SR%20Harmonized-blue)
![ML](https://img.shields.io/badge/Algorithms-RF%20%7C%20GTB%20%7C%20SVM-brightgreen)
![Lang](https://img.shields.io/badge/Language-GEE%20JavaScript-yellow)
![Institution](https://img.shields.io/badge/Institution-Universitas%20Kuningan-red)
![Updated](https://img.shields.io/badge/Last-Updated%20May%202026-orange)

---

## 🆕 What's New in V3.1

> **Updated from V3 (original PDF release).** The following features were added in the latest version accessible via the updated GEE link.

| # | New Feature | Description |
|---|---|---|
| 1| **📥 Import Training Samples from SHP Asset** | Fully new sub-panel in Step 4 — load existing training data from a GEE `FeatureCollection` asset (uploaded SHP), auto-read attribute columns, extract unique classes, map class codes and names, and merge with manually digitized samples |
| 2| **📖 Read Columns** | Dedicated button to read and populate attribute column dropdowns from the selected SHP asset — eliminates manual column name entry |
| 3 | **🔍 Extract Unique Classes** | Scans the selected SHP asset for all unique numeric class codes and renders an editable row per class (name + color) before import |
| 4 | **🔄 Dual Asset Refresh** | Separate asset refresh inputs for both the ROI boundary and the training sample SHP — previously only one input field existed |
| 5 | **⚠️ Accuracy Penalty Flag** | If only manual samples are used (no field-validated asset imported), the tool applies a **−5% correction** to OA and Kappa and displays a warning note — makes the reliability of the assessment transparent |
| 6 | **🌐 Bilingual UI (EN / ID)** | Full interface toggle between English and Bahasa Indonesia via EN / ID buttons on the map — all labels, buttons, placeholders, and status messages switch dynamically |
| 7 | **📋 Hex Color Copy Box** | Each class in the palette panel now renders an editable hex code textbox next to the class button — allows direct copy without needing to memorize or retype the color code |

---

## Overview

**GEEDEF** is a cloud-based, interactive land cover classification tool built entirely within the Google Earth Engine (GEE) Code Editor using the GEE JavaScript API. It is designed to accelerate supervised land cover mapping workflows at regional and local scales using Sentinel-2A Surface Reflectance (SR) Harmonized imagery.

The tool integrates three scientifically established machine learning classifiers — **Random Forest (RF)**, **Gradient Tree Boost (GTB)**, and **Support Vector Machine (SVM)** — operating over a 26-variable feature space composed of 10 native spectral bands and 16 derived spectral indices. The entire workflow, from image compositing and sample digitization to accuracy assessment and GeoTIFF export, is executed server-side on Google's distributed computing infrastructure.

**Developed by:** Defani Arman Alfitriansyah  
**Institution:** Faculty of Forestry and Environmental Science, Universitas Kuningan  
**Year:** 2025

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Interface Layout](#interface-layout)
3. [Six-Step Workflow](#six-step-workflow)
4. [Feature Space](#feature-space)
5. [Spectral Index Formulas](#spectral-index-formulas)
6. [Land Cover Palette Schemes](#land-cover-palette-schemes)
7. [Tips and Troubleshooting](#tips-and-troubleshooting)
8. [Full Script Repository](#full-script-repository)
9. [Scientific References](#scientific-references)

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **GEE Account** | Active account at [earthengine.google.com](https://earthengine.google.com) |
| **Internet Connection** | Stable connection required for server-side computation |
| **ROI Boundary** | As a GEE `FeatureCollection` asset, or drawn manually on the map |
| **Domain Knowledge** | Basic understanding of land cover concepts and satellite image interpretation |

---

## Interface Layout

GEEDEF uses a three-panel side-by-side layout:


<img width="1920" height="926" alt="Screenshot 2026-05-02 200728" src="https://github.com/user-attachments/assets/81520ee2-b29c-40d2-a7f4-c77e40327cd1" />



---

## Six-Step Workflow

All six steps must be executed **sequentially**. Skipping any step will trigger a warning in the status panel.

---

### Step 1 — Define Region of Interest (ROI)

The ROI defines the spatial extent for image collection filtering, classifier training, and area calculation. Two methods are available:

#### Method A — Load from GEE Asset

1. Enter your GEE account or project name in the text field (e.g., `ee-defaniarman`).
2. Click **🔄 Refresh Assets** to populate the dropdown with available `FeatureCollection` assets.
3. Select the boundary SHP from the dropdown.
4. Click **📥 Load ROI from Dropdown**.
5. The map centers on the loaded ROI and displays the boundary as a blue outline.

#### Method B — Manual Drawing

1. Activate the Drawing Tools from the top-left map toolbar (pencil icon).
2. Draw a polygon defining your study area boundary.
3. Click **🖊 Use Map Drawing Tools**.

> **Recommendation:** For district-scale or larger study areas, Method A is preferred to ensure administrative boundaries match official data.

---

### Step 2 — Sentinel-2A Composite Acquisition

Builds a cloud-free image composite from `COPERNICUS/S2_SR_HARMONIZED` according to user-defined parameters.

#### Acquisition Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| **Date Range** | Start and end date in `YYYY-MM-DD` format | `2024-01-01` to `2024-12-31` |
| **Cloud Max (%)** | Maximum `CLOUDY_PIXEL_PERCENTAGE` per scene | `20%` |
| **Cloud Masking** | Enable/disable pixel-level cloud masking | Enabled |
| **Composite Method** | Temporal aggregation strategy | Median |

#### Cloud Masking Methods

| Method | Description | Recommendation |
|--------|-------------|----------------|
| **Cloud Score+** | Uses `cs_cdf` layer; masks pixels with `cs_cdf < 0.60` | ✅ Recommended — highest accuracy (Pasquarella et al., 2023) |
| **SCL (ESA)** | Removes SCL classes: cloud shadow (3), unclassified (7), medium cloud (8), high cloud (9), thin cirrus (10), snow/ice (11) | Suitable for most tropical regions |
| **QA60 (Bitmask)** | Uses bit 10 (opaque cloud) and bit 11 (cirrus cloud) | Simplest but least precise |

#### Temporal Composite Methods

| Method | Description | Best Use |
|--------|-------------|----------|
| **Median (Default)** | Pixel-wise median across all scenes in date range | Annual mapping; stable and representative |
| **Median Dry Season** | Selects lowest NDVI quartile (25% driest scenes) | Spectral contrast between open land and vegetation |
| **Median Wet Season** | Selects highest NDVI quartile (25% greenest scenes) | Maximizing vegetation response |

---

### Step 3 — Classification Algorithm & Parameters

#### Random Forest (RF)

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `numTrees` | 50–1000 | 500 | Number of decision trees |
| `minLeafPopulation` | 1–20 | 1 | Minimum samples per terminal leaf |
| `bagFraction` | 0.3–1.0 | 0.5 | Proportion of samples per tree |

#### Gradient Tree Boost (GTB)

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `numTrees` | 50–500 | 200 | Number of boosting iterations |
| `shrinkage` | 0.01–0.30 | 0.05 | Learning rate |
| `samplingRate` | 0.30–1.0 | 0.7 | Proportion of samples per iteration |
| `maxNodes` | 2–10 | 5 | Maximum depth per tree |
| `loss` | — | `LeastAbsoluteDeviation` | Loss function |

#### Support Vector Machine (SVM)

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `kernel` | RBF / LINEAR / POLY / SIGMOID | RBF | Kernel function |
| `cost` (C) | 0.1–100 | 10 | Regularization parameter |
| `gamma` | 0.001–2.0 | 0.5 | Influence range (RBF, POLY, SIGMOID) |
| `degree` | 1–10 | 3 | Polynomial degree (POLY only) |
| `coef0` | 0.0–5.0 | 0.0 | Independent coefficient (POLY, SIGMOID) |

#### Training / Testing Split

Default **70/30**. Use **80/20** for datasets with fewer than 200 samples per class. Minimum 20–30 polygons per class required for statistically valid accuracy evaluation.

---

### Step 4 — Add Classes & Digitize Training Samples

#### Option A — Import from SHP Asset *(New in V3.1)*

1. Enter your GEE account/project name and click **🔄 Refresh** to load available SHP assets.
2. Select the training sample asset from the dropdown.
3. Click **📖 Read Columns** to populate attribute column dropdowns.
4. Select the **class code** column and the **class name/label** column.
5. Click **🔍 Extract Unique Classes** — an editable row appears for each class (name + color).
6. Edit names and colors as needed, then click **📥 Save & Import Mapped Samples**.

Imported samples are merged with any manually digitized samples before training.

#### Option B — Manual Class Entry

1. Type a class name, or click a class from the Left Panel palette for auto-fill.
2. Enter the hexadecimal color code (e.g., `#006400`).
3. Click **＋ ADD CLASS** — codes are assigned automatically and increment sequentially.

#### Digitizing Samples

4. Select the **active class** from the dropdown.
5. Activate Drawing Tools (top-left of map); choose **point** or **polygon**.
6. Draw sample areas on the map for the selected class. Repeat for all classes.

> **Best practice:** Distribute samples spatially. Use multiple small polygons per class to capture within-class spectral variability. Avoid transitional or ambiguous zones.

---

### Step 5 — Run Classification

Click **🚀 RUN CLASSIFICATION**. The tool executes server-side:

1. Extracts spectral values (26 variables) from all samples via `sampleRegions`
2. Randomly splits samples into training / validation sets using `randomColumn`
3. Trains the classifier on the training set
4. Classifies all pixels within the ROI
5. Computes error matrix → derives **OA** and **Kappa** from the validation set
6. Calculates per-class area via `ee.Image.pixelArea()` in hectares

#### Accuracy Interpretation

| Metric | Threshold | Note |
|--------|-----------|------|
| **Overall Accuracy (OA)** | > 85% | Generally accepted for regional land cover studies |
| **Kappa Coefficient** | > 0.80 | "Very Strong" agreement (Landis & Koch, 1977) |

> ⚠️ If only manual samples are used (no imported field-validated asset), a **−5% penalty** is applied to OA and Kappa and flagged in the results panel.

---

### Step 6 — Export to Google Drive

1. Set folder name (default: `GEE_Export`) and filename (default: `LandCover_DFRF_V3`).
2. Select output spatial resolution: **10 m**, **20 m**, or **30 m**.
3. Click **⬆ EXPORT — GeoTIFF to Drive**.
4. Monitor in the **Tasks** tab (clock icon, top-right of GEE Code Editor). Click **Run**.

Output is a **single-band integer raster** (pixel value = class code), CRS: `EPSG:4326`. Compatible with QGIS, ArcGIS, and all major GIS software.

---

## Feature Space

After loading the composite, GEEDEF automatically computes 16 spectral indices. Together with 10 native Sentinel-2A bands, the total feature space is **26 predictor variables per pixel**.

### Native Spectral Bands (10)

| Band | Name | Wavelength | Resolution |
|------|------|------------|------------|
| B2 | Blue | ~490 nm | 10 m |
| B3 | Green | ~560 nm | 10 m |
| B4 | Red | ~665 nm | 10 m |
| B5 | Red Edge 1 | ~705 nm | 20 m |
| B6 | Red Edge 2 | ~740 nm | 20 m |
| B7 | Red Edge 3 | ~783 nm | 20 m |
| B8 | NIR | ~842 nm | 10 m |
| B8A | NIR Narrow | ~865 nm | 20 m |
| B11 | SWIR 1 | ~1610 nm | 20 m |
| B12 | SWIR 2 | ~2190 nm | 20 m |

### Derived Spectral Indices (16)

| Index | Full Name | Primary Application |
|-------|-----------|---------------------|
| NDVI | Normalized Difference Vegetation Index | Vegetation density |
| EVI2 | Enhanced Vegetation Index 2 | Canopy structure; reduces atmospheric noise |
| CAI | Cellulose Absorption Index | Bare soil and litter discrimination |
| NDWI | Normalized Difference Water Index | Leaf water content |
| GCVI | Green Chlorophyll Vegetation Index | Chlorophyll estimation |
| SAVI | Soil-Adjusted Vegetation Index | Sparse vegetation over bare soil |
| PRI | Photochemical Reflectance Index | Canopy light use efficiency |
| HALL_COVER | Hall Forest Cover Index | Forest canopy cover estimation |
| IRECI | Inverted Red-Edge Chlorophyll Index | Red-edge based chlorophyll |
| NDRE | Normalized Difference Red Edge | Vegetation health and stress |
| MNDWI | Modified Normalized Difference Water Index | Open water body mapping |
| NDMI | Normalized Difference Moisture Index | Land moisture |
| NDBI | Normalized Difference Built-up Index | Urban and built-up area |
| NBR | Normalized Burn Ratio | Burned area / forest degradation |
| GVS | Green Vegetation Signal | Green vegetation fraction |
| NDFI | Normalized Difference Fraction Index | Forest degradation and fragmentation |

---

## Spectral Index Formulas

$$NDVI = \frac{\rho_{B8} - \rho_{B4}}{\rho_{B8} + \rho_{B4}}$$

$$EVI2 = 2.5 \times \frac{\rho_{B8} - \rho_{B4}}{\rho_{B8} + 2.4 \times \rho_{B4} + 1}$$

$$CAI = \frac{\rho_{B12}}{\rho_{B11}} \qquad NDWI = \frac{\rho_{B8} - \rho_{B11}}{\rho_{B8} + \rho_{B11}} \qquad GCVI = \frac{\rho_{B8}}{\rho_{B3}} - 1$$

$$SAVI = \frac{1.5 \times (\rho_{B8} - \rho_{B4})}{\rho_{B8} + \rho_{B4} + 0.5} \qquad PRI = \frac{\rho_{B2} - \rho_{B3}}{\rho_{B2} + \rho_{B3}}$$

$$HALL\_COVER = -0.017\rho_{B4} - 0.007\rho_{B8} - 0.079\rho_{B12} + 5.22$$

$$IRECI = \frac{\rho_{B7} - \rho_{B4}}{\rho_{B5} / \rho_{B6}} \qquad NDRE = \frac{\rho_{B8A} - \rho_{B5}}{\rho_{B8A} + \rho_{B5}} \qquad MNDWI = \frac{\rho_{B3} - \rho_{B11}}{\rho_{B3} + \rho_{B11}}$$

$$NDMI = \frac{\rho_{B8} - \rho_{B11}}{\rho_{B8} + \rho_{B11}} \qquad NDBI = \frac{\rho_{B11} - \rho_{B8}}{\rho_{B11} + \rho_{B8}} \qquad NBR = \frac{\rho_{B8} - \rho_{B12}}{\rho_{B8} + \rho_{B12}}$$

$$GVS = \frac{100 \times NDVI}{100|NDVI| + 100|NBR| + 1} \qquad NDFI = \frac{GVS - (1 - NDVI)}{GVS + (1 - NDVI)}$$

---

## Land Cover Palette Schemes

Color swatches below are rendered as inline SVG — visible on GitHub and most Markdown renderers.

---

### 🇮🇩 KLHK — Indonesian Ministry of Environment and Forestry

| ID | Class Name | Swatch | Hex |
|:--:|-----------|:------:|-----|
| 1 | Hutan Lahan Kering Primer | ![](https://placehold.co/28x16/60E663/60E663.png) | `#60E663` |
| 2 | Hutan Lahan Kering Sekunder | ![](https://placehold.co/28x16/72FF00/72FF00.png) | `#72FF00` |
| 3 | Hutan Mangrove Primer | ![](https://placehold.co/28x16/8EA704/8EA704.png) | `#8EA704` |
| 4 | Hutan Mangrove Sekunder | ![](https://placehold.co/28x16/C1A700/C1A700.png) | `#C1A700` |
| 5 | Hutan Rawa Primer | ![](https://placehold.co/28x16/60E663/60E663.png) | `#60E663` |
| 6 | Hutan Rawa Sekunder | ![](https://placehold.co/28x16/72FF00/72FF00.png) | `#72FF00` |
| 7 | Hutan Tanaman | ![](https://placehold.co/28x16/D3E598/D3E598.png) | `#D3E598` |
| 8 | Semak Belukar | ![](https://placehold.co/28x16/EBC0A7/EBC0A7.png) | `#EBC0A7` |
| 9 | Semak Belukar Rawa | ![](https://placehold.co/28x16/EBC0A7/EBC0A7.png) | `#EBC0A7` |
| 10 | Pertanian Lahan Kering | ![](https://placehold.co/28x16/F6FFA7/F6FFA7.png) | `#F6FFA7` |
| 11 | Pertanian Lahan Kering Campur | ![](https://placehold.co/28x16/EDF500/EDF500.png) | `#EDF500` |
| 12 | Sawah | ![](https://placehold.co/28x16/A8D6FF/A8D6FF.png) | `#A8D6FF` |
| 13 | Tambak | ![](https://placehold.co/28x16/7AF4F4/7AF4F4.png) | `#7AF4F4` |
| 14 | Permukiman Transmigrasi | ![](https://placehold.co/28x16/728EA7/728EA7.png) | `#728EA7` |
| 15 | Perkebunan | ![](https://placehold.co/28x16/E5D298/E5D298.png) | `#E5D298` |
| 16 | Permukiman | ![](https://placehold.co/28x16/686868/686868.png) | `#686868` |
| 17 | Bandara / Pelabuhan | ![](https://placehold.co/28x16/D60073/D60073.png) | `#D60073` |
| 18 | Lahan Terbuka | ![](https://placehold.co/28x16/D60073/D60073.png) | `#D60073` |
| 19 | Pertambangan | ![](https://placehold.co/28x16/A70400/A70400.png) | `#A70400` |
| 20 | Badan Air | ![](https://placehold.co/28x16/D4FCF7/D4FCF7.png) | `#D4FCF7` |
| 21 | Rawa | ![](https://placehold.co/28x16/98E5E5/98E5E5.png) | `#98E5E5` |
| 22 | Savana / Padang Rumput | ![](https://placehold.co/28x16/D5FF02/D5FF02.png) | `#D5FF02` |
| 23 | Awan | ![](https://placehold.co/28x16/D1D1D1/D1D1D1.png) | `#D1D1D1` |

---

### 🌿 MapBiomas Indonesia — Collection 3.0

| ID | Class Name | Swatch | Hex |
|:--:|-----------|:------:|-----|
| 3 | Formasi Hutan | ![](https://placehold.co/28x16/1f8d49/1f8d49.png) | `#1f8d49` |
| 5 | Mangrove | ![](https://placehold.co/28x16/04381d/04381d.png) | `#04381d` |
| 76 | Hutan Rawa Gambut | ![](https://placehold.co/28x16/2f7360/2f7360.png) | `#2f7360` |
| 13 | Tumbuhan Non-Hutan Lainnya | ![](https://placehold.co/28x16/d89f5c/d89f5c.png) | `#d89f5c` |
| 40 | Sawah | ![](https://placehold.co/28x16/c71585/c71585.png) | `#c71585` |
| 35 | Sawit | ![](https://placehold.co/28x16/9065d0/9065d0.png) | `#9065d0` |
| 9 | Kebun Kayu | ![](https://placehold.co/28x16/7a5900/7a5900.png) | `#7a5900` |
| 21 | Pertanian Lainnya | ![](https://placehold.co/28x16/ffefc3/ffefc3.png) | `#ffefc3` |
| 30 | Lubang Tambang | ![](https://placehold.co/28x16/9c0027/9c0027.png) | `#9c0027` |
| 24 | Permukiman | ![](https://placehold.co/28x16/d4271e/d4271e.png) | `#d4271e` |
| 25 | Non-Vegetasi Lainnya | ![](https://placehold.co/28x16/db4d4f/db4d4f.png) | `#db4d4f` |
| 31 | Tambak | ![](https://placehold.co/28x16/091077/091077.png) | `#091077` |
| 33 | Sungai, Danau, Laut | ![](https://placehold.co/28x16/2532e4/2532e4.png) | `#2532e4` |

---

### 🇺🇸 NLCD — National Land Cover Database (USGS)

| ID | Class Name | Swatch | Hex |
|:--:|-----------|:------:|-----|
| 11 | Open Water | ![](https://placehold.co/28x16/466b9f/466b9f.png) | `#466b9f` |
| 12 | Perennial Ice/Snow | ![](https://placehold.co/28x16/d1def8/d1def8.png) | `#d1def8` |
| 21 | Developed, Open Space | ![](https://placehold.co/28x16/dec5c5/dec5c5.png) | `#dec5c5` |
| 22 | Developed, Low Intensity | ![](https://placehold.co/28x16/d99282/d99282.png) | `#d99282` |
| 23 | Developed, Medium Intensity | ![](https://placehold.co/28x16/eb0000/eb0000.png) | `#eb0000` |
| 24 | Developed, High Intensity | ![](https://placehold.co/28x16/ab0000/ab0000.png) | `#ab0000` |
| 31 | Barren Land | ![](https://placehold.co/28x16/b3ac9f/b3ac9f.png) | `#b3ac9f` |
| 41 | Deciduous Forest | ![](https://placehold.co/28x16/68ab5f/68ab5f.png) | `#68ab5f` |
| 42 | Evergreen Forest | ![](https://placehold.co/28x16/1c5f2c/1c5f2c.png) | `#1c5f2c` |
| 43 | Mixed Forest | ![](https://placehold.co/28x16/b5c58f/b5c58f.png) | `#b5c58f` |
| 51 | Dwarf Scrub | ![](https://placehold.co/28x16/af963c/af963c.png) | `#af963c` |
| 52 | Shrub/Scrub | ![](https://placehold.co/28x16/ccb879/ccb879.png) | `#ccb879` |
| 71 | Grassland/Herbaceous | ![](https://placehold.co/28x16/dfdfc2/dfdfc2.png) | `#dfdfc2` |
| 72 | Sedge/Herbaceous | ![](https://placehold.co/28x16/d1d182/d1d182.png) | `#d1d182` |
| 73 | Lichens | ![](https://placehold.co/28x16/a3cc51/a3cc51.png) | `#a3cc51` |
| 74 | Moss | ![](https://placehold.co/28x16/82ba9e/82ba9e.png) | `#82ba9e` |
| 81 | Pasture/Hay | ![](https://placehold.co/28x16/dcd939/dcd939.png) | `#dcd939` |
| 82 | Cultivated Crops | ![](https://placehold.co/28x16/ab6c28/ab6c28.png) | `#ab6c28` |
| 90 | Woody Wetlands | ![](https://placehold.co/28x16/b8d9eb/b8d9eb.png) | `#b8d9eb` |
| 95 | Emergent Herbaceous Wetlands | ![](https://placehold.co/28x16/6c9fb8/6c9fb8.png) | `#6c9fb8` |

---

## Tips and Troubleshooting

### General Tips

- **Test with a small ROI first** before processing large areas to avoid computation time-outs.
- **Use Cloud Score+** as the primary masking method for tropical regions like Indonesia, where thin cirrus and coastal aerosols are common.
- **For mangrove studies**, use Median Dry Season composite to maximize spectral contrast between mangrove canopy and aquaculture ponds (*tambak*).
- **Distribute samples spatially** across the study area. Avoid concentrating all samples in one geographic location.
- **For SVM with RBF kernel**, perform a manual grid search over `C` and `gamma` before the final classification run.

### Common Issues

| Error / Issue | Solution |
|---------------|----------|
| `"Computation timed out"` | Reduce ROI extent; increase `scale` to 20 or 30 m; shorten the date range |
| `"Not enough pixels in region"` | Use 10 m scale or enlarge the sample polygon area |
| OA very low (< 70%) | Check sample placement; avoid transitional zones; add more samples; merge spectrally similar classes |
| Class missing from output | Ensure all classes have drawn polygons before clicking Run Classification |
| Error loading ROI from asset | Verify full asset path; asset must be `FeatureCollection`; check sharing/access settings |
| Map layer not appearing | Open Layer Manager (top-right of map); enable all layers; zoom out if ROI is small |

---

## Full Script Repository

**[https://code.earthengine.google.com/328e48a66c1f2b0a9268cbce3327b9df](https://code.earthengine.google.com/328e48a66c1f2b0a9268cbce3327b9df)**

### Default Configuration (`CFG` object)

```javascript
var CFG = {
  startDate:         '2024-01-01',
  endDate:           '2024-12-31',
  cloudMax:          20,
  classProp:         'lc',
  seed:              42,
  scale:             10,
  maxPix:            1e13,
  splitRatio:        0.7,
  // Random Forest
  rf_numTrees:       500,
  rf_minLeaf:        1,
  rf_bagFraction:    0.5,
  // Gradient Tree Boost
  gtb_numTrees:      200,
  gtb_shrinkage:     0.05,
  gtb_samplingRate:  0.7,
  gtb_maxNodes:      5,
  gtb_loss:          'LeastAbsoluteDeviation',
  // Support Vector Machine
  svm_kernel:        'RBF',
  svm_gamma:         0.5,
  svm_cost:          10,
  svm_degree:        3,
  svm_coef:          0.0
};
```

### Cloud Masking Functions

```javascript
function maskByCSPlus(image) {
  return image.updateMask(image.select('cs_cdf').gte(0.60));
}

function maskBySCL(image) {
  var scl = image.select('SCL');
  return image.updateMask(
    scl.neq(3).and(scl.neq(7)).and(scl.neq(8))
       .and(scl.neq(9)).and(scl.neq(10)).and(scl.neq(11))
  );
}

function maskByQA60(image) {
  var qa = image.select('QA60');
  return image.updateMask(
    qa.bitwiseAnd(1 << 10).eq(0).and(qa.bitwiseAnd(1 << 11).eq(0))
  );
}
```

### Export Configuration

```javascript
Export.image.toDrive({
  image:          STATE.classifiedImg,
  description:    'LandCover_DFRF_V3',
  folder:         'GEE_Export',
  fileNamePrefix: 'LandCover_DFRF_V3',
  region:         STATE.roi.geometry(),
  scale:          10,           // options: 10, 20, 30
  crs:            'EPSG:4326',
  maxPixels:      1e13,
  fileFormat:     'GeoTIFF'
});
```

---

## Scientific References

Auriga Nusantara. (2024). Algorithm Theoretical Basis Document (ATBD) MapBiomas Indonesia Koleksi 3 Versi 1. MapBiomas Indonesia.

Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32.

Cardille, J. A., Crowley, M. A., Saah, D., & Clinton, N. E. (Eds.). (2024). Cloud-based remote sensing with Google Earth Engine: Fundamentals and applications. Springer International Publishing. https://doi.org/10.1007/978-3-031-26588-4

Cortes, C., & Vapnik, V. (1995). Support-vector networks. Machine Learning, 20(3), 273–297.

Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. Annals of Statistics, 29(5), 1189–1232.

Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. Remote Sensing of Environment, 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031

Kementerian Lingkungan Hidup dan Kehutanan Republik Indonesia. (2024). Keputusan Menteri Lingkungan Hidup dan Kehutanan Nomor 399 Tahun 2024 tentang Standar Penyebarluasan Informasi Geospasial Tematik Lingkup KLHK. KLHK.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33(1), 159–174.

Pasquarella, V. J., Brown, C. F., Czerwinski, W., & Rucklidge, W. J. (2023). Comprehensive quality assessment of optical satellite imagery using weakly supervised video learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 2125–2135). https://doi.org/10.1109/CVPRW59228.2023.00206

U.S. Geological Survey. (2025). Annual National Land Cover Database (NLCD) Collection 1 Science Product User Guide (Version 1.1). USGS.

U.S. Geological Survey. (n.d.). National Land Cover Database (NLCD) class legend and description. USGS.




This tool is released for academic and educational use. All imagery access is subject to [Google Earth Engine Terms of Service](https://earthengine.google.com/terms/) and Copernicus Sentinel-2 data policies.
