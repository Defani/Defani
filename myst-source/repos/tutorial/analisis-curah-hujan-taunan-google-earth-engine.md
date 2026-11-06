---
title: "Analisis-Curah-Hujan-Taunan-Google-Earth-Engine"
---

[Repositori di GitHub](https://github.com/Defani/Analisis-Curah-Hujan-Taunan-Google-Earth-Engine)

📍 **Link Google Earth Engine Script**  
🔗 [Buka di GEE Code Editor](https://code.earthengine.google.com/)

---

## 📘 Deskripsi

Proyek ini menganalisis **total curah hujan tahunan (mm) di Provinsi Jawa Barat tahun 2023** menggunakan dataset **CHIRPS Daily v2.0 (Climate Hazards Group InfraRed Precipitation with Station data)** melalui **Google Earth Engine (GEE)**.  

Data CHIRPS memberikan estimasi curah hujan berbasis gabungan antara data satelit dan observasi lapangan dengan resolusi spasial tinggi (~5 km). Analisis ini dilakukan dengan menjumlahkan data harian selama periode 1 Januari – 31 Desember 2023 dan menampilkan hasilnya dalam peta tematik berwarna gradasi.

---

## 🛰️ Dataset

| Dataset | Keterangan |
|----------|-------------|
| **FAO/GAUL/2015/level1** | Batas administratif Provinsi Jawa Barat |
| **UCSB-CHG/CHIRPS/DAILY** | Data curah hujan harian global dari tahun 1981–sekarang |

**Sumber:** [Google Earth Engine Datasets - CHIRPS Daily v2.0](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_DAILY)

---

## ⚙️ Langkah Analisis

### 1️⃣ Definisi Wilayah Studi
Wilayah administratif Jawa Barat dipilih dari dataset **FAO GAUL Level 1**:
```js
var aoi = ee.FeatureCollection('FAO/GAUL/2015/level1')
  .filter(ee.Filter.eq('ADM1_NAME', 'Jawa Barat'))
  .geometry();

Map.centerObject(aoi, 8);
```
### 2️⃣ Pemanggilan dan Penjumlahan Data CHIRPS

Dataset CHIRPS diambil untuk periode tahun 2023 dan dijumlahkan:
```js
var citraCurahHujan = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY")
  .filter(ee.Filter.date('2023-01-01', '2023-12-31'))
  .sum()
  .clip(aoi);
```
### 3️⃣ Parameter Visualisasi

Palet warna digunakan untuk menampilkan distribusi curah hujan tahunan:
```js
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
```
### 4️⃣ Pembuatan Legenda Otomatis

Legenda menampilkan rentang nilai sesuai gradasi warna:
```js
var legenda = ui.Panel({ style: { position: 'bottom-left', padding: '8px 15px', border: '1px solid #cccccc' } });
var judulLegenda = ui.Label({
  value: 'Curah Hujan Tahunan (mm)\nProvinsi Jawa Barat',
  style: { fontWeight: 'bold', fontSize: '15px', margin: '0 0 6px 0', whiteSpace: 'pre' }
});
legenda.add(judulLegenda);

// Membuat gradasi warna otomatis
var nSteps = parameterVisual.palette.length;
var step = (parameterVisual.max - parameterVisual.min) / (nSteps - 1);

for (var i = 0; i < nSteps; i++) {
  var minVal = parameterVisual.min + i * step;
  var color = parameterVisual.palette[i];
  var label;

  if (i === 0) label = '< ' + Math.round(minVal);
  else if (i === nSteps - 1) label = '> ' + Math.round(minVal);
  else label = Math.round(minVal) + ' - ' + Math.round(minVal + step);

  var colorBox = ui.Label({ style: { backgroundColor: color, padding: '8px', margin: '0 0 4px 0' } });
  var description = ui.Label({ value: label, style: { margin: '0 0 4px 6px' } });
  legenda.add(ui.Panel({ widgets: [colorBox, description], layout: ui.Panel.Layout.Flow('horizontal') }));
}

legenda.add(ui.Label('Sumber Data: CHIRPS Daily v2.0', {margin: '8px 8px 4px 8px', fontSize: '10px'}));
Map.add(legenda);
```
### 5️⃣ Ekspor Hasil ke Google Drive
```js
Export.image.toDrive({
  image: citraCurahHujan,
  description: 'CurahHujan_JawaBarat_2023',
  folder: 'GEE_Export',
  fileNamePrefix: 'CurahHujan_JawaBarat_2023',
  region: aoi,
  scale: 5000,
  maxPixels: 1e13,
  crs: 'EPSG:4326'
});
```
### 🗺️ Hasil

Citra menampilkan variasi curah hujan tahunan di Jawa Barat:

🌿 Nilai tinggi (>4000 mm): area pegunungan dan hutan lebat (Selatan Jabar).

🌾 Nilai sedang (2500–3500 mm): dataran tengah dan area pertanian.

🏙️ Nilai rendah (<2000 mm): wilayah urban dan pesisir utara (Cirebon, Indramayu).

### 📚 Referensi

Funk, C. et al. (2015). The Climate Hazards Infrared Precipitation with Stations — a new environmental record for monitoring extremes. Scientific Data, 2, 150066. https://doi.org/10.1038/sdata.2015.66

Google Developers (2025). UCSB-CHG/CHIRPS/DAILY Dataset. https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_DAILY

FAO (2015). Global Administrative Unit Layers (GAUL) 2015. FAO Geonetwork.
