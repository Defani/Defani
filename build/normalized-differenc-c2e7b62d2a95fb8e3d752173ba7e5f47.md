---
title: "Normalized-Difference-Red-Edge-Index--GEE-"
---

Skrip ini menghitung dan memvisualisasikan NDRE (Normalized Difference Red Edge) dari composite citra Sentinel-2 SR tahun 2024 menggunakan cloud masking berbasis Cloud Score+ di Google Earth Engine (GEE) Code Editor.

[Repositori di GitHub](https://github.com/Defani/Normalized-Difference-Red-Edge-Index--GEE-)

Skrip ini menghitung dan memvisualisasikan **NDRE (Normalized Difference Red Edge)** dari composite citra Sentinel-2 SR tahun 2024 menggunakan cloud masking berbasis **Cloud Score+** di Google Earth Engine (GEE) Code Editor.

---
## Link : https://code.earthengine.google.com/0768d94e134507a8d134a0232498b0d7
## Deskripsi

NDRE merupakan pengembangan dari NDVI yang memanfaatkan band Red Edge (B5, 705 nm) sebagai pengganti band Red (B4), sehingga lebih sensitif terhadap kandungan klorofil pada vegetasi berkanopi lebat maupun kondisi stres tanaman (Gitelson & Merzlyak, 1994).

---

## Indeks Spektral

### NDRE — Normalized Difference Red Edge

Mengukur kandungan klorofil dan kondisi fisiologis vegetasi secara lebih sensitif dibanding NDVI, khususnya pada vegetasi dengan nilai indeks daun (LAI) tinggi (Gitelson & Merzlyak, 1994).

```
NDRE = (NIR - RedEdge) / (NIR + RedEdge)
     = (B8 - B5) / (B8 + B5)
```

| Band | Sentinel-2 | Panjang Gelombang |
|------|------------|-------------------|
| NIR | B8 | 842 nm |
| Red Edge | B5 | 705 nm |

Rentang nilai: -1 hingga +1. Nilai tinggi (> 0.4) mengindikasikan vegetasi sehat dengan kandungan klorofil tinggi.

> Gitelson, A. A., & Merzlyak, M. N. (1994). Spectral reflectance changes associated with autumn senescence of *Aesculus hippocastanum* L. and *Acer platanoides* L. leaves. *Journal of Plant Physiology*, 143(3), 286–292. https://doi.org/10.1016/S0176-1617(11)81633-0

---

## Data Citra

| Parameter | Nilai |
|-----------|-------|
| Koleksi | `COPERNICUS/S2_SR_HARMONIZED` |
| Periode | 1 Januari – 31 Desember 2024 |
| Filter cloud | `CLOUDY_PIXEL_PERCENTAGE < 20` |
| Cloud masking | Cloud Score+ `GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED` (`cs_cdf >= 0.60`) |
| Komposit | Median, dinormalisasi ke 0–1 (dibagi 10.000) |

---

## Visualisasi

Palet warna yang digunakan mengikuti klasifikasi diverging dari rendah ke tinggi:

| Warna | Hex | Interpretasi |
|-------|-----|--------------|
| Merah | `#d73027` | Nilai NDRE sangat rendah (non-vegetasi / stres berat) |
| Oranye | `#fdae61` | Nilai NDRE rendah |
| Kuning muda | `#fee08b` | Nilai NDRE sedang-rendah |
| Hijau muda | `#d9ef8b` | Nilai NDRE sedang-tinggi |
| Hijau | `#66bd63` | Nilai NDRE tinggi |
| Hijau tua | `#1a9850` | Nilai NDRE sangat tinggi (vegetasi sehat, klorofil tinggi) |

```javascript
var visNDRE = {
  min: 0,
  max: 0.6,
  palette: ['#d73027','#fdae61','#fee08b','#d9ef8b','#66bd63','#1a9850']
};
```

---

## Kode Lengkap

```javascript
// Cloud Score+ masking
var csPlus = ee.ImageCollection('GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED');

function maskS2CSPlus(image) {
  var qa = image.select('cs_cdf');
  return image.updateMask(qa.gte(0.60));
}

// Sentinel-2 SR base collection
var s2_base = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(geometry)
  .filterDate('2024-01-01', '2024-12-31')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20));

// Composite dengan Cloud Score+
var composite_csplus = s2_base
  .linkCollection(csPlus, ['cs_cdf'])
  .map(maskS2CSPlus)
  .median()
  .clip(geometry)
  .divide(10000);

// Hitung NDRE
var ndre = composite_csplus.normalizedDifference(['B8', 'B5']).rename('NDRE');

// Visualisasi
var visNDRE = {
  min: 0,
  max: 0.6,
  palette: ['#d73027','#fdae61','#fee08b','#d9ef8b','#66bd63','#1a9850']
};

Map.addLayer(ndre, visNDRE, 'NDRE Cloud Score+');
Map.centerObject(geometry, 13);
```

---

## Catatan

- Variabel `geometry` harus didefinisikan terlebih dahulu di GEE Code Editor sebagai geometri AOI (polygon atau point).
- Cloud Score+ (`cs_cdf`) merupakan metode cloud masking probabilistik yang lebih akurat dibanding QA60 bawaan Sentinel-2.
- Threshold `cs_cdf >= 0.60` mempertahankan piksel dengan confidence bebas awan minimal 60%.
- Zoom level `13` pada `Map.centerObject` sesuai untuk skala kecamatan hingga kabupaten.

---

## Dependensi

| Library / Platform | Sitasi |
|--------------------|--------|
| Google Earth Engine | Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of Environment*, 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031 |

---

## Referensi

- Gitelson, A. A., & Merzlyak, M. N. (1994). Spectral reflectance changes associated with autumn senescence of *Aesculus hippocastanum* L. and *Acer platanoides* L. leaves. *Journal of Plant Physiology*, 143(3), 286–292. https://doi.org/10.1016/S0176-1617(11)81633-0
- Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of Environment*, 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031
