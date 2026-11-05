---
title: "S2-CLOUD-MASK-COMPARISON-TNGC"
---

Notebook ini membandingkan empat algoritma cloud masking pada citra Sentinel-2 di wilayah Gunung Cereme, Jawa Barat, menggunakan Google Earth Engine (GEE).

[Repositori di GitHub](https://github.com/Defani/S2-CLOUD-MASK-COMPARISON-TNGC)

Notebook ini membandingkan empat algoritma cloud masking pada citra Sentinel-2 di wilayah **Gunung Cereme, Jawa Barat**, menggunakan Google Earth Engine (GEE).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yX0P9vs-MDTNGESFNGK4H0ADZPfMRe6z?usp=sharing)

---

## 📋 Deskripsi

Studi ini bertujuan untuk mengevaluasi seberapa efektif masing-masing metode cloud masking dalam menghilangkan piksel berawan dari komposit median Sentinel-2. Pendekatan yang digunakan adalah membandingkan kecerahan (brightness) hasil tiap algoritma terhadap **Cloud Score Plus (CS+)** sebagai baseline — metode yang dianggap paling bersih. Piksel yang secara signifikan lebih terang dari CS+ dianggap sebagai sisa awan yang tidak terdeteksi.

Periode pengamatan: **1 Mei 2025 – 30 Mei 2026**  
Area studi: **Gunung Cereme**, Kuningan–Majalengka, Jawa Barat  
ROI (Region of Interest): Asset GEE `projects/ee-defaniarman/assets/cereme`

---

## 🛰️ Data yang Digunakan

| Dataset | ID Google Earth Engine |
|---|---|
| Sentinel-2 SR Harmonized | `COPERNICUS/S2_SR_HARMONIZED` |
| Cloud Score Plus | `GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED` |
| S2 Cloud Probability | `COPERNICUS/S2_CLOUD_PROBABILITY` |

---

## 🔬 Algoritma yang Dibandingkan

### (a) QA60 Bitmask
Menggunakan band `QA60` bawaan Sentinel-2. Piksel dianggap berawan jika bit 10 (awan opak) atau bit 11 (cirrus) bernilai 1.

```python
def apply_qa(img):
    qa = img.select('QA60')
    mask = qa.bitwiseAnd(1 << 10).eq(0).And(qa.bitwiseAnd(1 << 11).eq(0))
    return img.updateMask(mask)
```

### (b) Scene Classification Layer (SCL)
Menggunakan band `SCL` dari produk Sentinel-2 SR. Piksel dengan nilai SCL 3 (shadow), 7 (unclassified), 8 (medium cloud), 9 (high cloud), 10 (thin cirrus), dan 11 (snow) di-mask.

```python
def apply_scl(img):
    scl = img.select('SCL')
    mask = scl.neq(3).And(scl.neq(7)).And(scl.neq(8)) \
              .And(scl.neq(9)).And(scl.neq(10)).And(scl.neq(11))
    return img.updateMask(mask)
```

### (c) Cloud Score Plus (CS+) *(Baseline)*
Menggunakan `cs_cdf` dari koleksi Cloud Score Plus. Piksel dengan nilai `cs_cdf ≥ 0.60` dianggap cukup bersih untuk dipertahankan.

```python
def apply_csplus(img):
    return img.updateMask(img.select('cs_cdf').gte(0.60))
```

### (d) s2cloudless Probability
Menggunakan koleksi `COPERNICUS/S2_CLOUD_PROBABILITY`. Piksel dengan probabilitas awan `< 65%` dipertahankan.

```python
def apply_s2c(img):
    return img.updateMask(img.select('probability').lt(65))
```

---

## 🧠 Metode Deteksi Sisa Awan

Untuk setiap algoritma, sisa awan (cloud leakage) dideteksi dengan cara:

1. Membuat komposit median dari koleksi yang sudah di-mask.
2. Menghitung rata-rata kecerahan RGB (`reduce(ee.Reducer.mean())`).
3. Membandingkan kecerahan tiap algoritma dengan kecerahan baseline CS+.
4. Piksel yang **lebih terang > 5% (0.05)** dari CS+ ditandai sebagai sisa awan.

```python
is_leftover = algo_brightness.subtract(cs_brightness).gt(0.05)
```

---

## 🗺️ Hasil Visualisasi

### Citra Asli Sebelum Masking

Komposit median Sentinel-2 tanpa cloud masking, menampilkan awan yang menutupi sebagian besar wilayah Gunung Cereme.

![Unmasked Sentinel-2](https://raw.githubusercontent.com/Defani/S2-CLOUD-MASK-COMPARISON-TNGC/main/Unmasked_Sentinel2_Cereme.png)

---

### Komparasi Sisa Awan (Highlight Merah)

Sisa awan yang lolos dari tiap algoritma ditampilkan dengan **warna merah**. Semakin sedikit area merah, semakin efektif algoritma tersebut.

![Komparasi Sisa Awan (RGB)](https://raw.githubusercontent.com/Defani/S2-CLOUD-MASK-COMPARISON-TNGC/main/Komparasi_Sisa_Awan_Cereme.png)

---

### Komparasi Sisa Awan (Peta Biner + Legenda)

Versi biner: piksel awan sisa ditampilkan **hitam**, area bersih ditampilkan **abu-abu**.

![Komparasi Sisa Awan (Biner)](https://raw.githubusercontent.com/Defani/S2-CLOUD-MASK-COMPARISON-TNGC/main/Komparasi_Sisa_Awan_AbuItem_Cereme_with_Legend.png)

---

## 📊 Ringkasan Hasil

| Algoritma | Sisa Awan Terdeteksi | Keterangan |
|---|---|---|
| QA60 Bitmask | 🔴 Tinggi | Banyak sisa awan, terutama di selatan dan barat |
| SCL | 🟡 Sedang | Lebih baik dari QA60, masih ada kebocoran |
| Cloud Score Plus (CS+) | ✅ Rendah | Baseline; hasil terbersih |
| s2cloudless | 🟡 Sedang | Sebanding dengan SCL, kebocoran di bagian tengah |

---

## ⚙️ Cara Menjalankan

1. Buka notebook di Google Colab:  
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yX0P9vs-MDTNGESFNGK4H0ADZPfMRe6z?usp=sharing)

2. Jalankan instalasi dependensi (Cell 1):
   ```bash
   pip install geemap cartopy matplotlib earthengine-api
   ```

3. Autentikasi Google Earth Engine:
   ```python
   ee.Authenticate()
   ee.Initialize(project='your-project-id')
   ```

4. Jalankan seluruh cell secara berurutan.

---

## 📦 Dependensi

```
earthengine-api
geemap
matplotlib
cartopy
```

---

## 📁 Struktur Repositori

```
📦 cloud-masking-cereme/
 ┣ 📓 Untitled60.ipynb          # Notebook utama
 ┣ 📄 README.md
 ┗ 📁 images/
    ┣ 🖼️ Unmasked_Sentinel2_Cereme.png
    ┣ 🖼️ Komparasi_Sisa_Awan_Cereme.png
    ┗ 🖼️ Komparasi_Sisa_Awan_AbuItem_Cereme_with_Legend.png
```

---

## 👤 Author

**Defani Arman**  
Google Earth Engine Project: `ee-defaniarman`
