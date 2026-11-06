---
title: "Normalized-Difference-Water-Index-GEE"
---

[Repositori di GitHub](https://github.com/Defani/Normalized-Difference-Water-Index-GEE)

![GEE](https://img.shields.io/badge/Platform-Google_Earth_Engine-green)
![JavaScript](https://img.shields.io/badge/Language-JavaScript-yellow)

Analisis **Normalized Difference Water Index (NDWI)** berbasis **Google Earth Engine (GEE)** menggunakan citra **Sentinel-2 Surface Reflectance** untuk **monitoring badan air** dan **perhitungan luas perairan** secara otomatis.

---

## 📌 Deskripsi Singkat

NDWI (*Normalized Difference Water Index*) adalah indeks spektral yang dikembangkan oleh **McFeeters (1996)** untuk mendelineasi badan air terbuka dengan memanfaatkan reflektansi **band hijau (Green)** dan **near-infrared (NIR)**.

Metode ini efektif untuk:

- 🔍 **Ekstraksi badan air**
- ☁️ **Reduksi pengaruh vegetasi dan tanah**
- 📐 **Perhitungan luas perairan (hektar)**
- 🗺️ **Konversi raster ke vektor**

---

## 🧮 Formula NDWI

Persamaan matematis untuk NDWI adalah sebagai berikut:

$$
NDWI = \frac{Green - NIR}{Green + NIR}
$$

Pada sensor Sentinel-2:
- **Green** : Band 3 (B3)
- **NIR** : Band 8 (B8)

---

## 🛰️ Data & Platform

- **Data** : Sentinel-2 SR Harmonized
- **Resolusi** : 10 meter
- **Platform** : Google Earth Engine
- **Bahasa** : JavaScript

---

## ⚙️ Alur Analisis

1. ☁️ Cloud masking menggunakan **Scene Classification Layer (SCL)**.
2. 📆 Filter waktu dan batas persentase tutupan awan.
3. 🧩 Komposit citra (menggunakan nilai median).
4. 🌊 Kalkulasi indeks NDWI.
5. 🎚️ Thresholding NDWI (`> 0.009`).
6. 📏 Perhitungan luas badan air (dalam satuan hektar).
7. 🧱 Konversi data raster menjadi vektor (polygon).

---

## 🎨 Visualisasi

*(Catatan: Tambahkan screenshot hasil analisis GEE Anda di bawah ini dengan mengganti tautan gambarnya)*
- Komposit Sentinel-2 **11-8-2**
- NDWI dengan palet warna gradasi
- Masking area air
- Layer vektor badan air

---

## 🚀 Cara Menggunakan

1. Buka [Google Earth Engine Code Editor](https://code.earthengine.google.com/).
2. Buka dan salin skrip dari file [`NDWI GEE (1).txt`](https://github.com/Defani/Normalized-Difference-Water-Index-GEE/blob/main/NDWI%20GEE%20(1).txt) yang ada di repositori ini.
3. Pastikan variabel **`geometry`** sudah didefinisikan pada peta Anda sebagai *Area of Interest*.
4. Klik tombol **Run** ▶️.
5. Cek hasil visualisasi di kanvas peta dan output luasan di tab **Console**.

---

## 🧑‍💻 Author

**Defani Arman Alfitriansyah** 🎓 Fakultas Kehutanan dan Lingkungan – Universitas Kuningan  
📧 Email: 20220710063@uniku.ac.id

---

## 📚 Referensi

- McFeeters, S.K. (1996). *The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features*.
- Gao, B. (1996). *NDWI—A normalized difference water index for remote sensing of vegetation liquid water*.
- Cardille et al. (2024). *Cloud-Based Remote Sensing with Google Earth Engine*. Springer.

---

✨ *Feel free to fork, modify, and use this script for research or learning purposes.*
