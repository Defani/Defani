---
title: "Terrio Toolbox: ArcToolbox di GeoLibre"
subtitle: Geoprocessing raster dan vektor di browser, dari Slope sampai Raster Calculator ala ArcMap
date: 2026-11-21
tags: [GeoLibre, plugin, geoprocessing, raster calculator, DEMNAS, Sentinel-2]
---

**Terrio Toolbox** adalah plugin GeoLibre yang saya buat: panel *Geoprocessing* ala ArcGIS Pro yang menempel di sisi kanan, seperti ArcToolbox di ArcMap. Mesinnya [terrio-js](https://terrio.dev) (MIT), pengolah raster dan vektor setara GDAL yang ditulis dengan Rust dan berjalan di browser lewat WebAssembly. Tidak perlu Python, GDAL, atau server.

- 36 tool dalam 4 toolbox: Analysis, Conversion, Data Management, Spatial Analyst
- Setiap proses menampilkan waktu jalannya dalam detik dan tercatat di **History**
- **Raster Calculator** dengan jendela seperti ArcMap: Con, SetNull, Float, Int, keypad
- Repositori: [Defani/geolibre-terrio-toolbox](https://github.com/Defani/geolibre-terrio-toolbox) · Unduh: [Releases](https://github.com/Defani/geolibre-terrio-toolbox/releases/latest)

Data yang dipakai di tutorial ini adalah data nyata: **DEMNAS** lembar 1309-12 (Gunung Ciremai, Kuningan) dan **Sentinel-2** di pesisir **Sembilang**, Sumatera Selatan.

## 1. Pasang plugin

1. Unduh `terrio-toolbox-<versi>.zip` dari halaman [Releases](https://github.com/Defani/geolibre-terrio-toolbox/releases/latest). Jangan diekstrak.
2. Di GeoLibre buka **Plugins → Installed → Manage plugins…**, pilih tab **Settings**, lalu klik **Choose .zip…** dan pilih file zip tadi.
3. Aktifkan lewat **Plugins → Installed → Terrio Toolbox**.

:::{figure} ../assets/tutorial/terrio-toolbox/00-install.jpg
:label: fig-tt-install
Memasang plugin dari file zip di Manage plugins → Settings.
:::

## 2. Kenali panelnya

Setelah aktif, panel **Terrio Toolbox** langsung terbuka di kanan, satu rel dengan panel Style dan Comments. Ada tiga tab:

- **Favorites**: tool yang diberi bintang.
- **Toolboxes**: pohon toolbox seperti ArcToolbox.
- **History**: semua proses di sesi ini beserta detiknya.

Baris paling bawah menunjukkan status mesin, misalnya `terrio 0.9.0 · 30 MB WebAssembly · ready in 0.36 s`.

:::{figure} ../assets/tutorial/terrio-toolbox/01-pane.jpg
:label: fig-tt-pane
Panel Terrio Toolbox di kanan, dengan DEMNAS Gunung Ciremai di peta.
:::

Raster yang bisa dipakai plugin adalah raster yang ditambahkan **dari URL** (Add data → Raster layer) dan **hasil tool Terrio sebelumnya**. Raster dari file lokal (drag-drop) belum dibagikan GeoLibre ke plugin; untuk itu klik **ikon folder** di sebelah pilihan raster dan pilih file yang sama.

## 3. Cari tool

Ketik nama tool di **Find Tools**. Hasilnya menampilkan letak tool di toolbox.

:::{figure} ../assets/tutorial/terrio-toolbox/02-find-tools.jpg
:label: fig-tt-find
Mencari "slope": muncul Slope, Aspect, dan Raster Calculator.
:::

## 4. Slope dari DEMNAS

1. Klik **Slope**. Halaman **Parameters** terbuka. Tanda `*` berarti wajib.
2. **Input raster**: `demnas_kuningan.tif`. **Output measurement**: DEGREE. **Z factor**: 1.
3. Klik **Run**.

:::{figure} ../assets/tutorial/terrio-toolbox/03-slope-params.jpg
:label: fig-tt-slope-params
Parameter Slope.
:::

DEMNAS memakai koordinat derajat (dan sebagian lembarnya disebarkan tanpa sistem koordinat). Terrio Toolbox mengenali ini: raster tanpa CRS yang koordinatnya jelas derajat dianggap WGS 84, dan untuk Slope jarak derajat diubah ke meter, sehingga kemiringan tetap benar. Hasilnya masuk ke peta dalam 2 detik.

:::{figure} ../assets/tutorial/terrio-toolbox/04-slope-done.jpg
:label: fig-tt-slope
Slope Gunung Ciremai, selesai dalam 2,04 detik.
:::

## 5. Raster Calculator ala ArcMap

Buka **Spatial Analyst Tools → Map Algebra → Raster Calculator**. Jendelanya sama seperti di ArcMap:

- **Layers and variables**: raster di peta. Klik dua kali untuk memasukkan namanya ke ekspresi.
- **Functions**: Conditional (Con, Pick, SetNull, IsNull), Math (Abs, Exp, Float, Int, Ln, Log10, Power, RoundUp, SquareRoot, …), dan Trigonometric. Klik sekali untuk melihat penjelasannya, klik dua kali untuk memasukkannya.
- **Keypad**: angka dan operator `== != & | > >= < <= + - * / ^ ~`.
- Di bawah kotak ekspresi ada pemeriksa langsung: **Valid · uses …** atau pesan kesalahannya.

### NDVI Sembilang

Nama raster ditulis dalam tanda kutip ganda, sama seperti di ArcMap:

```text
Float("sembilang_b8.tif" - "sembilang_b4.tif") / Float("sembilang_b8.tif" + "sembilang_b4.tif")
```

:::{figure} ../assets/tutorial/terrio-toolbox/05-calculator.jpg
:label: fig-tt-calc
Raster Calculator dengan ekspresi NDVI. Status di bawah ekspresi menunjukkan ekspresinya valid.
:::

Band Sentinel-2 bertipe bilangan bulat (UInt16). Kalau tidak diubah ke pecahan, hasil pembagian akan terpotong. `Float()` menangani itu, dan plugin juga otomatis menghitung raster integer sebagai pecahan.

:::{figure} ../assets/tutorial/terrio-toolbox/06-ndvi.jpg
:label: fig-tt-ndvi
NDVI pesisir Sembilang: daratan bervegetasi (mangrove) kuning, laut ungu. Selesai dalam 1,64 detik.
:::

### Con: memisahkan vegetasi

Hasil NDVI langsung bisa dipakai lagi. Ekspresi berikut memberi nilai 1 untuk NDVI di atas 0,4 dan 0 untuk sisanya:

```text
Con("ndvi_sembilang" > 0.4, 1, 0)
```

:::{figure} ../assets/tutorial/terrio-toolbox/07-con.jpg
:label: fig-tt-con
Kelas vegetasi dari Con. Jalur hitam di kanan berada di luar citra, jadi tetap NoData, sama seperti di ArcGIS.
:::

Contoh ekspresi lain:

| Tujuan | Ekspresi |
| --- | --- |
| Hapus lereng curam dari DEM | `SetNull("slope.tif" > 45, "dem.tif")` |
| Kelas tinggi 3 tingkat | `Con("dem.tif" < 500, 1, Con("dem.tif" < 1000, 2, 3))` |
| Isi NoData dengan 0 | `Con(IsNull("dem.tif"), 0, "dem.tif")` |
| Pembulatan ke bawah | `RoundDown("dem.tif" / 100) * 100` |

## 6. Raster To ASCII

**Conversion Tools → From Raster → Raster To ASCII** mengubah GeoTIFF menjadi ASCII grid (`.asc`) plus `.prj`, misalnya untuk MaxEnt atau model hidrologi. Atur **Band** dan **Decimal places**, lalu **Run**. Hasil berupa file muncul sebagai tombol **Save …**.

:::{figure} ../assets/tutorial/terrio-toolbox/08-ascii.jpg
:label: fig-tt-ascii
DEMNAS 2267 × 2000 piksel menjadi ASCII grid 51,5 MB dalam 1,63 detik.
:::

**View Details** menampilkan pesan proses seperti di ArcMap: perintah yang dijalankan, jam mulai, ukuran keluaran, dan waktu tiap tahap.

:::{figure} ../assets/tutorial/terrio-toolbox/09-details.jpg
:label: fig-tt-details
Pesan proses dari View Details.
:::

## 7. History

Tab **History** mencatat setiap proses di sesi ini beserta lamanya. Klik salah satu untuk membuka tool itu lagi dengan parameter yang sama.

:::{figure} ../assets/tutorial/terrio-toolbox/10-history.jpg
:label: fig-tt-history
History sesi: dua Raster Calculator dan satu Raster To ASCII.
:::

## 8. Seberapa cepat?

Diuji pada data nyata di laptop yang sama, semuanya berjalan di browser:

- Terrain (hillshade, slope, aspect): 8–14 kali lebih cepat dibanding whitebox-wasm.
- Kontur: 2–3 kali lebih cepat.
- Buffer dan dissolve: sekitar 2 kali lebih cepat dibanding Turf.js.
- NDVI satu tile Sentinel-2 penuh (2 band × 121 juta piksel) selesai di dalam GeoLibre.

:::{figure} ../assets/tutorial/terrio-toolbox/11-benchmark.png
:label: fig-tt-bench
Perbandingan waktu proses Terrio dengan whitebox-wasm dan Turf.js.
:::

## Batasan

- Memori WebAssembly maksimal 4 GB. Raster Calculator menghitung per potongan baris sehingga muat untuk raster besar. Untuk raster sangat besar, jalankan **Clip (Raster)** ke wilayah kajian lebih dulu.
- Semua proses berjalan di satu thread browser.
- Raster dari file lokal harus dipilih ulang lewat ikon folder (lihat bagian 2).

## Daftar tool

| Toolbox | Toolset | Tool |
| --- | --- | --- |
| Analysis | Extract | Clip, Select |
| | Overlay | Erase, Intersect, Union, Symmetrical Difference, Identity, Update |
| | Proximity | Buffer |
| Conversion | From Raster | Raster to Polygon, Raster To ASCII, Raster To Other Format |
| | To Raster | Feature to Raster |
| | To File | Feature Class To File (GPKG, Shapefile, GeoParquet, FlatGeobuf, KML/KMZ, DXF, CSV) |
| Data Management | Features | Repair Geometry, Multipart To Singlepart, Minimum Bounding Geometry |
| | Generalization | Dissolve, Simplify |
| | Projections and Transformations | Define Projection, Project Raster |
| | Raster | Clip (Raster), Mosaic To New Raster, Resample, Fill NoData |
| Spatial Analyst | Surface | Hillshade, Slope, Aspect, Terrain Ruggedness, Contour, Viewshed |
| | Map Algebra | Raster Calculator |
| | Neighborhood | Focal Statistics |
| | Reclass | Reclassify |
| | Zonal | Zonal Statistics as Table |
| | Distance | Euclidean Distance |

## Kredit

- [GeoLibre](https://github.com/opengeos/GeoLibre) oleh Qiusheng Wu (opengeos), lisensi MIT.
- [Terrio / terrio-js](https://terrio.dev) (opengeos), lisensi MIT.
- DEMNAS: Badan Informasi Geospasial. Sentinel-2: Copernicus, European Space Agency.
- Plugin Terrio Toolbox: Defani Arman Alfitriansyah, lisensi MIT.
