---
title: "Map-Layout-Geopandas"
---

[Repositori di GitHub](https://github.com/Defani/Map-Layout-Geopandas)

## 📌 Overview

This repository demonstrates a **map layout and cartographic visualization workflow** using **GeoPandas**.  
The focus of this project is not only spatial plotting, but also **map layout composition** following basic cartographic principles for clear and effective visual communication.

The full workflow is implemented in a **Google Colab notebook**, allowing users to run the code without local setup.

---

## 🚀 Open Notebook in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/Defani/fc53e43363d02a51555acc02e174d397/map-layout.ipynb)

---

## 🧭 Script Workflow Explanation

Below is an overview of what is included in the script and what each part does.

---

### 1️⃣ Library Imports 📦

This section loads the core Python libraries required for geospatial analysis and visualization.

Main purposes:
- Enable spatial data handling
- Prepare plotting and layout customization
- Support cartographic visualization

Key libraries include **GeoPandas** and **Matplotlib**.

---

### 2️⃣ Spatial Data Loading 🗺️

The script reads spatial vector data into a **GeoDataFrame**.

At this stage:
- Geometry (polygon, line, or point) is initialized
- Attribute data becomes available for styling and labeling
- The study area is defined

This step forms the **foundation of the map**.

---

### 3️⃣ Coordinate Reference System (CRS) Handling 🌍

The script checks and manages the **CRS** to ensure spatial accuracy.

Why this matters:
- Correct distance and scale representation
- Proper alignment between spatial layers
- Valid cartographic layout

If needed, reprojection is applied.

---

### 4️⃣ Base Map Plotting 🎨

This part creates the main plotting canvas:

- Figure and axis are defined
- The main spatial layer is rendered
- Basic color, edge, and transparency settings are applied

The result is a **clean base map** ready for layout elements.

---

### 5️⃣ Thematic Styling 🎯

Styling is applied to improve map readability and meaning:

- Color schemes based on attributes
- Line width and opacity adjustments
- Visual contrast enhancement

This step turns raw spatial data into a **thematic map**.

---

### 6️⃣ Map Layout Components 🧩

This is the core cartographic section of the script.

Included layout elements:
- 🏷️ Map title
- 📑 Legend
- 📏 Scale bar
- 🧭 North arrow
- ❌ Axis removal for a cleaner look

These elements transform a plot into a **proper map layout**.

---

### 7️⃣ Annotation and Labeling ✍️

Additional information is added through text annotations, such as:
- Area names
- Notes or descriptions
- Supporting contextual information

The goal is clarity without visual clutter.

---

### 8️⃣ Exporting the Output 💾

The final map is exported as an image file:

- High-resolution output
- Ready for reports, presentations, or portfolios
- Suitable for academic and professional use

---

## 🛠️ Tools and Technologies

- **Python**
- **GeoPandas**
- **Matplotlib**
- **Google Colab**
- **GIS & cartographic principles**

---

## 🎯 Use Cases

- GIS and remote sensing coursework
- Forestry and environmental mapping
- Map layout reference using Python
- Portfolio demonstration of spatial visualization skills

---

## 👤 Author

**Defani Arman Alfitriansyah**  
Forestry Student | GIS & Remote Sensing  
Interested in spatial analysis, cartography, and visual communication of geospatial data.

---

## 📝 Notes

This project emphasizes **map layout quality and cartographic clarity**,  
not merely spatial analysis output.  
Users are encouraged to adapt the layout structure for their own datasets.
