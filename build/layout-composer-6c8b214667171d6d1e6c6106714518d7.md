---
title: Panduan Layout Composer
---

**Panduan Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0001-02.png)

### **Dasar-Dasar Layout Peta di GeoLibre Menggunakan Plugin Layout Composer** 

Panduan lengkap dari halaman kosong sampai peta siap cetak: arsitektur, semua ikon dan menu, semua parameter, warna dan efek, color bar, LaTeX, contoh layout seri raster, hingga ekspor. 

_Peta Kelerengan Kabupaten Kuningan, disusun dengan Layout Composer_ 

##### **Defani Arman Alfitriansyah** 

**P L U G I N D E V E L O P E R** 

**Panduan Lengkap** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0002-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Kata Pengantar** 

###### **Defani Arman Alfitriansyah** 

**P L U G I N D E V E L O P E R** 

Layout Composer berawal dari kebutuhan yang sederhana: saya ingin menyusun peta yang rapi dan siap cetak langsung di GeoLibre, tanpa harus berpindah ke aplikasi lain. Dari kebutuhan kecil itu, sedikit demi sedikit plugin ini tumbuh menjadi alat yang bisa dipakai siapa saja. 

Panduan ini saya tulis agar teman-teman tidak perlu menebak-nebak fungsi setiap tombol. Setiap ikon ditampilkan apa adanya, setiap parameter dijelaskan satu per satu, dan semua contoh memakai data asli supaya mudah diikuti. 

Saya menyadari plugin dan panduan ini masih jauh dari sempurna. Karena itu, setiap masukan, laporan bug, maupun saran sangat saya harapkan agar keduanya bisa terus diperbaiki bersama. 

Terima kasih yang tulus kepada Dr. Qiusheng Wu yang telah menerima plugin ini dan memberi saya kesempatan untuk ikut berkontribusi. Terima kasih juga kepada komunitas GeoLibre dan semua pihak yang sudah mencoba, menguji, dan memberi masukan. Semoga panduan ini bermanfaat, memudahkan pekerjaan teman-teman dalam menyusun peta, dan menjadi sedikit kontribusi untuk kartografi terbuka. 

Salam hangat, 

###### **Defani Arman Alfitriansyah** 

**Plugin Developer** 

**002** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Panduan Lengkap** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0003-03.png)

#### **Daftar Isi** 

|**Bab 1. Pendahuluan dan Arsitektur**<br>**5 sampai 10**|
|---|
|Mengenal Layout Composer, cara kerjanya di dalam GeoLibre, dan bentuk file layout.|
|**Bab 2. Instalasi dan Antarmuka**<br>**11 sampai 26**|
|Memasang plugin, lalu mengenal setiap ikon di top bar, panel, menu klik kanan, dan status bar.|
|**Bab 3. Mengatur Halaman**<br>**27 sampai 34**|
|Ukuran kertas, warna kertas, garis tepi, alat bantu tata letak, dan variabel.|
|**Bab 4. Warna, Efek, dan Urutan Item**<br>**35 sampai 42**<br>Color wheel, transparansi, drop shadow, efek kaca (frosted glass), urutan tumpukan, grup, kunci, dan rotasi.|
|**Bab 5. Membangun Peta Langkah demi Langkah**<br>**43 sampai 70**<br>Menyusun Peta Kelerengan Kabupaten Kuningan dari halaman kosong sampai lengkap, dengan semua parameter setiap<br>elemen.|
|**Bab 6. Color Bar Lengkap**<br>**71 sampai 81**<br>Semua mode color bar gaya matplotlib: sumber data, 39 colormap, kelas, ujung, orientasi, tick, label, dan judul.|
|**Bab 7. Teks, LaTeX, Font, dan Simbol**<br>**82 sampai 90**|
|Semua preset teks, efek teks, font, penulisan rumus LaTeX, marker titik, dan katalog ikon.|
|**Bab 8. Bentuk, Isian, Garis, Gambar, dan Draw**<br>**91 sampai 97**<br>33 bentuk, tiga jenis isian, enam gaya garis, gambar dengan filter dan masker, serta alat gambar bebas.|
|**Bab 9. Tabel dan Grafik dari Data**<br>**98 sampai 103**<br>Membuat tabel atribut dan grafik langsung dari atribut layer; nilainya ikut berubah bila data berubah.|
|**Bab 10. Contoh: Layout Seri Raster Gaya Riset**<br>**104 sampai 110**|
|Menyusun empat peta raster Sentinel-2 (NDVI dan NBR+) dalam satu figur 2 × 2 bergaya matplotlib dengan palet jet.|
|**Bab 11. Ekspor, Penyimpanan, dan Penutup**<br>**111 sampai 119**|
|Mengekspor peta, menyimpan layout, bertukar template dengan QGIS, dan daftar periksa sebelum mencetak.|

**003** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Panduan Lengkap** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0004-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Cara Membaca Panduan Ini** 

Beberapa kebiasaan penulisan dipakai di seluruh panduan supaya mudah diikuti sambil membuka plugin. 

###### **Ikon ditampilkan langsung, misalnya Map atau Export** 

Ikon diambil dari kode plugin, jadi bentuknya sama persis dengan tombol di layar. Cari ikon itu di top bar atau panel. 

###### **Nama menu dan tombol dicetak tebal** 

Ditulis sama seperti di plugin (bahasa Inggris), misalnya **Sync from map** atau **Frame style** . 

###### **Kotak bernomor** 

Langkah yang dikerjakan berurutan. 

###### **Garis hijau di kiri teks** 

Tips, catatan, atau peringatan kecil. 

###### **Satuan** 

Posisi dan ukuran dalam milimeter kertas (mm), huruf dalam point (pt). 

###### **Data contoh** 

Kelas lereng Kabupaten Kuningan (vektor) dan citra Sentinel-2 NDVI/NBR+ (raster). 

Panduan ini memakai Layout Composer dari GeoLibre plugin registry. Fitur yang belum dirilis resmi tidak dibahas. 

**004** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 1 · Pendahuluan dan Arsitektur** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0005-02.png)

Plugin Layout Composer 

# **01** 

## **Pendahuluan dan Arsitektur** 

Mengenal Layout Composer, cara kerjanya di dalam GeoLibre, dan bentuk file layout. 

|Tentang panduan<br>Persiapan data|Arsitektur plugin|Alur render dan ekspor|Struktur file layout|
|---|---|---|---|

**005** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 1 · Pendahuluan dan Arsitektur** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0006-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Tentang Panduan Ini** 

Panduan ini menyusun satu peta utuh, **Peta Kelerengan Kabupaten Kuningan** , memakai data asli kelas lereng. Setiap langkah menunjukkan kondisi kanvas, lalu menjelaskan parameter yang dipakai satu per satu. 

###### **Data contoh** 

Poligon kelas lereng Kabupaten Kuningan (5 kelas: 0-8 %, 8-15 %, 15-25 %, 25-40 %, >40 %). 

###### **Contoh raster** 

Seri NDVI dan NBR+ Sentinel-2 dengan palet jet, gaya figur riset (Bab 10). 

###### **Kertas** 

A4 landscape (297 × 210 mm), margin 10 mm. 

###### **Satuan** 

Posisi dan ukuran item dalam mm kertas, ukuran huruf dalam pt. 

###### **Elemen peta** 

Bingkai peta, grid koordinat, judul, skala, mata angin, legenda, informasi, peta inset, penulis. 

###### **Hasil** 

PNG 300 dpi, PDF, Vector PDF, GeoPDF, atau SVG. 

_Kanvas akhir di dalam Layout Composer_ 

**006** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 1 · Pendahuluan dan Arsitektur** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0007-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Arsitektur Plugin** 

Layout Composer adalah satu modul JavaScript yang berjalan di dalam GeoLibre. Plugin membaca peta dan layer lewat **Plugin API** , lalu menyusun halaman di modul-modulnya sendiri. 

###### **GeoLibre (aplikasi induk)** 

Peta MapLibre beserta semua layer, simbologi, dan tampilan yang sedang dibuka. 

###### **Plugin API** 

getMap · listLayers · getProjectSnapshot · getLayerFeatures · registerToolbarMenu 

###### **Core state** 

Daftar layout, undo/redo, autosave. 

###### **Editor UI** 

Top bar, kanvas, penggaris, panel Layers dan Properti. 

###### **Item renderers** 

Setiap item digambar sebagai SVG dalam milimeter. 

###### **Live map frames** 

Salinan style MapLibre per bingkai peta. 

###### **Data items** 

Tabel atribut dan grafik, luas dan panjang di elipsoid. 

###### **Catalogs** 

Ikon Maki, Temaki, Material Symbols, Google Fonts, ukuran kertas, colormap. 

###### **Export** 

PNG, JPG, PDF, Vector PDF, GeoPDF, SVG. 

###### **QGIS templates** 

Impor dan ekspor .qpt . 

###### **Pustaka yang dimuat saat dibutuhkan** 

MathJax 3 (LaTeX), jsPDF dan svg2pdf.js (PDF), ikon via jsDelivr, Google Fonts. 

**007** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 1 · Pendahuluan dan Arsitektur** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0008-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Alur Render dan Ekspor** 

Semua item digambar sebagai SVG dalam milimeter halaman. SVG yang sama dipakai di layar dan saat ekspor, sehingga **pratinjau sama dengan hasil** . 

###### **1. Pilih pengaturan ekspor** 

Format, resolusi (dpi), latar, dan nama file di jendela Export. 

###### **2. Render setiap bingkai peta** 

Peta digambar ulang di luar layar dengan rasio piksel = dpi / 96, menghasilkan gambar per bingkai. 

###### **3. Susun halaman** 

Dekorasi halaman, semua item, efek, dan gambar peta digabung menjadi satu SVG halaman. 

###### **PNG · JPG · PDF · GeoPDF** 

###### **Vector PDF · SVG** 

SVG dirasterkan pada dpi pilihan. GeoPDF Teks, garis, dan simbol tetap vektor (svg2pdf.js). SVG menambahkan georeferensi WGS 84 untuk setiap menyertakan peta pada 200 dpi. bingkai peta. 

**008** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 1 · Pendahuluan dan Arsitektur** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0009-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Struktur File Layout** 

Layout disimpan sebagai file .layout.json . Isinya pengaturan halaman dan daftar item; setiap item punya posisi **x, y** , ukuran **w, h** dalam mm, dan **props** sesuai jenisnya. 

// examples/kelerengan-kuningan.layout.json (dipersingkat) { "name": "Kelerengan Kuningan", "page": { "size": "A4", "orientation": "landscape", "width": 297, "height": 210, "margin": 10 }, "items": [ { "type": "map", "name": "Main map", "x": 15, "y": 13, "w": 199, "h": 184, "props": { "view": { "center": [108.589, -6.987], "zoom": 10.09 }, "grid": { "show": true, "type": "dms", "lang": "id" } } }, { "type": "legend", "name": "Legend", //. }, { "type": "scalebar", "name": "Scale bar", //. } ] } 

Urutan di **items** sama dengan urutan tumpukan: item terakhir tampil paling depan. File ini dibuka lagi lewat **Main menu** , **Open layout file** . 

**009** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 1 · Pendahuluan dan Arsitektur** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0010-02.png)

###### **GeoLibre** 

#### **Persiapan Data di GeoLibre** 

Layout Composer membaca layer dan simbologi langsung dari GeoLibre. Atur dulu peta di GeoLibre, baru susun layout; legenda, color bar, tabel, dan grafik akan mengikuti. 

Muat data lewat **Add Data** (GeoJSON, shapefile, GeoPackage, raster/COG, atau **1** layanan tile). Atur simbologi di panel **Style** GeoLibre. Untuk data kelas, pakai warna per kategori agar **2** legenda terbaca otomatis per kelas. Beri nama layer yang jelas, misalnya **Kelerengan Kabupaten Kuningan** , karena nama **3** ini muncul di legenda. Untuk raster, atur colormap dan rentang nilai agar color bar bisa membaca min, max, **4** dan colormap-nya. Arahkan peta GeoLibre ke wilayah kerja. Bingkai peta baru mengikuti tampilan ini, dan **5** tombol **Match GeoLibre view** menyamakannya kapan saja. Simbologi yang rapi di GeoLibre menghemat waktu, karena legenda cukup diperbarui dengan **Sync from map** . 

**010** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0011-02.png)

Plugin Layout Composer 

# **02** 

## **Instalasi dan Antarmuka** 

Memasang plugin, lalu mengenal setiap ikon di top bar, panel, menu klik kanan, dan status bar. 

|Pasang dan aktifkan|Lima ba|gian jendela|Ikon top bar|Menu sisip|Main menu|
|---|---|---|---|---|---|
|Panel Layers<br>Panel|Properti|Menu klik ka|nan|||

**011** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0012-02.png)

#### **Memasang Plugin** 

Layout Composer terdaftar di **GeoLibre plugin registry** , jadi bisa dipasang langsung dari dalam GeoLibre. 

- **1** Buka menu **Settings** , lalu pilih **Manage Plugins** . 

- **2** Ketik **layout** di kotak pencarian, lalu klik **Install** pada Layout Composer. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0012-07.png)

<!-- Start of picture text -->
2<br>2<br>1<br>Cari lalu Install<br>Settings, Manage Plugins<br><!-- End of picture text -->

**012** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0013-02.png)

#### **Mengaktifkan dan Membuka** 

Aktifkan lewat **Plugins** , **Installed** , **Layout Composer** . Menu **Layout** muncul di bar atas dan ikon muncul di tombol kanan peta. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0013-05.png)

<!-- Start of picture text -->
2<br>2<br>Menu Layout atau tombol Open Layout Composer<br>3<br>1<br>Plugins, Installed, Layout Composer<br>Composer terbuka dengan halaman kosong<br><!-- End of picture text -->

**013** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0014-02.png)

#### **Lima Bagian Jendela** 

Semua alat ada di **top bar** ; pengaturan item terpilih ada di **panel Properti** sebelah kanan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0014-05.png)

<!-- Start of picture text -->
1<br>2 4<br>3<br>5<br><!-- End of picture text -->

###### **1 Top bar** 

Berkas dan riwayat di kiri, alat dan menu sisip di tengah, zoom, simpan, ekspor di kanan. 

###### **2 Panel Layers dan 3 Kanvas** 

Daftar item di kiri; halaman kertas dengan penggaris atas dan kiri di tengah. 

###### **4 Panel Properti dan 5 Status bar** 

Tab Item, Page, Variables di kanan; posisi kursor, Canvas grid, Guides, Snap, dan zoom di bawah. 

**014** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0015-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Top Bar: Zona Kiri** 

Zona kiri mengatur berkas layout dan riwayat perubahan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0015-06.png)

###### **Main menu** 

**Logo Layout Composer** Penanda jendela composer. 

###### **Panel Layers** 

Tampilkan atau sembunyikan panel kiri. 

**New layout / templates** Layout kosong, duplikat, template milikmu, impor template. 

Layout baru, duplikat, ganti nama, template, buka/simpan file, ekspor, template QGIS, panel, tutup. 

**Pemilih layout** Daftar layout di proyek; pilih untuk berpindah. 

**Undo** Ctrl+Z Batalkan langkah terakhir. 

**Redo** Ctrl+Y Ulangi langkah yang dibatalkan. 

**015** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0016-03.png)

#### **Top Bar: Mode Kerja dan Elemen Peta** 

Tiga ikon pertama di zona tengah adalah mode kerja; lima berikutnya menambahkan elemen kartografi utama di tengah tampilan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0016-06.png)

###### V **Select / move** 

Pilih, pindahkan, ubah ukuran, putar item. Shift+klik untuk banyak item. 

###### **Pan canvas** H 

Geser tampilan kanvas; bisa juga dengan menahan Space. 

###### **Move map content** C 

Geser isi peta di dalam bingkai; scroll untuk zoom; seret klik kanan untuk memutar. 

###### **Inset** 

Peta tunjuk yang menandai area bingkai lain. 

###### **Map** 

Bingkai peta hidup dari GeoLibre. 

###### **Legend** 

Legenda dari simbologi layer. 

###### **Color bar** 

Bilah warna gaya matplotlib. 

###### **North arrow** 

Galeri 26 mata angin. 

**016** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0017-03.png)

#### **Top Bar: Menu Sisip** 

Menu sisip membuka daftar atau galeri, lalu menaruh item di tengah tampilan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0017-06.png)

###### **Text** 

###### **Data** 

Heading, Subheading, Body text, Caption, Attribute table, Donut, Pie, Bar, Column Map label, Callout, Map title, Table / info chart. box, Formula (LaTeX). 

**Draw Shape** Polyline, Polygon, Bézier pen, Freehand, Galeri 33 bentuk. Arrow line. 

###### **Symbols** 

**Image** 12 marker titik dan katalog ikon Maki, Sisipkan gambar atau logo dari file. Temaki, Google Material Symbols. 

###### **Scale bar** 

Galeri 11 gaya skala, termasuk skala numerik dan dua satuan. 

**017** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0018-02.png)

Plugin Layout Composer 

#### **Top Bar: Zona Kanan** 

Zona kanan mengatur tampilan kanvas, menyimpan, dan mengekspor. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0018-06.png)

**Zoom out** Ctrl − Perkecil kanvas. 

###### **Opsi zoom** 

90% Persen zoom; klik untuk 50 %, 100 %, 200 %, 400 %, Fit page, Zoom to selection. 

**Zoom in** Ctrl + Perbesar kanvas. 

Ctrl 0 **Fit page** 

Seluruh halaman pas di layar. 

**Save layout file** Unduh layout sebagai .json. 

###### **Panel Properti** 

Tampilkan atau sembunyikan panel kanan. 

**Export** 

Buka jendela ekspor. 

**Close** 

Tutup Layout Composer. 

**018** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0019-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0019-04.png)

#### **Main Menu** 

Main menu mengumpulkan semua urusan berkas dan layout di satu tempat. 

###### **New layout or template** 

Buat layout baru atau dari template. 

###### **Duplicate, Rename, Delete layout** 

Kelola layout di proyek. 

###### **Save as template** 

Simpan susunan untuk dipakai lagi. 

**Open layout file, Save layout file** 

Buka atau unduh .layout.json. 

**Export** 

. Sama dengan ikon 

**Import / Export QGIS template (.qpt)** Tukar layout dengan QGIS 3. 

###### **Layers panel, Properties panel** 

Tampilkan atau sembunyikan panel. 

###### **Close Layout Composer** 

Tutup jendela. 

_Main menu_ 

**019** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0020-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0020-04.png)

#### **Layout Baru dan Template** 

Satu proyek bisa berisi banyak layout. Tombol + di samping pemilih layout membuka pilihan berikut. 

###### **Blank layout** 

Halaman kosong baru. 

###### **Duplicate this layout** 

Salinan layout aktif, cocok untuk versi peta lain. 

###### **My templates** 

Template milikmu; peta di dalamnya otomatis diarahkan ke tampilan GeoLibre saat ini. 

_Menu layout baru_ 

###### **Save this layout as template** 

Simpan susunan sebagai template. 

###### **Import template file** 

Buka template dari file. 

Template sangat membantu bila kamu membuat banyak peta dengan tata letak yang sama, misalnya satu seri peta per kecamatan. 

**020** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0021-02.png)

#### **Opsi Zoom Kanvas** 

Klik angka persen di top bar untuk membuka menu zoom. 

**Zoom in, Zoom out** 

Ctrl + dan Ctrl −, atau Ctrl + scroll mouse. 

**Fit page** 

Ctrl 0 atau Shift 1: seluruh halaman pas di layar. 

###### **Zoom to selection** 

Shift 2: item terpilih memenuhi layar. 

**50 %, 100 %, 200 %, 400 %** 

Zoom tetap. 100 % berarti ukuran kertas sebenarnya pada 96 dpi. 

###### **Slider zoom** 

_Menu zoom_ 

Di pojok kanan bawah status bar. 

**021** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0022-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0022-04.png)

#### **Panel Layers** 

Panel kiri mendaftar semua item di halaman. Urutan paling atas tampil paling depan. 

###### **Kotak pencarian** 

Ketik nama untuk menyaring item. 

###### **Klik** 

Pilih item; Shift+klik untuk banyak item. 

**Double-click nama** Ganti nama item ( ). 

###### **Seret** 

Ubah urutan tumpukan. 

**/** Tampilkan atau sembunyikan item. **/** 

Kunci item agar tidak tergeser. 

###### **Tanda grup** 

Item yang tergabung dalam grup diberi tanda. 

_Panel Layers_ 

**022** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0023-03.png)

#### **Panel Properti: Baris Ikon** 

Di atas panel Properti ada dua baris ikon untuk merapikan dan mengurutkan item. Dengan satu item, perataan mengacu ke halaman; dengan beberapa item, mengacu ke sesamanya. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0023-06.png)

**Align left Center horizontally** Rata kiri. Tengah horizontal. **Align right Align top** Rata kanan. Rata atas. **Center vertically Align bottom** Tengah vertikal. Rata bawah. **Distribute horizontally Distribute vertically** Jarak horizontal sama (3 item atau lebih). Jarak vertikal sama. **Bring to front Bring forward** Paling depan. Maju satu tingkat. **Send backward Send to back** Mundur satu tingkat. Paling belakang. **Match width Match height** Samakan lebar dengan item pertama. Samakan tinggi. **Duplicate** Ctrl+D **Delete** Del Gandakan item. Hapus item. 

**023** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0024-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Panel Properti: Tab dan Sub-tab** 

Panel kanan punya tiga tab utama, dan pengaturan item dikelompokkan dalam subtab. 

**Item** Pengaturan item yang dipilih. Kosong bila tidak ada yang dipilih. 

**Page** Ukuran kertas, garis tepi, grid kanvas, layout grid, guides, snapping. 

###### **Variables** 

_Kepala panel bingkai peta_ 

Nilai {title}, {date}, {scale}, dan variabel buatan sendiri. 

###### **Sub-tab Content, Style, Grid, Arrange** 

Kelompok pengaturan; **All** menampilkan semuanya sekaligus. 

###### **Bagian yang bisa dilipat** 

Klik judul bagian untuk membuka atau menutup. 

_Contoh isi tab Item untuk bingkai peta_ 

**024** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0025-02.png)

Plugin Layout Composer 

#### **Menu Klik Kanan** 

Klik kanan item di kanvas untuk membuka menu cepat. Isinya menyesuaikan jumlah item terpilih. 

###### **Rename** 

Ganti nama (satu item). 

###### **Copy, Duplicate, Paste** 

Ctrl+C, Ctrl+D, Ctrl+V. 

**Bring to front, Send to back** 

Atur urutan tumpukan. 

###### **Group, Ungroup** 

Ctrl+G dan Ctrl+Shift+G (beberapa item). 

**Lock, Hide** 

Kunci atau sembunyikan. 

**Pan map content, Match GeoLibre view** 

_Satu item_ 

Khusus bingkai peta. 

###### **Delete** 

Hapus (Del). 

###### **Klik kanan di halaman kosong** 

Paste, Select all, Show/Hide guides, Clear guides, Page settings. 

_Beberapa item: ada Group_ 

**025** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 2 · Instalasi dan Antarmuka** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0026-03.png)

#### **Status Bar dan Pintasan Keyboard** 

Status bar di bawah kanvas menampilkan posisi kursor, ukuran item terpilih, petunjuk singkat, dan tombol bantu tata letak. 

|||_Sisi kiri_|
|---|---|---|
|||_Sisi kanan: Canvas grid, Guides, Snap, zoom_|
|**Tombol**||**Fungsi**|
|V<br>H<br>|C|Select,<br>Pan (atau tahan Space),<br>Move map content|
|Shift 1|Shift 2|Fit page, zoom ke seleksi|
|Panah (|Shift ×10, Alt ×0,1)|Geser item 1 mm|
|Ctrl Z|Ctrl Y|Undo, redo|
|Ctrl C|Ctrl V<br>Ctrl D|Salin, tempel, duplikat|
|Ctrl G|Ctrl Shift G|Grup, lepas grup|
|Delete||Hapus item|
|Alt atau|Shift saat menyeret|Tanpa snap; kunci arah, proporsi, atau rotasi 15°|

**026** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0027-02.png)

# **03** 

## **Mengatur Halaman** 

Ukuran kertas, warna kertas, garis tepi, alat bantu tata letak, dan variabel. 

Ukuran dan orientasi Warna kertas Neatline Grid kanvas Layout grid Guides dan snap Variabel 

**027** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0028-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0028-04.png)

#### **Ukuran Kertas dan Orientasi** 

Klik kanvas kosong atau buka tab **Page** . Bagian **Page Size** mengatur ukuran dan satuan halaman. 

###### **Size** 

Katalog: ISO A0 sampai A6, B0 sampai B5, Letter, Legal, Tabloid, F4, ukuran minimum peta per skala, poster, foto, presentasi, media sosial. 

###### **Orientation** 

Portrait atau Landscape; tombol **Swap width and height** menukar ukuran. 

###### **Units** 

mm, cm, in, pt, atau px (px memakai Pixels per inch). 

###### **Width, Height** 

Ukuran khusus bila tidak memakai katalog. 

_Page Size_ 

_Katalog ukuran kertas_ 

**028** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0029-02.png)

#### **Mengganti Warna Kanvas (Paper color)** 

Warna kertas diatur di tab **Page** , baris **Paper color** . Klik kotak warna untuk membuka color wheel. 

_Hasil: kertas berwarna krem_ 

###### **Kapan dipakai** 

_Paper color di tab Page_ 

Poster, infografis, atau peta bergaya klasik. 

###### **Saat ekspor** 

Pilih **Background: Page color** agar warna ini ikut tercetak. 

###### **Transparan** 

Untuk PNG transparan, pilih Background transparan di jendela ekspor. 

_Pilih warna, misalnya krem #FDF3DC_ 

**029** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0030-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Garis Tepi Halaman (Neatline)** 

Bagian **Page Border (Neatline)** menggambar garis tepi di sekeliling halaman, tunggal atau ganda. 

###### **Show page border** 

Menyalakan garis tepi halaman. 

###### **Double line** 

Garis ganda: garis luar tebal dan garis dalam tipis. 

###### **Color, Width** 

Warna dan tebal garis (mm). 

###### **Inset, Double gap** 

_Page Border (Neatline)_ 

Jarak garis dari tepi kertas dan jarak antar garis ganda. 

Pada contoh Kuningan, garis tepi dibuat dari **Shape** persegi bernama **Neatline** supaya posisinya bisa diatur bebas. 

_Garis tepi di halaman A4 landscape_ 

**030** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0031-02.png)

#### **Grid Kanvas (Canvas grid)** 

Grid kanvas adalah kotak-kotak bantu di layar. Tidak ikut tercetak. 

**Show grid (not printed)** 

Tampilkan grid; juga lewat tombol **Canvas grid** di status bar. 

###### **Spacing, Major every** 

Jarak garis kecil (mm) dan setiap berapa garis ada garis tebal. 

###### **Style, Color, Opacity** 

Garis atau titik, warna, dan transparansi. 

###### **Snap to grid** 

Item menempel ke garis grid saat digeser. 

_Canvas grid_ 

**031** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0032-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Layout Grid (Kolom dan Baris)** 

Layout grid membagi halaman menjadi kolom dan baris seperti di Figma. Item menempel ke tepi kolom sehingga tata letak rapi dan seimbang. 

###### **Show columns and rows** 

Tampilkan kolom/baris (tidak tercetak). 

###### **Columns, Gutter** 

Jumlah kolom dan jarak antar kolom. 

###### **Rows, Gutter** 

Jumlah baris dan jarak antar baris (0 = tanpa baris). 

###### **Margin** 

Tepi grid; 0 memakai margin halaman. 

###### **Color** 

Warna kolom. 

_Layout grid_ 

###### **Snap to columns and rows** 

Item menempel ke tepi kolom. 

_Layout grid merah muda dan guides biru_ 

**032** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0033-02.png)

Plugin Layout Composer 

#### **Guides, Snapping, dan Nudge** 

Guides adalah garis bantu yang ditarik dari penggaris. Snapping membuat item menempel ke guides, margin, dan item lain. 

###### **Membuat guide** 

Tarik dari penggaris atas atau kiri, atau tambahkan pada posisi tepat (Vertical/Horizontal at X/Y lalu **Add** ). 

###### **Guide color, Show guides** 

Warna dan tampil/sembunyi; juga tombol **Guides** di status bar. 

###### **Page margin, Show margin** 

Garis margin halaman. 

###### **Clear all guides** 

Hapus semua guide. 

_Guides_ 

###### **Smart snap** 

Menempel ke item, halaman, margin, dan guides. 

###### **Snap distance** 

Jarak tarik snap (px). 

###### **Arrow keys, Shift + arrows** 

Langkah geser tombol panah (mm). 

_Snapping & nudge_ 

**033** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 3 · Mengatur Halaman** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0034-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0034-04.png)

#### **Variabel Layout** 

Tab **Variables** menyimpan nilai yang bisa disisipkan ke teks mana pun. Ubah sekali, semua teks yang memakainya ikut berubah. 

###### **{title}** 

Judul peta, dari nama proyek GeoLibre bila belum diisi. 

###### **{date}, {year}** 

Tanggal dan tahun saat ini. 

###### **{scale}** 

Skala bingkai peta utama, otomatis mengikuti zoom. 

###### **{projection}** 

Sistem koordinat. 

###### **{author}, {organization}, {source}** 

Pembuat, instansi, sumber data. 

_Layout Variables_ 

###### **Add, hapus** 

Tambah variabel sendiri, lalu tulis {nama} di teks. 

_Judul, skala, dan informasi peta memakai variabel_ 

**034** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0035-02.png)

Plugin Layout Composer 

# **04** 

## **Warna, Efek, dan Urutan Item** 

Color wheel, transparansi, drop shadow, efek kaca (frosted glass), urutan tumpukan, grup, kunci, dan rotasi. 

|Color wheel|Opacity|Drop shadow|Frosted glass|Urutan tumpukan|Grup dan kunci|
|---|---|---|---|---|---|
|Flip dan rotasi||||||

**035** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0036-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Color Wheel: Memilih Warna** 

Setiap kotak warna di panel membuka **color wheel** bulat. Contoh ini dibuka dari warna isi panel informasi. 

###### **Lingkaran warna** 

Klik atau seret untuk memilih warna (hue dan saturasi). 

###### **Brightness** 

Slider kecerahan, dari gelap ke terang. 

###### **Kotak hex** 

Ketik kode warna, misalnya #1E3F8F . 

###### **Eyedropper** 

Ambil warna dari mana saja di layar, misalnya dari logo atau peta. 

###### **Palette** 

Warna siap pakai yang serasi. 

###### **Recent** 

Warna yang baru dipakai muncul di bawah palette. 

###### **None** 

Untuk isi atau latar: centang None agar transparan. 

_Color wheel_ 

**036** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0037-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Transparansi (Opacity)** 

Hampir semua item punya pengaturan transparansi. Gunakan untuk kotak latar di atas peta, label, atau penanda area. 

###### **Opacity item (tab Arrange)** 

Transparansi seluruh item, 0 sampai 1. 

###### **Fill opacity (Shape)** 

Transparansi isi saja, garis tepi tetap pekat. 

###### **Background opacity (Text, Legend)** 

Transparansi latar kotak; teks tetap jelas. 

###### **Opacity grid koordinat** 

Membuat garis grid lebih samar dari label. 

###### **Fill opacity penanda inset** 

Kotak merah di peta inset dengan isi 10 % agar wilayah di bawahnya tetap terlihat. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0037-15.png)

<!-- Start of picture text -->
Contoh Opacity 35 % (kanan atas) dibanding isi penuh<br><!-- End of picture text -->

**037** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0038-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0038-04.png)

#### **Drop Shadow** 

**Drop shadow** memberi bayangan di belakang item sehingga tampak terangkat. Ada di bagian **Effects** pada setiap item. 

Pilih item, buka sub-tab **Style** atau **All** , lalu **1** bagian **Effects** . 

- **2** Centang **Drop shadow** . 

Atur **Color** dan opacity bayangan (misalnya **3** hitam 0,35). 

Atur **Blur** (kelembutan), **X** dan **Y** (arah dan jarak **4** bayangan) dalam mm. 

Bayangan ikut tercetak di semua format ekspor. Gunakan secukupnya agar peta tetap bersih. 

_Bagian Effects_ 

_Drop shadow, Frosted glass, dan gabungan keduanya di atas peta_ 

**038** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0039-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Frosted Glass (Efek Kaca)** 

**Frosted glass** memburamkan peta di belakang item seperti kaca buram. Cocok untuk kotak judul atau keterangan yang diletakkan di atas peta. 

###### **Frosted glass** 

Centang untuk menyalakan efek kaca. 

###### **Blur** 

Tingkat buram peta di belakang (mm). 

###### **Radius** 

Kelengkungan sudut kaca (mm). 

###### **Tint, Tint opacity** 

Warna lapisan kaca dan kepekatannya; putih 0,4 memberi kesan kaca bening. 

###### **Light edge** 

Garis tepi terang tipis seperti pantulan cahaya. 

_Pengaturan kaca_ 

Efek kaca dibuat ulang saat ekspor, jadi hasil PNG dan PDF sama dengan tampilan di layar. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0039-18.png)

<!-- Start of picture text -->
Kartu kaca di atas peta Kuningan<br><!-- End of picture text -->

**039** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0040-02.png)

###### **GeoLibre** 

#### **Urutan Tumpukan Item** 

Item yang dibuat belakangan tampil di atas. Ubah urutan dengan ikon, menu klik kanan, atau panel Layers. 

###### **Bring to front** 

**Bring forward** Naik satu tingkat. 

Pindah ke paling atas. Naik satu tingkat. **Send backward Send to back** Turun satu tingkat. Pindah ke paling bawah. 

###### **Lewat panel Layers** 

Seret nama item ke atas atau ke bawah. Item paling atas di daftar tampil paling depan. 

###### **Lewat menu klik kanan** 

Bring to front dan Send to back. 

###### **Contoh** 

Kotak panel informasi harus di bawah teks judul, jadi panel dikirim ke belakang (Send to back) atau teks dibawa ke depan. 

_Baris kedua: Bring to front, Bring forward, Send backward, Send to back_ 

**040** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0041-02.png)

Plugin Layout Composer 

#### **Grup, Kunci, dan Sembunyikan** 

Untuk tata letak yang rumit, gabungkan item yang selalu bergerak bersama dan kunci item yang sudah pas. 

###### **Group (Ctrl+G)** 

Pilih beberapa item (Shift+klik), lalu klik kanan, **Group** . Grup dipindah dan diubah ukurannya bersama. 

###### **Ungroup (Ctrl+Shift+G)** 

Lepas grup kembali. 

###### **Lock position** 

Item tidak bisa tergeser tidak sengaja; lewat tab Arrange, klik kanan, atau panel Layers. 

###### **Hide** 

Sembunyikan item tanpa menghapus; tidak ikut tercetak. 

###### **Select all (Ctrl+A)** 

Klik kanan di halaman kosong untuk memilih semua item yang tidak terkunci. 

_Group, Lock, Hide di menu klik kanan_ 

**041** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 4 · Warna, Efek, dan Urutan Item** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0042-02.png)

Plugin Layout Composer 

#### **Posisi Presisi, Flip, dan Rotasi** 

Sub-tab **Arrange** berisi posisi dan ukuran tepat untuk setiap item. 

###### **Name** 

Nama item di panel Layers. 

**Titik acuan 9 posisi** X dan Y dihitung dari sudut, tepi, atau tengah item (seperti QGIS). 

**X, Y, W, H** 

Posisi dan ukuran; kunci rasio untuk ukuran proporsional. 

###### **Units** 

mm, cm, in, pt, atau px. 

**Rotation, −90°, +90°** 

Putar bebas atau 90°. 

**Flip H, Flip V** 

Balik horizontal atau vertikal. 

_Position & Size_ 

###### **Center** 

Ketengahkan di halaman. 

**Opacity, Lock position, Hide** Transparansi, kunci, sembunyikan. 

**042** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0043-02.png)

Plugin Layout Composer 

# **05** 

## **Membangun Peta Langkah demi Langkah** 

Menyusun Peta Kelerengan Kabupaten Kuningan dari halaman kosong sampai lengkap, dengan semua parameter setiap elemen. 

|Bingka<br>Inset|i peta<br>Finish|Grid dan double tick<br>ing|Judul dan teks|Skala dan mata angin|Legenda|
|---|---|---|---|---|---|

**043** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0044-01.png)

**GeoLibre** Plugin Layout Composer 

**Langkah 1. Halaman dan Garis Tepi** Mulai dari A4 landscape dengan margin 10 mm. Tambahkan garis tepi: **Shape** , pilih **Rectangle** , lalu di tab **Arrange** isi X 5, Y 5, W 287, H 200 mm. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0044-04.png)

<!-- Start of picture text -->
Halaman kosong Dengan garis tepi<br>Fill: centang None agar kotak transparan<br>Style: warna dan tebal garis<br><!-- End of picture text -->

**044** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0045-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Langkah 2. Bingkai Peta Utama** 

Klik **Map** di top bar. Bingkai muncul di tengah kanvas berisi peta GeoLibre. Seret sudutnya, atau isi posisi di tab Arrange: X 15, Y 13, W 199, H 184 mm. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0045-05.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

Double-click bingkai atau tekan **C** ( ) untuk menggeser dan zoom isi peta. Tekan **Esc** untuk selesai. 

**045** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0046-02.png)

#### **Map: Sumber Peta (Content)** 

Bagian **Content** menentukan dari mana isi bingkai diambil. 

###### **Live map** 

Peta MapLibre hidup: layer vektor dan basemap digambar ulang pada resolusi cetak. Tajam di semua dpi. 

###### **Capture** 

Tangkapan dari tampilan GeoLibre, termasuk layer raster/COG. Arahkan GeoLibre ke area yang diinginkan lalu klik **Recapture GeoLibre view** . Resolusi mengikuti layar. 

_Content_ 

Gunakan **Capture** bila peta berisi raster (COG) yang tidak ikut tergambar di Live map. 

**046** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0047-03.png)

#### **Map: Tampilan dan Skala (Map View)** 

Bagian **Map View** mengatur area, skala, rotasi, dan basemap bingkai. 

**Tombol navigasi** zoom in, zoom out, fit all layers, extent move content. sebelumnya/berikutnya, 

**Match GeoLibre view** Samakan area bingkai dengan tampilan GeoLibre. 

###### **Pan map content** 

Mode geser isi peta. 

**Scale 1 :** 

Isi angka skala atau pilih **Preset** (1:25.000, 1:50.000, dan seterusnya). 

###### **Lock scale** 

Skala tetap saat bingkai digeser atau diubah ukurannya. 

###### **Longitude, Latitude** 

Koordinat pusat bingkai. 

**Extent: Zoom to layer** Pas ke batas layer tertentu. 

###### **Map rotation** 

_Map View_ 

Memutar peta (°); mata angin ikut berputar. 

###### **Basemap, Background** 

Sama dengan GeoLibre, Streets, Light gray, Bright streets, Satellite imagery, Topographic, atau None; warna latar. 

###### **Reload layers from GeoLibre** 

Ambil ulang style dan layer terbaru. 

**047** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0048-02.png)

#### **Map: Layer per Bingkai dan Bingkai** 

Setiap bingkai bisa menampilkan kumpulan layer sendiri, dan bentuk bingkainya pun bisa diubah. 

###### **Layers** 

Centang layer yang tampil di bingkai ini; **Show all** dan **Hide all** . Legenda yang terhubung ikut menyesuaikan. 

###### **Shape** 

Rectangle, rounded, circle/ellipse, triangle, diamond, pentagon, hexagon, octagon, star, heart, shield, arch, atau gambar sebagai masker. 

_Layers_ 

###### **Show frame, Color, Width** 

Garis bingkai peta, warna, dan tebalnya (mm). 

_Frame_ 

_Bingkai lingkaran, segi enam, masker gambar, dan segitiga_ 

**048** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0049-01.png)

**GeoLibre** Plugin Layout Composer 

**Langkah 3. Grid Koordinat** Dengan bingkai peta terpilih, buka bagian **Coordinate Grid / Graticule** dan centang **Show coordinate grid** . 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0049-04.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

**049** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0050-03.png)

#### **Parameter Grid Koordinat** 

Semua pengaturan grid ada di satu bagian panel bingkai peta. 

###### **System** 

DMS, DM, DD (desimal), atau UTM (meter). 

###### **Interval** 

Auto, atau 1" sampai 30°. Untuk UTM: 100 m sampai 100 km. 

###### **UTM zone, Label units** 

Zona 0 = otomatis; label meter atau kilometer. 

###### **Hemisphere labels** 

E/W, N/S atau BT/LS (Indonesia). 

###### **Decimals** 

Desimal untuk DD. 

**Grid lines: Style** 

Solid, Crosses (+), Point, atau No lines (labels only). 

###### **Color, Width, Line, Opacity, Cross size** 

Tampilan garis grid. 

###### **Grid frame** 

Frame style dan Tick length. 

###### **Coordinate labels** 

Top, Bottom, Left, Right; Outside/Inside; Vertical left/right labels; Label offset; Label font. 

_Coordinate Grid / Graticule_ 

**050** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0051-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Gaya Bingkai Grid (Frame style)** 

**Frame style** menentukan tampilan tepi bingkai peta. Gambar di bawah adalah pojok kiri atas peta Kuningan dengan tiap gaya. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0051-05.png)

<!-- Start of picture text -->
Plain Zebra (black-white) Ticks inside<br>Ticks outside Ticks inside + outside (double tick)<br><!-- End of picture text -->

Zebra cocok untuk peta topografi; tick memberi tampilan bersih seperti peta ilmiah. 

**051** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0052-02.png)

###### **GeoLibre** 

#### **Cara Mengatur Double Tick** 

Double tick adalah tanda koordinat yang menonjol **ke dalam dan ke luar** bingkai peta sekaligus. 

- Pilih bingkai peta, buka **Coordinate Grid** 

- **1 / Graticule** , centang **Show coordinate grid** . 

- Pada **Grid frame** , pilih **Frame style:** 

- **2 Ticks inside + outside** . 

- Isi **Tick length** , misalnya 2 mm: tick 

- **3** menonjol 2 mm ke dalam dan 2 mm ke luar. 

_Ticks inside + outside_ 

- Bila hanya ingin tick tanpa garis grid, 

- **4** pilih **Style: No lines (labels only)** . 

- Atur label: **Position Outside** , **Label offset** 

- **5** sekitar 1 mm, centang Top, Bottom, Left, Right. 

- Centang **Vertical left/right labels** agar 

- **6** label sisi kiri dan kanan berdiri tegak. 

_Grid frame dan Coordinate labels_ 

**052** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0053-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Langkah 4. Panel Informasi dan Judul** 

Buat kotak panel dengan **Shape** Rectangle (X 222, Y 13, W 65, H 184). Tambahkan judul dari **Text** , **Heading** , lalu subjudul dan garis pembatas. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0053-05.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

Garis pembatas dibuat dari Shape dengan tinggi 0,01 mm sehingga tampil sebagai garis lurus. 

**053** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0054-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0054-04.png)

#### **Teks: Isi, Variabel, dan Preset** 

Pilih teks, lalu ketik langsung di halaman (double-click atau Enter) atau di kotak **Text** panel kanan. 

###### **Kotak Text** 

Isi teks, boleh beberapa baris. Matematika ditulis di antara $…$ . 

###### **Insert** 

Sisipkan variabel: {title}, {date}, {year}, {scale}, {projection}, {author}, {organization}, {source}. 

###### **Fit height to text** 

Tinggi kotak menyesuaikan jumlah baris. 

###### **Toolbar melayang** 

Muncul di atas teks terpilih: font, ukuran, tebal, miring, garis bawah, warna, perataan, superscript, subscript. 

_Bagian Text (atas)_ 

_Toolbar teks melayang_ 

**054** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0055-02.png)

Plugin Layout Composer 

#### **Teks: Tipografi** 

Bagian bawah panel Text mengatur tampilan huruf secara rinci. 

###### **Font** 

Semua Google Fonts (sekitar 2.000 keluarga) dan font yang terpasang di komputer; ikut tertanam di hasil ekspor. 

###### **Weight, Size, Color, Opacity** 

Ketebalan 100 sampai 900, ukuran (pt), warna, transparansi. 

###### **Style, Case** 

Miring, small caps, garis bawah, coret; huruf besar, kecil, atau seperti diketik. 

###### **Line height, Letter spacing** 

Jarak antarbaris dan antarhuruf. 

###### **Paragraph gap, Padding** 

Jarak antarparagraf dan jarak ke tepi kotak. 

###### **Align, Vertical** 

Kiri, tengah, kanan, rata kiri-kanan; atas, tengah, bawah. 

###### **Resize, Wrap** 

Kotak tetap, tinggi otomatis, atau lebar otomatis. 

_Bagian Text (bawah)_ 

**055** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0056-02.png)

#### **Teks: Halo, Latar, Border** 

Untuk label di atas peta atau kotak keterangan, gunakan halo dan latar. 

###### **Text halo / outline** 

Garis tepi huruf agar terbaca di atas peta; Halo color dan Halo width (mm). 

###### **Background, Background opacity** 

Warna dan transparansi latar kotak teks. 

###### **Border** 

Color, Width, Style (6 gaya garis), Radius sudut. 

###### **Effects** 

Drop shadow dan Frosted glass, sama seperti item lain (Bab 4). 

_Halo, Background & Border_ 

**056** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0057-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0057-04.png)

#### **Shape: Panel dan Garis Pembatas** 

Item **Shape** dipakai untuk panel, kotak, garis pembatas, dan penanda. 

**Shape** 33 bentuk: persegi, rounded, elips, segitiga, panah, bintang, callout, garis, dan lainnya. **Fill** Solid, Gradient, atau Hatch (Bab 8); None untuk transparan; Opacity. **Style: Line** Warna dan tebal garis tepi; Line style (6 gaya); Corner radius. 

_Shape_ 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0057-09.png)

<!-- Start of picture text -->
Fill<br><!-- End of picture text -->

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0057-10.png)

<!-- Start of picture text -->
Style<br><!-- End of picture text -->

**057** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0058-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Langkah 5. Skala dan Mata Angin** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0058-04.png)

Tambahkan skala numerik dan skala batang dari **Scale bar** , lalu mata angin dari . **North arrow** . Ratakan ke tengah panel dengan 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0058-06.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

**058** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0059-03.png)

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0059-04.png)

#### **Parameter Skala Batang** 

Pilih gaya di **Scale Bar Style** , lalu atur di bagian **Settings** . 

###### **Map** 

Bingkai peta acuan skala. 

###### **Units** 

Auto, Kilometers, Meters, Miles, Nautical miles. 

**Segments, Value/segment** Jumlah segmen dan nilai tiap segmen; 0 = otomatis mengisi lebar kotak. 

###### **Subdivided left segment** 

Segmen kiri dibagi kecil seperti skala klasik. 

###### **Unit label** 

Teks satuan, misalnya km. 

###### **Bar height, Line width** 

Tinggi batang dan tebal garis (mm). 

**Color 1, Color 2** 

Warna selang-seling. 

###### **Font** 

Huruf angka skala. 

###### **Also show numeric scale below** 

Tambahkan 1:n di bawah batang; Numeric prefix dan Align. 

_Settings_ 

**059** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0060-02.png)

#### **Galeri 11 Gaya Skala** 

Klik ikon Scale bar di top bar untuk memilih gaya. Gaya bisa diganti kapan saja lewat **Scale Bar Style** di panel. 

_Single box, Double box, Line ticks up, Line ticks down, Line ticks middle, Stepped line, Hollow box, Alternating line, Ruler, Dual units, Numeric (1 : n)_ 

**060** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0061-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Skala Ganda (Dual Units)** 

Gaya **Dual units** menampilkan dua satuan sekaligus: jarak di lapangan di bawah dan ukuran di kertas di atas. 

Pilih skala batang, buka **Scale Bar Style** , klik **Dual 1 units** . Atur **Units** untuk satuan bawah, misalnya **2** Kilometers. Pilih **Second unit** untuk satuan atas: Centimeters **3** on paper (bawaan), km, m, mi, atau nmi. Isi **Second label** bila ingin teks satuan sendiri, **4** misalnya cm. 

Atur **Segments** dan **Bar height** sampai **5** proporsinya pas. 

_Hasil skala ganda_ 

_Settings gaya Dual units_ 

**061** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0062-02.png)

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0062-03.png)

#### **Mata Angin dan Skala Numerik** 

Mata angin punya 26 gaya. Skala numerik adalah gaya **Numeric (1 : n)** di galeri skala. 

###### **Letter** 

N, U (Indonesia), atau tanpa huruf; Letter font. 

###### **Primary, Secondary color** 

Dua warna mata angin. 

###### **Follow map rotation** 

Ikut berputar saat peta diputar; Map acuan dan Extra rotation (°). 

###### **Numeric prefix** 

Teks di depan angka skala, misalnya Skala 1 : . 

**Align (numeric)** 

Kiri, tengah, kanan. 

_Galeri 26 mata angin_ 

_Settings_ 

**062** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0063-02.png)

#### **Langkah 6. Legenda** 

Klik **Legend** . Legenda dibuat dari simbologi layer di bingkai peta yang terhubung. Tambahkan teks total luas di bawahnya. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0063-05.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

**063** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0064-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0064-04.png)

#### **Legenda: Sinkron dan Entri** 

Bagian **Legend** dan **Entries** mengatur isi legenda. 

###### **Sync from map** 

Ambil ulang entri dari layer GeoLibre. 

###### **Fit height** 

Tinggi kotak pas dengan isi. 

###### **Title, Title font, Title alignment** 

Judul legenda dan perataannya. 

###### **Map** 

Bingkai peta sumber legenda. 

###### **Entries** 

_Legend_ 

Centang untuk tampil, ubah label dan warna, naik/turunkan, hapus. 

###### **Add manual entry** 

Entri buatan sendiri: kotak, garis, titik, sungai, danau, arsiran, dan lainnya. 

###### **Opsi** 

Show group headings, Auto-sync when the composer opens, Box height follows content. 

_Entries_ 

**064** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0065-02.png)

Plugin Layout Composer 

#### **Legenda: Tata Letak dan Latar** 

Bagian **Layout** dan **Background & Border** merapikan tampilan legenda. 

**Columns, Column gap** Legenda beberapa kolom dan jaraknya. **Symbol width, height** Ukuran kotak simbol (mm). **Row gap, Padding** Jarak antarbaris dan jarak isi ke tepi. **Group font, Entry font** Huruf judul kelompok dan entri. **Background, opacity** Latar legenda. **Border, Color, Width, Corner radius** _Layout_ Garis tepi kotak legenda. 

_Background & Border_ 

**065** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0066-01.png)

**GeoLibre** Plugin Layout Composer 

**Langkah 7. Informasi Peta** Tambahkan **Body text** berisi sistem koordinat, datum, grid, dan sumber data. Gunakan variabel seperti {projection} dan {source} . 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0066-04.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

**066** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0067-02.png)

#### **Langkah 8. Peta Inset** 

Klik **Inset** . Bingkai peta kecil muncul dan otomatis menandai area peta utama. Tambahkan judul PETA SITUASI dan keterangan kotak merah. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0067-05.png)

<!-- Start of picture text -->
Kanvas pada tahap ini<br><!-- End of picture text -->

**067** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0068-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0068-04.png)

#### **Mengatur Inset (1): Area dan Layer** 

Inset adalah bingkai peta biasa dengan skala lebih kecil. Atur dulu wilayah yang ditampilkan. 

Pilih bingkai inset, atur ukuran di tab Arrange **1** (contoh: X 229, Y 136, W 54, H 40 mm). 

- Di **Map View** , isi skala kecil atau zoom out 

- **2** sampai seluruh provinsi terlihat. 

- Isi **Longitude** dan **Latitude** pusat wilayah, misalnya 

- **3** Jawa Barat. 

- Pilih **Basemap** sederhana, misalnya Light gray, agar 

- **4** kotak penanda menonjol. 

Di **Layers** , sembunyikan layer rinci dan sisakan batas **5** wilayah saja. 

_Map View inset_ 

_Layers inset_ 

**068** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0069-03.png)

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0069-04.png)

#### **Mengatur Inset (2): Penanda Area** 

Bagian **Overview / Locator** menggambar posisi peta utama di dalam inset. 

###### **Show extent of** 

Bingkai yang ditandai, biasanya **Main map** ; none untuk mematikan. 

###### **Marker** 

Extent box (kotak luasan), Location point (titik), atau Box + crosshair. 

###### **Line, Width** 

Warna dan tebal garis penanda, misalnya merah 0,5 mm. 

###### **Fill, Opacity** 

Isi kotak penanda, misalnya merah 10 %. 

_Overview / Locator_ 

Kotak penanda ikut bergerak otomatis setiap kali peta utama digeser atau di-zoom. 

_Hasil inset_ 

**069** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 5 · Membangun Peta Langkah demi Langkah** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0070-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Langkah 9. Penulis dan Finishing** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0070-04.png)

Tambahkan teks pembuat dan tahun. Rapikan semua item dengan perataan, distribusi, dan posisi presisi di tab Arrange. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0070-06.png)

<!-- Start of picture text -->
Layout lengkap di dalam Layout Composer<br><!-- End of picture text -->

Periksa sekali lagi: judul, skala, mata angin, legenda, grid, inset, sistem koordinat, sumber data, pembuat dan tahun. 

**070** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0071-02.png)

Plugin Layout Composer 

# **06** 

## **Color Bar Lengkap** 

Semua mode color bar gaya matplotlib: sumber data, 39 colormap, kelas, ujung, orientasi, tick, label, dan judul. 

|Sumber nilai|39 colo|rmap<br>Kontinu dan|kelas|Ujung pointed dan square|
|---|---|---|---|---|
|Vertikal dan ho|rizontal|Penempatan tick|Judul||

**071** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0072-02.png)

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0072-03.png)

#### **Mengenal Color Bar** 

Color bar menunjukkan arti warna pada peta raster atau peta bergradasi. Klik **Color bar** di top bar; bilah muncul di tengah tampilan. 

###### **Data** 

Sumber nilai, minimum, maksimum, colormap, kelas, reverse. 

###### **Bar** 

Orientation, ujung (Ends), bentuk ujung, panjang ujung, tebal, outline. 

###### **Ticks & Labels** 

Penempatan, jumlah, desimal, prefix/suffix, sisi, arah tick, panjang, warna, huruf. 

###### **Title** 

Teks (boleh LaTeX), posisi, perataan, huruf. 

###### **Background & Border** 

Latar, padding, garis tepi. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0072-16.png)

<!-- Start of picture text -->
Color bar vertikal untuk raster NDVK0<br><!-- End of picture text -->

**072** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0073-02.png)

Plugin Layout Composer 

#### **Color Bar: Sumber Nilai (Data)** 

Color bar bisa membaca nilai langsung dari layer raster di GeoLibre. 

###### **Values from** 

Pilih layer raster atau layer bergradasi. Min, max, dan colormap dibaca otomatis dari stretch atau statistik layer. 

###### **Re-read from layer** 

Baca ulang setelah simbologi layer diubah. 

###### **Minimum, Maximum** 

Rentang nilai; bisa diisi manual. 

###### **Colormap** 

39 colormap atau Custom (lihat halaman berikut). 

###### **Classes** 

_Data_ 

0 = gradasi kontinu; 2 atau lebih = kelas bertingkat. 

###### **Reverse** 

Balik urutan warna (seperti akhiran _r di matplotlib). 

**073** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0074-03.png)

#### **Memilih Colormap** 

Klik tombol colormap untuk membuka katalog. Pratinjau setiap colormap ikut menampilkan efek Reverse. 

###### **Sekuensial** 

viridis, plasma, inferno, magma, cividis, greys, blues, greens, oranges, reds, purples, ylgn, ylorrd, ylgnbu, ylorbr, bupu, gnbu: nilai rendah ke tinggi. 

###### **Divergen** 

spectral, rdylgn, rdylbu, rdbu, brbg, coolwarm, bwr, seismic, piyg, prgn, puor: dua arah dari nilai tengah. 

###### **Pelangi dan khusus** 

jet, turbo, rainbow, hot, cool, terrain, ocean, gist_earth, gray, twilight, cubehelix. 

###### **Custom** 

Isi warna sendiri dari rendah ke tinggi, dipisah koma. 

_Katalog colormap_ 

**074** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0075-02.png)

#### **39 Colormap** 

Semua colormap yang tersedia, dirender langsung oleh Layout Composer. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0075-05.png)

<!-- Start of picture text -->
viridis sampai cubehelix<br><!-- End of picture text -->

Contoh di atas memakai rentang 0 sampai 1 supaya semua warnanya bisa dibandingkan dengan rentang yang sama. Untuk raster sungguhan, rentangnya mengikuti nilai rasternya, termasuk nilai negatif seperti -1 atau -3,5. 

**075** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0076-02.png)

#### **Gradasi Kontinu, Kelas, Reverse, Custom** 

Atur **Classes** untuk mengubah gradasi menjadi kelas bertingkat, dan **Reverse** untuk membalik urutan warna. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0076-05.png)

<!-- Start of picture text -->
Classes 0, 5, 10; Reverse; Custom colors; Outline; Thickness<br><!-- End of picture text -->

Kelas bertingkat cocok untuk data yang dikelompokkan (misalnya kelas kerapatan), gradasi kontinu cocok untuk nilai menerus seperti NDVI atau elevasi. 

**076** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0077-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Ujung Bilah: Flat, Min, Max, Both** 

**Ends** menambahkan ujung yang menandakan nilai di luar rentang, seperti extend di matplotlib. **End shape** mengatur bentuknya. 

**Flat** Tanpa ujung. **Min** Ujung di sisi nilai terendah. **Max** Ujung di sisi nilai tertinggi. **Both** Ujung di kedua sisi. **End shape** Pointed (segitiga) atau Square (kotak). **End length** Panjang ujung relatif terhadap bilah. 

_Tujuh kombinasi ujung_ 

**077** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0078-02.png)

#### **Orientasi dan Posisi Judul** 

Color bar bisa horizontal atau vertikal. Judul bisa di atas, bawah, atau samping, dan tick bisa di kiri atau kanan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0078-05.png)

<!-- Start of picture text -->
Vertical: judul Top, Bottom, Side; tick di kiri; judul LaTeX dengan ujung Max<br>Horizontal: Title Above (Left, Center), Title Below (Right), Side<br><!-- End of picture text -->

**078** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0079-02.png)

#### **Tick dan Label** 

Bagian **Ticks & Labels** mengatur angka di sepanjang bilah. 

###### **Placement** 

Even (merata seperti numpy.linspace), Rounded (angka bulat di dalam rentang), Custom (isi nilai sendiri). 

###### **Number of ticks, Values** 

Jumlah tick atau daftar nilai custom. 

###### **Decimals, 1,000 separator** 

Auto atau 0 sampai 4; pemisah ribuan. 

###### **Prefix, Suffix** 

Teks di depan dan belakang angka: m, °C, %. 

###### **Side** 

Below/Above (horizontal) atau Right/Left (vertikal). 

###### **Tick marks** 

Out, In, Both, None; Length, Width, Tick color. 

_Contoh setiap pengaturan tick_ 

###### **Label font** 

Huruf angka. 

**079** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0080-02.png)

#### **Panel Bar dan Ticks** 

Tampilan lengkap pengaturan bilah dan tick di panel kanan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0080-05.png)

<!-- Start of picture text -->
Bar<br>Title<br><!-- End of picture text -->

_Ticks & Labels_ 

**080** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 6 · Color Bar Lengkap** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0081-03.png)

#### **Contoh Resep Color Bar** 

Beberapa kombinasi yang sering dipakai di peta tematik dan figur penelitian. 

|**Kebutuhan**|**Pengaturan**|
|---|---|
|NDVI|Colormap rdylgn, min -0,2 max 0,9, Ends Both Pointed, Even 6 ticks|
|Elevasi|Colormap terrain, Rounded ticks, Suffix " m", 1,000 separator, judul "Elevasi<br>($m$)"|
|Suhu permukaan|Colormap coolwarm atau rdbu Reverse, Suffix " °C"|
|Kelas kerapatan|Classes 5, colormap ylgn, Tick marks None|
|Figur riset gaya<br>matplotlib|Vertical, jet atau viridis, Even 6 ticks, Decimals 1, judul kosong, font DejaVu<br>Sans|
|Persentase|Min 0 max 100, Suffix " %", Decimals 0|

Untuk figur ilmiah, hindari judul ganda: kosongkan judul color bar bila judul sudah ada di atas peta. 

**081** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0082-02.png)

Plugin Layout Composer 

# **07** 

## **Teks, LaTeX, Font, dan Simbol** 

Semua preset teks, efek teks, font, penulisan rumus LaTeX, marker titik, dan katalog ikon. 

|Menu Text|Efek teks|Google Fonts|Formula LaTeX|LaTeX dalam teks|Marker|
|---|---|---|---|---|---|
|Katalog ikon||||||

**082** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0083-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0083-04.png)

#### **Menu Text** 

Menu Text berisi sembilan preset. Pilih salah satu, item muncul di tengah tampilan. 

###### **Heading, Subheading** 

Judul 26 pt dan 15 pt tebal. 

**Body text** 

Paragraf yang membungkus. 

**Caption** 

Catatan kecil miring. 

**Map label** Huruf kapital renggang dengan halo, untuk nama tempat di atas peta. 

###### **Callout** 

_Menu Text_ 

Teks di atas kotak berwarna. 

**Map title** 

Memakai variabel {title}. 

###### **Table / info box** 

Baris dan kolom, misalnya kotak judul. 

**Formula (LaTeX)** Rumus MathJax. 

**083** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0084-02.png)

#### **Delapan Efek Teks** 

Bagian **Text effects** memberi gaya pada huruf. Atur **Effect color** dan **Strength** untuk tiap efek. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0084-05.png)

<!-- Start of picture text -->
None, Shadow, Lift, Hollow, Outline, Highlight, Neon, Echo<br>Shadow, Lift<br>Bayangan tegas atau lembut di bawah huruf.<br>Hollow, Outline<br>Huruf berongga atau bergaris tepi.<br>Highlight<br>Stabilo di belakang teks.<br>Neon, Echo<br>Cahaya berpendar dan bayangan berlapis, cocok untuk poster.<br><!-- End of picture text -->

**084** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0085-02.png)

#### **Memilih Font** 

Klik nama font di panel teks untuk membuka pemilih font. 

###### **Google Fonts** 

Sekitar 2.000 keluarga, bisa disaring: sans, serif, display, script, mono. Setiap nama ditampilkan dengan hurufnya sendiri. 

###### **Installed** 

Font yang terpasang di komputer. 

###### **Pencarian** 

Ketik nama font. 

###### **Saat ekspor** 

Google Fonts ikut tertanam di PNG, JPG, PDF, dan SVG sehingga tampil sama di komputer lain. 

_Pemilih font: tab All, Google Fonts, Installed_ 

**085** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0086-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0086-04.png)

#### **Menulis LaTeX (1): Item Formula** 

Menu Text, **Formula (LaTeX)** membuat rumus vektor dengan MathJax 3. Tulis kode LaTeX di kotak **Formula** . 

###### **Kotak Formula** 

Kode LaTeX apa pun, contoh \frac{NIR-Red}{NIR+Red} . 

###### **Tombol template** 

Fraction, Superscript, Subscript, Square root, n-th root, Sum, Product, Integral, Limit, Vector, Overline, Hat, Binomial, 2×2 matrix, Upright text. 

###### **Recent** 

Rumus yang pernah dipakai. 

###### **Size, Color** 

Ukuran (pt) dan warna. 

###### **Style** 

Display atau Inline. 

###### **Align, Vertical** 

Posisi di dalam kotak. 

###### **Fit box to formula** 

Ukuran kotak pas dengan rumus. 

_Formula_ 

###### **Symbols** 

Katalog: Greek, Operators, Units, Arrows, Sets & logic. 

_Rumus NDVI_ 

**086** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0087-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Menulis LaTeX (2): Di Dalam Teks** 

Di teks biasa, judul legenda, judul color bar, dan label marker, apit kode dengan tanda dolar: $…$ . Contoh: Kelas lereng ($\%$) . 

|**Ditulis**|**Hasil**|**Ditulis**|**Hasil**|
|---|---|---|---|
|$km^{2}$|km²|$\alpha, \beta, \sigma$|α,β,σ|
|$x_{i}$|xᵢ|$^{\circ}C$|°C|
|$\frac{a}{b}$|pecahan|$\%$|%|
|$\sqrt{x}$|akar x|$\pm, \times, \leq$|±, ×,≤|
|$\sum_{i=1}^{n} x_i$|sigma|$\mathrm{Mg\,ha^{-1}}$|Mg ha⁻¹|
|$\bar{x}$|x̄|$R^{2}$|R²|
||_Teks d_|_engan LaTeX_||

\, memberi spasi kecil, \mathrm{…} membuat huruf tegak untuk satuan. Bagian **LaTeX & Symbols** di panel Text menyisipkan kode langsung ke posisi kursor. 

**087** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0088-02.png)

#### **Katalog Simbol LaTeX** 

Bagian **Symbols** berisi lima kelompok simbol. Klik simbol untuk menyisipkannya. 

**Greek** α β γ δ ε … Ω (34 huruf). 

**Operators** ± × ÷ · √ ∑ ∏ ∫ ∂ ∇ ∞ ≈ ≠ ≤ ≥ dan lainnya. 

###### **Units** 

m², km², ha⁻¹, Mg ha⁻¹, g C m⁻², µm, °C, %, ‰ , R², p<.05, x̄ . 

###### **Arrows** 

→ ← ↔ ⇒ ⇔ ↑ ↓ ↦. 

**Sets & logic** 

∈ ∉ ⊂ ⊆ ∪ ∩ ∀ ∃ ¬ ∧ ∨ ∅ ℝ ℕ ℤ. 

_Symbols_ 

**088** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0089-02.png)

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0089-03.png)

#### **Marker Titik** 

Menu Symbols membuka 12 marker titik. Setiap marker bisa diberi label. 

**Symbol** Pin, Circle, Dot, Capital, Square, Triangle, Peak, Diamond, Star, Cross, Flag, Sample point. 

**Fill, Stroke, Size** Warna isi, garis, dan ukuran. _Point markers_ 

**Label, Position, Font** Teks label, posisi di sekitar marker, huruf (boleh LaTeX). _Galeri marker_ 

**089** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 7 · Teks, LaTeX, Font, dan Simbol** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0090-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0090-04.png)

#### **Katalog Ikon** 

Dari menu Symbols, pilih **Icon catalog** . Ada tiga sumber ikon yang bisa dicari sambil mengetik. 

###### **Maki (215)** 

Ikon peta CC0: transportasi, layanan umum, wisata, dan lainnya. 

###### **Temaki (557)** 

Ikon tematik CC0: air, medan, vegetasi, bahaya, utilitas. 

###### **Google Material Symbols (3.912)** 

17 kategori; gaya Outlined, Rounded, Sharp; isi kosong atau penuh. 

###### **Icon** 

Color, Label, Font. 

###### **Offline** 

Ikon yang ditempatkan disimpan di dalam layout. 

_Maki dan Temaki_ 

_Material Symbols_ 

**090** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0091-02.png)

Plugin Layout Composer 

# **08** 

## **Bentuk, Isian, Garis, Gambar, dan Draw** 

33 bentuk, tiga jenis isian, enam gaya garis, gambar dengan filter dan masker, serta alat gambar bebas. 

|Galeri bentuk<br>Masker<br>Dra|Solid, gradient, hatch<br>w dan pena|Gaya garis|Toolbar bentuk|Gambar dan filter|
|---|---|---|---|---|

**091** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0092-01.png)

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0092-03.png)

#### **Galeri 33 Bentuk** 

Klik Shape di top bar untuk memilih bentuk. Bentuk bisa diganti kapan saja lewat bagian **Shape** di panel. 

_Rectangle, Rounded, Ellipse, Triangle, Right triangle, Diamond, Pentagon, Hexagon, Octagon, Star, panah, Chevron, Ribbon, Callout, Heart, Speech bubble, garis, dan lainnya_ 

**092** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0093-02.png)

Plugin Layout Composer 

#### **Tiga Jenis Isian (Fill)** 

Bagian **Fill** pada Shape dan Drawing punya tiga jenis isian. 

###### **Solid** 

Satu warna; centang None untuk transparan. 

**Gradient** Dari warna **From** ke **To** dengan **Angle** 0 sampai 360°. 

**Hatch** Arsiran: Diagonal /, Diagonal \, Crosshatch ×, Horizontal, Vertical, Grid +, Dots. 

**Hatch: Line color, Spacing, Line width** Warna, jarak, dan tebal arsiran. 

_Dua belas contoh isian_ 

**Fill behind** 

Warna latar di belakang arsiran. 

**Opacity** Transparansi isian. 

**093** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0094-02.png)

#### **Enam Gaya Garis** 

Garis tepi Shape, garis Drawing, border teks, dan garis grid bisa memakai enam gaya. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0094-05.png)

<!-- Start of picture text -->
Solid, Dashed, Long dash, Dotted, Dash-dot, Long dash-dot<br><!-- End of picture text -->

Batas administrasi biasa memakai Dash-dot atau Long dash-dot; jalan setapak memakai Dotted. 

**094** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0095-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Toolbar Bentuk Melayang** 

Saat Shape dipilih, toolbar kecil muncul di atasnya untuk pengaturan cepat tanpa membuka panel. 

_Toolbar Shape_ **Fill, None** Warna isi atau transparan. **Line, Width** Warna dan tebal garis tepi. **Line style** Gaya garis. **Opacity** Transparansi. Flip, duplikat, kunci, hapus. 

**095** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0096-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0096-04.png)

#### **Gambar dan Logo** 

Klik Image di top bar, lalu **Choose image** untuk memilih file PNG, JPG, atau SVG. 

###### **Fit** 

Contain (rasio tetap), Cover (dipotong), Stretch. 

###### **Mask** 

Rectangle, Circle/ellipse, Hexagon, Star, Heart, Blob. 

###### **Opacity** 

Transparansi gambar. 

_Preset filter dan masker_ 

###### **Border, Color, Width, Corner radius** 

Bingkai gambar. 

###### **Adjust** 

Brightness, Contrast, Saturation, Grayscale, Sepia, Hue, Blur. 

###### **Preset** 

Original, Mono, Vivid, Warm, Faded, Dramatic. 

**096** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 8 · Bentuk, Isian, Garis, Gambar, dan Draw** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0097-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0097-04.png)

#### **Draw: Menggambar Bebas** 

Menu Draw berisi lima alat gambar. 

###### **Polyline** 

Klik titik demi titik untuk garis. 

**Polygon** _Menu Draw_ 

Area tertutup dengan isian. 

**Bézier pen** Klik = sudut, seret = lengkung. 

###### **Freehand** 

Gambar bebas, otomatis dihaluskan. 

###### **Arrow line** 

Garis dengan kepala panah. 

###### **Selesai menggambar** 

Enter atau double-click; Backspace menghapus titik terakhir; Esc membatalkan. 

###### **Drawing** 

Line, Line style, Fill (untuk area tertutup). 

Gunakan Draw untuk menandai rute, batas rencana, atau anotasi di atas peta. 

**097** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 9 · Tabel dan Grafik dari Data** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0098-02.png)

# **09** 

## **Tabel dan Grafik dari Data** 

Membuat tabel atribut dan grafik langsung dari atribut layer; nilainya ikut berubah bila data berubah. 

|Menu Data|Attribute table|Gaya tabel|Pie dan donut|Bar dan column|
|---|---|---|---|---|

**098** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 9 · Tabel dan Grafik dari Data** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0099-02.png)

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0099-03.png)

#### **Menu Data** 

Menu Data berisi satu tabel dan empat jenis grafik. 

###### **Attribute table** 

Luas atau jumlah per kelas, atau daftar fitur. 

###### **Donut chart** 

Porsi tiap kelas, total di tengah. 

**Pie chart** Porsi tiap kelas. 

_Menu Data_ 

###### **Bar chart** 

Batang mendatar, cocok untuk nama kelas panjang. 

###### **Column chart** 

Batang tegak untuk membandingkan kelas. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0099-16.png)

<!-- Start of picture text -->
Tabel ringkasan, donut, dan grafik batang dari data Kuningan<br><!-- End of picture text -->

**099** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 9 · Tabel dan Grafik dari Data** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0100-02.png)

Plugin Layout Composer 

#### **Tabel Atribut: Data** 

Bagian **Data** menentukan apa yang dihitung. 

###### **Layer, Group by** 

Layer sumber dan kolom kelas. 

###### **Value** 

Area (ha atau km²), Length (km), Count, Sum atau Average sebuah kolom. 

###### **Field** 

Kolom angka untuk Sum atau Average. 

###### **Filter** 

=, ≠ , >, <, contains. 

###### **Sort** 

Largest first, smallest first, A-Z. 

###### **Show top, Rest as** 

N kelas teratas, sisanya digabung jadi Other. 

###### **Decimals, Number format** 

Desimal dan format 1,234.56 atau 1.234,56. 

_Data_ 

###### **Refresh from layer** 

Hitung ulang. 

**100** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 9 · Tabel dan Grafik dari Data** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0101-02.png)

Plugin Layout Composer 

#### **Tabel Atribut: Isi dan Gaya** 

Bagian **Table Content** dan **Table Style** mengatur kolom dan tampilan. 

###### **Show** 

Summary (ringkasan per kelas) atau Feature list (daftar fitur dengan kolom pilihan). 

###### **Count column, Percent column, Total row** 

Kolom jumlah, persen, dan baris total. 

###### **Header row, Fit height to rows** 

Baris judul dan tinggi otomatis. 

###### **Font, Title font, Header** 

Huruf dan warna header. 

_Table Content_ 

**Striped rows, Stripe color** 

Baris belang. 

###### **Inner/outer border, Column widths** 

Garis dalam/luar dan lebar kolom. 

_Table Style_ 

**101** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 9 · Tabel dan Grafik dari Data** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0102-02.png)

#### **Empat Jenis Grafik** 

Pie, Donut, Bar, dan Column dari data kelas lereng Kuningan. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0102-05.png)

<!-- Start of picture text -->
Pie, Donut, Bar, Column<br><!-- End of picture text -->

###### **Labels** 

Percent, Value, Class, atau tanpa label. 

**Legend beside the chart** Legenda di samping; Legend values. 

###### **Hole, Center** 

Lubang donut dan isi tengah (Total). 

###### **Gridlines** 

Garis bantu pada Bar dan Column. 

**102** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 9 · Tabel dan Grafik dari Data** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0103-02.png)

Plugin Layout Composer 

#### **Grafik: Warna dan Gaya** 

Warna grafik bisa mengikuti simbologi layer, palet, atau satu warna. 

**Colors: Layer** Warna sama dengan simbologi di peta, sehingga grafik dan legenda serasi. **Colors: Palette** viridis, plasma, dan lainnya; Reverse. **Colors: One color** Satu warna untuk semua batang. **Slice outline** _Chart_ Garis antar irisan pie/donut. 

**Style** 

Font teks dan judul, Padding, Border. 

_Colors_ 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0103-10.png)

<!-- Start of picture text -->
Style<br><!-- End of picture text -->

**103** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0104-02.png)

Plugin Layout Composer 

# **10** 

## **Contoh: Layout Seri Raster Gaya Riset** 

Menyusun empat peta raster Sentinel-2 (NDVI dan NBR+) dalam satu figur 2 × 2 bergaya matplotlib dengan palet jet. 

|Data NBR+<br>Judul subplot|Empat bingkai|Layer per bingkai|Ticks outside|Color bar jet|
|---|---|---|---|---|

**104** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0105-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Hasil: Analisis Kebakaran NBR+** 

Figur riset 2 × 2: (a) NDVI, (b) NBR+ sebelum kebakaran, (c) NBR+ sesudah kebakaran, (d) area terbakar. Setiap panel punya color bar jet sendiri. 

_Disusun seluruhnya di Layout Composer_ 

**105** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0106-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Langkah 1: Data dan Palet** 

Data berasal dari folder hasil pengolahan Sentinel-2 (NDVI, NBR+ pre-fire, NBR+ post-fire, burn mask). 

- **1** Muat keempat raster ke GeoLibre dan beri nama yang jelas. 

- Atur colormap **jet** untuk setiap raster dengan rentang tetap: NDVI 0,4 sampai 0,9; NBR+ 

- **2** -0,8 sampai 0,2 (sama untuk sebelum dan sesudah agar bisa dibandingkan); area terbakar 0,3 sampai 0,8. 

- Untuk burn mask, area yang tidak terbakar dibuat abu-abu muda agar petak terbakar 

- **3** menonjol. 

- **4** Buat halaman **custom** 222 × 222 mm, margin 0 (tab Page). 

Rentang yang sama pada panel (b) dan (c) penting agar perubahan warna benar-benar menunjukkan perubahan nilai. 

**106** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0107-02.png)

#### **Langkah 2: Empat Bingkai dan Layer per Bingkai** 

Tambahkan empat bingkai peta 62 × 82 mm dalam susunan 2 × 2. Setiap bingkai hanya menampilkan satu raster lewat bagian **Layers** . 

_Bingkai (a) NDVI terpilih; panel Layers per bingkai di kanan_ 

###### **Posisi** 

Kolom kiri X 20, kolom kanan X 124; baris atas Y 22, baris bawah Y 122. 

###### **Layers** 

Centang hanya raster milik panel itu. 

###### **Basemap** 

Same as GeoLibre dengan latar putih, tanpa basemap jalan. 

###### **Duplikat** 

Buat satu bingkai dulu, lalu Ctrl+D tiga kali agar ukurannya sama. 

**107** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0108-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Langkah 3: Sumbu Koordinat Gaya Matplotlib** 

Grid koordinat diatur agar mirip sumbu matplotlib: hanya tick di luar bingkai dan label derajat desimal. 

###### **System** 

Decimal degrees (DD), Decimals 2, Hemisphere E/W N/S. 

###### **Interval** 

0,02° agar ada 2 sampai 3 label per sisi. 

###### **Style** 

No lines (labels only): tanpa garis grid di dalam peta. 

###### **Frame style** 

Ticks outside, Tick length 1,1 mm. 

###### **Labels** 

Left dan Bottom saja, Outside, Vertical left/right labels. 

###### **Label font** 

DejaVu Sans 5,5 pt, hitam. 

_Panel (a) dengan tick di luar_ 

###### **Frame** 

Show frame, hitam, 0,25 mm. 

**108** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0109-02.png)

#### **Langkah 4: Color Bar Jet dan Judul** 

Tambahkan color bar vertikal di kanan setiap bingkai, lalu judul subplot di atasnya. 

###### **Color bar** 

Orientation Vertical, X = bingkai + 64 mm, W 9 mm, H 82 mm, Thickness 3,2 mm. 

###### **Data** 

Colormap jet, Min dan Max sama dengan rentang raster, Classes 0. 

###### **Ticks** 

Even, 6 ticks, Decimals 1, Tick marks Out, font DejaVu Sans 5,5 pt; judul dikosongkan. 

###### **Judul subplot** 

Text 8 pt di atas bingkai: (a) NDVI, (b) NBR+ sebelum kebakaran, dan seterusnya. 

_Panel (d) dengan color bar jet_ 

###### **Judul utama** 

Heading 11 pt tebal di tengah atas halaman. 

###### **Sumber** 

Caption 6 pt di bawah: data, palet, sistem koordinat. 

Rapikan dengan Align top untuk baris, Align left untuk kolom, dan Distribute horizontally. 

**109** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 10 · Contoh: Layout Seri Raster Gaya Riset** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0110-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Tips Figur Seri** 

Beberapa kebiasaan yang membuat figur seri tampak profesional. 

###### **Ukuran sama** 

Semua bingkai berukuran sama dan berskala sama; kunci skala dengan Lock scale. 

###### **Rentang konsisten** 

Panel yang dibandingkan memakai min dan max yang sama. 

###### **Label huruf** 

- (a), (b), (c), (d) memudahkan rujukan di naskah. 

###### **Simpan sebagai template** 

Save this layout as template, lalu ganti raster untuk lokasi atau tanggal lain. 

###### **Ekspor** 

Vector PDF untuk naskah jurnal, PNG 300 dpi untuk slide atau poster. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0110-15.png)

<!-- Start of picture text -->
Figur seri yang sudah jadi<br><!-- End of picture text -->

**110** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0111-02.png)

# **11 Ekspor, Penyimpanan, dan Penutup** 

Mengekspor peta, menyimpan layout, bertukar template dengan QGIS, dan daftar periksa sebelum mencetak. 

|Format ekspor|Resolusi dan latar|Simpan layout|Template QGIS|Daftar periksa|
|---|---|---|---|---|
|Penutup|||||

**111** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

**GeoLibre** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0112-02.png)

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0112-04.png)

#### **Ekspor Peta** 

Klik ikon Export di kanan atas. Jendela ekspor menampilkan format, resolusi, latar, dan nama file. 

###### **PNG** 

Gambar; bisa berlatar transparan. 

###### **JPG** 

Gambar lebih kecil. 

###### **PDF** 

Halaman diratakan. 

###### **Vector PDF** 

Teks dan garis tetap tajam. 

###### **GeoPDF** 

Setiap bingkai peta tergeoreferensi (WGS 84). 

_Jendela Export_ 

###### **SVG** 

Vektor yang bisa diedit. 

###### **Resolution** 

75 sampai 600 dpi; ukuran piksel hasil tampil di bawahnya. 

###### **Background, File name** 

Page color, putih, atau transparan; nama file. 

**112** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0113-01.png)

**GeoLibre** Plugin Layout Composer 

#### **Progres Ekspor dan Rekomendasi** 

Bilah progres terisi dari kiri ke kanan: render bingkai peta, susun halaman, tulis file. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0113-05.png)

<!-- Start of picture text -->
Progres ekspor<br>Tujuan Format dan resolusi<br>Cetak kertas, poster PNG atau PDF 300 dpi<br>Slide, web, media sosial PNG atau JPG 150 dpi<br>Naskah jurnal, laporan Vector PDF<br>Dibuka di aplikasi GIS lapangan GeoPDF<br>SVG<br>Diedit lagi di Inkscape/Illustrator<br><!-- End of picture text -->

**113** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0114-01.png)

###### **GeoLibre** 

Plugin Layout Composer 

#### **Menyimpan Layout dan Template QGIS** 

Layout tersimpan otomatis di proyek. Simpan juga sebagai file agar bisa dipakai di komputer lain. 

###### **Save layout file** 

Unduh .layout.json dari ikon di kanan atas. 

###### **Open layout file** 

Main menu: buka file layout. 

###### **Save as template** 

Simpan susunan untuk peta berikutnya. 

###### **Export as QGIS template (.qpt)** 

Label, bingkai peta, gambar, bentuk, skala, dan legenda menjadi item asli QGIS; item lain dibawa sebagai gambar SVG. 

###### **Import QGIS template** 

Buka template QGIS 3: ukuran halaman, label, peta, gambar, bentuk, skala, legenda, garis, poligon. 

_Semua perintah berkas ada di Main menu_ 

**114** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0115-02.png)

###### **GeoLibre** 

#### **Daftar Periksa Sebelum Mencetak** 

Gunakan daftar ini setiap kali menyelesaikan peta. 

- ☑ Judul dan subjudul jelas 

   - ☑ Peta inset dengan penanda area 

- ☑ Peta utama dengan skala tepat 

   - ☑ Sistem koordinat dan datum 

- ☑ Grid koordinat dan label lengkap 

   - ☑ Sumber data 

- ☑ Skala batang atau numerik 

   - ☑ Pembuat dan tahun 

- ☑ Mata angin 

   - ☑ Ejaan dan ukuran huruf terbaca 

- ☑ Legenda lengkap dan urut 

- ☑ Resolusi ekspor sesuai tujuan 

_Semua butir terpenuhi pada layout contoh_ 

**115** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

**GeoLibre** Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0116-02.png)

#### **Hasil Akhir** 

Peta Kelerengan Kabupaten Kuningan, diekspor dari Layout Composer. Semua elemen di peta ini dibahas di panduan ini. 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0116-05.png)

<!-- Start of picture text -->
Peta Kelerengan Kabupaten Kuningan<br><!-- End of picture text -->

**116** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0117-03.png)

#### **Penutup** 

Terima kasih sudah membaca panduan ini sampai akhir. Semoga setiap halaman membantu teman-teman menyusun peta yang rapi, informatif, dan siap dibagikan. 

Layout Composer adalah proyek terbuka. Kode sumber, rilis terbaru, dan contoh layout tersedia di GitHub. Bila menemukan bug, punya ide fitur, atau ingin ikut mengembangkan, silakan buka _issue_ atau kirim _pull request_ . Setiap masukan, sekecil apa pun, sangat berarti. 

###### **github.com/Defani/Layout-Composer** 

Kode sumber, rilis, contoh layout, dan laporan bug · Lisensi MIT 

###### **Pasang** 

GeoLibre, Settings, Manage Plugins, cari **layout** , Install. 

**Laporkan bug atau ide** Tab **Issues** di repositori GitHub. 

###### **Ikut berkontribusi** 

Fork repositori, ubah, lalu kirim pull request. 

Selamat memetakan, 

###### **Defani Arman Alfitriansyah** 

**Plugin Developer** 

**117** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0118-03.png)

#### **Referensi (1): Perangkat Lunak, Engine, dan Layanan** 

Semua pustaka, set ikon, sumber font, dan layanan peta yang dipakai Layout Composer dan panduan ini. 

**1.** Alfitriansyah, D. A. (2026). _Layout Composer: cartographic layout designer for GeoLibre_ (v1.8.2) [Software]. MIT License. github.com/Defani/Layout-Composer 

**2.** Wu, Q., & Open Geospatial Solutions. (2026). _GeoLibre: a free and open-source, cloud-native GIS platform_ [Software]. geolibre.app · github.com/opengeos/GeoLibre 

**3.** Open Geospatial Solutions. (2026). _GeoLibre plugin registry_ and _plugin template_ . 

   - plugins.geolibre.app · github.com/opengeos/geolibre-plugins · github.com/opengeos/geolibre-plugin-template 

**4.** MapLibre contributors. _MapLibre GL JS_ [Software]. BSD-3-Clause. 

   - maplibre.org · github.com/maplibre/maplibre-gl-js 

**5.** Cervone, D. (2012). MathJax: a platform for mathematics on the Web. _Notices of the AMS_ , 59(2), 312-316. MathJax 3.2.2, Apache-2.0. 

mathjax.org · github.com/mathjax/MathJax 

**6.** Hall, J., et al. _jsPDF_ 2.5.1 [Software]. MIT. github.com/parallax/jsPDF 

**7.** yWorks GmbH. _svg2pdf.js_ 2.2.4 [Software]. MIT. github.com/yWorks/svg2pdf.js 

**8.** Mapbox. _Maki_ icon set 8.2.0. CC0-1.0. github.com/mapbox/maki 

**9.** Rapid Editor contributors. _Temaki_ icon set 5.13.0. CC0-1.0. github.com/rapideditor/temaki 

**10.** Google. _Material Symbols_ (@material-symbols/svg-400 0.47.4). Apache-2.0. fonts.google.com/icons · github.com/google/material-design-icons 

**11.** Google. _Google Fonts_ ; family list from the Fontsource API. SIL OFL 1.1 / Apache-2.0 / UFL. fonts.google.com · fontsource.org 

**12.** jsDelivr. Open-source CDN used to load icons on demand. jsdelivr.com 

**13.** OpenFreeMap. Vector basemap styles (Liberty, Positron, Bright). BSD-3-Clause. openfreemap.org 

**14.** OpenStreetMap contributors. Map data. ODbL-1.0. openstreetmap.org/copyright 

**15.** Esri. World Imagery and World Topographic Map tile services. arcgis.com 

**16.** Mapzen / AWS Open Data. Terrain Tiles (Terrarium) for hillshade. 

   - registry.opendata.aws/terrain-tiles 

**17.** QGIS Development Team. _QGIS Geographic Information System_ . Open Source Geospatial Foundation. Used to check .qpt exchange. qgis.org 

**18.** esbuild. JavaScript bundler used to build the plugin. MIT. esbuild.github.io 

**118** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

**Bab 11 · Ekspor, Penyimpanan, dan Penutup** 

**GeoLibre** 

Plugin Layout Composer 

![](../assets/panduan/layout-composer/panduan-layout-composer.pdf-0119-03.png)

#### **Referensi (2): Pustaka Ilmiah dan Data** 

Sumber colormap, indeks spektral, dan data yang dipakai pada contoh. 

**1.** Hunter, J. D. (2007). Matplotlib: a 2D graphics environment. _Computing in Science & Engineering_ , 9(3), 90-95. doi.org/10.1109/MCSE.2007.55 

**2.** van der Walt, S., & Smith, N. (2015). _mpl colormaps_ (viridis, plasma, inferno, magma). bids.github.io/colormap 

**3.** Nuñez, J. R., Anderton, C. R., & Renslow, R. S. (2018). Optimizing colormaps with consideration for color vision deficiency to enable accurate interpretation of scientific data. _PLOS ONE_ , 13(7), e0199239. (cividis) doi.org/10.1371/journal.pone.0199239 

**4.** Mikhailov, A. (2019). Turbo, an improved rainbow colormap for visualization. _Google Research Blog_ . research.google/blog 

**5.** Harrower, M., & Brewer, C. A. (2003). ColorBrewer.org: an online tool for selecting colour schemes for maps. _The Cartographic Journal_ , 40(1), 27-37. doi.org/10.1179/000870403235002042 

**6.** Moreland, K. (2009). Diverging color maps for scientific visualization. In _Advances in Visual Computing (ISVC 2009)_ , LNCS 5876, 92-103. (coolwarm) doi.org/10.1007/978-3-642-10520-3_9 

**7.** Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1974). Monitoring vegetation systems in the Great Plains with ERTS. _NASA SP-351_ , 309-317. (NDVI) ntrs.nasa.gov/citations/19740022614 

**8.** Alcaras, E., Costantino, D., Guastaferro, F., Parente, C., & Pepe, M. (2022). Normalized Burn Ratio Plus (NBR+): a new index for Sentinel-2 imagery. _Remote Sensing_ , 14(7), 1727. doi.org/10.3390/rs14071727 

**9.** European Space Agency. Copernicus Sentinel-2 MultiSpectral Instrument data. dataspace.copernicus.eu 

**10.** ISO 32000-2:2020. Document management, Portable document format, PDF 2.0 (geospatial /VP /Measure /GEO used by GeoPDF export). iso.org/standard/75839.html 

Data contoh: kelas lereng Kabupaten Kuningan, Jawa Barat (data penulis); raster NDVI dan NBR+ Sentinel-2 hasil pengolahan penulis. Cantumkan sumber datamu sendiri di setiap layout. 

**119** / 119 

Panduan Lengkap Layout Composer · **Defani Arman Alfitriansyah** 

