---
title: "EE-SPECTRAL-EXPLORATION"
---

A Google Earth Engine (GEE) GUI Application for Multi-Sensor Vegetation Index Computation, Thresholding, Area Statistics, and Export Developed by Defani Arman Alfitriansyah — Faculty of Forestry and Environment, Universitas Kuningan

[Repositori di GitHub](https://github.com/Defani/EE-SPECTRAL-EXPLORATION)

> **A Google Earth Engine (GEE) GUI Application for Multi-Sensor Vegetation Index Computation, Thresholding, Area Statistics, and Export**
> 
> Developed by **Defani Arman Alfitriansyah** — Faculty of Forestry and Environment, Universitas Kuningan

---

## 📌 Overview

This application provides a fully interactive, panel-based GUI within the Google Earth Engine Code Editor for computing spectral indices from Sentinel-2, Landsat 8, and Landsat 9 surface reflectance imagery. The tool is designed to support remote sensing research workflows including vegetation mapping, mangrove monitoring, biomass estimation proxies, and land cover analysis.

**Key capabilities:**
- Multi-sensor support (Sentinel-2 SR, Landsat 8 SR, Landsat 9 SR)
- 40+ built-in spectral indices including red-edge, chlorophyll, water, and burn indices
- Three computation modes: Ready-Use Index, Normalized Difference, and Raster Calculator
- Live palette selection with reverse option (20 colour palettes)
- Dynamic thresholding with single-bound or range-based masking
- Pixel-area statistics for masked regions (in Hectares)
- Export to Google Drive or GEE Asset

---

## 🔗 Access the Application

> **Open the script directly in the GEE Code Editor:**

[![Open in GEE](https://img.shields.io/badge/Open%20in-Google%20Earth%20Engine-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://code.earthengine.google.com/855c2692093e0ff2901447b2b9cb7814?hl=id)

```
https://code.earthengine.google.com/855c2692093e0ff2901447b2b9cb7814?hl=id
```

> ⚠️ A **Google Earth Engine account** is required. Register at [earthengine.google.com](https://earthengine.google.com) if you do not have access.

---

## 🖥️ Interface Layout

The interface is divided into three panels:

| Panel | Location | Function |
|---|---|---|
| **Left Panel** | Left side | Colour palette, thresholding, area statistics, legend |
| **Map Panel** | Centre | Interactive satellite basemap with rendered layers |
| **Right Panel** | Right side | All data controls: AOI, sensor, date, index, export |

> 💡 **All analysis controls are on the RIGHT panel. Visual and display controls are on the LEFT panel.**

---

## 🚀 Step-by-Step Usage Guide

Follow the numbered steps below. Replace GIF placeholders with your own screen recordings.

---

### Step 1 — Open the Script

1. Click the GEE link above to open the script in the Code Editor
2. Click **▶ Run** (top of the Code Editor) to initialize the GUI
3. The interface loads with a three-panel layout; the map defaults to a satellite view centred on Indonesia



https://github.com/user-attachments/assets/ebbc7870-fe27-49e6-b51c-e2efb3523152



### Step 2 — Define an Area of Interest (AOI)

You have two options:

**Option A — Draw on the map (Right Panel → Section 1):**
1. Click **⬟ Draw Polygon** or **⬛ Draw Rectangle**
2. Click on the map to draw your study area
3. Complete the shape; the AOI is saved automatically and the boundary is hidden



https://github.com/user-attachments/assets/dd9b2209-b2e6-4919-800d-3f66b01c7720


**Option B — Load a GEE Asset (Right Panel → Section 2):**
1. Paste your uploaded GEE Asset ID into the text box (e.g., `projects/your-project/assets/your-shapefile`)
2. Click **⬆ Load Asset as AOI**
3. The asset boundary will be displayed in orange on the map



https://github.com/user-attachments/assets/a6e534c4-95b3-487c-8f91-c2e5852d3a32


### Step 3 — Configure Sensor and Date Range

In the **Right Panel → Section 3 — Sensor & Date Range:**

1. **Select Sensor** from the dropdown:
   - `Sentinel-2 SR` — 10 m resolution, red-edge bands available (B5, B6, B7, B8A)
   - `Landsat 8 SR` — 30 m resolution, OLI/TIRS bands
   - `Landsat 9 SR` — 30 m resolution, improved OLI-2 radiometry

2. **Set the time period** — enter Start Date and End Date in `YYYY-MM-DD` format

3. **Adjust Max Cloud Cover** using the slider (default: 20%)

4. **Cloud masking** — check *Apply Automatic Cloud Masking* and select the method:
   - For Sentinel-2: `Cloud Score+ (CS+)` *(recommended)*, `SCL`, or `QA60`
   - For Landsat: `QA_PIXEL — Landsat Bitmask`


https://github.com/user-attachments/assets/54f5547b-73e7-4361-a907-0890546305af


### Step 4 — Select or Define a Spectral Index

In the **Right Panel → Section 4 — Spectral Calculator**, choose one of three modes:

**Mode 1 — Ready-Use Index (recommended for standard indices):**
- Select the desired index from the dropdown list (40+ indices available)
- The formula is automatically resolved to the correct sensor bands

**Mode 2 — Normalized Difference:**
- Manually select Band A and Band B
- Computes `(A − B) / (A + B)`

**Mode 3 — Raster Calculator:**
- Build a custom arithmetic expression using the on-screen numpad
- Use band names (e.g., `B8`, `B4`), operators (`+`, `-`, `*`, `/`, `sqrt()`), and parentheses
- Click any **Index button** in the quick-insert panel to embed a ready-use formula into your expression

---

*📷 Insert GIF here: Selecting NDVI from Mode 1 dropdown, then switching to Mode 3 and building a custom expression*

```
![Step 4 - Select Index](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step4_select_index.gif)
```

---

### Step 5 — Run Analysis and Render the Map

In the **Right Panel → Section 5 — Execute Analysis & Render:**

1. Enter a descriptive name in the **Output layer name** field (e.g., `NDVI_Mangrove_2023`)
2. Click **▶ RUN ANALYSIS** — this computes the median composite and the selected index over your AOI
3. Wait for the status bar (top right) to confirm `✔ Analysis complete`
4. Click **👁 RENDER MAP** to display the result on the map

> The map will show both the **True Color composite** (hidden by default, toggle via Layer Control) and the **index layer** with automatic stretch.

---

*📷 Insert GIF here: Clicking RUN ANALYSIS, waiting for status confirmation, then clicking RENDER MAP*

```
![Step 5 - Run and Render](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step5_run_render.gif)
```

---

### Step 6 — Adjust Colour Palette and Visualization

In the **Left Panel → Colour Palette:**

1. Scroll through the palette list and click any palette name to apply it instantly (e.g., `NDVI_Custom`, `RdYlGn`, `Viridis`)
2. Check **Reverse Palette** to invert the colour ramp
3. The **Legend** at the bottom of the left panel updates automatically with the current min/max values

---

*📷 Insert GIF here: Clicking through different palettes and observing the map update*

```
![Step 6 - Palette Selection](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step6_palette.gif)
```

---

### Step 7 — Apply Thresholding (Optional)

In the **Left Panel → Enable Thresholding:**

1. Check **Enable Thresholding** to reveal the thresholding controls
2. Choose a mode:
   - **1 Criterion (Lower Bound)** — use the slider to mask all pixels *below* a threshold value (e.g., show only pixels with NDVI ≥ 0.4 to isolate dense vegetation)
   - **2 Criteria (Min & Max Range)** — enter a minimum and maximum value to retain only pixels within that range, then click **Apply Threshold**
3. The map updates in real-time to reflect the mask

---

*📷 Insert GIF here: Enabling thresholding, sliding the lower bound to isolate high-NDVI vegetation*

```
![Step 7 - Thresholding](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step7_threshold.gif)
```

---

### Step 8 — Calculate Area Statistics

In the **Left Panel → Area Statistics:**

1. After applying any threshold (optional), click **Calculate Masked Area**
2. The total area of unmasked (valid) pixels within the AOI is computed and displayed in **Hectares**

> This is particularly useful for estimating the spatial extent of mangrove canopy, dense vegetation, or any class defined by your threshold.

---

*📷 Insert GIF here: Clicking Calculate Masked Area and the result appearing in Hectares*

```
![Step 8 - Area Statistics](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step8_area.gif)
```

---

### Step 9 — Export Results

In the **Right Panel → Section 6 — Export:**

1. Select **Export Destination**: `Google Drive` or `GEE Asset`
2. Enter a **Task Name**, **File Name**, and **Folder Name** (or Asset Path)
3. Select **Export Scale** in metres per pixel (default: 10 m for Sentinel-2; use 30 m for Landsat)
4. Select **CRS** (default: `EPSG:4326`)
5. Click **⬇ SUBMIT EXPORT TASK**
6. Open the **Tasks tab** (▶ icon in the top-right of the Code Editor) and click **Run** next to your new task

---

*📷 Insert GIF here: Filling in export parameters, submitting the task, and opening the Tasks tab*

```
![Step 9 - Export](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step9_export.gif)
```

---

### Step 10 — Layer Control

In the **Right Panel → Section 7 — Layer Control:**

- A list of all rendered layers is displayed with checkboxes
- Toggle any layer on/off by checking or unchecking it
- The **True Color** composite is added at each render and can be toggled for visual reference

---

*📷 Insert GIF here: Toggling layers on and off using the Layer Control checkboxes*

```
![Step 10 - Layer Control](https://raw.githubusercontent.com/Defani/EE-SPECTRAL-EXPLORATION/main/assets/step10_layers.gif)
```

---

## 📐 Supported Spectral Indices

| Category | Indices |
|---|---|
| **Broadband Vegetation** | NDVI, EVI, EVI2, SAVI, MSAVI, MSAVI2, OSAVI, ARVI, VARI |
| **Simple & Transformed Ratios** | SR, TRVI, MSR_Red, RDVI, DVI, IPVI |
| **Green-band Indices** | GRVI, GNDVI, GCI, MSR_Green, GCVI, CVI |
| **Chlorophyll & Pigment** | CCI, GLI, NDYI, TGI, TriVI, SIPI, PRI, NNIR |
| **Water & Moisture** | NDWI (Gao), MNDWI (McFeeters) |
| **SWIR-based** | NBR, AFRI2100, SLAVI, CAI, NDBI, BSI |
| **Red-Edge (Sentinel-2 only)** | NDREI, RENDVI, CIRE, MCARI, MTCI, mRE-SR |

> 🔴 **Red-edge indices** require Sentinel-2 SR. They will not compute correctly with Landsat sensors due to the absence of red-edge bands.

---

## 🧰 Technical Notes

**Scaling and Reflectance Correction:**
- Sentinel-2: divided by 10,000 to convert DN to surface reflectance (0–1)
- Landsat 8/9: Collection 2 scaling applied — `SR × 0.0000275 + (−0.2)`

**Cloud Masking Methods (Sentinel-2):**
- `Cloud Score+`: Uses the `cs_cdf` band with a ≥ 0.60 threshold — recommended for most applications
- `SCL`: Masks classes 3, 7, 8, 9, 10, 11 (shadows, clouds, cirrus, snow)
- `QA60`: Bitmask masking for opaque cloud (bit 10) and cirrus (bit 11)

**Composite Method:**
- Temporal median composite across all filtered images within the specified date range

**Area Calculation:**
- Uses `ee.Image.pixelArea()` reduced over the AOI geometry
- Scale: 10 m (sufficient for Sentinel-2 outputs)

---

## 📁 Recommended Directory Structure for GIFs

```
your-repo/
├── README.md
├── assets/
│   ├── step1_open_script.gif
│   ├── step2_define_aoi.gif
│   ├── step3_sensor_date.gif
│   ├── step4_select_index.gif
│   ├── step5_run_render.gif
│   ├── step6_palette.gif
│   ├── step7_threshold.gif
│   ├── step8_area.gif
│   ├── step9_export.gif
│   └── step10_layers.gif
└── script/
    └── ee_spectral_explorer.js
```

---

## 📬 Contact

**Defani Arman Alfitriansyah**  
Faculty of Forestry and Environment  
Universitas Kuningan  

---

*Last updated: 2025*
