---
title: 'Mengunduh Citra Satelit Sentinel 2 Menggunakan Google Earth Engine'
date: 2025-06-18
tags: ['google-earth-engine']
---

18 June 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/mengunduh-citra-satelit-sentinel-2-menggunakan-google-earth-engine-c252f29b55f9) · [Semua tulisan](../blog.md)

**Oleh:** Defani Arman Alfitriansyah

![](https://cdn-images-1.medium.com/max/1024/1*YO1SAlU6pWwxlvqOg70Sqg.png)

Sebagai mahasiswa kehutanan yang aktif menggunakan data penginderaan jauh untuk studi vegetasi dan pemetaan lingkungan, saya sering diminta menjelaskan cara mendapatkan citra satelit yang bersih dari awan untuk keperluan analisis di ArcGIS atau QGIS. Tutorial ini saya susun agar bisa dimengerti oleh teman-teman yang baru belajar Google Earth Engine (GEE), dengan gaya penjelasan yang mengalir dan disertai pemahaman konsep teknis di balik setiap langkah.

#### ✍️**Tujuan Tutorial**

- Menampilkan citra Sentinel-2 tahun 2023 dengan masking awan
- Menghasilkan komposit tahunan bebas awan
- Mengekspor hasil RGB ke Google Drive
- Memahami struktur script GEE sebagai alat analisis spasial

#### 📘 Tabel Ringkasan Fungsi & Sintaks yang Digunakan

![](https://cdn-images-1.medium.com/max/1024/1*6x47RjldAEMjVagAb-4ImQ.png)

Gambar 1. Tabel Fungsi /Syntax GEE untuk mengunduh citra satelit

#### Deksripsi Data Sentinel 2

![](https://cdn-images-1.medium.com/max/1024/1*YB2dRJ88X-12Sf2ZSFphSQ.png)

Tampilan lama data katalog Sentinel 2 SR di Google Earth Engine Data Catalog (Sumber : <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands>)

[Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-2A (SR)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands)

### **Step Pra analisis (Penentuan Area Kajian)**

<https://medium.com/media/41b2f192ebcbf64094a84b4d17b1cb93/href>

#### 💻 Script GEE dengan Komentar

#### 1. Fungsi Masking Awan (Cloud Masking)

    // Fungsi untuk menyaring piksel awan dan bayangan awan berdasarkan nilai SCL
    var sentinel2_mask = function(image) {
      var scl = image.select('SCL'); // Ambil band klasifikasi piksel
      var mask = scl.neq(3)          // Bukan bayangan awan
                  .and(scl.neq(8))   // Bukan awan probabilitas sedang
                  .and(scl.neq(9))   // Bukan awan tebal
                  .and(scl.neq(10))  // Bukan cirrus
                  .and(scl.neq(11)); // Bukan awan
      return image.updateMask(mask); // Terapkan masker ke citra
    };

![](https://cdn-images-1.medium.com/max/1024/1*kn_Hk4YgY0Jc_GWvST9x4g.png)

Tabel 1 . SCL Data Properties (Sumber : <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands>)

Blok kode ini adalah kunci untuk mendapatkan citra bersih dari awan. Kita menggunakan SCL (Scene Classification Layer) dari Sentinel-2 Level-2A untuk menyaring piksel yang mengganggu analisis, seperti awan dan bayangannya.

#### 2. Koleksi Sentinel-2 dan Komposit Median

    // Ambil koleksi Sentinel-2 tahun 2023, hanya area tertentu, dan awan < 20%
    var citra_rgb = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
      .filterDate('2023-01-01', '2023-12-31')           // Filter tahun 2023
      .filterBounds(geometry)                           // Area studi
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) // Hanya citra dengan awan <20%
      .map(sentinel2_mask)                              // Terapkan masking awan
      .median()                                         // Komposit median
      .clip(geometry)                                   // Potong ke batas studi
      .multiply(0.0001);                                // Skala reflektansi

Bagian ini membuat citra komposit tahunan. Kita filter berdasarkan waktu, lokasi, dan cuaca, lalu membuat rata-rata tengah (median) dari semua citra yang lolos. Hasil akhirnya adalah satu citra RGB 2023 yang bersih dari awan.

#### **3. Visualisasi Komposit RGB**

    // Parameter visualisasi RGB
    var vis_rgb = {
      bands: ['B4', 'B3', 'B2'], // Merah, Hijau, Biru (Band bisa disesuaikan)
      min: 0.0,
      max: 0.3,
      gamma: 1.1
    };

    Map.centerObject(geometry, 11); // Pusatkan ke AOI
    Map.addLayer(citra_rgb, vis_rgb, 'Komposit RGB'); // Tambahkan layer ke peta

Agar kita bisa melihat citra sebelum diekspor, kita definisikan parameter visualisasinya. Kita pakai RGB natural (merah, hijau, biru) dan mengatur nilai minimum, maksimum, serta gamma untuk memperbaiki pencahayaan.

#### 4. Ekspor ke Google Drive

    // Ekspor hasil RGB ke Google Drive sebagai file GeoTIFF
    Export.image.toDrive({
      image: citra_rgb.select(['B4', 'B3', 'B2']), // Band RGB saja
      description: 'RGB_Sentinel2_2023',           // Nama task
      folder: 'GEE_Export',                        // Folder tujuan
      fileNamePrefix: 'Komposit_RGB_2023',         // Nama file awal
      region: geometry,                            // Batas wilayah ekspor
      scale: 10,                                   // Resolusi (10 meter)
      crs: 'EPSG:4326',                            // Sistem koordinat WGS 84
      maxPixels: 1e13                              // Batas piksel
    });

Langkah terakhir adalah mengekspor hasilnya ke Drive. Di sini kita hanya ekspor band RGB (B4, B3, B2) dengan resolusi 10 meter. Format output-nya .tif, bisa langsung digunakan di QGIS, ArcGIS, atau software GIS lainnya.

#### 📁 **Output yang Dihasilkan**

- File: Komposit_RGB_2023.tif
- Resolusi: 10 meter
- Lokasi: Folder GEE_Export di Google Drive
- Kegunaan: Klasifikasi lahan, NDVI, interpretasi visual, overlay spasial, dll.

#### 📚 Referensi Tambahan

[Google Earth Engine \| Google for Developers](https://developers.google.com/earth-engine)

> *Cardille, J. A., Crowley, M. A., Saah, D., & Clinton, N. E. (Eds.). (2024).* Cloud-based remote sensing with Google Earth Engine: Fundamentals and applications*. Springer.* [*https://doi.org/10.1007/978-3-031-26588-4*](https://doi.org/10.1007/978-3-031-26588-4)
