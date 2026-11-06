---
title: "Konsep-regresi-linier-dalam-permodelan-karbon"
---

[Repositori di GitHub](https://github.com/Defani/Konsep-regresi-linier-dalam-permodelan-karbon)

**Penulis: Defani Arman Alfitriansyah**

Fakultas Kehutanan dan Lingkungan, Universitas Kuningan,
Tahun 2025


---



Analisis ini bertujuan untuk membangun model regresi linier berganda untuk memprediksi biomassa (AGC\_ton\_per\_ha) berdasarkan beberapa variabel independen: NDVI, IRECI, dan TRVI. Model regresi linier berganda menggambarkan hubungan linier antara variabel dependen dan beberapa variabel independen. Dalam kasus ini, biomassa (AGC\_ton\_per\_ha) adalah variabel dependen ($y$), dan NDVI, IRECI, serta TRVI adalah variabel independen ($x_1, x_2, x_3$). Rumus umum model regresi linier berganda adalah:

$$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon $$

Di mana:
- $y$ adalah variabel dependen (AGC\_ton\_per\_ha)
- $\beta_0$ adalah *intercept* (konstanta)
- $\beta_1, \beta_2, \dots, \beta_n$ adalah koefisien regresi untuk setiap variabel independen
- $x_1, x_2, \dots, x_n$ adalah variabel independen (NDVI, IRECI, TRVI)
- $\epsilon$ adalah *error term* (galat acak)

Langkah-langkah yang dilakukan dalam analisis ini meliputi:

1.  **Memuat Data**: Data biomassa, yang mencakup kolom ID, NDVI, IRECI, TRVI, dan AGC\_ton\_per\_ha, dimuat dari file Excel menggunakan library **pandas**. Pandas (`import pandas as pd`) adalah library fundamental dalam Python untuk manipulasi dan analisis data tabular, menyediakan struktur data seperti DataFrame yang memudahkan pengelolaan data.
2.  **Persiapan Data untuk Regresi**: Variabel independen (NDVI, IRECI, TRVI) dan variabel dependen (AGC\_ton\_per\_ha) dipisahkan dari DataFrame utama. Untuk analisis menggunakan library **statsmodels**, yang digunakan untuk analisis statistik yang lebih mendalam dibandingkan `sklearn.linear_model`, sebuah kolom konstanta dengan nilai 1 ditambahkan ke variabel independen. Penambahan konstanta ini ($X_{sm} = sm.add\_constant(X)$) memungkinkan model untuk menghitung *intercept*. Statsmodels (`import statsmodels.api as sm`) menyediakan berbagai model statistik dan hasil ringkasan yang detail.
3.  **Pelatihan Model Regresi**: Model regresi linier berganda dilatih menggunakan fungsi OLS (Ordinary Least Squares) dari library **statsmodels**. Metode OLS bertujuan untuk meminimalkan jumlah kuadrat *error* antara nilai aktual dan nilai prediksi. Proses pelatihan dilakukan dengan `model_sm = sm.OLS(y, X_sm).fit()`. Hasil dari proses *fitting* ini mencakup estimasi koefisien regresi ($\beta$ values), *p-value* untuk signifikansi setiap koefisien, dan statistik keseluruhan model.
4.  **Evaluasi Model dan Visualisasi**: Kinerja model dievaluasi menggunakan dua metrik utama: R-squared dan Root Mean Squared Error (RMSE).
    - **R-squared ($R^2$)**: Menunjukkan proporsi variabilitas dalam variabel dependen yang dapat dijelaskan oleh variabel independen dalam model. Nilai R-squared berkisar antara 0 hingga 1; nilai yang lebih tinggi menunjukkan model yang lebih baik dalam menjelaskan variabilitas data. Rumusnya adalah:
    $$ R^2 = 1 - \frac{\text{SSR}}{\text{SST}} $$
    Di mana SSR (Sum of Squares of Residuals) adalah jumlah kuadrat selisih antara nilai aktual dan prediksi, dan SST (Total Sum of Squares) adalah jumlah kuadrat selisih antara nilai aktual dan rata-rata nilai aktual.
    - **Root Mean Squared Error (RMSE)**: Mengukur rata-rata besar *error* antara nilai prediksi dan nilai aktual. RMSE dihitung sebagai akar kuadrat dari Mean Squared Error (MSE). Nilai RMSE yang lebih rendah menunjukkan *error* prediksi yang lebih kecil dan kinerja model yang lebih baik. Rumusnya adalah:
    $$ \text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2} $$
    Di mana $N$ adalah jumlah observasi, $y_i$ adalah nilai aktual, dan $\hat{y}_i$ adalah nilai prediksi.
    Visualisasi perbandingan antara nilai aktual dan prediksi dibuat menggunakan scatter plot (`seaborn.scatterplot`) dengan garis diagonal (nilai aktual = nilai prediksi) sebagai referensi (`matplotlib.pyplot.plot`). Visualisasi ini membantu menilai seberapa dekat titik-titik data dengan garis referensi. **Matplotlib.pyplot** (`import matplotlib.pyplot as plt`) adalah library dasar untuk membuat grafik, sementara **Seaborn** (`import seaborn as sns`) menyediakan antarmuka tingkat tinggi untuk visualisasi statistik yang lebih menarik.
5.  **Analisis Korelasi**: Matriks korelasi antar variabel (kecuali kolom ID yang tidak relevan) dihitung menggunakan fungsi `.corr()` dari pandas. Matriks korelasi menampilkan koefisien korelasi Pearson antar setiap pasangan variabel. Koefisien korelasi ($r$) mengukur kekuatan dan arah hubungan linier antara dua variabel, dengan nilai berkisar antara -1 (korelasi negatif sempurna) hingga 1 (korelasi positif sempurna), dan 0 menunjukkan tidak ada korelasi linier. 
**Koefisien Korelasi Pearson ($r$)** dihitung dengan rumus:

$$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

dengan:
- $x_i$ = nilai variabel X ke-$i$
- $y_i$ = nilai variabel Y ke-$i$
- $\bar{x}$ = rata-rata variabel X  
- $\bar{y}$ = rata-rata variabel Y  
- $n$ = jumlah observasi

Nilai $r$ berkisar antara -1 hingga 1:
- $r = 1$ menunjukkan korelasi positif sempurna  
- $r = -1$ menunjukkan korelasi negatif sempurna  
- $r = 0$ menunjukkan tidak ada korelasi linier

Secara keseluruhan, analisis ini menggunakan kombinasi library **pandas** untuk manipulasi data, **sklearn** (diimpor meskipun tidak semua fungsinya digunakan secara eksplisit dalam sel yang ditampilkan, menunjukkan kemungkinan penggunaan di langkah lain atau impor umum), **statsmodels** untuk pemodelan regresi statistik mendalam, **matplotlib**, dan **seaborn** untuk visualisasi data dan hasil model. Alur kerja ini mencakup pemuatan data, persiapan data, pelatihan model regresi, evaluasi kinerja model, dan analisis korelasi antar variabel.

## Notebook

Notebook dari repositori ini, tampil lengkap dengan sel kode dan hasilnya:

- [Analisis_Regresi_Linier_Berganda.ipynb](nb/konsep-regresi-linier-dalam-permodelan-karbon--analisis-regresi-linier-berganda.ipynb) · [GitHub](https://github.com/Defani/Konsep-regresi-linier-dalam-permodelan-karbon/blob/main/Analisis_Regresi_Linier_Berganda.ipynb) · [Colab](https://colab.research.google.com/github/Defani/Konsep-regresi-linier-dalam-permodelan-karbon/blob/main/Analisis_Regresi_Linier_Berganda.ipynb)
