---
title: "Visualisasi-Raster-GIF-python"
---

[Repositori di GitHub](https://github.com/Defani/Visualisasi-Raster-GIF-python)

Repository ini berisi kode Python untuk mengonversi dan memvisualisasikan data raster (GeoTIFF) menjadi animasi GIF. Proyek ini ditujukan untuk kebutuhan analisis spasial dan temporal dalam penginderaan jauh, seperti pemantauan perubahan NDVI, LST, maupun variabel lingkungan lainnya.

## Fitur
- Membaca data raster GeoTIFF menggunakan Rasterio
- Normalisasi nilai raster untuk kebutuhan visualisasi
- Visualisasi raster menggunakan Matplotlib
- Menggabungkan raster multitemporal menjadi animasi GIF
- Cocok untuk analisis citra satelit dan data penginderaan jauh

## Library yang Digunakan
- rasterio
- numpy
- matplotlib
- pillow

Instalasi dependensi:
pip install rasterio numpy matplotlib pillow

## Struktur Direktori
.
├── raster_gif_visualization.ipynb
├── input_raster/
│   ├── raster_1.tif
│   ├── raster_2.tif
│   └── ...
├── output/
│   └── animation.gif
└── README.md

## Cara Menjalankan
1. Simpan seluruh file raster (GeoTIFF) dalam satu folder
2. Buka dan jalankan notebook raster_gif_visualization.ipynb
3. Atur path direktori raster input pada bagian kode
4. GIF hasil visualisasi akan tersimpan otomatis di folder output

## Contoh Penggunaan
Kode ini dapat digunakan untuk:
- Visualisasi NDVI multitemporal
- Monitoring perubahan tutupan lahan
- Analisis spasial berbasis waktu
- Visualisasi hasil penelitian penginderaan jauh

## Catatan Penting
- Semua raster harus memiliki:
  - Sistem koordinat (CRS) yang sama
  - Resolusi spasial yang sama
  - Extent atau coverage yang sama
- Nilai NoData akan ditangani secara otomatis saat visualisasi

## Output
Hasil akhir berupa file GIF animasi yang merepresentasikan perubahan spasial dari waktu ke waktu.

## Author
Defani  
Remote Sensing & GIS Enthusiast

## License
This project is licensed under the MIT License.

## Notebook

Notebook dari repositori ini, tampil lengkap dengan sel kode dan hasilnya:

- [raster_gif_visualization.ipynb](nb/visualisasi-raster-gif-python--raster-gif-visualization.ipynb) · [GitHub](https://github.com/Defani/Visualisasi-Raster-GIF-python/blob/main/raster_gif_visualization.ipynb) · [Colab](https://colab.research.google.com/github/Defani/Visualisasi-Raster-GIF-python/blob/main/raster_gif_visualization.ipynb)
