---
title: "NBR-Karhutla-Gunung-Lawu-GEE"
---

Implementasi Normalized Burn Ratio Plus (NBR+) pada Google Earth Engine untuk mendeteksi dan memetakan area kebakaran hutan di kawasan Gunung Lawu, Jawa Tengah–Jawa Timur, menggunakan citra Sentinel-2A SR Harmonized dengan pendekatan bi-temporal.

[Repositori di GitHub](https://github.com/Defani/NBR-Karhutla-Gunung-Lawu-GEE)

Implementasi **Normalized Burn Ratio Plus (NBR+)** pada Google Earth Engine untuk mendeteksi dan memetakan area kebakaran hutan di kawasan **Gunung Lawu**, Jawa Tengah–Jawa Timur, menggunakan citra Sentinel-2A SR Harmonized dengan pendekatan bi-temporal.

[![GEE Script](https://img.shields.io/badge/Google%20Earth%20Engine-Script-brightgreen?logo=google-earth)](https://code.earthengine.google.com/457addfc0dcb9d8e840be1ac7d5e2c4d)
[![Sentinel-2](https://img.shields.io/badge/Sentinel--2-SR%20Harmonized-blue)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)
[![Cloud Score+](https://img.shields.io/badge/Cloud%20Masking-Cloud%20Score%2B-orange)](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Latar Belakang

Kebakaran hutan di kawasan Gunung Lawu pada September–Oktober 2023 berdampak signifikan terhadap vegetasi pegunungan di wilayah perbatasan Jawa Tengah dan Jawa Timur. Pemantauan spasial kejadian ini dilakukan menggunakan indeks **NBR+** yang dikembangkan oleh Alcaras et al. (2022) sebagai penyempurnaan dari Normalized Burn Ratio (NBR) konvensional.

Keunggulan utama NBR+ terhadap NBR standar terletak pada penambahan band Blue (B2) dan Green (B3) ke dalam formulasinya, yang secara eksplisit menekan respons spektral badan air dan awan sehingga meminimalkan kesalahan komisi tanpa memerlukan masker tambahan (Alcaras et al., 2022).

---

## Formula

$$\text{NBR+} = \frac{B12 - B8A - B3 - B2}{B12 + B8A + B3 + B2}$$

| Band | Nama | Panjang Gelombang | Resolusi |
|------|------|-------------------|----------|
| B2 | Blue | 490 nm | 10 m |
| B3 | Green | 560 nm | 10 m |
| B8A | Narrow NIR | 865 nm | 20 m |
| B12 | SWIR2 | 2190 nm | 20 m |

Untuk pendekatan bi-temporal, perubahan dihitung sebagai:

$$\Delta\text{NBR+} = \text{NBR+}_{\text{post}} - \text{NBR+}_{\text{pre}}$$

---

## Metodologi

### 1. Preprocessing — Cloud Masking

Cloud masking menggunakan **Cloud Score+** (`GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED`) dengan parameter:

- `cs_cdf ≥ 0.60` — threshold probabilitas bebas awan
- `CLOUDY_PIXEL_PERCENTAGE < 20%` — filter tingkat tutupan awan per scene

Pendekatan ini dipilih karena Cloud Score+ menghasilkan masker awan yang lebih andal untuk wilayah tropis lembab dibandingkan metode berbasis QA60 maupun SCL.

### 2. Komposit Median Bi-Temporal

| Periode | Tanggal | Keterangan |
|---------|---------|------------|
| Pre-fire | 1–29 Agustus 2023 | Kondisi sebelum kebakaran |
| Post-fire | 1–31 Oktober 2023 | Kondisi pasca kebakaran |

Komposit median digunakan untuk mereduksi noise residual dan variabilitas antar-akuisisi dalam rentang temporal masing-masing periode.

### 3. Perhitungan ΔNBR+ dan Klasifikasi

Area terbakar diklasifikasikan menggunakan threshold:

$$\Delta\text{NBR+} \geq 0.30$$

Nilai threshold ini mengacu pada rentang perubahan spektral yang konsisten dengan perubahan vegetasi akibat kebakaran pada citra Sentinel-2, sebagaimana dilaporkan dalam Alcaras et al. (2022).

---

## Kode GEE

```javascript
// CLOUD MASKING FUNCTION — CLOUD SCORE+
var mask_s2 = function(image) {
  var cs = image.select('cs_cdf');
  return image.updateMask(cs.gte(0.6));
};

// IMAGE COLLECTION
var s2_collection = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(lawu)
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .linkCollection(
    ee.ImageCollection('GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED'),
    ['cs_cdf']
  )
  .map(mask_s2);

// BI-TEMPORAL COMPOSITE
var pre_fire = s2_collection
  .filterDate('2023-08-01', '2023-08-29')
  .median()
  .clip(lawu);

var post_fire = s2_collection
  .filterDate('2023-10-01', '2023-10-31')
  .median()
  .clip(lawu);

// NBR+ CALCULATION
var calc_nbr_plus = function(image) {
  var b12 = image.select('B12');
  var b8a = image.select('B8A');
  var b3  = image.select('B3');
  var b2  = image.select('B2');

  var num = b12.subtract(b8a).subtract(b3).subtract(b2);
  var den = b12.add(b8a).add(b3).add(b2);

  return num.divide(den).rename('nbr_plus');
};

var nbr_plus_pre  = calc_nbr_plus(pre_fire);
var nbr_plus_post = calc_nbr_plus(post_fire);

// DELTA NBR+ AND CLASSIFICATION
var d_nbr_plus    = nbr_plus_post.subtract(nbr_plus_pre).rename('d_nbr_plus');
var burn_treshold = d_nbr_plus.gte(0.3);

// VISUALIZATION
Map.centerObject(lawu, 12);
Map.addLayer(
  post_fire,
  {bands: ['B11', 'B8', 'B4'], min: 0, max: 4000},
  'Citra Pasca Kebakaran (B11-B8-B4)'
);
Map.addLayer(
  burn_treshold.selfMask(),
  {palette: ['red']},
  'Area Terbakar (ΔNBR+ ≥ 0.30)'
);
```

> **Catatan:** Variabel `lawu` merujuk pada objek geometri ROI kawasan Gunung Lawu yang didefinisikan secara terpisah sebagai aset atau geometri manual di GEE.

---

## Akurasi Referensi

Berdasarkan evaluasi Alcaras et al. (2022) pada citra Sentinel-2A di wilayah Sisilia, Italia, NBR+ menunjukkan performa tertinggi dibandingkan lima indeks pembanding (NBR, NBRSWIR, NDSWIR, MIRBI, BAIS2):

| Pendekatan | OA (NBR+) | OA (NBR) | OA (BAIS2) |
|------------|-----------|----------|------------|
| Single-date (Group A) | **0.908** | 0.685 | 0.798 |
| Single-date (Group B) | **0.925** | 0.805 | 0.809 |
| Bi-temporal (Group A) | **0.974** | 0.909 | 0.881 |
| Bi-temporal (Group B) | **0.998** | 0.993 | 0.940 |

Group A mencakup badan air dan awan; Group B mengecualikannya.

---

## Prasyarat

- Akun Google Earth Engine yang aktif
- ROI kawasan Gunung Lawu (didefinisikan sebagai variabel `lawu`)
- Akses ke dataset:
  - `COPERNICUS/S2_SR_HARMONIZED`
  - `GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED`

---

## Referensi

Alcaras, E., Costantino, D., Guastaferro, F., Parente, C., & Pepe, M. (2022). Normalized Burn Ratio Plus (NBR+): A New Index for Sentinel-2 Imagery. *Remote Sensing*, *14*(7), 1727. https://doi.org/10.3390/rs14071727

---

## Lisensi

Kode pada repositori ini didistribusikan di bawah lisensi [MIT](https://github.com/Defani/NBR-Karhutla-Gunung-Lawu-GEE/blob/main/LICENSE).
