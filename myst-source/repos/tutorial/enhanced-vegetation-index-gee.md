---
title: "Enhanced-Vegetation-Index-GEE"
---

Repositori ini berisi script Google Earth Engine (GEE) berbasis JavaScript untuk menghitung dan mengekspor nilai Enhanced Vegetation Index (EVI) menggunakan citra satelit Sentinel-2 Surface Reflectance (SR) Harmonized.

[Repositori di GitHub](https://github.com/Defani/Enhanced-Vegetation-Index-GEE)

Repositori ini berisi script Google Earth Engine (GEE) berbasis JavaScript untuk menghitung dan mengekspor nilai Enhanced Vegetation Index (EVI) menggunakan citra satelit Sentinel-2 Surface Reflectance (SR) Harmonized.

## Tautan Script GEE

Script dapat diakses langsung melalui tautan Google Earth Engine berikut:
[https://code.earthengine.google.com/b58ebee2a304369f43d1fec06055ace4](https://code.earthengine.google.com/b58ebee2a304369f43d1fec06055ace4)

## Landasan Teori

Indeks vegetasi merupakan transformasi spektral dari dua band atau lebih yang dirancang untuk mempertegas kontribusi properti vegetasi dan memungkinkan perbandingan spasial serta temporal yang dapat diandalkan dari aktivitas fotosintetik terestrial[cite: 1]. Terdapat dua indeks vegetasi yang umum digunakan untuk memantau aktivitas fotosintesis secara konsisten, yaitu Normalized Difference Vegetation Index (NDVI) dan Enhanced Vegetation Index (EVI)[cite: 1].

NDVI bertumpu pada rasio normalisasi dari band near-infrared (NIR) dan merah (red)[cite: 1]. Kelemahan utama dari NDVI adalah indeks ini cenderung mengalami saturasi asimtotik pada wilayah dengan biomassa yang tinggi dan sangat sensitif terhadap variasi latar belakang kanopi[cite: 1].

Sebagai bentuk penyempurnaan, EVI dikembangkan untuk mengoptimalkan sinyal vegetasi dengan sensitivitas yang lebih baik di wilayah bermassa biologis tinggi[cite: 1]. Peningkatan ini dicapai melalui pemisahan sinyal latar belakang kanopi dan pengurangan pengaruh atmosfer[cite: 1]. EVI menggunakan band biru (blue) untuk mengoreksi pengaruh aerosol pada band merah[cite: 1]. Persamaan EVI mengambil bentuk sebagai berikut:

EVI = G * ((NIR - Red) / (NIR + C1 * Red - C2 * Blue + L))

Koefisien yang digunakan dalam algoritma EVI adalah L = 1, C1 = 6, C2 = 7.5, dan faktor pengali atau gain (G) = 2.5[cite: 1]. Berkat algoritma ini, EVI tetap peka terhadap variasi kanopi pada wilayah dengan kepadatan tinggi seperti hutan hujan tropis, di mana NDVI biasanya telah mencapai titik jenuh[cite: 1].

## Deskripsi Script

Script ini melakukan pemrosesan citra Sentinel-2 pada rentang waktu 1 Januari 2024 hingga 22 Desember 2025 dengan tahapan sebagai berikut:
1. Cloud Masking: Menggunakan band SCL (Scene Classification) untuk menyaring piksel yang teridentifikasi sebagai bayangan awan (3), awan probabilitas rendah (7), awan probabilitas sedang (8), awan probabilitas tinggi (9), cirrus (10), dan salju/es (11).
2. Filtrasi: Memfilter citra berdasarkan batas area (geometry) dan persentase tutupan awan di bawah 20%.
3. Kalkulasi EVI: Menghitung indeks EVI menggunakan formula standar dengan band NIR (B8), Red (B4), dan Blue (B2).
4. Visualisasi: Menambahkan layer hasil EVI ke dalam peta dengan palet warna representatif.
5. Ekspor: Mengirim hasil pengolahan berupa file GeoTIFF langsung ke Google Drive.

## Script GEE

```javascript
// CLOUD MASKING SCL
function maskS2Cloud(image) {
  var scl = image.select('SCL');
  return image.updateMask(
    scl.neq(3)   
      .and(scl.neq(7))  
      .and(scl.neq(8))  
      .and(scl.neq(9))  
      .and(scl.neq(10)) 
      .and(scl.neq(11)) 
  );
}

// IMPORT CITRA SENTINEL-2
var s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(geometry)
  .filterDate('2024-01-01', '2025-12-22')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .map(maskS2Cloud)
  .median()
  .clip(geometry)
  .divide(10000);

// VARIABEL BAND
var nir = s2.select('B8');
var red = s2.select('B4');
var blue = s2.select('B2');

// PERHITUNGAN EVI
var EVI = nir.subtract(red)
  .divide(
    nir.add(red.multiply(6.0))
      .subtract(blue.multiply(7.5))
      .add(1.0)
  )
  .multiply(2.5)
  .rename('EVI');

// VISUALISASI
var visParam = {
  min: -0.0,
  max: 0.83,
  palette: ['#d73027','#fdae61','#fee08b','#d9ef8b','#66bd63','#1a9850']
};

Map.addLayer(EVI, visParam, 'EVI Index');
Map.centerObject(geometry, 13);

// EXPORT EVI KE GOOGLE DRIVE
Export.image.toDrive({
  image: EVI,
  description: 'EVI_Sentinel2_2024_2025',
  folder: 'GEE_Output',
  fileNamePrefix: 'EVI_S2_2024_2025',
  region: geometry,
  scale: 10,
  maxPixels: 1e13,
  fileFormat: 'GeoTIFF'
});
```
**Daftar Pustaka**
---
Huete, A., Didan, K., Miura, T., Rodriguez, E. P., Gao, X., & Ferreira, L. G. (2002). Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sensing of Environment, 83, 195-213.
