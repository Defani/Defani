---
title: BAB I Pendahuluan
short_title: BAB I
numbering:
  figure: false
  table: false
  equation: true
---

Bagian dari skripsi *Pemodelan Simpanan Karbon Mangrove Berbasis Citra Sentinel 2A di Muara Sungai Cipunegara, Subang, Jawa Barat* · [Daftar isi](../skripsi.md)

(s1-1-latar-belakang)=
## 1.1 Latar Belakang

Hutan mangrove merupakan salah satu ekosistem pesisir yang memiliki peran penting dalam mitigasi perubahan iklim global karena kemampuannya dalam menyerap dan menyimpan karbon dalam jumlah yang lebih besar dibandingkan ekosistem hutan tropis lainnya (Choudhary *et al*., 2024; Taillardat *et al*., 2018). Hutan mangrove Indonesia menyimpan sekitar 24% total karbon pesisir global, sehingga keberadaan ekosistem ini menjadi sangat strategis dan menjadi prioritas utama dalam mendukung pencapaian target penurunan emisi gas rumah kaca nasional (Arifanti *et al*., 2024; Gunawan *et al*., 2025). Namun demikian, peran penting mangrove secara ekologis masih belum dipahami secara optimal oleh berbagai pihak. Kondisi tersebut menyebabkan konversi dan degradasi hutan mangrove yang berdampak pada menurunnya kemampuan penyerapan karbon. Bahkan, kehilangan simpanan karbon akibat kerusakan mangrove diperkirakan membutuhkan waktu antara 15 sampai 40 tahun untuk mengembalikan stok karbon yang hilang (Wirabuana *et al*., 2025). Oleh karena itu, diperlukan sistem pemantauan mangrove yang efektif, berkelanjutan, dan mampu menggambarkan kondisi simpanan karbon secara akurat sebagai dasar pengelolaan dan konservasi ekosistem mangrove, untuk menjaga dan melestarikan fungsi ekologisnya.

Metode survei lapangan yang umum digunakan dalam pengukuran biomassa dan karbon mangrove memiliki keterbatasan, terutama dalam aspek efisiensi waktu, biaya, dan cakupan wilayah. Seiring perkembangan teknologi, pendekatan penginderaan jauh berbasis komputasi awan *(cloud computting)* melalui Google Earth Engine (GEE) menawarkan alternatif yang dinilai lebih efektif untuk mendukung pemantauan simpanan dan luasan karbon mangrove secara spasial dan temporal (Karang *et al*., 2024a; Suardana *et al*., 2023a; Thoha, Purwanto, *et al*., 2025). Platform GEE memungkinkan pengolahan dan analisis data geospasial skala besar secara cepat tanpa memerlukan spesifikasi perangkat komputer yang tinggi (Gorelick *et al*., 2017). Selain itu, GEE telah terintegrasi dengan berbagai sumber data penginderaan jauh, seperti citra Sentinel 2, SAR, dan LiDAR GEDI, sehingga mendukung analisis dan permodelan karbon mangrove tanpa perlu mengunduh data secara manual (Zhu *et al*., 2025). Keunggulan lain dari Platform ini adalah tersedianya fitur *cloud masking* yang mampu mengurangi gangguan tutupan awan pada citra optik (Yancho *et al*., 2020), karena objek yang tertutup awan tidak dapat diidentifikasi secara visual maupun digital (Kosasih *et al*., 2019).

Citra Sentinel-2A menjadi salah satu data penginderaan jauh yang direkomendasikan dalam pemodelan karbon di atas permukaan atau *Above Ground Carbon* (AGC) karena memiliki resolusi spasial dan spektral yang tinggi, terutama dengan ketersediaan kanal red-edge dan Near-Infrared (NIR) yang sensitif terhadap karakteristik vegetasi dan mampu meningkatkan akurasi model estimasi karbon (Karang *et al*., 2024a; Suardana *et al*., 2023a; Thoha, Purwanto, *et al*., 2025). Berbagai penelitian menunjukkan bahwa indeks vegetasi berbasis Sentinel-2A mampu meningkatkan akurasi estimasi biomassa dan karbon mangrove. Penelitian Suardana *et al*. (2023) di Teluk Benoa, Bali, serta Thoha *et al*. (2025) di pesisir Sumatera Utara berbasis citra Sentinel-2 dengan menguji tujuh indeks vegetasi menunjukkan bahwa kombinasi NDVI, TRVI, dan IRECI memiliki performa paling tinggi dalam mendeteksi variasi biomassa mangrove dibandingkan indeks lainnya. Hasil tersebut diperkuat oleh Novanda *et al*. (2025), yang menguji 32 indeks vegetasi dan menemukan bahwa TRVI termasuk enam indeks dengan korelasi tertinggi terhadap biomassa mangrove. Sementara itu, Karang *et al*. (2024) melaporkan bahwa indeks IRECI memberikan tingkat akurasi tertinggi dalam estimasi karbon mangrove di kawasan pesisir di Nusa Tenggara. .

Di Kabupaten Subang, penelitian mengenai estimasi biomassa dan karbon mangrove telah dilakukan oleh Rianzani *et al*. (2018) menggunakan citra Landsat 8 OLI dengan pendekatan model alometrik berbasis NDVI tunggal yang mengacu pada model yang dikembangkan Budi (2000) untuk ekosistem mangrove di Segara Anakan, Cilacap. Penelitian tersebut menghasilkan estimasi biomassa rata-rata sebesar 6,93 ton/ha, namun model yang digunakan belum dikalibrasi sesuai kondisi lokal ekosistem mangrove di wilayah penelitian. Penelitian lain oleh Sodikin *et al*., (2024a) di Muara Sungai Cipunegara menunjukkan adanya peningkatan luas mangrove hingga mencapai 696 hektar pada tahun 2023 dengan ketersediaan karbon harian sebesar 19,53 ton/ha berdasarkan pengukuran lapangan. Selanjutnya, Santoso *et al* (2026) melakukan pemodelan karbon mangrove di seluruh pesisir utara Kabupaten Subang menggunakan pendekatan *Hypertunning Parameter* berbasis data lapangan dan data penginderaan jauh. Namun, hasil penelitian tersebut masih berupa estimasi nilai total karbon dan belum menghasilkan model matematis yang praktis untuk digunakan dalam pendugaan karbon secara operasional.

Berdasarkan uraian tersebut, dapat diketahui bahwa penelitian mengenai pemodelan karbon mangrove di Muara Sungai Cipunegara masih memiliki beberapa keterbatasan, yaitu belum tersedianya model estimasi AGC yang terkalibrasi secara lokal, belum adanya pengujian beberapa indeks vegetasi Sentinel-2A untuk menentukan indeks terbaik dalam menduga karbon mangrove, serta belum tersusunnya model matematis yang dapat diaplikasikan secara praktis dalam pemantauan karbon mangrove berbasis penginderaan jauh. Oleh karena itu, penelitian ini dilakukan untuk membangun model estimasi Above Ground Carbon (AGC) mangrove berbasis citra Sentinel-2A dan Google Earth Engine dengan memanfaatkan beberapa indeks vegetasi guna menghasilkan model penduga karbon mangrove berupa persamaan matematis yang sesuai dengan karakteristik ekosistem mangrove di Muara Sungai Cipunegara, Kabupaten Subang, Jawa Barat.

(s1-2-identifikasi-masalah)=
## 1.2 Identifikasi Masalah

Informasi simpanan karbon mangrove di muara sungai Cipunegara baru sebatas data hasil pengukuran lapangan (Sodikin *et al*., 2024), sementara model spasial berbasis komparasi indeks vegetasi yang dilaporkan dalam bentuk publikasi ilmiah belum tersedia. Ketiadaan model ini menjadi tantangan dalam merancang strategi mitigasi dan konservasi yang presisi. Oleh karena itu, penelitian ini berfokus untuk menjawab kebutuhan tersebut dengan mengembangkan sebuah model estimasi karbon di atas permukaan tanah yang terkalibrasi secara lokal. Dengan memanfaatkan kemajuan teknologi penginderaan jauh, khususnya citra Sentinel-2A yang memiliki resolusi spasial dan spektral lebih tinggi, serta efisiensi platform Google Earth Engine (GEE), studi ini bertujuan untuk menghasilkan sebuah alat bantu *(tool)* yang andal dan aplikatif untuk mendukung pengambilan keputusan dalam pengelolaan mangrove yang berkelanjutan di kawasan tersebut.

(s1-3-rumusan-masalah)=
## 1.3 Rumusan Masalah

1.  Bagaimana kondisi dan distribusi tutupan mangrove di Muara Sungai Cipunegara berdasarkan citra Sentinel-2A?

2.  Bagaimana nilai simpanan karbon atas permukaan (*Above Ground Carbon*/AGC) mangrove berdasarkan data lapangan di Muara Sungai Cipunegara?

3.  Bagaimana hubungan antara indeks vegetasi berbasis citra Sentinel-2A dengan simpanan karbon mangrove di Muara Sungai Cipunegara?

4.  Indeks vegetasi manakah yang memiliki korelasi dan performa terbaik dalam memodelkan simpanan karbon mangrove di lokasi penelitian?

5.  Bagaimana model matematis estimasi simpanan karbon mangrove berbasis citra Sentinel-2A yang terkalibrasi secara lokal di Muara Sungai Cipunegara?

(s1-4-batasan-masalah)=
## 1.4 Batasan Masalah

1.  Simpanan karbon yang dimodelkan merupakana karon di atas permukaan tanah

2.  Parameter yang digunakan untuk menduga simapanan biomassa dan karbon adalah diameter batang (DBH) mangrove pada pohon

3.  Klasifikasi tutupan mangrove dilakukan menggunakan data citra Sentinel 2A dengan metode klasifikasi terbimbing berbasis algoritma random forest

4.  Citra yang digunakan adalah Sentinel 2A *(Surface Reflectance)* hasil komposit multitemporal pada rentang waktu 1 September 2025 -- 5 Mei 2026

5.  Model penduga simpanan karbon dibangun menggunakan algoritma pembelaaran mesin linear dan dievaluasi menggunakan R{sup}`2` dan RMSE

(s1-5-tujuan)=
## 1.5 Tujuan

1.  Mengidentifikasi dan memetakan tutupan mangrove di Muara Sungai Cipunegara menggunakan citra Sentinel-2A.

2.  Menghitung nilai simpanan karbon atas permukaan (Above Ground Carbon/AGC) mangrove berdasarkan data pengukuran lapangan.

3.  Menganalisis hubungan antara indeks vegetasi citra Sentinel-2A dengan simpanan karbon mangrove di Muara Sungai Cipunegara.

4.  Menentukan indeks vegetasi terbaik yang mampu merepresentasikan variasi simpanan karbon mangrove.

5.  Menyusun model matematis estimasi simpanan karbon mangrove berbasis citra Sentinel-2A yang terkalibrasi secara lokal menggunakan platform komputasi awan Google Colaboratory

(s1-6-manfaat)=
## 1.6 Manfaat

Model matematis yang dihasilkan dalam penelitian ini dapat dimanfaatkan untuk mengestimasi simpanan karbon mangrove di Muara Sungai Cipunegara secara cepat dan efisien melalui pemanfaatan data penginderaan jauh dari citra satelit Sentinel-2A, sehingga dapat mengurangi kebutuhan survei lapangan yang memerlukan waktu dan biaya yang lebih besar.
