---
title: "LAND-COVER-CLASSIFICATION-RANDOM-FOREST-MULTI-INDEX"
---

Skrip ini melakukan klasifikasi tutupan lahan terbimbing (supervised) di Google Earth Engine (GEE) menggunakan citra Sentinel-2 Surface Reflectance dan pengklasifikasi Random Forest.

[Repositori di GitHub](https://github.com/Defani/LAND-COVER-CLASSIFICATION-RANDOM-FOREST-MULTI-INDEX)

### Google Earth Engine · Sentinel-2 SR · Random Forest · Indeks Spektral

[![GEE](https://img.shields.io/badge/Platform-Google%20Earth%20Engine-4285F4?logo=google&logoColor=white)](https://earthengine.google.com/)
[![Sentinel-2](https://img.shields.io/badge/Data-Sentinel--2%20SR-00A550)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)
[![Language](https://img.shields.io/badge/Bahasa-JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/Lisensi-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 👤 Informasi Penulis

| | |
|---|---|
| **Penulis** | Defani Arman Alfitriansyah |
| **Institusi** | Fakultas Kehutanan dan Lingkungan, Universitas Kuningan |
| **Tanggal** | 11 Maret 2026 |
| **Bahasa Pemrograman** | JavaScript (Google Earth Engine Code Editor) |

---

## 📋 Gambaran Umum

Skrip ini melakukan **klasifikasi tutupan lahan terbimbing (supervised)** di Google Earth Engine (GEE) menggunakan citra Sentinel-2 Surface Reflectance dan pengklasifikasi Random Forest. Skrip mengintegrasikan band multispektral dengan sembilan indeks spektral turunan untuk membedakan empat kelas tutupan lahan pada wilayah kajian yang ditentukan pengguna.

Alur kerja mencakup seluruh pipeline klasifikasi: masking awan → komposit citra → komputasi indeks spektral → stratifikasi sampel → pelatihan model → klasifikasi → visualisasi → ekspor.

---

## 🗂️ Struktur Repositori

```text
├── script.txt          # Skrip klasifikasi GEE utama
├── README.md           # Dokumentasi ini
└── Link GEE            # Link project GEE
```

## 🌏 Skrip Kode : [Klik di ini!](https://code.earthengine.google.com/cdb5d139bd16afd994164327997cf0ae?hl=id)
---

## ⚙️ Parameter

Seluruh parameter yang dapat dikonfigurasi dideklarasikan di bagian atas skrip untuk mendukung reprodusibilitas dan transparansi.

### Parameter Temporal & Penyaringan

| Parameter | Nilai Default | Keterangan |
|---|---|---|
| `START_DATE` | `'2024-01-01'` | Tanggal awal koleksi citra (format ISO 8601) |
| `END_DATE` | `'2026-03-02'` | Tanggal akhir koleksi citra (format ISO 8601) |
| `CLOUD_LIMIT` | `30` | Persentase tutupan awan maksimum yang diizinkan per scene (%) |
| `TRAIN_SPLIT` | `0.7` | Proporsi sampel untuk pelatihan (sisanya digunakan untuk validasi) |
| `CLASS_FIELD` | `'lc'` | Nama properti yang menyimpan label kelas pada koleksi fitur latih |

### Skema Kelas Tutupan Lahan

| Indeks Kelas | Nama Kelas | Warna Hex | Keterangan |
|---|---|---|---|
| `0` | Hutan | `#005F02` | Hutan kanopi rapat (vegetasi berkayu padat) |
| `1` | Semak | `#6D9E51` | Semak belukar / vegetasi terbuka |
| `2` | Lahan Terbuka | `#C0B87A` | Lahan gundul / tanah terbuka / lahan bera |
| `3` | Air | `#0992C2` | Badan air (sungai, danau, kolam) |

---

## 🛰️ Data Masukan

### Koleksi Sentinel-2 SR Harmonized

- **ID Koleksi:** `COPERNICUS/S2_SR_HARMONIZED`
- **Resolusi spasial:** 10 m (band tampak/NIR), 20 m (band red-edge/SWIR, di-resample ke 10 m oleh GEE)
- **Komposit temporal:** **Median** piksel dari seluruh akuisisi valid yang telah dimasking awan dalam rentang tanggal yang ditentukan
- **Skala radiometrik:** Nilai reflektans dibagi 10.000 untuk menghasilkan reflektans permukaan tanpa satuan dalam rentang [0, 1]

### Band Spektral yang Digunakan

| Band | Band Sentinel-2 | Panjang Gelombang Tengah (nm) | Resolusi Asli (m) |
|---|---|---|---|
| `B2` | Biru | 490 | 10 |
| `B3` | Hijau | 560 | 10 |
| `B4` | Merah | 665 | 10 |
| `B5` | Red-Edge 1 | 705 | 20 |
| `B6` | Red-Edge 2 | 740 | 20 |
| `B7` | Red-Edge 3 | 783 | 20 |
| `B8` | NIR | 842 | 10 |
| `B8A` | NIR Sempit | 865 | 20 |
| `B11` | SWIR-1 | 1610 | 20 |
| `B12` | SWIR-2 | 2190 | 20 |

---

## ☁️ Masking Awan

Masking awan diterapkan menggunakan **Scene Classification Layer (SCL)** yang disediakan bersama produk Sentinel-2 L2A. Kelas SCL berikut dikeluarkan dari analisis:

| Nilai SCL | Label Kelas |
|---|---|
| 3 | Bayangan awan |
| 8 | Awan, probabilitas sedang |
| 9 | Awan, probabilitas tinggi |
| 10 | Cirrus tipis |
| 11 | Salju / es |

```javascript
function maskS2(img) {
  var scl  = img.select('SCL');
  var mask = scl.neq(3).and(scl.neq(8)).and(scl.neq(9))
                        .and(scl.neq(10)).and(scl.neq(11));
  return img.updateMask(mask).divide(10000);
}
```

> **Catatan:** Pendekatan berbasis SCL umumnya lebih disarankan dibandingkan bitmask QA60 untuk produk S2 SR, karena memberikan diskriminasi yang lebih rinci terhadap jenis awan dan bayangan (Baetens et al., 2019).

---

## 📉 Indeks Spektral

Sembilan indeks spektral dihitung dan ditambahkan ke dalam tumpukan fitur. Indeks-indeks ini merepresentasikan struktur vegetasi, kandungan air, keterbukaan lahan, dan tingkat gangguan kebakaran — secara kolektif meningkatkan separabilitas antar kelas tutupan lahan.

### 🌳Indeks Vegetasi

| Indeks | Rumus | Referensi |
|---|---|---|
| **NDVI** | (B8 − B4) / (B8 + B4) | Rouse et al. (1974) |
| **EVI** | 2,5 × (B8 − B4) / (B8 + 6·B4 − 7,5·B2 + 1) | Huete et al. (2002) |
| **SAVI** | [(B8 − B4) / (B8 + B4 + 0,5)] × 1,5 | Huete (1988) |
| **IRECI** | (B8 − B4) / (B5 / B6) | Frampton et al. (2013) |

### 🌊 Indeks Air & Kelembaban

| Indeks | Rumus | Referensi |
|---|---|---|
| **NDWI** | (B3 − B8) / (B3 + B8) | Gao (1996) |
| **NDMI** | (B8 − B11) / (B8 + B11) | Hunt & Rock (1989) |

### 🧱 Indeks Lahan Terbangun & Tanah

| Indeks | Rumus | Referensi |
|---|---|---|
| **NDBI** | (B11 − B8) / (B11 + B8) | Zha et al. (2003) |
| **BSI** | [(B11 + B4) − (B8 + B2)] / [(B11 + B4) + (B8 + B2)] | Rikimaru et al. (2002) |

### 🔥 Indeks Kebakaran / Gangguan Lahan

| Indeks | Rumus | Referensi |
|---|---|---|
| **NBR** | (B8 − B12) / (B8 + B12) | Key & Benson (2006) |

> **Catatan tentang IRECI:** Inverted Red-Edge Chlorophyll Index memanfaatkan band red-edge Sentinel-2 (B5, B6) dan sangat sensitif terhadap konsentrasi klorofil pada kanopi rapat, sehingga efektif untuk membedakan hutan dari vegetasi yang terdegradasi (Frampton et al., 2013).

---

## Pengklasifikasi Random Forest

Pengklasifikasi **smile Random Forest** dilatih dengan hiperparameter berikut:

| Parameter | Nilai | Alasan Pemilihan |
|---|---|---|
| `numberOfTrees` | 500 | Jumlah pohon yang cukup untuk konvergensi galat out-of-bag yang stabil |
| `variablesPerSplit` | 4 | Approx. √19 fitur — heuristik standar untuk Random Forest |
| `bagFraction` | 0,7 | Pengambilan sampel bootstrap 70% per pohon, sesuai Breiman (2001) |
| `seed` | 42 | Seed tetap untuk menjamin reprodusibilitas hasil |

Pengklasifikasi dilatih menggunakan **19 fitur**: 10 band Sentinel-2 (`S2_BANDS`) + 9 indeks spektral (`INDEX_BANDS`).

---

## 🏷️ Data Latih & Pengambilan Sampel

Sampel latih disediakan sebagai empat objek `FeatureCollection` terpisah di GEE:

- `Hutan` — Kawasan hutan
- `Semak` — Semak belukar
- `LahanTerbuka` — Lahan terbuka / tanah gundul
- `Air` — Badan air

Seluruh koleksi digabung, lalu kolom acak ditambahkan melalui `.randomColumn()`. Sampel dengan nilai `random < 0.7` digunakan untuk pelatihan; sisanya (30%) digunakan untuk validasi independen.

**Ekstraksi fitur** dilakukan pada skala 10 m menggunakan `.sampleRegions()`, mengekstraksi nilai piksel untuk seluruh 19 band fitur pada setiap titik sampel.

> ⚠️ **Penting:** Sampel latih harus didigitasi secara manual atau bersumber dari survei lapangan / citra resolusi tinggi. Keterwakilan spasial dan kemurnian spektral sampel secara langsung menentukan kinerja pengklasifikasi. Ketidakseimbangan kelas (class imbalance) perlu diperiksa sebelum pelatihan dilakukan.

---

## 📊 Keluaran yang Diharapkan

| Keluaran | Format | Skala | Keterangan |
|---|---|---|---|
| `RF_TutupanLahan` | GeoTIFF | 10 m | Raster tutupan lahan terklasifikasi (nilai integer 0–3) |

### Konfigurasi Ekspor

```javascript
Export.image.toDrive({
  image       : classified,
  description : 'RF_TutupanLahan',
  folder      : 'GEE',
  region      : geometry,
  scale       : 10,
  fileFormat  : 'GeoTIFF',
  maxPixels   : 1e13
});
```

---

## 🚀 Cara Memulai

### Prasyarat

1. Akun [Google Earth Engine](https://earthengine.google.com/) (gratis untuk keperluan riset)
2. Wilayah kajian yang didefinisikan sebagai objek `geometry` di GEE (digambar secara interaktif atau diimpor sebagai aset)
3. Objek `FeatureCollection` sampel latih yang telah diunggah ke GEE Assets dengan properti `lc` yang menyimpan nilai integer kelas (0–3)

### Langkah Penggunaan

1. Buka [GEE Code Editor](https://code.earthengine.google.com/)
2. Buat sampel latih untuk setiap kelas dan impor sebagai aset dengan nama:
   - `Hutan`, `Semak`, `LahanTerbuka`, `Air`
3. Definisikan poligon wilayah kajian sebagai variabel `geometry`
4. Tempel skrip ke dalam Code Editor
5. Sesuaikan `START_DATE`, `END_DATE`, dan `CLOUD_LIMIT` sesuai kebutuhan
6. Klik **Run**
7. Jalankan tugas ekspor dari panel **Tasks**

### Penyesuaian Rentang Tanggal

Untuk hasil optimal, pertimbangkan untuk mempersempit rentang tanggal pada **musim kemarau** di wilayah kajian guna meminimalkan kontaminasi awan residual dan variasi fenologi musiman. Rentang minimum 3–6 bulan umumnya direkomendasikan untuk memastikan jumlah observasi valid yang cukup per piksel dalam membentuk komposit median yang stabil.

---

## 📏 Penilaian Akurasi

Skrip ini tidak menyertakan modul penilaian akurasi otomatis. Sangat disarankan untuk melakukan langkah pasca-klasifikasi berikut:

1. **Matriks konfusi** — dihitung menggunakan 30% sampel validasi yang disisihkan:
   ```javascript
   var validation = samples.filter(ee.Filter.gte('random', TRAIN_SPLIT));
   var validated  = featureImage.select(FEATURE_BANDS).sampleRegions({
     collection : validation,
     properties : [CLASS_FIELD],
     scale      : 10
   });
   var testResult  = validated.classify(classifier);
   var errorMatrix = testResult.errorMatrix(CLASS_FIELD, 'classification');
   print('Matriks Konfusi:', errorMatrix);
   print('Akurasi Keseluruhan:', errorMatrix.accuracy());
   print('Koefisien Kappa:', errorMatrix.kappa());
   ```

2. **Kepentingan fitur (feature importance)** — untuk memeriksa kontribusi setiap band:
   ```javascript
   var importance = ee.Dictionary(classifier.explain().get('importance'));
   print('Kepentingan Variabel:', importance);
   ```

3. **Validasi independen** — apabila memungkinkan, lakukan validasi terhadap data lapangan kontemporer atau citra resolusi tinggi untuk menghindari artefak autokorelasi spasial yang melekat pada evaluasi split-sampel.

---

## ⚠️ Keterbatasan yang Diketahui

- **Komposit temporal:** Komposit median dalam jendela waktu multi-tahun (2024–2026) berpotensi mencampurkan kondisi fenologi dari berbagai musim. Pertimbangkan untuk mempersempit rentang waktu atau melakukan stratifikasi komposit per musim jika dinamika intra-tahunan menjadi perhatian utama.
- **Ketidaksesuaian resolusi:** Band red-edge dan SWIR (B5, B6, B7, B8A, B11, B12) secara native beresolusi 20 m dan di-resample secara bilinear ke 10 m oleh GEE. Proses resample ini menimbulkan penghalusan spasial, terutama pada batas antar kelas.
- **Kualitas sampel latih:** Kinerja pengklasifikasi sangat bergantung pada keterwakilan dan kemurnian spektral sampel latih. Piksel campuran (mixed pixels) pada batas kelas sebaiknya dihindari saat digitasi.
- **Separabilitas kelas:** NDBI dan BSI berpotensi menunjukkan kebingungan spektral antara tanah terbuka dan tipe hutan/semak berkanopi rendah di kawasan tropis, khususnya pada musim kemarau.

---

## 📚 Daftar Pustaka

- Baetens, L., Desjardins, C., & Hagolle, O. (2019). Validation of Copernicus Sentinel-2 Cloud Masks Obtained from MAJA, Sen2Cor, and FMask Processors Using Reference Cloud Masks Generated with a Supervised Active Learning Procedure. Remote Sensing, 11(4), 433. https://doi.org/10.3390/rs11040433
- Breiman, L. (2001) Random Forests. Machine Learning, 45, 5-32.
http://dx.doi.org/10.1023/A:1010933404324
- Frampton, W. J., et al. (2013). Evaluating the capabilities of Sentinel-2 for quantitative estimation of biophysical variables in vegetation. *ISPRS Journal of Photogrammetry and Remote Sensing*, 82, 83–92.
- Gao, B. C. (1996). NDWI — A normalized difference water index for remote sensing of vegetation liquid water from space. *Remote Sensing of Environment*, 58(3), 257–266.
- Huete, A. R. (1988). A soil-adjusted vegetation index (SAVI). *Remote Sensing of Environment*, 25(3), 295–309.
- Huete, A., et al. (2002). Overview of the radiometric and biophysical performance of the MODIS vegetation indices. *Remote Sensing of Environment*, 83(1–2), 195–213.
- Key, C. H., & Benson, N. C. (2006). Landscape assessment: Ground measure of severity, the Composite Burn Index. *FIREMON: Fire Effects Monitoring and Inventory System*, LA-1–LA-51.
- Rikimaru, A., Roy, P. S., & Miyatake, S. (2002). Tropical forest cover density mapping. *Tropical Ecology*, 43(1), 39–47.
- Rouse, J. W., et al. (1974). Monitoring vegetation systems in the Great Plains with ERTS. *Proceedings of the 3rd ERTS Symposium*, 1, 48–62.
- Zha, Y., Gao, J., & Ni, S. (2003). Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. *International Journal of Remote Sensing*, 24(3), 583–594.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT**. Lihat [`LICENSE`](https://github.com/Defani/LAND-COVER-CLASSIFICATION-RANDOM-FOREST-MULTI-INDEX/blob/main/LICENSE) untuk detail selengkapnya.

---



*Skrip ini ditulis sepenuhnya dalam bahasa **JavaScript** menggunakan lingkungan [Google Earth Engine Code Editor](https://code.earthengine.google.com/). Seluruh pemrosesan citra, komputasi indeks spektral, pelatihan model, dan ekspor hasil dilakukan secara server-side di infrastruktur GEE tanpa memerlukan instalasi perangkat lunak lokal.*
