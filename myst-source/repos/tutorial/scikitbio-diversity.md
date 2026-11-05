---
title: "scikitbio-diversity-"
---

Tutorial ini memperagakan cara menghitung dan memvisualisasikan indeks keanekaragaman alfa (alpha diversity) komunitas herpetofauna di empat tipe habitat Taman Nasional Bali Barat (TNBB) menggunakan pustaka Python scikit-bio.

[Repositori di GitHub](https://github.com/Defani/scikitbio-diversity-)

### Tutorial Alpha Diversity menggunakan scikit-bio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18xAp_h8hw1-2URPO2CyMe8mhS-jJblv-?usp=sharing)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-bio](https://img.shields.io/badge/scikit--bio-0.7.0-green)


---

## Deskripsi

Tutorial ini memperagakan cara menghitung dan memvisualisasikan **indeks keanekaragaman alfa (alpha diversity)** komunitas herpetofauna di empat tipe habitat Taman Nasional Bali Barat (TNBB) menggunakan pustaka Python **scikit-bio**. Dataset bersumber dari Amarasinghe et al. (2021) yang mendokumentasikan kekayaan dan kelimpahan reptil serta amfibi di TNBB.

---

## Struktur Repositori

```
.
├── tnbb_herpetofauna.csv          # Dataset kelimpahan spesies per habitat
├── tutorial_scikit_bio_v2.ipynb   # Notebook tutorial lengkap
└── README.md
```

---

## Dataset

**File:** `tnbb_herpetofauna.csv`

Matriks kelimpahan spesies × habitat dengan format:

| Kolom | Keterangan |
|---|---|
| `species` | Nama ilmiah spesies (index baris) |
| `perkebunan_jati` | Kelimpahan di habitat perkebunan jati |
| `hutan_gugur` | Kelimpahan di habitat hutan gugur |
| `hutan_lembab` | Kelimbahan di habitat hutan lembab |
| `savana` | Kelimpahan di habitat savana |

**Sumber:** Amarasinghe et al. (2021), *Global Ecology and Conservation*, 28, e01638.

---

## Teori Dasar

### Konsep Alpha Diversity

Alpha diversity mengukur keanekaragaman spesies **dalam satu komunitas atau habitat** tertentu. Berbeda dengan beta diversity (perbedaan komposisi antar habitat) atau gamma diversity (keanekaragaman total suatu lanskap), alpha diversity merangkum tiga dimensi utama komunitas: **kekayaan spesies** (*species richness*), **kelimpahan relatif** (*relative abundance*), dan **kemerataan** (*evenness*) (Whittaker, 1972).

Dalam konteks data omik dan ekologi, scikit-bio (Aton et al., 2025) mengimplementasikan berbagai metrik alpha diversity yang bekerja langsung pada vektor kelimpahan integer, tanpa memerlukan konversi ke proporsi secara manual.

---

### 1. Kekayaan Spesies — *Species Richness* (S)

Kekayaan spesies adalah jumlah spesies yang **hadir** (kelimpahan > 0) dalam suatu sampel. Ini merupakan metrik paling sederhana dan tidak mempertimbangkan kelimpahan relatif antar spesies.

$$S = \sum_{i=1}^{N} \mathbf{1}[n_i > 0]$$

Di mana $n_i$ adalah jumlah individu spesies ke-$i$ dan $N$ adalah total spesies yang diamati.

**Fungsi scikit-bio:**
```python
observed_features(counts)
```

---

### 2. Indeks Shannon-Wiener (H')

Indeks Shannon-Wiener berasal dari teori informasi (Shannon, 1948) dan mengukur **ketidakpastian** dalam mengidentifikasi spesies dari satu individu yang dipilih secara acak. Nilai H' meningkat seiring bertambahnya jumlah spesies dan semakin meratanya distribusi kelimpahan.

$$H' = -\sum_{i=1}^{S} p_i \ln(p_i)$$

Di mana:
- $S$ = jumlah spesies yang hadir
- $p_i = \dfrac{n_i}{\sum_{j=1}^{S} n_j}$ = proporsi individu spesies ke-$i$ terhadap total individu
- $\ln$ = logaritma natural (basis $e$)

**Interpretasi nilai H':**

| Nilai H' | Kategori keanekaragaman |
|---|---|
| H' < 1,0 | Rendah |
| 1,0 ≤ H' ≤ 3,0 | Sedang |
| H' > 3,0 | Tinggi |

> Nilai H' maksimum ($H'_{max} = \ln S$) tercapai ketika semua spesies memiliki kelimpahan yang sama persis (komunitas perfectly even).

**Fungsi scikit-bio:**
```python
shannon(counts, base=np.e)
```

---

### 3. Indeks Simpson (D) dan Gini-Simpson

Indeks Simpson (Simpson, 1949) mengukur **probabilitas** bahwa dua individu yang dipilih secara acak dari komunitas berasal dari spesies yang sama. Nilai D mendekati 1 menandakan dominasi kuat oleh satu atau sedikit spesies.

$$D = \sum_{i=1}^{S} p_i^2$$

Turunannya, **Gini-Simpson index** (juga disebut *probability of interspecific encounter*), merupakan komplemen dari D:

$$\text{Gini-Simpson} = 1 - D = 1 - \sum_{i=1}^{S} p_i^2$$

Gini-Simpson lebih intuitif karena nilainya meningkat seiring meningkatnya keanekaragaman (searah dengan H').

> **Perhatian implementasi:** Fungsi `simpson()` pada scikit-bio mengembalikan nilai **Gini-Simpson (1 − D)**, bukan D. Untuk memperoleh Simpson's Dominance Index: `D = 1 - simpson(counts)`.

**Fungsi scikit-bio:**
```python
gini = simpson(counts)      # mengembalikan 1 - D
D    = 1 - simpson(counts)  # untuk mendapat Simpson's D
```

---

### 4. Kemerataan Pielou (J)

Kemerataan Pielou atau *Pielou's Evenness* (Pielou, 1966) mengukur seberapa merata kelimpahan individu terdistribusi di antara spesies yang ada. J diperoleh dengan menormalisasi H' terhadap nilai maksimum teoretisnya:

$$J = \frac{H'}{\ln(S)} = \frac{H'}{H'_{max}}$$

- $J = 1$ → semua spesies memiliki kelimpahan yang identik (komunitas paling merata)
- $J \to 0$ → komunitas didominasi oleh satu atau sedikit spesies

J tidak terdefinisi untuk komunitas dengan hanya satu spesies ($S = 1$, karena $\ln(1) = 0$).

**Fungsi scikit-bio:**
```python
pielou_e(counts)
```

---

### Ringkasan Metrik

| Metrik | Simbol | Rentang | Makin tinggi berarti |
|---|---|---|---|
| Species Richness | S | ≥ 1 (integer) | Lebih banyak spesies |
| Shannon-Wiener | H' | ≥ 0 | Lebih beragam |
| Simpson's Dominance | D | 0 – 1 | Lebih terdominasi |
| Gini-Simpson | 1−D | 0 – 1 | Lebih beragam |
| Pielou's Evenness | J | 0 – 1 | Lebih merata |

---

## Pustaka scikit-bio yang Digunakan

```python
from skbio.diversity.alpha import (
    observed_features,   # Kekayaan spesies (S)
    shannon,             # Shannon-Wiener H'
    simpson,             # Gini-Simpson (1 - D)
    pielou_e             # Pielou's Evenness J
)
```

Semua fungsi menerima input berupa **array integer kelimpahan** (jumlah individu per spesies), bukan proporsi. Contoh: `np.array([30, 8, 4, 9, 2])`.

---

## Cara Menjalankan

### Google Colab (direkomendasikan)

Klik badge **Open in Colab** di bagian atas, lalu jalankan sel secara berurutan.

### Lokal

```bash
git clone https://github.com/Defani/tutorial-scikit-bio-tnbb.git
cd tutorial-scikit-bio-tnbb
pip install scikit-bio numpy pandas matplotlib
jupyter notebook tutorial_scikit_bio_v2.ipynb
```

---

## Dependensi

| Pustaka | Versi minimum | Fungsi |
|---|---|---|
| scikit-bio | 0.6.0 | Kalkulasi alpha diversity |
| numpy | 1.21 | Operasi array |
| pandas | 1.3 | Manajemen dataframe |
| matplotlib | 3.4 | Visualisasi |

---

## Daftar Pustaka

Amarasinghe, A. A. T., Madawala, M. B., Karunarathna, D. M. S. S., Manawaduge, R. P. C. D., Gabadage, D. E., Botejue, M., Henkanaththegedara, S. M., & Karunarathna, S. (2021). Herpetofaunal diversity of West Bali National Park, Indonesia. *Global Ecology and Conservation*, *28*, e01638. https://doi.org/10.1016/j.gecco.2021.e01638

Aton, M., McDonald, D., Cañardo Alastuey, J., Azom, R., Batra, P., Bezshapkin, V., Bolyen, E., Cagle, A., Caporaso, J. G., Debelius, J. W., Gorlick, K., Hamsanipally, N., Hunger, L., Keluskar, A., Liao, D., Lu, Y. Y., Navas-Molina, J. A., Pitman, A., Rideout, J. R., … Zhu, Q. (2025). Scikit-bio: a fundamental Python library for biological omic data analysis. *Nature Methods*. https://doi.org/10.1038/s41592-025-02981-z

Pielou, E. C. (1966). The measurement of diversity in different types of biological collections. *Journal of Theoretical Biology*, *13*, 131–144. https://doi.org/10.1016/0022-5193(66)90013-0

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, *27*(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Simpson, E. H. (1949). Measurement of diversity. *Nature*, *163*(4148), 688. https://doi.org/10.1038/163688a0

Whittaker, R. H. (1972). Evolution and measurement of species diversity. *Taxon*, *21*(2–3), 213–251. https://doi.org/10.2307/1218190

---

*Tutorial ini dibuat untuk keperluan pendidikan ekologi kuantitatif dan analisis keanekaragaman hayati menggunakan Python.*
