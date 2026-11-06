---
title: 'Tutorial: Memetakan Sebaran Mangrove Menggunakan NDVI Threshold di GEE'
date: 2025-04-30
tags: ['mangrove', 'remote-sensing', 'sentinel', 'google-earth-engine', 'mangrove-indonesia']
---

30 April 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/%EF%B8%8F-tutorial-memetakan-sebaran-mangrove-menggunakan-ndvi-threshold-di-gee-8cdec804d17e) · [Semua tulisan](../blog.md)

Dalam tutorial ini, kita akan memetakan mangrove di Pesisir Utara Kabupaten Subang menggunakan Sentinel-2 dan threshold NDVI yang ditentukan berdasarkan nilai *Inspector*. Kita tidak menggunakan nilai baku nasional, melainkan menyesuaikan dengan karakteristik lokal mangrove di wilayah studi.

![](https://cdn-images-1.medium.com/max/1024/1*lV4pldzlWZq3V3P6Db4Xew.png)

**Menggambar Area Studi**

Area studi dibuat menggunakan tools “Draw shape”, usahakan batasan area studi tidak terlalu luas dan terfokus di wilayah bermangrove agar mudah menentukan nilai threshold.

![](https://cdn-images-1.medium.com/max/1024/1*Usz1BxkgjN-aHps4hHzuqw.png)

Pemilihan Area Studi

**Masking Awan dengan Band SCL Sentinel-2**

Kita mulai dengan menghilangkan awan dan bayangan awan dari citra Sentinel-2 menggunakan band SCL (Scene Classification Layer). Kita hanya menyisakan piksel yang bukan awan, bayangan awan, dan area tertutup awan.

    var sentinel2_mask = function(image) {
      var scl = image.select('SCL');
      var mask = scl.neq(3)
                  .and(scl.neq(8))
                  .and(scl.neq(9))
                  .and(scl.neq(10))
                  .and(scl.neq(11));
      return image.updateMask(mask);
    };

**Memilih Citra Satelit yang Akan Digunakan**

Selanjutnya, kita memuat koleksi Sentinel-2 yang telah dikoreksi atmosfer (SR) selama tahun 2024, memfilter awan kurang dari 20%, dan membuat komposit median. Area dibatasi oleh geometry, yaitu polygon batas studi.

    var sentinel2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
      .filterBounds(geometry)
      .filterDate('2024-01-01', '2025-01-01')
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
      .map(sentinel2_mask)
      .median()
      .clip(geometry)
      .multiply(0.0001);

**Komposit Band untuk Visualisasi**

Setelah masking, kita bisa membuat komposit band RGB menggunakan band B8, B11, dan B4. Band ini akan memberikan gambaran visual yang jelas mengenai kondisi vegetasi di wilayah yang kita pelajari.

    var multispectral = sentinel2.select(['B8', 'B11', 'B4']);
    var multispectral_param = {min: 0, max: 0.25};
    Map.addLayer(multispectral, multispectral_param, 'Sentinel 2 (RGB)');

![](https://cdn-images-1.medium.com/max/1024/1*gOwiYAuRE8cG7YxrpDRNjg.png)

Hasil Komposite Band 8–11–4

**Menghitung NDVI**

NDVI dihitung menggunakan rumus (NIR - Red) / (NIR + Red), di mana band NIR = B8 dan Red = B4. Nilai ini merepresentasikan kehijauan atau kepadatan vegetasi.

    var ndvi = sentinel2.normalizedDifference(['B8', 'B4']).rename('NDVI');

**Menampilkan NDVI**

Peta NDVI ditampilkan dengan palet warna dari hitam (vegetasi rendah) hingga hijau gelap (vegetasi tinggi). Ini membantu kita mengidentifikasi area vegetasi padat seperti mangrove.

    Map.centerObject(geometry, 13);
    Map.addLayer(ndvi, {
      min: -1,
      max: 1,
      palette: [
        '000000', 'a50026', 'd73027', 'f46d43', 'fdae61', 'fee08b',
        'ffffbf', 'd9ef8b', 'a6d96a', '66bd63', '1a9850', '006837'
      ]
    }, 'NDVI');

![](https://cdn-images-1.medium.com/max/1024/1*3oeU8gOdCb8s2WQqN5sRlA.png)

Hasil Perhitungan NDVI

**Masking Mangrove Berdasarkan Threshold Lokal**

Di tahap ini, kita menetapkan nilai threshold NDVI berdasarkan observasi langsung di lapangan atau menggunakan *Inspector Tool* di GEE. *Inspector Tool* diarahkan pada wilayah batas mangrove dengan kerapatan ter rendah. Dalam kasus mangrove di Subang, nilai NDVI berkisar ≥0.7

![](https://cdn-images-1.medium.com/max/866/1*6Zxg0QfBg4Uu45QbhSe3HQ.png)

Tampilan Nilai Pixel

Setelah mengetahui nilai piksel, maka buat perhitungan menggunakan kode di bawah:

    var NDVI_threshold = NDVI.updateMask(NDVI.gte(0.7));
    Map.addLayer(NDVI_threshold, {min: 0.6, max: 1.0, palette: ['darkgreen']}, 'NDVI >= 0.7 (Mangrove))');

![](https://cdn-images-1.medium.com/max/1024/1*lV4pldzlWZq3V3P6Db4Xew.png)

Hasil Threshold

**Ekspor Hasil Ke Drive**

Terakhir, hasil pemetaan disiapkan untuk diekspor dalam format GeoTIFF ke Google Drive. Pastikan folder GEE_Export sudah dibuat sebelumnya di akun Drive kamu.

    Export.image.toDrive({
      image: NDVI_threshold,
      description: 'GEE_Export',
      folder: 'GEE',
      scale: 10,
      region: geometry,
      fileFormat: 'GeoTIFF'
      });

Dengan mengikuti langkah-langkah ini, kamu akan mendapatkan peta sebaran mangrove di wilayah studi berdasarkan analisis NDVI. Semoga tutorial ini bermanfaat, dan jika ada yang ingin ditanyakan atau dikembangkan, jangan ragu untuk menghubungi saya!
