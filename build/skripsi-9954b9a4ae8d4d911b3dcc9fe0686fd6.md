---
title: Skripsi
subtitle: Pemodelan Simpanan Karbon Mangrove Berbasis Citra Sentinel 2A di Muara Sungai Cipunegara, Subang, Jawa Barat
short_title: Skripsi
---

:::{figure} assets/skripsi/image1.png
:width: 160px
:align: center
:::

**Pemodelan Simpanan Karbon Mangrove Berbasis Citra Sentinel 2A di Muara Sungai Cipunegara, Subang, Jawa Barat**

Defani Arman Alfitriansyah · Program Studi Kehutanan, Fakultas Kehutanan dan Lingkungan, Universitas Kuningan · 2026

Pembimbing: Dede Kosasih, S.Hut., M.Si dan Dr. Iing Nasihin, S.Hut., M.Si

:::{note} Draf
Ini draf skripsi yang dibukukan di web. Isi bisa berubah sampai versi akhir disahkan.
:::

## Abstract

DEFANI ARMAN ALFITRIANSYAH. *Mangrove Carbon Stock Modeling Based on Sentinel-2A Imagery in the Cipunegara River Estuary, Subang, West Java.* *Supervised by* DEDE KOSASIH *and* IING NASIHIN.

*Mangrove forests play a vital role in mitigating climate change due to their high carbon sequestration capacity. However, traditional field measurements for carbon estimation are time-consuming and limited in spatial coverage. This study aims to develop a locally calibrated Above Ground Carbon (AGC) estimation model for the mangrove ecosystem in the Cipunegara River Estuary, West Java, utilizing Sentinel-2A imagery and python based cloud computing platform. Field data were collected from 25 plots to measure the diameter at breast height (DBH) and calculate AGC using allometric equations. Spatial analysis involved cloud masking using Cloud Score+ and mangrove mapping via the Random Forest classifier. The study evaluated three vegetation indices (NDVI, IRECI, and TRVI) and their combinations through linear regression models.*

*The classification identified 710.44 ha of mangrove area with an overall accuracy of 95.4%. Field measurements revealed an average AGC of 80.21 ton/ha, dominated by Avicennia genus. The supervised regression analysis demonstrated that the combination of IRECI and TRVI yielded the most accurate predictive model, outperforming single indices like NDVI, which suffered from spectral saturation. The optimal model achieved a Coefficient of Determination (R{sup}`2`) of 0.743 and a Root Mean Square Error (RMSE) of 19.724 ton/ha. The resulting mathematical equation* $AGC = 81.6197(IRECI) - 1.0512(TRVI) - 6.5443$*, was applied to generate a spatial carbon map, estimating AGC values between 23.21 and 171.16 ton/ha. This study confirms that integrating red-edge and near-infrared bands significantly enhances the accuracy of mangrove carbon modeling.*

*Keywords : AGB, Sentinel 2A, Remote Sensing\*

## Daftar Isi

- [**Persembahan dan Kata Pengantar**](skripsi/kata-pengantar.md)
- [**BAB I Pendahuluan**](skripsi/bab-1.md)
  - [1.1 Latar Belakang](#s1-1-latar-belakang)
  - [1.2 Identifikasi Masalah](#s1-2-identifikasi-masalah)
  - [1.3 Rumusan Masalah](#s1-3-rumusan-masalah)
  - [1.4 Batasan Masalah](#s1-4-batasan-masalah)
  - [1.5 Tujuan](#s1-5-tujuan)
  - [1.6 Manfaat](#s1-6-manfaat)
- [**BAB II Kajian Pustaka**](skripsi/bab-2.md)
  - [2.1 Kajian Teori](#s2-1-kajian-teori)
    - [2.1.1 Simpanan Karbon Mangrove dan Potensinya dalam Mitigasi Perubahan Iklim di Indonesia](#s2-1-1-simpanan-karbon-mangrove-dan-potensinya-dalam-mitigasi-perub)
    - [2.1.2 Penginderaan Jauh Berbasis Komputasi Awan dalam Permodelan dan Estimasi Simpanan Karbon Mangrove](#s2-1-2-penginderaan-jauh-berbasis-komputasi-awan-dalam-permodelan-d)
    - [2.1.3 Citra Sentinel 2A](#s2-1-3-citra-sentinel-2a)
  - [2.2 Kajian Hasil Penelitian](#s2-2-kajian-hasil-penelitian)
  - [2.3 Kerangka Pemikiran](#s2-3-kerangka-pemikiran)
- [**BAB III Metode Penelitian**](skripsi/bab-3.md)
  - [3.1 Desain Penelitian](#s3-1-desain-penelitian)
  - [3.2 Lokasi dan Waktu Penelitian](#s3-2-lokasi-dan-waktu-penelitian)
  - [3.3 Populasi dan Sampel Penelitian](#s3-3-populasi-dan-sampel-penelitian)
  - [3.4 Definisi Operasional Variabel](#s3-4-definisi-operasional-variabel)
  - [3.5 Pengumpulan data](#s3-5-pengumpulan-data)
  - [3.6 Teknik Analisis Data](#s3-6-teknik-analisis-data)
- [**BAB IV Kondisi Umum Lokasi Penelitian**](skripsi/bab-4.md)
  - [4.1 Letak Geografis](#s4-1-letak-geografis)
  - [4.2 Kondisi Lingkungan](#s4-2-kondisi-lingkungan)
- [**BAB V Hasil dan Pembahasan**](skripsi/bab-5.md)
  - [5.1 Tutupan Mangrove di Muara Sungai Cipunegara](#s5-1-tutupan-mangrove-di-muara-sungai-cipunegara)
  - [5.2 Simpanan Biomassa dan Karbon](#s5-2-simpanan-biomassa-dan-karbon)
  - [5.3 Indeks Vegetasi](#s5-3-indeks-vegetasi)
  - [5.4 Model Simpanan Karbon](#s5-4-model-simpanan-karbon)
- [**BAB VI Kesimpulan dan Saran**](skripsi/bab-6.md)
  - [6.1 Kesimpulan](#s6-1-kesimpulan)
  - [6.2 Saran](#s6-2-saran)
- [**Daftar Pustaka**](skripsi/daftar-pustaka.md)
- [**Lampiran**](skripsi/lampiran.md)

## Daftar Gambar

- [Gambar 1. Simpanan Karbon di Berbagai Ekosistem (Taillardat et al., 2018)](skripsi/bab-2.md)
- [Gambar 2. Kerangka Pemikran](skripsi/bab-2.md)
- [Gambar 3. Desain Penelitian](skripsi/bab-3.md)
- [Gambar 4. Peta Lokasi Penelitian](skripsi/bab-3.md)
- [Gambar 1. Desain Petak ukur Pengukuan DBH (Suardana et al., 2023)](skripsi/bab-3.md)
- [Gambar 5.Ketentuan Pengukuran DBH Mangrove Di Berbagai Kondisi Dan Tipe Vegetasi (Pearson et al., 2005)](skripsi/bab-3.md)
- [Gambar 6. Algoritma Random Forest dalam Pemetaan Mangrove (Jamaluddin et al., 2022)](skripsi/bab-3.md)
- [Gambar 7. Komparasi Komposit Citra Pra dan Pasca Masking Awan di Muara Sungai Cipunegara](skripsi/bab-5.md)
- [Gambar 8. Peta Sebaran Mangrove di Muara Sungai Cipunegara (Hasil Klasifikasi Citra Sentinel 2A)](skripsi/bab-5.md)
- [Gambar 9. Kondisi Mangrove Muara Sungai Cipunegara](skripsi/bab-5.md)
- [Gambar 10. Sebaran Biomassa dan Karbon Pada Petak Pengukuran](skripsi/bab-5.md)
- [Gambar 11. Nilai Reflektansi Indeks Pada 25 Petak Pengukuran](skripsi/bab-5.md)
- [Gambar 12. Sebaran NDVI Mangrove Muara Sungai Cipunegara](skripsi/bab-5.md)
- [Gambar 13. Sebaran IRECI Mangrove Muara Sungai Cipunegara](skripsi/bab-5.md)
- [Gambar 14. Sebaran TRVI Mangrove Muara Cipunegara](skripsi/bab-5.md)
- [Gambar 15. Komparasi Performa Model](skripsi/bab-5.md)
- [Gambar 16. Visualisasi Model Spasial Simpanan Karbon Mangrove](skripsi/bab-5.md)

## Daftar Tabel

- [Tabel 1. Metode Estimasi dan Pengukuran Karbon Mangrove](skripsi/bab-2.md)
- [Tabel 2. Deksripsi Kanal Citra Sentinel 2A](skripsi/bab-2.md)
- [Tabel 3. Kanal Masking Awan Citra Sentinel 2A](skripsi/bab-2.md)
- [Tabel 4 Perhitungan penilaian akurasi klasifikasi citra](skripsi/bab-3.md)
- [Tabel 5 Tingkat Kepercayaan Hasil Klasifikasi](skripsi/bab-3.md)
- [Tabel 6. Persamaan Indeks Vegetasi dalam Permodelan Karbon di Atas Permukaan](skripsi/bab-3.md)
- [Tabel 7. Kanal Sentinel 2A dalam perhitungan indeks vegetasi](skripsi/bab-3.md)
- [Tabel 8. Model Alometrik Jenis Mangrove Muara Sungai Cipunegara](skripsi/bab-3.md)
- [Tabel 9. Komposisi Variabel Permodelan Regresi](skripsi/bab-3.md)
- [Tabel 10. Persamaan Matematis Model Simapanan Karbon](skripsi/bab-5.md)

## Daftar Lampiran

- [Lampiran 1.Tallysheet Pengukuran Parameter Biomassa Mangrove](skripsi/lampiran.md)
- [Lampiran 3. Tabel Uji Regresi Linier](skripsi/lampiran.md)
- [Lampiran 4. Output Pemodelan Scikitlearn](skripsi/lampiran.md)
- [Lampiran 5. Srip Kode Analisis](skripsi/lampiran.md)
- [Lampiran 6. Dokumentasi Program Komputasi](skripsi/lampiran.md)
- [Lampiran 7. Dokumentasi Survei Lapangan](skripsi/lampiran.md)
