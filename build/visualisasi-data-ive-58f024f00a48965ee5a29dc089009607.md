---
title: "Visualisasi-Data-Iventarisasi-Hutan-Python"
---

[Repositori di GitHub](https://github.com/Defani/Visualisasi-Data-Iventarisasi-Hutan-Python)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1v5OXRIJ6ZZU0JBM90M_AsapGsUBnaK6u?usp=sharing)

## Deskripsi

Script Python untuk **visualisasi** struktur dan komposisi vegetasi berdasarkan fase pertumbuhan (Semai, Pancang, Tiang, Pohon). Menghasilkan dua visualisasi utama:
1. Distribusi spesies terhadap gradien elevasi
2. Spesies dominan berdasarkan Indeks Nilai Penting (INP)

## Requirements

```python
pandas
matplotlib
seaborn
```

## Instalasi

```bash
pip install pandas matplotlib seaborn
```

## Penggunaan

### 1. Import Library

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
```

### 2. Load dan Label Data

```python
# Membaca data
df_semai = pd.read_csv('data_semai.csv')
df_pancang = pd.read_csv('data_pancang.csv')
df_tiang = pd.read_csv('data_tiang.csv')
df_pohon = pd.read_csv('data_pohon.csv')

# Labeling fase pertumbuhan
df_semai['Fase'] = 'Semai'
df_pancang['Fase'] = 'Pancang'
df_tiang['Fase'] = 'Tiang'
df_pohon['Fase'] = 'Pohon'

# Gabungkan semua data
df_all = pd.concat([df_semai, df_pancang, df_tiang, df_pohon], ignore_index=True)
```

### 3. Visualisasi 1: Distribusi Elevasi

```python
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_all,
    x='Ketinggian (mdpl)',
    y='Jumlah Jenis',
    hue='Fase',
    style='Fase',
    s=100,
    palette='viridis'
)

plt.title('Hubungan Ketinggian Tempat vs Jumlah Jenis Tumbuhan', 
          fontsize=16, weight='bold')
plt.xlabel('Ketinggian (mdpl)', fontsize=12)
plt.ylabel('Jumlah Jenis (Spesies)', fontsize=12)
plt.legend(title='Fase Pertumbuhan', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
```

**Output**: Scatter plot yang menampilkan pola distribusi jumlah spesies pada berbagai ketinggian untuk setiap fase pertumbuhan.

### 4. Visualisasi 2: Spesies Dominan

```python
# Ambil 3 spesies teratas per fase
top_species = df_all.sort_values('INP (%)', ascending=False).groupby('Fase').head(3)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_species,
    x='INP (%)',
    y='Jenis Dominan',
    hue='Fase',
    dodge=False,
    palette='viridis'
)

plt.title('Spesies Dominan Berdasarkan Indeks Nilai Penting (INP)', 
          fontsize=16, weight='bold')
plt.xlabel('Indeks Nilai Penting (%)', fontsize=12)
plt.ylabel('Nama Spesies', fontsize=12)
plt.legend(title='Fase Pertumbuhan', loc='lower left')
plt.tight_layout()
plt.show()
```

**Output**: Bar plot horizontal menampilkan 3 spesies dengan INP tertinggi untuk setiap fase pertumbuhan.

## Format Data Input

File CSV harus memiliki kolom:
- `Ketinggian (mdpl)`: Elevasi lokasi
- `Jumlah Jenis`: Jumlah spesies
- `Jenis Dominan`: Nama spesies dominan
- `INP (%)`: Indeks Nilai Penting

## Fase Pertumbuhan

| Fase | Kriteria |
|------|----------|
| **Semai** | Tinggi < 1.5 m |
| **Pancang** | Tinggi > 1.5 m, Diameter < 10 cm |
| **Tiang** | Diameter 10-19 cm |
| **Pohon** | Diameter ≥ 20 cm |

## Interpretasi Visualisasi

### Plot 1: Ketinggian vs Jumlah Jenis
- Menunjukkan zonasi vegetasi terhadap elevasi
- Identifikasi zona optimal untuk setiap fase
- Pola keanekaragaman vertikal

### Plot 2: Spesies Dominan
- INP > 100% = dominasi sangat tinggi
- Mengidentifikasi spesies kunci ekosistem
- Perbandingan dominansi antar fase

## Referensi

**Adhya, I., Hendrayana, Y., Supartono, T., Ismail, A.Y., & Nurdin. (2021).** Vegetation structure and species composition of habitat types *Goniothalamus macrophyllus* (Blume) Hook.f. and Thomson in Lowland Forest, Kuningan Regency, West Java. *IOP Conference Series: Earth and Environmental Science*, 819, 012063. https://doi.org/10.1088/1755-1315/819/1/012063

**Highlights dari penelitian:**
- Lokasi: Hutan dataran rendah, Kabupaten Kuningan, Jawa Barat
- Elevasi: 432 - 1,273 m dpl
- Komposisi: 108 jenis semai, 125 jenis pancang, 98 jenis tiang, 105 jenis pohon
- Dominansi tertinggi: *Coffea* spp. (semai), *Decapermum paniculatum* (pancang), *Villebrunea rubenscens* (tiang & pohon)

---

**Note**: Script ini fokus pada **visualisasi data yang sudah terproses**. Untuk metodologi analisis vegetasi lengkap, lihat paper Adhya et al. (2021).

## Notebook

Notebook dari repositori ini, tampil lengkap dengan sel kode dan hasilnya:

- [Anveg.ipynb](nb/visualisasi-data-iventarisasi-hutan-python--anveg.ipynb) · [GitHub](https://github.com/Defani/Visualisasi-Data-Iventarisasi-Hutan-Python/blob/main/Anveg.ipynb) · [Colab](https://colab.research.google.com/github/Defani/Visualisasi-Data-Iventarisasi-Hutan-Python/blob/main/Anveg.ipynb)
