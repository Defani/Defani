---
title: 'Dasar Pengolahan DEM dalam bahasa R'
date: 2025-07-18
---

18 July 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/dasar-dasar-pengolahan-data-dem-digital-elevation-model-menggunakan-bahasa-r-slope-topografi-0cb9cccca6b4) · [Semua tulisan](../blog.md)

oleh : Defani Arman Alfitriansyah

![](https://cdn-images-1.medium.com/max/1024/1*ieG5k5AGavaRA32l6PYMWg.jpeg)

### **Pendahuluan**

Digital Elevation Model (DEM) adalah data raster yang menyimpan informasi ketinggian permukaan bumi pada setiap pikselnya. DEM banyak dimanfaatkan dalam bidang kehutanan, konservasi, tata guna lahan, hingga mitigasi bencana. Dari DEM, kita dapat menghitung parameter turunan seperti slope (kemiringan lereng), aspect (arah lereng), dan hillshade (efek bayangan permukaan) yang memudahkan interpretasi topografi.

Salah satu perangkat lunak yang populer untuk analisis data spasial adalah R. Di R, tersedia paket terra yang dirancang khusus untuk memproses dan menganalisis data raster maupun vektor secara efisien. Paket terra dikembangkan oleh Robert J. Hijmans (University of California, Davis) sebagai penerus dari paket raster dengan kinerja yang lebih baik dan dukungan terhadap format data modern. Dokumentasi resminya tersedia di https://CRAN.R-project.org/package=terra.

### **Persiapan**

Sebelum memulai, pastikan Anda sudah menginstal R dan paket terra.

Sebelum memulai, pastikan Anda sudah menginstal R dan paket terra.

    install.packages("terra")

Unduh data DEM (format .tif). Simpan file DEM Anda, misalnya di direktori D:/DEM.tif.

### **Memanggil Data**

Langkah pertama adalah memuat paket terra dan membaca file DEM.

    library(terra)                
    dem <- rast("D:/DEM.tif")   

library(terra) memanggil semua fungsi dari paket terra.

rast("D:/DEM.tif") membaca file DEM bertipe TIFF dan mengubahnya menjadi objek SpatRaster bernama dem.

### Menghitung Slope dan Aspect

Setelah data DEM dimuat, kita dapat menghitung slope (kemiringan) dan aspect (arah lereng).

    slope  <- terrain(dem, v = "slope",  unit = "degrees")
    aspect <- terrain(dem, v = "aspect", unit = "degrees")

terrain() adalah fungsi untuk menghitung turunan medan.

v = "slope" menghitung kemiringan lereng, dengan unit = "degrees" berarti hasilnya dalam derajat.

v = "aspect" menghitung arah lereng menghadap ke mana (azimuth).

### Membuat Hillshide

Untuk memberi efek bayangan pada peta topografi, gunakan fungsi shade().

    hill <- shade(slope, aspect, angle = 45, direction = 315)

aspect, angle = 45, direction = 315)

angle = 45 artinya matahari diasumsikan pada elevasi 45°.

direction = 315 artinya sumber cahaya berasal dari barat laut (315°).\
Hasilnya adalah raster hillshade yang memberi kesan 3D.

### **Mengatur Proporsi Layout**

Agar semua peta tampil berjejer dalam satu baris:

    par(mfrow = c(1,3), mar = c(4,4,4,6))

mfrow = c(1,3) artinya satu baris tiga kolom.

mar = c(4,4,4,6) mengatur margin (bawah, kiri, atas, kanan).

### Visualisasi Hasil

#### slope

    plot(slope, col = terrain.colors(100),
         main = "Slope Kecamatan Rancah",
         plg = list(title = "Derajat"))
    grid(col = "gray50", lty = 1, lwd = 0.4)

plot() memvisualisasikan raster slope.

terrain.colors(100) memberi palet gradasi medan.

main memberi judul peta, plg memberi judul legenda.

grid() menambahkan garis grid.

### Peta Topografi (DEM)

    plot(dem, col = rev(topo.colors(100)),
         main = "Topografi Kecamatan Rancah",
         plg = list(title = "MDPL"))
    grid(col = "gray50", lty = 1, lwd = 0.4)

rev(topo.colors(100)) membalik gradasi warna topografi.

**Legenda diberi satuan MDPL (meter di atas permukaan laut).**

### **Peta Hillshade**

    plot(hill, col = gray.colors(100, start = 0, end = 1),
         main = "Hillshade Kecamatan Rancah")
    grid(col = "gray50", lty = 1, lwd = 0.4)

gray.colors() membuat palet gradasi abu‑abu.

Hasilnya memberikan efek 3D yang memudahkan interpretasi medan.

### **Kesimpulan**

Paket terra menyediakan fungsi yang lengkap dan efisien untuk mengolah data DEM di R. Dengan beberapa langkah sederhana, kita dapat membaca data DEM, menghitung slope dan aspect, hingga membuat hillshade. Visualisasi ini sangat membantu dalam analisis spasial, khususnya di bidang kehutanan, konservasi, dan perencanaan tata ruang.

### **Referensi**

Hijmans, R. J. (2024). terra: Spatial Data Analysis. R package version 1.7‑78. Available at: https://CRAN.R-project.org/package=terra

Hijmans, R. J., & van Etten, J. (2012). raster: Geographic analysis and modeling with raster data. R package version 3.6-20.
