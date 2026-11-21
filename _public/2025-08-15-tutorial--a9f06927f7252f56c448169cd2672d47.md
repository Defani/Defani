---
title: 'Tutorial Analisis Spasial Rata -Rata Curah Hujan Tahunan Menggunakan Google Earth Engine'
date: 2025-08-15
---

15 August 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/tutorial-analisis-spasial-rata-rata-curah-hujan-tahunan-menggunakan-google-earth-engine-1338b8380256) · [Semua tulisan](../blog.md)

Oleh : Defani Arman Alfitriansyah

![](https://cdn-images-1.medium.com/max/1024/1*AJXSTuyfJzF1cpSd8QrNsQ.png)

### **Ringkasan Pembahasan**

Curah hujan merupakan salah satu parameter iklim fundamental yang memengaruhi berbagai sektor, mulai dari hidrologi, pertanian, hingga mitigasi bencana. Analisis curah hujan dalam agregat tahunan memberikan gambaran umum mengenai kondisi basah atau kering suatu wilayah selama satu periode. Platform Google Earth Engine (GEE) menyediakan kapabilitas komputasi awan untuk pemrosesan data geospasial berskala besar. Penelitian ini mendemonstrasikan alur kerja untuk akuisisi, pengolahan, dan visualisasi data curah hujan tahunan menggunakan koleksi data **CHIRPS Daily** dalam lingkungan GEE, studi kasus di Kabupaten Ciamis, Indonesia. Alur kerja ini mencakup pembuatan legenda kartografis kustom untuk interpretasi data yang lebih informatif.

### **Pendahuluan**

Curah hujan tahunan didefinisikan sebagai total presipitasi (dalam satuan milimeter) yang terakumulasi di suatu lokasi selama satu tahun kalender. Data ini krusial untuk pemodelan neraca air hidrologis, perencanaan agrikultur terkait penentuan pola tanam, serta sebagai indikator awal untuk analisis potensi kekeringan maupun banjir (Dore, 2005).

Untuk melakukan analisis tersebut, diperlukan data curah hujan yang memiliki konsistensi temporal dan resolusi spasial yang memadai. Salah satu produk data yang paling sering digunakan dalam komunitas ilmiah adalah **CHIRPS**.

### **Dataset CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)**

CHIRPS adalah dataset presipitasi quasi-global (mencakup 50°S — 50°N) yang dikembangkan oleh Climate Hazards Group di University of California, Santa Barbara (UCSB) bekerja sama dengan U.S. Geological Survey (USGS) Earth Resources Observation and Science (EROS) Center.

Dataset ini memiliki beberapa keunggulan utama:

- **Resolusi Spasial Tinggi**: CHIRPS menyediakan data dengan resolusi spasial 0.05° (sekitar 5.3 km), yang sangat detail untuk analisis skala regional maupun lokal.
- **Periode Data Panjang**: Data tersedia dari tahun 1981 hingga mendekati waktu-nyata (near real-time), memungkinkan analisis tren jangka panjang.
- **Metodologi Hibrida**: CHIRPS mengintegrasikan data satelit inframerah (InfraRed — IR) dari citra Cold Cloud Duration (CCD) dengan data observasi dari stasiun-stasiun cuaca di seluruh dunia. Pendekatan ini menghasilkan estimasi curah hujan yang lebih akurat dibandingkan jika hanya menggunakan satu sumber data (Funk et al., 2015).

Data ini dapat diakses secara bebas melalui katalog data Google Earth Engine dengan ID: UCSB-CHG/CHIRPS/DAILY.

### **Tahapan Analisis**

Tahapan analisis yang diterapkan terdiri dari beberapa tahapan komputasi yang dieksekusi pada platform GEE.

### **1. Penentuan Wilayah Kajian**

Wilayah studi didefinisikan sebagai batas administrasi Provinsi Jawa Barat. Data batas wilayah ini diekstraksi dari dataset FAO Global Administrative Unit Layers (GAUL) level 1, yang merepresentasikan entitas provinsi.

    var aoi = ee.FeatureCollection('FAO/GAUL/2015/level1')
      .filter(ee.Filter.eq('ADM1_NAME', 'Jawa Barat'))
      .geometry();

ee.FeatureCollection('FAO/GAUL/2015/level1'): Fungsi ini memuat sebuah koleksi data vektor global dari *Food and Agriculture Organization (FAO)*. Dataset **GAUL (Global Administrative Unit Layers)** level 1 ini berisi batas-batas administrasi tingkat provinsi atau negara bagian di seluruh dunia.

.filter(ee.Filter.eq('ADM1_NAME', 'Jawa Barat')): Setelah seluruh data provinsi dimuat, fungsi .filter() diterapkan untuk menyaringnya. Filter ini mencari fitur (poligon) yang memiliki kolom atribut (properti) bernama ADM1_NAME dengan nilai yang sama persis (eq atau *equals*) dengan "Jawa Barat". Hasilnya adalah sebuah FeatureCollection yang hanya berisi satu fitur, yaitu poligon Provinsi Jawa Barat.

.geometry(): Fungsi ini mengekstrak hanya informasi spasial (yaitu, bentuk poligonnya) dari fitur yang telah disaring dan mengabaikan semua data atribut lainnya (seperti nama, kode, dll.). Hasil akhir yang disimpan dalam variabel aoi adalah sebuah objek geometri poligon murni.

### 2. Memusatkan Tampilan Peta

Tindakan ini mengatur tampilan antarmuka peta agar fokus pada wilayah yang telah ditentukan.

    Map.centerObject(aoi, 8);

Map.centerObject(aoi, 8): Fungsi ini memerintahkan peta untuk secara otomatis menggeser dan menyesuaikan tampilannya agar objek aoi (poligon Jawa Barat) berada di tengah layar. Angka 8 adalah **tingkat zoom**, di mana nilai yang lebih tinggi berarti tampilan yang lebih dekat ke permukaan bumi. Tingkat 8 dipilih agar seluruh provinsi dapat terlihat dengan baik.

### 3. Akuisisi dan Pengolahan Data Curah Hujan

Bagian ini adalah inti dari analisis data, di mana data mentah curah hujan harian diunduh, disaring, diagregasi, dan dipotong.

    var citraCurahHujan = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY")
      .filter(ee.Filter.date('2023-01-01', '2023-12-31'))
      .sum()
      .clip(aoi);

ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY"): Memuat seluruh koleksi citra satelit **CHIRPS Daily**. Ini adalah kumpulan data time-series yang berisi ribuan citra, di mana setiap citra merepresentasikan estimasi curah hujan global untuk satu hari.

.filter(ee.Filter.date('2023-01-01', '2023-12-31')): Menyaring koleksi citra raksasa tersebut untuk mengambil hanya citra yang tanggal akuisisinya berada dalam rentang 1 Januari 2023 hingga 31 Desember 2023. Hasilnya adalah 365 citra (untuk tahun tersebut).

.sum(): Fungsi ini melakukan operasi matematika penting. Ia "menumpuk" ke-365 citra harian tersebut dan menjumlahkan nilai piksel di setiap lokasi. Hasilnya adalah satu citra tunggal (ee.Image) di mana setiap nilai pikselnya merepresentasikan **total curah hujan tahunan** dalam satuan milimeter.

.clip(aoi): Memotong citra hasil penjumlahan tadi menggunakan poligon aoi sebagai "cetakan". Semua data piksel yang berada di luar batas Provinsi Jawa Barat akan dibuang, sehingga menghasilkan citra curah hujan yang hanya mencakup wilayah studi.

### 4. Pengaturan Visualisasi Peta

Bagian ini mendefinisikan bagaimana data curah hujan akan direpresentasikan secara visual di peta.

    var parameterVisual = {
      min: 1000.0,
      max: 5000.0,
      palette: [
        '#ffffcc', '#ffeda0', '#fed976', '#feb24c', 
        '#fd8d3c', '#fc4e2a', '#e31a1c', '#b10026'
      ]
    };

- var parameterVisual = { ... }: Membuat sebuah objek JavaScript untuk menyimpan parameter visualisasi.
- min: 1000.0: Menetapkan bahwa nilai curah hujan 1000 mm akan direpresentasikan oleh warna pertama dalam palet. Nilai di bawah ini juga akan menggunakan warna pertama.
- max: 5000.0: Menetapkan bahwa nilai 5000 mm (dan nilai di atasnya) akan direpresentasikan oleh warna terakhir dalam palet.
- palette: \[ ... \]: Sebuah array (daftar) yang berisi kode-kode warna heksadesimal. GEE akan secara otomatis membuat gradasi warna dari nilai min ke max menggunakan urutan warna ini, dari kuning (#ffffcc) untuk curah hujan rendah hingga merah tua (#b10026) untuk curah hujan tinggi.

### 5. Menambahkan Data sebagai Layer Peta

Fungsi ini mengambil data yang sudah diolah dan divisualisasikan, lalu menampilkannya di atas peta dasar.

    Map.addLayer(citraCurahHujan, parameterVisual, 'Curah Hujan Tahunan 2023 (mm)');

Map.addLayer(...): Menambahkan sebuah layer baru ke panel peta.

citraCurahHujan: Objek data (ee.Image) yang ingin ditampilkan

parameterVisual: Objek yang berisi aturan pewarnaan (min, max, palette).

'Curah Hujan Tahunan 2023 (mm)': Nama layer yang akan muncul di panel kontrol layer di pojok kanan atas peta.

### **6. Konstruksi Legenda Peta**

Bagian ini secara dinamis membangun sebuah panel legenda yang informatif menggunakan komponen antarmuka pengguna (UI) GEE.

    var legenda = ui.Panel({
      style: {
        position: 'bottom-left', padding: '8px 15px', 
        border: '1px solid #cccccc'
      }
    });

    var judulLegenda = ui.Label({
      value: 'Curah Hujan Tahunan (mm)\nProvinsi Jawa Barat',
      style: {
        fontWeight: 'bold', fontSize: '15px', margin: '0 0 6px 0',
         padding: '0', whiteSpace: 'pre'
      }
    });

    legenda.add(judulLegenda);

ui.Panel({...}): Membuat sebuah widget panel kosong, yang berfungsi sebagai "wadah" untuk semua elemen legenda lainnya. Properti style mengatur tampilannya: posisi di pojok kiri bawah, memiliki bantalan (padding), dan diberi bingkai (border).

ui.Label({...}): Membuat widget label teks. Properti value berisi teks yang akan ditampilkan. Karakter \n berfungsi untuk membuat baris baru karena whiteSpace: 'pre' diatur dalam style. Properti style lainnya mengatur teks menjadi tebal, ukuran font, dan margin.

legenda.add(judulLegenda): Menambahkan widget judulLegenda ke dalam legenda (panel utama).

### Pembuatan Legenda Dinamis

    var nSteps = parameterVisual.palette.length;
    var step = (parameterVisual.max - parameterVisual.min) / (nSteps - 1);

    for (var i = 0; i < nSteps; i++) {
      var minVal = parameterVisual.min + i * step;
      var color = parameterVisual.palette[i];
      var label;

      if (i === 0) {
        label = '< ' + Math.round(minVal);
      } else if (i === nSteps - 1) {
        label = '> ' + Math.round(minVal);
      } else {
        var maxVal = minVal + step;
        label = Math.round(minVal) + ' - ' + Math.round(maxVal);
      }

      var colorBox = ui.Label({ style: { backgroundColor: color, 
          padding: '8px', margin: '0 0 4px 0' } });
      var description = ui.Label({ value: label, 
          style: { margin: '0 0 4px 6px' } });

      var barisLegenda = ui.Panel({
        widgets: [colorBox, description],
        layout: ui.Panel.Layout.Flow('horizontal')
      });
      legenda.add(barisLegenda);
    }

for (var i = 0; i \< nSteps; i++): Ini adalah sebuah perulangan (loop) yang akan berjalan sebanyak jumlah warna yang ada di palet. Untuk setiap iterasi, kode di dalamnya akan membuat satu baris legenda (kotak warna + label teks).

if/else if/else: Blok logika ini digunakan untuk membuat format label teks yang berbeda untuk setiap baris.

if (i === 0): Untuk iterasi pertama (warna pertama), labelnya diformat sebagai "\< \[nilai minimum\]".

else if (i === nSteps - 1): Untuk iterasi terakhir (warna terakhir), labelnya diformat sebagai "\> \[nilai awal rentang terakhir\]".

else: Untuk semua baris di antaranya, labelnya diformat sebagai "\[nilai awal\] - \[nilai akhir\]".

ui.Label({ style: { backgroundColor: color, ... } }): Membuat sebuah label yang tidak memiliki teks, tetapi diberi warna latar belakang sesuai warna palet saat ini (color). Ini berfungsi sebagai **kotak warna**.

ui.Label({ value: label, ... }): Membuat label teks yang berisi rentang nilai yang sudah dihitung.

ui.Panel({ widgets: \[...\], layout: ... }): Membuat panel kecil untuk satu baris. widgets berisi daftar elemen yang akan dimasukkan (kotak warna dan deskripsi). layout: ui.Panel.Layout.Flow('horizontal') mengatur agar kedua elemen tersebut disusun berdampingan secara horizontal.

legenda.add(barisLegenda): Menambahkan panel baris yang baru dibuat ke dalam panel legenda utama.

### **Penambahan Sumber dan Menampilkan Legenda**

    var sumberLabel = ui.Label('Sumber Data: CHIRPS Daily v2.0', 
      {margin: '8px 8px 4px 8px', fontSize: '10px'});
    legenda.add(sumberLabel);

    Map.add(legenda);

ui.Label(...): Membuat satu label teks terakhir untuk informasi sumber data.

legenda.add(sumberLabel): Menambahkan label sumber ke bagian bawah panel legenda.

Map.add(legenda): Setelah seluruh elemen (judul, baris-baris warna, dan sumber) selesai ditambahkan ke dalam panel legenda, fungsi ini akhirnya menampilkan keseluruhan panel legenda tersebut di antarmuka peta.

### **Kode lengkap**

    var aoi = ee.FeatureCollection('FAO/GAUL/2015/level1')
      .filter(ee.Filter.eq('ADM1_NAME', 'Jawa Barat'))
      .geometry();

    Map.centerObject(aoi, 8);

    var citraCurahHujan = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY")
      .filter(ee.Filter.date('2023-01-01', '2023-12-31'))
      .sum()
      .clip(aoi);

    var parameterVisual = {
      min: 1000.0,
      max: 5000.0,
      palette: [
        '#ffffcc', '#ffeda0', '#fed976', '#feb24c', 
        '#fd8d3c', '#fc4e2a', '#e31a1c', '#b10026'
      ]
    };

    Map.addLayer(citraCurahHujan, parameterVisual, 
                'Curah Hujan Tahunan 2023 (mm)');

    var legenda = ui.Panel({
      style: {
        position: 'bottom-left', padding: '8px 15px', 
        border: '1px solid #cccccc'
      }
    });

    var judulLegenda = ui.Label({
      value: 'Curah Hujan Tahunan (mm)\nProvinsi Jawa Barat',
      style: {
        fontWeight: 'bold', fontSize: '15px', margin: '0 0 6px 0', 
        padding: '0', whiteSpace: 'pre'
      }
    });
    legenda.add(judulLegenda);

    var nSteps = parameterVisual.palette.length;
    var step = (parameterVisual.max - parameterVisual.min) / (nSteps - 1);

    for (var i = 0; i < nSteps; i++) {
      var minVal = parameterVisual.min + i * step;
      var color = parameterVisual.palette[i];
      var label;

      if (i === 0) {
        label = '< ' + Math.round(minVal);
      } else if (i === nSteps - 1) {
        label = '> ' + Math.round(minVal);
      } else {
        var maxVal = minVal + step;
        label = Math.round(minVal) + ' - ' + Math.round(maxVal);
      }

      var colorBox = ui.Label({ style: { backgroundColor: color, padding: '8px',
           margin: '0 0 4px 0' } });
      var description = ui.Label({ value: label, 
           style: { margin: '0 0 4px 6px' } });

      var barisLegenda = ui.Panel({
        widgets: [colorBox, description],
        layout: ui.Panel.Layout.Flow('horizontal')
      });
      legenda.add(barisLegenda);
    }

    var sumberLabel = ui.Label('Sumber Data: CHIRPS Daily v2.0', 
      {margin: '8px 8px 4px 8px', fontSize: '10px'});
    legenda.add(sumberLabel);

    Map.add(legenda);

### **Referensi**

Dore, M. H. I. (2005). Climate change and changes in global precipitation patterns: What do we know?. *Environment International*, *31*(8), 1167–1181. <https://doi.org/10.1016/j.envint.2005.03.004>

Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., Husak, G., Rowland, J., Harrison, L., Hoell, A., & Michaelsen, J. (2015). The climate hazards infrared precipitation with stations — A new environmental record for monitoring extremes. *Scientific Data*, *2*, Article 150066. <https://doi.org/10.1038/sdata.2015.66>
