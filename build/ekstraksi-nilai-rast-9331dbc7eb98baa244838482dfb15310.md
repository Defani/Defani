---
title: "Ekstraksi-nilai-raster-di-gee-python-menjadi-GPKG-dan-CSV"
---

Notebook ini mengekstrak nilai band spektral dan indeks vegetasi/lahan dari citra Sentinel-2 pada titik-titik sampel lapangan menggunakan Google Earth Engine (GEE) di lingkungan Google Colab.

[Repositori di GitHub](https://github.com/Defani/Ekstraksi-nilai-raster-di-gee-python-menjadi-GPKG-dan-CSV)

Notebook ini mengekstrak nilai band spektral dan indeks vegetasi/lahan dari citra Sentinel-2 pada titik-titik sampel lapangan menggunakan Google Earth Engine (GEE) di lingkungan Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aP9PMgzkhk2LR9lFwz_qVS8LrlaUbbW3?usp=sharing)

---

## Deskripsi

Pipeline ini membaca shapefile titik sampel lapangan, membangun composite citra Sentinel-2 SR tahunan (2024), menghitung empat indeks spektral, lalu mengekstrak nilai piksel di setiap titik sampel. Hasil akhir disimpan sebagai CSV dan GeoPackage (.gpkg) di Google Drive.

---

## Alur Kerja

```
Shapefile Sampel (.shp)
        |
        v
  Google Earth Engine
  FeatureCollection
        |
        v
  Sentinel-2 SR Composite
  (2024, cloud-masked)
        |
        v
  Hitung Indeks Spektral
  NDVI | NDWI | NDMI | NDBI
        |
        v
  sampleRegions() -> DataFrame
        |
        v
  Gabung koordinat (lon/lat)
        |
        v
  Export -> CSV & GPKG
```

---

## Indeks Spektral

### NDVI — Normalized Difference Vegetation Index

Mengukur kerapatan dan kehijauan vegetasi berdasarkan perbedaan reflektansi NIR dan merah (Rouse et al., 1974).

```
NDVI = (NIR - Red) / (NIR + Red)
     = (B8 - B4) / (B8 + B4)
```

Rentang nilai: -1 hingga +1. Nilai tinggi (> 0.5) mengindikasikan vegetasi lebat.

---

### NDWI — Normalized Difference Water Index

Mengidentifikasi badan air terbuka dan mengukur kandungan air permukaan (McFeeters, 1996).

```
NDWI = (Green - NIR) / (Green + NIR)
     = (B3 - B8) / (B3 + B8)
```

Rentang nilai: -1 hingga +1. Nilai positif (> 0) mengindikasikan keberadaan air.

> McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. *International Journal of Remote Sensing*, 17(7), 1425–1432. https://doi.org/10.1080/01431169608948714

---

### NDMI — Normalized Difference Moisture Index

Mengukur kelembaban kandungan air pada vegetasi menggunakan band NIR dan SWIR (Gao, 1996).

```
NDMI = (NIR - SWIR1) / (NIR + SWIR1)
     = (B8 - B11) / (B8 + B11)
```

Rentang nilai: -1 hingga +1. Nilai tinggi mengindikasikan vegetasi dengan kandungan air tinggi.

> Gao, B.-C. (1996). NDWI — A normalized difference water index for remote sensing of vegetation liquid water from space. *Remote Sensing of Environment*, 58(3), 257–266. https://doi.org/10.1016/S0034-4257(96)00067-3

---

### NDBI — Normalized Difference Built-up Index

Mengidentifikasi dan memetakan kawasan lahan terbangun/impervious menggunakan band SWIR dan NIR (Zha et al., 2003).

```
NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)
     = (B11 - B8) / (B11 + B8)
```

Rentang nilai: -1 hingga +1. Nilai positif mengindikasikan dominasi lahan terbangun.

> Zha, Y., Gao, J., & Ni, S. (2003). Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. *International Journal of Remote Sensing*, 24(3), 583–594. https://doi.org/10.1080/01431160304987

---

## Data Citra

| Parameter | Nilai |
|-----------|-------|
| Koleksi | `COPERNICUS/S2_SR_HARMONIZED` |
| Periode | 1 Januari – 31 Desember 2024 |
| Filter cloud | `CLOUDY_PIXEL_PERCENTAGE < 20` |
| Cloud masking | Cloud Score+ (`cs_cdf >= 0.60`) |
| Komposit | Median, dinormalisasi ke 0–1 (dibagi 10.000) |
| Skala sampling | 10 meter |

---

## Struktur Output

| Kolom | Keterangan |
|-------|------------|
| `rand_point` | ID titik sampel acak |
| `id` | ID tambahan dari atribut shapefile |
| `lon`, `lat` | Koordinat geografis (EPSG:4326) |
| `B2`, `B3`, `B4` | Band Blue, Green, Red |
| `B8` | Band NIR (842 nm) |
| `B11`, `B12` | Band SWIR1 (1610 nm), SWIR2 (2190 nm) |
| `NDVI` | Normalized Difference Vegetation Index |
| `NDWI` | Normalized Difference Water Index |
| `NDMI` | Normalized Difference Moisture Index |
| `NDBI` | Normalized Difference Built-up Index |

File output:
```
MyDrive/
├── sampel_indeks.csv    <- tabel hasil sampling
└── sampel_indeks.gpkg   <- geodata untuk QGIS/ArcGIS
```

---

## Cara Penggunaan

### 1. Prasyarat
- Akun Google Earth Engine yang sudah diaktifkan
- Google Drive dengan shapefile sampel tersedia
- Google Colab

### 2. Instalasi dependensi
```python
!pip install geemap geopandas
```

### 3. Siapkan file input
Letakkan shapefile titik sampel di Google Drive:
```
MyDrive/sampel_lapangan.shp  (beserta .dbf, .prj, .shx)
```

Sesuaikan project ID GEE di cell autentikasi:
```python
ee.Initialize(project='ee-<your-project-id>')
```

### 4. Jalankan semua cell secara berurutan

| Cell | Fungsi |
|------|--------|
| Install | Install `geemap` dan `geopandas` |
| Import | Load semua library |
| Mount Drive & Auth | Koneksi Google Drive + autentikasi GEE |
| Load Shapefile | Baca titik sampel, konversi ke EPSG:4326 |
| Convert ke EE | Ubah GeoDataFrame ke EE FeatureCollection |
| AOI + S2 Composite | Buat composite Sentinel-2 dengan cloud masking |
| Hitung Indeks | Kalkulasi NDVI, NDWI, NDMI, NDBI |
| Sampling | Ekstrak nilai piksel di titik sampel |
| Tambah Koordinat | Gabung lon/lat dari GeoDataFrame asal |
| Export | Simpan CSV & GPKG ke Google Drive |

---

## Dependensi

| Library | Sitasi |
|---------|--------|
| `geemap` | Wu, Q. (2020). geemap: A Python package for interactive mapping with Google Earth Engine. *Journal of Open Source Software*, 5(51), 2305. https://doi.org/10.21105/joss.02305 |
| `geopandas` | Jordahl, K., Van den Bossche, J., Fleischmann, M., et al. (2020). geopandas/geopandas: v0.8.1. Zenodo. https://doi.org/10.5281/zenodo.3946761 |
| `pandas` | The Pandas Development Team. (2020). pandas-dev/pandas: Pandas. Zenodo. https://doi.org/10.5281/zenodo.3509134 |
| `numpy` | Harris, C. R., et al. (2020). Array programming with NumPy. *Nature*, 585, 357–362. https://doi.org/10.1038/s41586-020-2649-2 |
| `matplotlib` | Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. *Computing in Science & Engineering*, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55 |

---

## Referensi

- Gao, B.-C. (1996). NDWI — A normalized difference water index for remote sensing of vegetation liquid water from space. *Remote Sensing of Environment*, 58(3), 257–266. https://doi.org/10.1016/S0034-4257(96)00067-3
- Jordahl, K., Van den Bossche, J., Fleischmann, M., Wasserman, J., McBride, J., Gerard, J., … Leblanc, F. (2020). geopandas/geopandas: v0.8.1 (Version v0.8.1). Zenodo. http://doi.org/10.5281/zenodo.3946761
- McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. *International Journal of Remote Sensing*, 17(7), 1425–1432. https://doi.org/10.1080/01431169608948714
- Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1974). Monitoring vegetation systems in the Great Plains with ERTS. *Third ERTS Symposium, NASA SP-351*, 1, 309–317.
- Wu, Q. (2020). geemap: A Python package for interactive mapping with Google Earth Engine. *Journal of Open Source Software*, 5(51), 2305. https://doi.org/10.21105/joss.02305
- Zha, Y., Gao, J., & Ni, S. (2003). Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. *International Journal of Remote Sensing*, 24(3), 583–594. https://doi.org/10.1080/01431160304987
