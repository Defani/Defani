---
title: BAB II Kajian Pustaka
short_title: BAB II
numbering:
  figure: false
  table: false
  equation: true
---

Bagian dari skripsi *Pemodelan Simpanan Karbon Mangrove Berbasis Citra Sentinel 2A di Muara Sungai Cipunegara, Subang, Jawa Barat* · [Daftar isi](../skripsi.md)

(s2-1-kajian-teori)=
## 2.1 Kajian Teori

(s2-1-1-simpanan-karbon-mangrove-dan-potensinya-dalam-mitigasi-perub)=
### 2.1.1 Simpanan Karbon Mangrove dan Potensinya dalam Mitigasi Perubahan Iklim di Indonesia

Secara global, mangrove merupakan hutan pesisir dengan potensi besar sebagai solusi iklim berbasis ekosistem. Meskipun memiliki luasan spasial yang terbatas di tingkat global, potensi karbon biru mangrove sangat efektif dalam mitigasi perubahan iklim pada skala nasional (Taillardat *et al*., 2018). Hutan mangrove di seluruh dunia diperkirakan menyimpan antara 3,1 hingga 12,3 gigaton karbon (GtC) (Sasmito *et al*., 2019). Sekitar 24% dari total ekosistem mangrove global tersebut berada di Indonesia (Wirabuana *et al*., 2025). Hutan mangrove Indonesia sangat vital untuk mitigasi iklim nasional dan global karena menyimpan sepertiga dari seluruh karbon yang ada di wilayah pesisir dunia (Gunawan *et al*., 2025).

:::{figure} ../assets/skripsi/image2.png
:width: 100%

Gambar 1. Simpanan Karbon di Berbagai Ekosistem (Taillardat et al., 2018)
:::

Grafik menunjukkan (a) laju penyerapan karbon pada skala petak ukur (lokal), (b) cakupan luas permukaan global, dan (c) total potensi penyerapan karbon secara global.

Melihat besarnya simpanan karbon dan potensinya dalam mitigasi perubahan iklim, melindungi, mengelola, dan merestorasi hutan mangrove di Indonesia adalah kunci untuk mencapai target pengurangan emisi negara pada tahun 2030 (Novita *et al*., 2022). Sebaliknya, ketika mangrove dikonversi menjadi penggunaan lahan lain, ekosistem tersebut akan menghasilkan emisi gas rumah kaca (GRK) dalam jumlah besar (Arifanti *et al*., 2024). Dengan demikian, konservasi mangrove harus diprioritaskan karena merupakan cara termurah dan termudah untuk mengurangi emisi dari ekosistem ini (Arifanti *et al*., 2022).

a.  Biomassa dan Karbon di Atas Permukaan Tanah

Biomassa di atas permukaan pada ekosistem mangrove adalah total biomassa hidup dari bagian tumbuhan yang berada di atas permukaan tanah, termasuk batang, cabang, dan daun (Murdiyarso *et al*., 2025). Biomassa di atas tanah dapat diperkirakan hanya menggunakan diameter setinggi dada (DBH) (Kusmana *et al*., 2018). Nilai biomassa diestimasi dari diameter batang melalui kalkulasi dengan model alometrik (Sodikin *et al*., 2024a). Menurut (Standar Nasional Indonesia, berlaku), Karbon di atas tanah merupakan simpanan karbon yang dihasilkan dari penjumlahan nilai biomassa dengan faktor koreksi 0.47. Model alometrik merupakan pendekatan matematis yang digunakan untuk mengestimasi AGB mangrove berdasarkan parameter lapangan yang mudah diukur seperti diameter batang pada ketinggian dada (DBH), tinggi pohon, dan kerapatan kayu. Model ini dikembangkan melalui analisis regresi antara biomassa aktual hasil penimbangan langsung dengan variabel morfometrik pohon. Dalam konteks mangrove, model alometrik sangat penting karena memungkinkan estimasi biomassa secara non-destruktif dan efisien di ekosistem yang sensitif. Terdapat dua jenis model yang umum digunakan, yaitu model umum (*general equations*) dan model spesifik-spesies (*species-specific equations*). Salah satu contoh model umum yang banyak digunakan di wilayah Asia adalah persamaan: b = 0,251 × ρ × d².⁴⁶, di mana *b* adalah biomassa (kg), *ρ* adalah kerapatan kayu (g/cm³), dan *d* adalah DBH (cm). Sementara itu, model spesifik seperti yang diterapkan untuk *Bruguiera gymnorrhiza* menggunakan bentuk: b = 0,0464 × (d²h)\^0,94275 × ρ, yang mempertimbangkan tambahan variabel tinggi pohon (*h*) untuk meningkatkan akurasi estimasi. Pemilihan model alometrik yang sesuai menjadi krusial karena variasi morfologi antar spesies mangrove dapat berdampak signifikan terhadap hasil perhitungan biomassa (Howard *et al*., 2014).

b.  Metode Estimasi dan Permodelan Karbon Mangrove

Metode berbasis lapangan dan alometrik tetap menjadi dasar utama dalam penilaian cadangan karbon di Asia Tenggara. Di Indonesia, persamaan alometrik lokal terbukti akurat dalam memperkirakan AGB pada berbagai ekosistem seperti hutan dataran rendah, mangrove, dan agroforestri, meskipun masih terkendala oleh heterogenitas spesies dan keterbatasan cakupan wilayah. Malaysia menunjukkan kemajuan melalui penggunaan *airborne LiDAR* dan *Terrestrial Laser Scanning (TLS)* dengan tingkat akurasi tinggi (R² \> 0,90), sedangkan di Vietnam, penerapan penginderaan jauh dan *machine learning* masih menunjukkan variasi hasil karena kompleksitas topografi dan terbatasnya data kalibrasi. Teknologi UAV dan penginderaan jauh membantu menjembatani data lapangan dengan estimasi skala luas, namun masih dihadapkan pada kendala biaya, ketersediaan data, serta saturasi sinyal SAR pada hutan lebat (Latifah *et al*., 2025).

| Metode | Variabel | Hasil | Referensi |
|:---------------------|:----------------|:----------------|:---------------|
| Pendekatan lapangan (alometrik & inventarisasi) | Diameter setinggi dada (DBH), tinggi pohon (h), dan kerapatan kayu (wd). | Model alometrik spesies; Estimasi ketersediaan dan daya serap karbon dalam satuan ton/hektar | (Kusmana *et al*., 2018; Sodikin *et al*., 2024a) |
| Penginderaan jauh optis (indeks vegetasi & regresi) | Citra optis , indeks vegetasi, dan data DBH | Model estimasi karbon di atas permukaan berbasis regresi linier | (Karang *et al*., 2024a; Novanda *et al*., 2025a; Suardana *et al*., 2023a; Thoha, Purwanto, *et al*., 2025) |
| Metode Struktur Kanopi (lidar/UAV) | Data Ketinggian Aktif: Airborne lidar. Data Struktur UAV *(Photogrammetry).* | Model Estimasi Karbon berdasarkan perubahan struktur dan ketinggian kanopi. | (Basyuni *et al*., 2025; S. Huang *et al*., 2025; Zulkarnain *et al*., 2025) |
| Pembelajaran Mesin *(Machine learning)* dan Komparasi Multisensor | Fusi Multisumber: Data GEDI lidar, Sentinel-2 (Optis), Sentinel-1 (SAR), dan ALOS-2 PALSAR-2 (SAR). Algoritma ML: Random Forest (RF), Support Vector Regression (SVR), xgboost (XGB), Generalized Boosting (GB). | Model prediksi karbon berbasis algoritma SVR*(Suport Vector Regression)* dan RF *(Random Forest)* untuk deteksi perubahan dan estimasi biomassa. | (Maung *et al*., 2025a; Pham *et al*., 2020; Zulkarnain *et al*., 2025) |

**Tabel 1. Metode Estimasi dan Pengukuran Karbon Mangrove**

(s2-1-2-penginderaan-jauh-berbasis-komputasi-awan-dalam-permodelan-d)=
### 2.1.2 Penginderaan Jauh Berbasis Komputasi Awan dalam Permodelan dan Estimasi Simpanan Karbon Mangrove

Penginderaan Jauh menawarkan alternatif yang efektif untuk mengestimasi stok karbon atas permukaan (*Above-Ground Carbon*) mangrove dengan menganalisis hubungan antara nilai piksel satelit dan pengukuran berbasis lapangan (Rodríguez *et al*., 2025) Metode konvensional *field survei* untuk mengestimasi AGC tidak efektif karena metode ini membutuhkan sejumlah besar waktu dan biaya (Thoha, Purwanto, *et al*., 2025). Pendekatan lapangan tradisional juga sulit dilakukan untuk monitoring di area mangrove yang luas karena memerlukan upaya, energi, waktu, dan biaya yang sangat besar (Purwanto *et al*., 2023). Keterbatasan ini diatasi dengan pendekatan data penginderaan jauh berbasis komputasi awan yang menyediakan solusi skalabel dan dapat diakses untuk analisis geospasial skala planet (Gorelick *et al*., 2017).

Platform Google Earth Engine (GEE) mengatasi tantangan alur kerja tradisional seperti volume data yang besar dan pra-pemrosesan yang kompleks (Islam *et al*., 2025). GEE memungkinkan pengguna untuk memanfaatkan ketersediaan citra satelit seperti Sentinel-2 secara efisien tanpa perlu mengunduh data dalam volume besar (Malerba *et al*., 2023). Platform *cloud* memfasilitasi integrasi data multisumber termasuk data optik Sentinel-2, radar Sentinel-1, dan data LiDAR GEDIdengan data inventarisasi lapangan untuk estimasi Biomassa Atas Permukaan (AGB) (Zulkarnain *et al*., 2025). Model estimasi AGB ini secara umum mengandalkan algoritma pembelajaran mesin (Pham *et al*., 2020). Algoritma yang digunakan seperti SVR*,* RF, dan XGboost terbukti efektif mengestimasi AGB mangrove (Zhu *et al*., 2025). Pemanfaatan pengideraan jauh berbasis *cloud* ini sangat mendukung kebijakan publik karena menyediakan referensi yang andal bagi pemangku kepentingan dalam mengelola dan melindungi ekosistem mangrove (Rodriguez *et al*., 2025).

a.  Klasifikasi Citra dalam Pemetaan Mangrove

Klasifikasi terbimbing (*supervised classification*) adalah metode klasifikasi citra yang mengandalkan sampel pelatihan (*training samples*), yaitu area-area yang jenisnya sudah diketahui dari referensi lapangan (*ground reference sites*), untuk menentukan kelas bagi piksel-piksel lain yang belum teridentifikasi (M. Abdalla, 2025). Dalam permodelan simpanan karbon mangrove, proses klasifikasi terbimbing dilakukan untuk mengekstraksi persebaran mangrove secara spasial (Zhang & Fan, 2025). Ekstraksi spasial sebaran mangrove berbasis klasifikasi terbimbing dengan referensi data lapangan dinilai efisien dalam pemetaan mangrove berbasis lokal, karena pola sebaran mangrove lokal bervariasi bahkan antar negara tetangga (Schill *et al*., 2024). Beberapa penelitian menciptakan indeks yang lebih sederhana untuk memetakan mangrove, seperti MVI *(Mangrove Vegetation Index* (Baloloy *et al*., 2020) yang mengandalkan segmentasi berbasis ambang batas *(thresholding)*, pendekatan ambang batas ini memiliki keterbatasan signifikan terkait misklasifikasi, mengingat pola sebaran mangrove seringkali bercampur dengan lingkungan sekitar yang bervariasi seperti tambak dan pertanian (Jian *et al*., 2025).

Algoritma Random Forest (RF) diperkenalkan oleh Breiman (2001) sebagai metode *ensemble learning* yang menggabungkan sejumlah besar *decision tree* untuk meningkatkan akurasi klasifikasi dan menurunkan kesalahan generalisasi (*generalization error*) dengan membangun setiap pohon menggunakan subset data dan fitur yang dipilih secara acak, kemudian menggabungkan hasilnya melalui proses *voting* atau *averaging* (Breiman, 2001). Pendekatan ini membuat RF lebih stabil, tahan terhadap *overfitting*, serta efektif dalam menangani data non-linear dan berdimensi tinggi (Cardille *et al*., 2024). Dalam bidang penginderaan jauh, RF menjadi algoritma yang paling banyak digunakan karena kemampuannya dalam mengklasifikasikan data multispektral dan multitemporal dengan akurasi tinggi serta memberikan informasi mengenai pentingnya setiap variabel (*variable importance*) terhadap hasil klasifikasi (Chowdhury, 2024)

Meskipun Google Earth Engine (GEE) menyediakan lebih dari 15 algoritma klasifikasi berbeda, hampir 15.000 publikasi ilmiah dalam lima tahun terakhir menggunakan RF untuk klasifikasi tutupan lahan, termasuk pemetaan mangrove (Diniz *et al*., 2019) . Penelitian yang dilakukan oleh (Jamaluddin *et al*., 2022a) menunjukkan bahwa penggunaan citra Landsat-7 dan Landsat-8 dengan algoritma RF menghasilkan akurasi keseluruhan 0,966 dan *user accuracy* 0,936, yang menegaskan keandalan RF dalam klasifikasi tutupan lahan pesisir. Sementara itu, (Purwanto *et al*., 2023)melaporkan bahwa penerapan RF pada citra Sentinel-2 mampu mencapai akurasi hingga 99,12%, menunjukkan performa tinggi dalam pemetaan vegetasi pesisir. (Zhu *et al*., 2025)membuktikan bahwa RF memiliki kemampuan prediktif yang kuat dalam estimasi biomassa mangrove menggunakan citra multispektral resolusi menengah.

a.  Indeks Vegetasi

Indeks vegetasi adalah kombinasi matematis sederhana dari dua atau lebih kanal spektral yang telah menjadi alat penting untuk memantau status dan dinamika vegetasi (Yan *et al*., 2025). NDVI secara historis merupakan indeks yang paling dominan diterapkan, digunakan dalam 82% studi tinjauan untuk memetakan luasan, biomassa, dan kepadatan karbon mangrove (Tran *et al*., 2022) . Selain indeks dari sensor optik, model alometrik yang mengaitkan AGB dengan data penginderaan jauh, seperti data lidar GEDI atau data optik-SAR, telah menunjukkan kinerja prediktif yang kuat (R² \> 0,85) di Asia Tenggara (Latifah *et al*., 2025). Data GEDI sendiri digunakan untuk mengembangkan model kepadatan AGBD (*Aboveground Biomass Density*) pada skala *footprint* 25m, yang krusial untuk pemetaan karbon global (Duncanson *et al*., 2022). Peta ketinggian kanopi global, seperti yang dihasilkan dari data TanDEM-X dan divalidasi GEDI, juga penting untuk evaluasi stok karbon dan jasa ekosistem mangrove (Simard *et al*., 2025)

Aplikasi Indeks vegetasi pada citra satelit Sentinel-2A terbukti efektif untuk pemodelan karbon karena citra ini menyediakan tiga kanal spektral unik di rentang *red-edge* yang sangat berharga untuk pemantauan vegetasi (Karang *et al*., 2024a; Novanda *et al*., 2025a; Suardana *et al*., 2023a). Studi di Teluk Benoa, Bali, menunjukkan bahwa model estimasi karbon di atas permukaan) terbaik dari data Sentinel-2 menggunakan kombinasi indeks *Inverted Red Edge Chlorophyll Index* (IRECI) dan *Total Ratio Vegetation Index* (TRVI), yang menghasilkan RMSE 11.09 Mg/ha (Suardana *et al*., 2023). Untuk mengurangi efek saturasi optik di hutan lebat, integrasi data Sentinel-2 (menggunakan OSAVI) dengan radar ALOS-2 L-band (polarisasi HV) terbukti meningkatkan akurasi model AGB secara signifikan (R² = 0,735) (Zhu *et al*., 2025). Meskipun Sentinel-2 populer, citra Landsat-8 juga tetap relevan, di mana *Soil Adjusted Vegetation Index* (SAVI) menunjukkan korelasi tertinggi (R² = 0,924) untuk pemodelan AGB di Vietnam (Nguyen & Nguyen, 2021).

1)  NDVI *(Normalized Difference Vegetation Index)*

Normalized Difference Vegetation Index (NDVI) merupakan indeks vegetasi yang digunakan untuk mendeteksi dan mengukur tingkat kehijauan serta kerapatan vegetasi berdasarkan selisih dan jumlah reflektansi kanal inframerah dekat (NIR) dan merah (Red) (Rouse *et al*., 1974). NDVI juga digunakan sebagai salah satu variabel input dalam pembentukan indeks gabungan seperti OSCMI *(Optical and SAR Combined Mangrove Index)* untuk meningkatkan akurasi pemetaan mangrove berbasis citra Sentinel-2 dan Sentinel-1 (Huang *et al*., 2022) . NDVI juga digunakan sebagai algoritma utama untuk menganalisis perubahan temporal dan mengevaluasi kondisi mangrove secara global (Ruan *et al*., 2022).

2)  IRECI *(Inverted Red-Edge Chlorophyll Index)*

IRECI *(Inverted Red-Edge Chlorophyll Index )* merupakan indeks vegetasi yang dikembangkan untuk meningkatkan akurasi estimasi variabel biofisik vegetasi, khususnya kandungan klorofil kanopi, dengan memanfaatkan kanal red-edge (Blackburn, 1998) . Efektivitas IRECI dalam pemetaan vegetasi dibuktikan oleh Suardana *et al*. (2023) yang menggunakannya dalam model estimasi karbon di atas permukaan hutan mangrove di Teluk Benoa, Bali. Hasilnya, IRECI menunjukkan korelasi kuat dengan AGC lapangan (RMSE: 13,72 Mg/ha), dan kombinasi dengan TRVI menghasilkan model terbaik (RMSE: 11,09 Mg/ha; r = 0,95), memperkuat peran penting red-edge dan NIR dalam estimasi biomassa hutan mangrove secara spasial.

3)  TRVI *(Total Ratio Vegetation Index)*

TRVI *(Total Ratio Vegetation Index)* indeks vegetasi yang dirumuskan untuk meningkatkan akurasi estimasi tutupan vegetasi dengan cara mengurangi pengaruh latar belakang tanah (Fadaei *et al*., 2012a). Dalam konteks hutan mangrove, TRVI juga menunjukkan performa tinggi dalam estimasi cadangan biomassa di atas permukaan tanah (AGC). Suardana *et al*. (2023) menemukan bahwa TRVI memiliki korelasi kuat terhadap AGC (r = 0,88; RMSE = 18,57 Mg/ha), dan kombinasi TRVI dengan IRECI menghasilkan model terbaik dengan akurasi sangat tinggi (r = 0,95; RMSE = 11,09 Mg/ha), menjadikan TRVI sebagai alternatif yang efektif dalam pemodelan biomassa mangrove berbasis citra Sentinel-2.

(s2-1-3-citra-sentinel-2a)=
### 2.1.3 Citra Sentinel 2A

Sentinel-2 merupakan misi satelit penginderaan jauh milik European Space Agency (ESA) yang terdiri dari dua satelit optik kembar, yaitu Sentinel-2A dan Sentinel-2B. Dengan resolusi spasial hingga 10 meter dan waktu ulang observasi sekitar lima hari, Sentinel-2 sangat ideal untuk pemantauan vegetasi, tutupan lahan, dan parameter lingkungan dalam skala regional hingga global (ESA, 2015). Sentinel level-2A telah melalui koreksi atmosfer untuk merepresentasikan nilai reflektansi permukaan bumi yang sebenarnya. Produk ini dihasilkan melalui pemrosesan otomatis menggunakan algoritma seperti *Sen2Co*r dan mencakup kanal reflektansi di semua panjang gelombang Sentinel-2 dengan resolusi 10 m, 20 m, dan 60 m . Hal yang membedakan antara Sentinel 2 TOA dengan level SR adalah terdapat kanal SCL yang menambah fitur dalam proses masking awan.

| Kanal | Deksripsi                                           | Resolusi |
|:------|:----------------------------------------------------|:---------|
| B01   | Coastal aerosol, 442.7 nm (S2A), 442.3 nm (S2B)     | 60m      |
| B02   | Blue, 492.4 nm (S2A), 492.1 nm (S2B)                | 10m      |
| B03   | Green, 559.8 nm (S2A), 559.0 nm (S2B)               | 10m      |
| B04   | Red, 664.6 nm (S2A), 665.0 nm (S2B)                 | 10m      |
| B05   | Vegetation red edge, 704.1 nm (S2A), 703.8 nm (S2B) | 20m      |
| B06   | Vegetation red edge, 740.5 nm (S2A), 739.1 nm (S2B) | 20m      |
| B07   | Vegetation red edge, 782.8 nm (S2A), 779.7 nm (S2B) | 20m      |
| B08   | NIR, 832.8 nm (S2A), 833.0 nm (S2B)                 | 10m      |
| B8A   | Narrow NIR, 864.7 nm (S2A), 864.0 nm (S2B)          | 20m      |
| B09   | Water vapour, 945.1 nm (S2A), 943.2 nm (S2B)        | 60m      |
| B11   | SWIR, 1613.7 nm (S2A), 1610.4 nm (S2B)              | 20m      |

**Tabel 2. Deksripsi Kanal Citra Sentinel 2A**

Sumber : ESA (2015)

| Kanal | Nilai Minimum | Nilai Maksimum | Panjang Gelombang | Deskripsi & Ketersediaan |
|:--------|:------------|:-----------|:------------|:-------------------------|
| SCL | 1 | 11 | -- | Nilai *\"No Data\"* (0) sudah termasking secara otomatis. |
| QA10 | -- | -- | -- | Selalu kosong / tidak memiliki data. |
| QA20 | -- | -- | -- | Selalu kosong / tidak memiliki data. |
| QA60 | -- | -- | -- | Masking awan. Tidak tersedia pada periode 25 Jan 2022 -- 28 Feb 2024. |

**Tabel 3. Kanal Masking Awan Citra Sentinel 2A**

Sumber : GEE Data Catalogue

(s2-2-kajian-hasil-penelitian)=
## 2.2 Kajian Hasil Penelitian

1.  **Pendugaan Simpanan Biomassa Mangrove Berbasis Citra Landsat 8 Berbasis Evaluasi Model di Pesisir Utara Kabupaten Subang**

Salah satu studi yang relevan dilakukan oleh Rianzani *et al*. (2018), yang mengestimasi biomassa mangrove di Kabupaten Subang dengan memanfaatkan citra satelit Landsat 8 OLI dan pendekatan alometrik berbasis indeks vegetasi NDVI. Proses analisis mencakup tahapan koreksi geometrik dan radiometrik guna memastikan ketelitian spasial dan spektral citra, transformasi indeks vegetasi untuk mendapatkan nilai kehijauan kanopi, serta validasi menggunakan data lapangan berupa pengukuran diameter setinggi dada (DBH) pohon mangrove. Pengolahan data dilakukan dengan menggunakan perangkat lunak ENVI untuk koreksi atmosfer (menggunakan metode FLAASH) dan ArcGIS untuk analisis spasial dan pemetaan. Hasil penelitian menunjukkan bahwa model alometrik terbaik berasal dari Budi (2000), dengan estimasi biomassa rata-rata sebesar 6,93 ton/ha dan standar deviasi 9,97 ton/ha. Sebaran biomassa didominasi oleh kisaran 5--10 ton/ha, dengan wilayah Legon Kulon sebagai area yang memiliki kontribusi biomassa terbesar. Temuan ini menunjukkan bahwa teknologi pengindraan jauh mampu memberikan estimasi biomassa mangrove secara efisien dan mencakup wilayah yang luas.

2.  **Pendugaan Simpanan Biomassa Mangrove di Muara Sungai Cipunegara Kabupaten Subang tahun 2011, 2017, dan 2023 Berbasis Pengukuran Lapangan**

Sodikin *et al*. (2024) melakukan penelitian estimasi ketersediaan dan serapan biomassa pada ekosistem mangrove di Muara Sungai Cipunegara**,** tepatnya di Desa Patimban, Kecamatan Pusakanagara, Kabupaten Subang. Penelitian ini menjadi relevan karena dilakukan di lokasi yang sama dengan penelitian yang diusulkan, meskipun dengan pendekatan konvensional tanpa menggunakan penginderaan jauh. Penelitian tersebut menggunakan interpretasi citra Google Earth tahun 2011, 2017, dan 2023, yang divalidasi melalui *ground check* lapangan dan pengukuran diameter pohon dengan metode transek. Analisis biomassa dilakukan menggunakan persamaan alometrik untuk jenis-jenis mangrove dominan seperti *Avicennia marina*, *Rhizophora mucronata*, dan *Sonneratia alba*. Berdasarkan hasil perhitungan, diperoleh rata-rata biomassa sebesar 390,70 ton/ha/hari**,** ketersediaan biomassa sebesar 19,53 ton/ha/hari, dan kemampuan serapan biomassa mencapai 71,69 ton/ha/hari. Temuan ini menunjukkan potensi besar ekosistem mangrove di kawasan tersebut dalam menyerap emisi biomassa. Meskipun pendekatan yang digunakan belum mencakup pemodelan spasial atau indeks vegetasi dari citra satelit, penelitian ini memberikan gambaran awal mengenai struktur hutan dan kandungan biomassa aktual. Oleh karena itu, studi Sodikin *et al* (2024) menjadi dasar penting untuk pengembangan model estimasi biomassa berbasis penginderaan jauh di lokasi yang sama, sehingga hasilnya dapat dibandingkan dan divalidasi lebih lanjut secara spasial dan temporal.

3.  **Pendugaan Simpanan Biomassa Mangrove Berbasis Sentinel 2A Menggunakan Platform Komputasi Awan di Pulau Benoa Bali**

Suardana *et al*. (2023) melakukan penelitian estimasi dan pemetaan cadangan biomassa di atas permukaan *(Above-Ground Carbon)* hutan mangrove di Teluk Benoa, Provinsi Bali, menggunakan citra Sentinel-2 dan pemrosesan data berbasis Google Earth Engine (GEE). Pendekatan ini mengintegrasikan data lapangan dengan model semi-empiris berbasis indeks vegetasi, serta menerapkan algoritma *Random Forest* untuk klasifikasi antara mangrove dan non-mangrove. Data citra Sentinel-2 yang digunakan berupa komposit tahunan bebas awan (Level-2A), dengan proses masking awan dan seleksi wilayah studi dilakukan secara otomatis menggunakan parameter NDVI, MNDWI, dan DEM. Dari hasil klasifikasi, diperoleh luas area mangrove sebesar 1.134,92 ha dengan akurasi keseluruhan *(Overall Accuracy)* sebesar 0,984 dan koefisien kappa sebesar 0,961.

Model AGC dibangun dari kombinasi beberapa indeks vegetasi, terutama yang sensitif terhadap kanal red edge dan NIR. Hasil terbaik diperoleh dari kombinasi indeks IRECI dan TRVI dengan RMSE sebesar 11,09 Mg/ha dan korelasi (r) sebesar 0,95 antara data lapangan dan hasil prediksi model. Model alternatif tanpa menggunakan kanal red edge (TRVI dan DVI) tetap menunjukkan performa baik dengan RMSE 13,63 Mg/ha. Penelitian ini menunjukkan bahwa penggunaan kanal *red edge* secara signifikan meningkatkan akurasi model estimasi biomassa mangrove. Studi ini sangat relevan sebagai referensi metodologis karena menggunakan pendekatan yang sejenis dengan penelitian ini, yaitu pemodelan spasial biomassa mangrove berbasis indeks vegetasi Sentinel-2 di platform GEE. Validasi yang kuat dan kompleksitas model menjadikan penelitian ini sebagai salah satu acuan penting dalam pengembangan estimasi biomassa hutan mangrove berbasis penginderaan jauh.

(s2-3-kerangka-pemikiran)=
## 2.3 Kerangka Pemikiran

![](../assets/skripsi/image3.png)

Gambar 2. Kerangka Pemikran
