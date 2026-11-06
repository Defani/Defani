---
title: "Download-Landsat-8-SR-Google-Earth-Engine"
---

[Repositori di GitHub](https://github.com/Defani/Download-Landsat-8-SR-Google-Earth-Engine)

Repository ini berisi script Google Earth Engine (GEE) untuk pengolahan citra Landsat 8 Collection 2 Level-2 (Surface Reflectance), meliputi cloud masking, scaling reflektansi, visualisasi false color, dan export band per band ke Google Drive 🛰️

🔗 Earth Engine Script  
https://code.earthengine.google.com/4ac276892842c267f1e13843fdbe781d

---

## 📌 Fitur
- ☁️ Cloud, shadow, dan cirrus masking menggunakan QA_PIXEL  
- 🛰️ Komposit median Landsat 8 Surface Reflectance  
- 🎨 False Color Composite (SWIR1–NIR–Blue)  
- 📤 Export setiap band secara terpisah  
- 🗺️ Output CRS: EPSG:4326  

---

## 🛰️ Dataset
**Landsat 8 Collection 2 Tier 1 Level-2**  
ID: `LANDSAT/LC08/C02/T1_L2`

Band yang digunakan:
- SR_B1 (Coastal)
- SR_B2 (Blue)
- SR_B3 (Green)
- SR_B4 (Red)
- SR_B5 (NIR)
- SR_B6 (SWIR1)
- SR_B7 (SWIR2)

---

## ☁️ Cloud Masking
Masking berbasis band QA_PIXEL untuk menghilangkan:
- Cloud  
- Cloud shadow  
- Cirrus  

Pendekatan ini memastikan hanya piksel valid yang digunakan dalam analisis.

---

## 🔢 Scaling Surface Reflectance
Scaling reflektansi mengikuti faktor resmi Landsat 8:

Reflectance = (DN × 0.0000275) − 0.2

Diterapkan pada seluruh band reflektansi (SR_B1–SR_B7).

---

## 🎨 Visualisasi
False Color Composite:
- Red   → SR_B6 (SWIR1)  
- Green → SR_B5 (NIR)  
- Blue  → SR_B2 (Blue)  

Parameter:
- min: 0  
- max: 0.391  

---

## 📤 Export
Setiap band diekspor terpisah ke Google Drive dengan parameter:
- Folder: 2025  
- Region: AOI (geometry)  
- Resolusi: 30 meter  
- CRS: EPSG:4326  
- MaxPixels: 1e13  

Contoh nama file:
LANDSAT8_SR_SR_B5.tif

---

## 🧠 Kegunaan
Cocok untuk:
- Analisis indeks spektral (NDVI, NDWI, NDBI, dll)
- Klasifikasi tutupan lahan
- Analisis kehutanan dan lingkungan
- Pre-processing data Landsat 8

---

## 👤 Author
**Defani**  
Remote Sensing & GIS Enthusiast 🌱  
Google Earth Engine | Spatial Analysis | Environmental Mapping

---

## ⭐ Catatan
Jika repository ini bermanfaat, silakan beri ⭐ di GitHub  
Feel free untuk fork dan modifikasi sesuai kebutuhan 🚀
