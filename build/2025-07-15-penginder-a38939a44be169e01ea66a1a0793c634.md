---
title: 'Penginderaan Jarak Jauh Dasar Menggunakan Bahasa R | Analisis NDVI Citra Satelit Sentinel 2A'
date: 2025-07-15
tags: ['sentinel', 'r-programming', 'remotesensingtech', 'rstudio', 'ndvi']
---

15 July 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/penginderaan-jarak-jauh-dasar-menggunakan-bahasa-r-analisis-ndvi-citra-satelit-sentinel-2a-242237e5c396) · [Semua tulisan](../blog.md)

Oleh : Defani Arman A

Dalam analisis spektral, banyak platform tersedia, namun saya memilih **R** karena bersifat open-source, kuat dalam analisis data spasial, serta didukung oleh banyak paket seperti raster, terra, dan sf. Selain itu, R memungkinkan integrasi langsung antara statistik, visualisasi, dan pengolahan citra satelit dalam satu lingkungan kerja.

Seri ini saya buat untuk membantu memahami konsep dasar analisis spektral menggunakan R, dimulai dari perhitungan **NDVI**, salah satu indeks vegetasi paling umum dalam penginderaan jauh.

### **NDVI (Normalized Difference Vegetation Index)**

**NDVI (Normalized Difference Vegetation Index)** adalah salah satu indeks vegetasi paling populer dalam penginderaan jauh yang digunakan untuk memantau kondisi dan kerapatan vegetasi di permukaan bumi. Indeks ini **diciptakan oleh Rouse et al. pada tahun 1973** melalui penelitian legendaris yang berjudul *“Monitoring Vegetation Systems in the Great Plains with ERTS”* di Texas A&M University. Dalam penelitian tersebut, Rouse dan timnya memanfaatkan data satelit ERTS‑1 (kemudian dikenal sebagai Landsat‑1) untuk memantau rangeland di kawasan Great Plains, Amerika Serikat. Mereka mengembangkan sebuah metode kuantitatif untuk mengukur kondisi vegetasi dengan menggunakan rasio pantulan antara panjang gelombang **inframerah dekat (NIR)** dan **merah (Red)**. Hasil penelitian itu menunjukkan bahwa rasio ini sangat berkorelasi dengan biomassa hijau di atas permukaan tanah dan kelembapan vegetasi, sehingga dapat menjadi indikator efektif kondisi vegetasi secara regional.

Secara matematis, NDVI dirumuskan sebagai:

NDVI = (Near Infrared-Red)/(Near Infrared+Red)

di mana **NIR** adalah nilai pantulan pada band inframerah dekat dan **RED** adalah nilai pantulan pada band merah. Nilai NDVI berkisar antara –1 hingga +1. Nilai mendekati +1 menunjukkan vegetasi sehat dan lebat karena tanaman sehat memantulkan banyak cahaya inframerah dekat dan menyerap banyak cahaya merah untuk fotosintesis. Nilai mendekati 0 biasanya menunjukkan tanah terbuka atau area dengan vegetasi jarang, sedangkan nilai negatif mengindikasikan badan air atau objek non‑vegetasi.

Dalam konteks citra **Sentinel‑2** yang digunakan dalam contoh ini, NDVI dihitung dengan memanfaatkan **Band 8 (Near Infrared)** sebagai NIR dan **Band 4 (Red)** sebagai RED. Kedua band ini sudah disimpan dalam format **GeoTIFF (.tif)** dan siap diproses di R. Berkat kesederhanaannya, NDVI hingga saat ini tetap menjadi indeks dasar yang digunakan luas dalam kehutanan, pertanian, pemantauan lahan, dan berbagai bidang lain yang membutuhkan informasi cepat dan akurat mengenai kondisi vegetasi.

![](https://cdn-images-1.medium.com/max/612/1*FRhVW2d5ZiiQmvqBAT-F-w.png)

Nilai NDVI pada setiap tipe objek di bumi (Rizvi et al., 2009)

### **Instalasi Perangkat Lunak R Studio**

Sebelum melakukan analisis penginderaan jauh di R, kita perlu memastikan lingkungan kerja sudah siap. Langkah pertama adalah memastikan perangkat lunak **R** dan **RStudio** sudah terpasang di komputer. R dapat diunduh dari situs resmi CRAN di <https://cran.r-project.org/>dan RStudio sebagai Integrated Development Environment (IDE) yang memudahkan penulisan kode dapat diunduh di <https://posit.co/download/rstudio-desktop/>. Setelah keduanya terpasang, kita dapat mulai menginstal package yang dibutuhkan. Berikut merupakan antar muka software R Studio

![](https://cdn-images-1.medium.com/max/1024/1*_Eon6qjy-zT_QvzLCEDJUA.png)

Antarmuka Software R Studio (Sumber : Tangkapan Layar)

### Pengenalan Package raster

Dalam dunia penginderaan jauh, data citra satelit umumnya disimpan dalam format **raster**, yaitu kumpulan grid piksel yang merepresentasikan nilai reflektansi atau intensitas dari permukaan bumi. Setiap piksel menyimpan angka yang dapat diolah menjadi informasi, misalnya untuk memetakan vegetasi, permukaan air, atau penggunaan lahan. Untuk memproses data jenis ini di R, komunitas geospasial mengandalkan sebuah package penting bernama **raster**.

Package **raster** dikembangkan oleh **Robert J. Hijmans** sebagai penulis utama sekaligus maintainer, dengan kontribusi dari banyak pakar lain seperti Jacob van Etten, Michael Sumner, Joe Cheng, Dan Baston, Andrew Bevan, Roger Bivand, Lorenzo Busetto, Mort Canty, dan masih banyak lagi. Sejak awal pengembangannya sekitar tahun **2010**, raster terus berevolusi dan menjadi standar de facto untuk analisis data raster di lingkungan R. Versi yang tercatat pada dokumentasi terbaru adalah **versi 3.6‑32**, yang dirilis di CRAN pada **28 Maret 2025**, menandakan bahwa pengembangannya tetap aktif dan relevan hingga kini.

Tujuan dibuatnya package ini adalah untuk **membaca, menulis, memanipulasi, menganalisis, dan memodelkan data raster** secara efisien, bahkan untuk data dengan ukuran sangat besar yang tidak dapat dimuat sepenuhnya ke memori. Package ini menyediakan kelas objek seperti **RasterLayer**, **RasterStack**, dan **RasterBrick** untuk mengelola data raster tunggal maupun multi‑band. Dengan raster, pengguna dapat melakukan operasi matematika antar layer (dikenal sebagai *raster algebra*), mengubah resolusi atau proyeksi, melakukan cropping dan masking, menghitung statistik seperti rata‑rata atau histogram, serta membuat peta tematik dengan fungsi plot() atau plotRGB().

Meskipun saat ini sudah tersedia package penerus bernama **terra** yang lebih modern, raster tetap banyak digunakan karena dokumentasinya yang sangat lengkap, kompatibilitasnya dengan berbagai tutorial lama, dan komunitas pengguna yang besar. Tidak heran jika raster menjadi langkah awal yang tepat untuk mempelajari dasar‑dasar penginderaan jauh menggunakan Bahasa R, sebelum nantinya beralih ke package yang lebih baru seperti terra.

### **Instalasi Package raster**

Sebelum menggunakan fungsi‑fungsi yang disediakan oleh package **raster**, kita harus memastikan bahwa package tersebut sudah terinstal di dalam lingkungan R. Proses instalasinya sangat sederhana dan hanya perlu dilakukan satu kali saja. Pastikan R dan RStudio sudah terpasang dengan baik di komputer, kemudian buka RStudio dan pastikan perangkat terhubung ke internet. Ketik perintah install.packages("raster") pada konsol lalu tekan Enter. R secara otomatis akan mengunduh package raster dari repositori CRAN dan memasangnya di sistem. Setelah proses instalasi selesai, setiap kali memulai sesi baru di RStudio kita harus memanggil package ini ke memori dengan menggunakan perintah library(raster). Langkah ini wajib dilakukan agar fungsi‑fungsi seperti raster(), plot(), atau operasi aljabar raster dapat digunakan tanpa menimbulkan error. Dengan selesainya tahap instalasi dan pemanggilan package, maka lingkungan kerja R sudah siap untuk membaca dan mengolah data raster.

    install.packages("raster")

![](https://cdn-images-1.medium.com/max/1024/1*dYnIxODNBxX-pSvZXb1p3A.png)

Instalasi Package raster (Sumber : Tangkapan Layar)

### **Membaca Data Raster Sentinel 2A**

Setelah package **raster** berhasil diinstal dan dimuat, tahap berikutnya adalah membaca data raster yang sudah diunduh. Pada contoh ini digunakan data **Sentinel‑2** dengan dua band utama yang diperlukan untuk perhitungan NDVI, yaitu Band 8 (NIR) dan Band 4 (Red). Kedua file tersebut sudah disimpan di komputer dalam format **GeoTIFF (.tif)** dengan nama **B8.tif** untuk Band 8 dan **B4.tif** untuk Band 4. Berikut potongan kode untuk memanggilnya di R:

    NIR <- raster("D:/R/B8.tif")
    RED <- raster("D:/R/B4.tif")

![](https://cdn-images-1.medium.com/max/1024/1*jaN2Ey4uWSGYVmMUe8KhOw.png)

Memanggil data raster (Sumber : Tangkapan Layar)

**Penjelasan tiap bagian kode:**

- **raster()** → Fungsi dari package raster untuk membaca file raster dari direktori lokal.
- **"D:/R/B8.tif"** → Path lengkap file Band 8 (Near Infrared/NIR) Sentinel‑2 dalam format GeoTIFF.
- **"D:/R/B4.tif"** → Path lengkap file Band 4 (Red) Sentinel‑2 dalam format GeoTIFF.
- **\<-** → Operator assignment yang menyimpan hasil pembacaan ke variabel di sebelah kiri.
- **NIR** → Variabel untuk menyimpan objek raster hasil pembacaan Band 8 (NIR).
- **RED** → Variabel untuk menyimpan objek raster hasil pembacaan Band 4 (Red).

Setelah kedua perintah ini dijalankan, objek NIR dan RED sudah tersedia di memori R dan siap untuk diolah lebih lanjut. Tahap ini sangat penting karena menjadi dasar dari setiap perhitungan berikutnya. Dengan memuat band NIR dan Red ke dalam R, kita telah menyiapkan data yang diperlukan untuk perhitungan NDVI, yang akan dibahas pada subbab selanjutnya. Meskipun pada langkah ini kita belum melakukan perhitungan apa pun, memastikan bahwa data sudah terbaca dengan benar adalah kunci utama untuk mencegah kesalahan di proses berikutnya.

### **Menghitung NDVI**

etelah data raster Band 8 (NIR) dan Band 4 (Red) dari Sentinel‑2 berhasil dibaca, langkah berikutnya adalah menghitung **NDVI** menggunakan operasi aljabar raster. Package raster memungkinkan kita melakukan operasi matematika langsung di antara dua objek raster, sehingga perhitungan NDVI dapat ditulis dengan sangat sederhana. Berikut kode yang digunakan:

    NDVI <- (NIR-RED)/(NIR+RED)

![](https://cdn-images-1.medium.com/max/1024/1*Bbwoh0yeFLUJacmVWXVt2Q.png)

Menghitung NDVI (Sumber : Tangkapan Layar)

**Penjelasan kode:**

- **NIR - RED** menghitung selisih nilai piksel antara Band 8 (Near Infrared) dan Band 4 (Red).
- **NIR + RED** menghitung jumlah nilai piksel antara kedua band.
- **/** membagi hasil selisih dengan hasil jumlah untuk setiap piksel, sehingga menghasilkan nilai NDVI.
- **NDVI** adalah variabel baru yang menyimpan hasil raster NDVI.

Pada tahap ini, kita sudah memiliki objek raster NDVI di memori R yang siap digunakan untuk berbagai analisis lebih lanjut.

### **Memvisualisasikan Hasil Perhitungan NDVI**

Setelah NDVI selesai dihitung, kita dapat memvisualisasikannya menjadi peta tematik sehingga lebih mudah dipahami. Package raster menyediakan fungsi plot() yang dapat langsung digunakan untuk menampilkan raster di jendela grafis. Kita juga dapat menambahkan judul dengan parameter main untuk memberi keterangan pada peta. Untuk menjalankan semua kode dilakukan dengan menekan tombol “run” atau dengan ctrl + A lalu tekan “enter” . Berikut contohnya:

    plot(NDVI, main = "Normalized Difference Vegetation Index")

![](https://cdn-images-1.medium.com/max/1024/1*sL9XBEB7hi-b330F-y363g.png)

Menampilkan Visualisasi NDVI (Sumber : Tangkapan Layar)

**Penjelasan kode:**

- **plot(NDVI)** memanggil fungsi untuk menampilkan raster NDVI sebagai peta.
- **main = "Normalized Difference Vegetation Index"** menambahkan judul pada peta agar pembaca peta tahu bahwa yang ditampilkan adalah hasil NDVI.

Hasil visualisasi akan menampilkan peta dengan rentang nilai NDVI dari –1 hingga +1. Warna pada peta menunjukkan variasi nilai NDVI di seluruh area citra. Nilai mendekati +1 tampak pada area dengan vegetasi sehat, nilai mendekati 0 menunjukkan area dengan vegetasi jarang atau tanah terbuka, sedangkan nilai negatif umumnya terlihat pada area perairan atau objek non‑vegetasi. Visualisasi akan tampil sebagai berikut

![](https://cdn-images-1.medium.com/max/1024/1*euhOHiGg--3QFigVdw0f2A.png)

Plot NDVI dalam antarmuka R Studio (Sumber : Tangkapan Layar)

![](https://cdn-images-1.medium.com/max/1024/1*7vl7i5B3vGH0i9IIFuh9HQ.png)

Menyimpan Hasil NDVI dalam format “GeoTIFF)

Setelah NDVI dihitung dan divisualisasikan, kita sering kali memerlukan penyimpanan hasil dalam bentuk file baru agar dapat digunakan kembali tanpa perlu menghitung ulang. Package **raster** menyediakan fungsi writeRaster() untuk menyimpan objek raster ke berbagai format file, termasuk GeoTIFF (.tif) yang umum digunakan dalam aplikasi GIS. Menyimpan hasil NDVI juga berguna ketika kita ingin membagikannya kepada orang lain atau menggunakannya di perangkat lunak GIS lain seperti QGIS atau ArcGIS. Berikut contoh kode untuk menyimpan NDVI ke dalam file GeoTIFF:

    writeRaster(NDVI, "D:/R/NDVI.tif", format = "GTiff", overwrite = TRUE)

**Penjelasan kode:**

- ✅ **NDVI** adalah objek raster yang akan disimpan.
- ✅ **"D:/R/NDVI.tif"** adalah lokasi dan nama file output yang dihasilkan.
- ✅ **format = "GTiff"** memastikan file disimpan sebagai GeoTIFF.
- ✅ **overwrite = TRUE** memperbolehkan file lama dengan nama yang sama untuk ditimpa.

Setelah perintah ini dijalankan, file **NDVI.tif** akan muncul di direktori yang dituju. File tersebut dapat langsung dibuka di perangkat lunak GIS atau diolah kembali dalam sesi R berikutnya. Dengan demikian, hasil analisismu tidak hanya tampil di layar tetapi juga tersimpan sebagai file yang bisa digunakan kapan saja.

### **Mengekspor Layout NDVI ke PNG**

Selain menyimpan hasil NDVI sebagai file raster (GeoTIFF), sering kali kita juga ingin menyimpan tampilan peta NDVI yang sudah divisualisasikan ke dalam bentuk gambar. Format **PNG** sangat umum digunakan untuk laporan, presentasi, atau publikasi karena ringan, mendukung transparansi, dan mudah dibagikan.

Di R, kita bisa menggunakan fungsi png() untuk membuka perangkat grafis PNG, lalu memanggil fungsi plot() untuk membuat peta, dan terakhir menggunakan dev.off() untuk menutup perangkat dan menyimpan file gambar. Berikut contohnya:


    png("D:/R/NDVI_layout.png", width = 1200, height = 1000, res = 150)

    plot(NDVI, main = "Normalized Difference Vegetation Index")

    dev.off()

**Penjelasan kode:**

- **png("D:/R/NDVI_layout.png")** membuka perangkat grafis untuk menulis output ke file PNG dengan nama NDVI_layout.png di folder D:/R/.
- **width dan** **height** mengatur ukuran gambar dalam piksel, sedangkan **res** mengatur resolusi (dpi) untuk hasil yang tajam.
- **plot(NDVI, main = "...")** menampilkan peta NDVI, outputnya akan langsung diarahkan ke file PNG.
- **dev.off()** menutup perangkat grafis, langkah ini wajib dilakukan agar file PNG benar‑benar tersimpan.

### **Penutup**

Melalui artikel **Dasar‑Dasar Penginderaan Jauh Menggunakan Bahasa R (Part 1)** ini, kita telah mempelajari tahapan awal pengolahan citra satelit menggunakan R. Mulai dari instalasi dan pemanggilan package raster, membaca band citra Sentinel‑2, menghitung **Normalized Difference Vegetation Index (NDVI)** yang diciptakan oleh **Rouse et al. (1973)**, menampilkan hasilnya dalam bentuk peta, hingga menyimpannya sebagai file GeoTIFF dan mengekspor layout peta ke PNG. Pemahaman dasar ini menjadi fondasi penting sebelum melangkah ke teknik lanjutan seperti masking, cropping, atau klasifikasi citra. Dengan menguasai langkah‑langkah dasar ini, kamu dapat melakukan analisis vegetasi sederhana yang sudah terbukti secara ilmiah dan siap untuk diterapkan pada berbagai studi lapangan maupun penelitian.

### **Referensi Tulisan**

- **Hijmans, R. J., van Etten, J., Cheng, J., Baston, D., Bevan, A., Bivand, R., et al.** (2025). *raster: Geographic Data Analysis and Modeling.* R package version 3.6‑32. <https://CRAN.R-project.org/package=raster>
- **Rizvi, R. H., Yadav, R. S., Singh, R., Datt, K., Khan, I. A., & Dhyani, S. K.** (2009). *Spectral analysis of remote sensing image for assessment of agroforestry areas in Yamunanagar district of Haryana.* Proceedings of ISRS Symposium 2009.
- **Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W.** (1973). *Monitoring vegetation systems in the Great Plains with ERTS.* NASA Goddard Space Flight Center 3rd ERTS Symposium, NASA SP-351, vol. 1, 309–317.
