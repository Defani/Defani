---
title: "Map-Biomas-Land-cover-Style-QGIS"
---

[Repositori di GitHub](https://github.com/Defani/Map-Biomas-Land-cover-Style-QGIS)

Repository ini menyediakan **Library Simbol (Style Manager)** untuk data vektor **MapBiomas Indonesia Koleksi 3.0**.

Dengan mengimpor library ini, Anda dapat menyimpan palet warna resmi MapBiomas secara permanen di QGIS dan mencarinya dengan mudah menggunakan kode angka nilai piksel (DN). Simbologi ini mengacu pada dokumen *ATBD MapBiomas ID Col 3.0*.

## File Library

* **Nama File:** `MapBiomas_Library_Fix.xml`
* **Fungsi:** Menambahkan 14 simbol resmi ke dalam Style Manager QGIS.
* **Fitur Pencarian:** Simbol diberi nama unik (contoh: `[3] Formasi Hutan`) agar Anda bisa mencari warna hanya dengan mengetik angka ID-nya.

---

## Cara Penggunaan

Berikut adalah panduan cepat cara mengimpor dan menggunakan library ini:

![Demo Cara Pakai](https://raw.githubusercontent.com/Defani/Map-Biomas-Land-cover-Style-QGIS/main/tutorial_mapbiomas.gif)

---

## Cara Instalasi & Penggunaan

Ikuti langkah ini untuk memasukkan simbol ke QGIS Anda:

1.  **Unduh** file `MapBiomas_Library_Fix.xml` dari repository ini.
2.  Buka **QGIS**, lalu klik menu **Settings** > **Style Manager...**
3.  Klik tombol **Import / Export** di bagian kiri bawah, lalu pilih **Import Item(s)...**
4.  Pada pilihan file, ubah format file menjadi **XML files (*.xml)**.
5.  Pilih file `MapBiomas_Library_Fix.xml`.
6.  Klik **Select All** untuk memilih semua simbol, lalu klik **Import**.
7.  **Selesai!** Simbol sudah tersimpan.


## Persiapan File
1. Import File raster tutupan lahan
2. raster >conversion>raster to polygon>by DN>OK

https://github.com/user-attachments/assets/93d609e6-79f7-4733-935c-0ab42382cc36

## Cara Memakai di Layer
Saat Anda ingin mewarnai layer (baik *Single Symbol* atau *Categorized*):
1.  Klik kotak warna (Symbol Selector).
2.  Di kolom pencarian, ketik kode angka dengan kurung siku.
    * Contoh: Ketik **`[3]`** untuk mendapatkan warna Hutan.
    * Contoh: Ketik **`[35]`** untuk mendapatkan warna Sawit.


https://github.com/user-attachments/assets/d2fd64f6-5492-4e1b-87a8-e375941c1bef


---

## Tabel Legenda (Kelas & Kode)

Referensi kode warna berdasarkan dokumen ATBD MapBiomas Indonesia Koleksi 3.

| ID | Simbol | Nama Kelas (Indonesia) | Nama Kelas (English) |
| :---: | :---: | :--- | :--- |
| **3** | `#1f8d49`<br>![](https://placehold.co/30x15/1f8d49/1f8d49.png) | Formasi Hutan | Forest Formation |
| **5** | `#04381d`<br>![](https://placehold.co/30x15/04381d/04381d.png) | Mangrove | Mangrove |
| **76** | `#2f7360`<br>![](https://placehold.co/30x15/2f7360/2f7360.png) | Hutan Rawa Gambut | Peat Swamp Forest |
| **13** | `#d89f5c`<br>![](https://placehold.co/30x15/d89f5c/d89f5c.png) | Tumbuhan Non-Hutan Lainnya | Other Natural Veg |
| **40** | `#c71585`<br>![](https://placehold.co/30x15/c71585/c71585.png) | Sawah | Rice Paddy |
| **35** | `#9065d0`<br>![](https://placehold.co/30x15/9065d0/9065d0.png) | Sawit | Oil Palm |
| **9** | `#7a5900`<br>![](https://placehold.co/30x15/7a5900/7a5900.png) | Kebun Kayu | Pulpwood Plantation |
| **21** | `#ffefc3`<br>![](https://placehold.co/30x15/ffefc3/ffefc3.png) | Pertanian Lainnya | Other Agriculture |
| **30** | `#9c0027`<br>![](https://placehold.co/30x15/9c0027/9c0027.png) | Lubang Tambang | Mining Pit |
| **24** | `#d4271e`<br>![](https://placehold.co/30x15/d4271e/d4271e.png) | Permukiman | Urban Area |
| **25** | `#db4d4f`<br>![](https://placehold.co/30x15/db4d4f/db4d4f.png) | Non-Vegetasi Lainnya | Other Non-Vegetation |
| **31** | `#091077`<br>![](https://placehold.co/30x15/091077/091077.png) | Tambak | Aquaculture |
| **33** | `#2532e4`<br>![](https://placehold.co/30x15/2532e4/2532e4.png) | Sungai, Danau, Laut | Water Body |
| **27** | `#ffffff`<br>![](https://placehold.co/30x15/ffffff/ffffff.png) | Citra Tertutup Awan | Cloud / Not Observed |

---
## Hasil
<img width="3507" height="2480" alt="lll" src="https://github.com/user-attachments/assets/e9b38bfb-164e-4c0c-a196-f90f7e2f81c8" />
## ℹ️ Sumber Referensi

Gaya dan klasifikasi ini didasarkan pada dokumen:
* **Judul:** ATBD MapBiomas Indonesia Koleksi 3
* **Dokumen:** [Link download ](https://landy.mapbiomas.id/assets/files/ATBD%20MapBiomas%20ID%20Col%203.0.pdf)

Website Map Biomas : https://platform.indonesia.mapbiomas.org/
---
