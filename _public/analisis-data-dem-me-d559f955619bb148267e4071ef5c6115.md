---
title: "Analisis-Data-DEM-Menggunakan-R"
---

[Repositori di GitHub](https://github.com/Defani/Analisis-Data-DEM-Menggunakan-R)

Pengolahan Data DEM di R untuk Analisis Topografi
Repositori ini berisi skrip R untuk pengolahan data Digital Elevation Model (DEM) guna analisis topografi. Skrip ini mendemonstrasikan alur kerja dasar analisis spasial menggunakan paket 

terra, yang merupakan penerus dari paket raster dengan kinerja lebih baik. Proses yang dicakup meliputi:
Membaca Data: Memuat data DEM dalam format raster (.tif) menggunakan fungsi rast().
Mengkalkulasi kemiringan lereng (slope) dan arah lereng (aspect) dari data DEM menggunakan fungsi terrain().
Membuat Hillshade: Menghasilkan visualisasi efek bayangan (hillshade) untuk memberikan kesan 3D pada topografi dengan fungsi shade().
Visualisasi: Menampilkan tiga peta (Slope, Topografi, dan Hillshade) secara berdampingan dalam satu layout untuk memudahkan interpretasi.
Proyek ini bertujuan untuk menyediakan contoh praktis bagi pengguna yang tertarik pada analisis data spasial di bidang kehutanan, konservasi, tata guna lahan, dan mitigasi bencana menggunakan R.
