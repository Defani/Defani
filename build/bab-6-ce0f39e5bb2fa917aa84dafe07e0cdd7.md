---
title: BAB VI Kesimpulan dan Saran
short_title: BAB VI
numbering:
  figure: false
  table: false
  equation: true
---

Bagian dari skripsi *Pemodelan Simpanan Karbon Mangrove Berbasis Citra Sentinel 2A di Muara Sungai Cipunegara, Subang, Jawa Barat* · [Daftar isi](../skripsi.md)

(s6-1-kesimpulan)=
## 6.1 Kesimpulan

1.  Klasifikasi tutupan mangrove di Muara Sungai Cipunegara menggunakan algoritma *Random Forest* pada citra Sentinel-2A menghasilkan luasan sebesar 710,44 ha dengan tingkat akurasi yang sangat baik, yaitu *overall accuracy* 95,4% dan koefisien kappa 94,87%.

2.  Berdasarkan hasil pengukuran lapangan, rata-rata simpanan karbon atas permukaan (*Above Ground Carbon*/AGC) mangrove di lokasi penelitian adalah sebesar 80,21 ± 30,46 ton/ha. Nilai simpanan karbon ini bervariasi dengan rentang minimum sebesar 0,25 ton/ha hingga maksimum mencapai 152,73 ton/ha, pada kawasan yang didominasi oleh spesies *Avicennia marina* dan *Avicennia alba*.

3.  Hubungan antara indeks vegetasi citra Sentinel-2A dengan simpanan karbon menunjukkan variasi sensitivitas. Indeks berbasis normalisasi (NDVI) rentan mengalami saturasi pada area dengan tutupan kanopi rapat (R² = 0,345), sedangkan indeks yang memanfaatkan kanal *red-edge* (IRECI) memiliki korelasi yang jauh lebih baik (R² = 0,739) dalam merespons gradasi kandungan biomassa dan karbon.

4.  Kombinasi indeks vegetasi ganda (*Double Index*) terbukti memberikan akurasi prediktif yang lebih tinggi dibandingkan indeks tunggal. Kombinasi indeks IRECI dan TRVI merupakan prediktor terbaik yang paling mampu merepresentasikan variasi simpanan karbon mangrove di lokasi penelitian, dengan nilai determinasi (R²) sebesar 0,743 dan tingkat galat (RMSE) sebesar 19,724 ton/ha.

5.  Model matematis terbaik untuk estimasi simpanan karbon mangrove yang terkalibrasi secara lokal dirumuskan melalui persamaan regresi linier berganda: AGC = 81,6197(IRECI) - 1,0512(TRVI) - 6,5443. Pengaplikasian model ini melalui *Google Earth Engine* menghasilkan estimasi distribusi spasial simpanan karbon di Muara Sungai Cipunegara yang berada pada rentang 23,21 ton/ha hingga 171,16 ton/ha.

(s6-2-saran)=
## 6.2 Saran

1.  Penentuan sampel dalam penelitian ini telah mempertimbangkan keterwakilan spektral berdasarkan indeks NDVI, penyebaran petak ukur dapat diperinci dengan stratifikasi pada variasi nilai indeks Red-Edge atau menggunakan indeks vegetasi berkonstanta seperti EVI dan SAVI untuk mereduksi keterbatasan NDVI, karena meski menurut Santoso *et al* (2026) mangrove Cipunegara homogen pada tingkat regional, namun pada tingkat lanskap memiliki karakteristik heterogen pada kondisi biofisik yang menjadi batasan penelitian ini pada proses pengukuran lapangan.

2.  Eksplorasi indeks Red-Edge tambahan seperti NDRE, CIre, SRre, dan mRE-SR direkomendasikan untuk mengurangi efek saturasi sinyal optis dan memberi gambaran yang lebih detail untuk algoritma pembeljaran mesin dalam memprediksi variasi biomasa.

3.  Penerapan algoritma pembelajaran mesin linnear tetap direkomendasikan guna menghasilkan persamaan matematis praktis untuk pemantauan cepat dan multitemporal.

4.  Integrasi data multisensor, seperti radar sintetis Sentinel-1 SAR atau LiDAR GEDI, direkomendasikan untuk meningkatkan akurasi estimasi struktur tinggi kanopi yang tidak dapat dideteksi oleh sensor optis.

5.  Jika penelitian lanjutan akan menggunakan sensor Landsat, maka direkomendasikan menggunakan sensor Landsat 10 dengan 26 kanal turunan, yang akan rilis pada tahun 2030.

6.  Penggunaan algoritma Cloud Score+ dengan nilai ambang batas (*threshold*) ≥ 0,60 pada kanal *cs_cdf* direkomendasikan, krena terbukti menghasilkan komposit piksel yang lebih bersih dan representatif untuk analisis indeks vegetasi dan pemetaan mangrove berbasis Sentinel-2A.

7.  Model yang dihasilkan dalam penelitian ini dapat dimanfaatkan sebagai metode estimasi karbon secara cepat pada tahap awal pemantauan ekosistem mangrove di Muara Sungai Cipunegara sebelum tersedianya model yang terpublikasi dengan tingkat presisi lebih tinggi.

&nbsp;

S.
