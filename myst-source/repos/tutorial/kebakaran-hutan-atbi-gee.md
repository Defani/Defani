---
title: "Kebakaran-Hutan--ATBI---GEE"
---

Pemetaan Keparahan Kebakaran Hutan dengan dATBI menggunakan Google Earth Engine Implementasi berbasis jurnal: Bilal, M. (2025). The automated temporal burn index (ATBI)

[Repositori di GitHub](https://github.com/Defani/Kebakaran-Hutan--ATBI---GEE)

> **Implementasi berbasis jurnal:** Bilal, M. (2025). *The automated temporal burn index (ATBI) for accurate and scalable burned area mapping.* International Journal of Applied Earth Observation and Geoinformation, 144, 104866. https://doi.org/10.1016/j.jag.2025.104866

---

*Script GEE: https://code.earthengine.google.com/330ea07830bdf414b5f28e05baa426f6*
---
## Latar Belakang

Kebakaran hutan merupakan salah satu gangguan ekologis dan klimatik terbesar di Bumi, berdampak pada dinamika gas rumah kaca, distribusi vegetasi, dan komunitas manusia (Goldammer et al., 2008; Kloster et al., 2012). Kejadian kebakaran baru-baru ini menegaskan meningkatnya keparahan dan skala kebakaran secara global akibat perubahan iklim (Bowman et al., 2020; Liu et al., 2014).

Pemetaan area terbakar yang akurat sangat kritis untuk:
- Penilaian dampak kebakaran terhadap kesehatan dan properti (Reid et al., 2016)
- Estimasi emisi gas rumah kaca dan siklus karbon (Randerson et al., 2006)
- Perencanaan pemulihan pasca-kebakaran (Lentile et al., 2006)
- Pemantauan tren kebakaran jangka panjang (Boschetti et al., 2015)

Indeks konvensional seperti **dNBR (Differenced Normalized Burn Ratio)** — yang menjadi standar operasional dalam program BAER, MTBS, dan ABoVE (Key & Benson, 2006; Eidenshink et al., 2007) — rentan terhadap kesalahan komisi (*commission errors*), yaitu mengklasifikasikan vegetasi yang tidak terbakar, awan, bayangan, atau salju sebagai area terbakar (Sparks et al., 2015; Meddens et al., 2016).

Studi ini mengimplementasikan **Automated Temporal Burn Index (ATBI)** (Bilal, 2025), sebuah indeks baru yang memanfaatkan tanda spektral ko-kurensi kebakaran (NIR↓ dan SWIR↑) melalui formulasi multiplikatif untuk menekan kesalahan komisi secara signifikan.

---

## Landasan Teori

### Respons Spektral Kebakaran

Kebakaran hutan menghasilkan perubahan spektral yang khas dan berlawanan arah pada saluran Near-Infrared (NIR) dan Shortwave-Infrared (SWIR):

| Kondisi | NIR | SWIR | Penjelasan |
|---|---|---|---|
| Vegetasi sehat | Tinggi | Rendah | Pantulan mesofil tinggi; kandungan air daun menyerap SWIR |
| Pasca-kebakaran | Rendah | Tinggi | Hilangnya struktur sel daun; paparan arang/substrat kering |
| Bayangan/awan | Rendah | Rendah | Tidak memenuhi kondisi ko-kurensi kebakaran |
| Salju/es | Tinggi | Rendah | NIR tinggi, SWIR tetap rendah |

Kombinasi NIR↓ dan SWIR↑ merupakan "sidik jari spektral" (*spectral fingerprint*) kebakaran yang tidak dimiliki oleh perubahan non-kebakaran (Ceccato et al., 2001; Veraverbeke et al., 2011).

### Prinsip Logika AND pada ATBI

ATBI dirancang dengan **logika AND** — nilai tinggi hanya dihasilkan ketika **kedua** kondisi spektral kebakaran terpenuhi secara bersamaan:

- NIR menurun (kehilangan struktur vegetasi)
- SWIR meningkat (paparan arang/substrat kering)

Kondisi non-kebakaran seperti bayangan (NIR↓, SWIR↓), tanah lembab (NIR tetap, SWIR tetap), dan perubahan fenologi (NIR naik, SWIR turun) gagal memenuhi salah satu kondisi ini, sehingga menghasilkan nilai ATBI rendah dan menekan deteksi palsu (Bilal, 2025).

---

## Formulasi Matematis

### 1. Normalized Burn Ratio (NBR)

$$\text{NBR} = \frac{\text{NIR} - \text{SWIR}}{\text{NIR} + \text{SWIR}}$$

### 2. Automated Temporal Burn Index (ATBI)

$$\text{ATBI} = \underbrace{\frac{\text{NIR} - \text{SWIR}}{\text{NIR} + \text{SWIR}}}_{\text{NBR (kontras keparahan)}} \times \underbrace{\frac{\text{SWIR}}{\text{NIR}}}_{\text{bobot kekeringan}}$$

yang dapat ditulis ulang sebagai:

$$\text{ATBI} = \text{NBR} \times \frac{\text{SWIR}}{\text{NIR}}$$

**Keterangan band per sensor Landsat:**

| Variabel | Landsat 8-9 OLI | Landsat 5 TM / 7 ETM+ |
|---|---|---|
| NIR | Band 5 | Band 4 |
| SWIR | Band 7 | Band 7 |

**Interpretasi fisik dua komponen ATBI:**
- **Komponen 1 — NBR:** Mengukur kontras keparahan bakar; kebakaran menurunkan NIR (hilangnya struktur seluler daun) dan meningkatkan SWIR (hilangnya kandungan air + paparan arang/substrat).
- **Komponen 2 — SWIR/NIR:** Faktor bobot kekeringan/paparan permukaan. Nilai kecil (<<1) untuk vegetasi sehat (NIR tinggi, SWIR rendah); nilai besar (>>1) untuk permukaan terbakar (NIR rendah, SWIR tinggi). Faktor ini memperkuat piksel yang secara fisik "mirip terbakar" dan melemahkan yang "mirip vegetasi".

**Contoh numerik perbandingan dATBI vs dNBR:**

Piksel hutan pra-kebakaran: NIR ≈ 0.5, SWIR ≈ 0.2

$$\text{NBR}_{\text{pre}} = \frac{0.5 - 0.2}{0.5 + 0.2} \approx 0.43, \quad \text{ATBI}_{\text{pre}} = 0.43 \times \frac{0.2}{0.5} \approx 0.17$$

Piksel pasca-kebakaran tinggi: NIR ≈ 0.1, SWIR ≈ 0.3

$$\text{NBR}_{\text{post}} = \frac{0.1 - 0.3}{0.1 + 0.3} \approx -0.50, \quad \text{ATBI}_{\text{post}} = -0.50 \times \frac{0.3}{0.1} \approx -1.50$$

Sehingga:

$$\text{dNBR} = 0.43 - (-0.50) \approx 0.93$$

$$\text{dATBI} = 0.17 - (-1.50) \approx 1.67$$

Perubahan spektral yang sama menghasilkan respons **~1.8× lebih kuat** pada dATBI dibandingkan dNBR, memperlebar jarak dinamis dan meningkatkan stabilitas klasifikasi.

### 3. Differenced ATBI (dATBI) — Pendekatan Bi-temporal

$$\text{dATBI} = \text{ATBI}_{\text{pre}} - \text{ATBI}_{\text{post}} \tag{2}$$

### 4. dATBI Temporal (dATBIt) — Pendekatan Multi-temporal

Untuk setiap citra pasca-kebakaran pada waktu $t$ ($t = 1, \ldots, n$):

$$
D_t(x,y) = \text{ATBI}_{\text{pre}}(x,y) - \text{ATBI}_{\text{post}(t)}(x,y)
$$

Masker kebakaran biner dengan ambang batas $T$ (dATBI ≥ 0.20):

$$
M_t(x,y) =
\begin{cases}
1, & \text{jika } D_t(x,y) \geq T \\
0, & \text{sebaliknya}
\end{cases}
$$

Jumlah deteksi kebakaran per piksel:

$$
K(x,y) = \sum_{t=1}^{n} M_t(x,y)
$$


### 5. Temporal Mean Burned Area Composite (dATBItm)

$$
\text{dATBI}_{tm}(x,y) =
\begin{cases}
\dfrac{1}{K(x,y)} \sum_{t=1}^{n} D_t(x,y) \cdot M_t(x,y), & \text{jika } K(x,y) \geq 1 \\
\text{null}, & \text{sebaliknya}
\end{cases}
$$


### 6. Differenced NBR (dNBR) — Pembanding

$$
\text{NBR} = \frac{\text{NIR} - \text{SWIR}}{\text{NIR} + \text{SWIR}}
$$

$$
\text{dNBR} = \text{NBR}_{\text{pre}} - \text{NBR}_{\text{post}}
$$


### 7. Metrik Validasi

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

$$
\text{F1 Score} = \frac{2 \cdot (\text{Precision} \cdot \text{Recall})}{\text{Precision} + \text{Recall}}
$$

$$
M = \frac{|\mu_b - \mu_{ub}|}{\sigma_b + \sigma_{ub}}
$$

### Hasil Validasi (Park Fire 2024, California)

Validasi menggunakan klasifikasi Random Forest (RF) sebagai referensi independen:

| Indeks | Presisi | Recall | F1-Score |
|---|---|---|---|
| **dATBI** | **0.919** | 0.975 | **0.946** |
| dNBR | 0.729 | 0.979 | 0.836 |

### Indeks Separabilitas (M)

| Indeks | Piksel Terbakar | Piksel Tidak Terbakar | $\mu_b$ | $\mu_{ub}$ | $\sigma_b$ | $\sigma_{ub}$ | **M** |
|---|---|---|---|---|---|---|---|
| **dATBI** | 1,258,751 (66.17%) | 643,515 (33.83%) | 0.481 | 0.072 | 0.219 | 0.079 | **1.38** |
| dNBR | 1,571,297 (84.01%) | 299,081 (15.99%) | 0.481 | 0.115 | 0.219 | 0.065 | 1.29 |

> dATBI memberikan nilai rata-rata kelas tidak terbakar yang jauh lebih rendah ($\mu_{ub}$ = 0.072 vs 0.115), meningkatkan jarak antar kelas dan mengurangi overlap histogram. Hal ini secara kuantitatif mengkonfirmasi bahwa dATBI menyediakan diskriminasi kelas yang lebih baik dibandingkan dNBR.

### Keunggulan Utama dATBI

- **Presisi lebih tinggi** (~0.92 vs ~0.73): jauh lebih sedikit deteksi palsu pada vegetasi sehat, bayangan, dan salju
- **F1-Score lebih tinggi** (~0.94 vs ~0.84): klasifikasi keseluruhan lebih andal
- **Separabilitas lebih baik** (M = 1.38 vs 1.29): jarak antar kelas lebih lebar
- **Recall setara** (~0.97–0.98): tidak mengorbankan deteksi area terbakar yang nyata
- **Stabilitas ambang batas**: performa tidak sensitif terhadap pergeseran ambang batas kecil, tidak seperti dNBR yang memerlukan kalibrasi per-scene
- **Robust terhadap gangguan atmosfer**: SREM-corrected imagery menghasilkan output dATBI yang lebih bersih dibandingkan produk LaSRC standar

---

## Struktur Kode

Script ini dijalankan di [Google Earth Engine (GEE)](https://code.earthengine.google.com/330ea07830bdf414b5f28e05baa426f6) dan terdiri dari beberapa tahapan:

```
DATBI.js
├── Akuisisi Citra
│   ├── Citra Sentinel-2 SR Sebelum Kebakaran (pre-fire)
│   └── Citra Sentinel-2 SR Sesudah Kebakaran (post-fire)
├── Komputasi Indeks
│   ├── hitungATBI()  ← fungsi utama ATBI
│   ├── atbiSebelum   ← ATBI pre-fire
│   ├── atbiSesudah   ← ATBI post-fire
│   └── dATBI         ← selisih (differenced ATBI)
├── Klasifikasi Keparahan
│   └── areaKebakaran (4 kelas: 0, 1, 2, 3)
├── Visualisasi
│   ├── RGB True Color Pre-fire
│   ├── False Color Post-fire
│   └── Peta Keparahan (Low/Moderate/High)
└── Ekspor
    ├── dATBI_LosAngeles_2025.tif
    └── Keparahan_Kebakaran_LosAngeles_2025.tif
```

---

## Cara Penggunaan

### Prasyarat

- Akun [Google Earth Engine](https://earthengine.google.com/)
- Area kajian didefinisikan sebagai variabel `batas_wilayah` (geometry GEE)

### Langkah 1 — Definisikan Area Kajian

Sebelum menjalankan script, buat atau import geometry batas wilayah di GEE:

```javascript
var batas_wilayah = ee.Geometry.Rectangle([/* koordinat bbox */]);
// atau import shapefile via Assets
```

### Langkah 2 — Akuisisi Citra

```javascript
// Citra Pra-Kebakaran
var sebelumKebakaran = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(batas_wilayah)
  .filterDate('2024-10-01', '2024-12-31')      // Sesuaikan tanggal
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .mosaic()
  .clip(batas_wilayah)
  .multiply(0.0001);                            // Scaling faktor Sentinel-2

// Citra Pasca-Kebakaran
var sesudahKebakaran = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(batas_wilayah)
  .filterDate('2025-01-15', '2025-02-15')      // Sesuaikan tanggal
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .mosaic()
  .clip(batas_wilayah)
  .multiply(0.0001);
```

> **Catatan band Sentinel-2:** Script menggunakan `B8` (NIR, 842 nm) dan `B12` (SWIR, 2190 nm), setara dengan Band 5 dan Band 7 pada Landsat 8-9 OLI yang digunakan dalam paper rujukan.

### Langkah 3 — Komputasi ATBI

```javascript
var hitungATBI = function(img) {
  var nir  = img.select('B8');   // Near-Infrared
  var swir = img.select('B12');  // Shortwave-Infrared

  // NBR = (NIR - SWIR) / (NIR + SWIR)
  var nbr   = nir.subtract(swir).divide(nir.add(swir));

  // SWIR/NIR = faktor bobot kekeringan
  var rasio = swir.divide(nir);

  // ATBI = NBR × (SWIR/NIR)
  return nbr.multiply(rasio).rename('ATBI');
};

var atbiSebelum = hitungATBI(sebelumKebakaran);
var atbiSesudah = hitungATBI(sesudahKebakaran);

// dATBI = ATBIpre - ATBIpost
var dATBI = atbiSebelum.subtract(atbiSesudah).rename('dATBI');
```

### Langkah 4 — Klasifikasi Keparahan

```javascript
var areaKebakaran = dATBI
  .where(dATBI.lt(0.20),                           0)  // Tidak terbakar
  .where(dATBI.gte(0.20).and(dATBI.lt(0.27)),      1)  // Keparahan rendah
  .where(dATBI.gte(0.27).and(dATBI.lt(0.66)),      2)  // Keparahan sedang
  .where(dATBI.gte(0.66),                           3)  // Keparahan tinggi
  .rename('Keparahan_Kebakaran');
```

### Langkah 5 — Ekspor Hasil

```javascript
// Ekspor dATBI kontinu
Export.image.toDrive({
  image: dATBI,
  description: 'dATBI_LosAngeles_2025',
  folder: 'GEE_Kebakaran',
  scale: 10,                  // Resolusi spasial 10m (Sentinel-2)
  region: batas_wilayah,
  fileFormat: 'GeoTIFF'
});

// Ekspor peta keparahan teklasifikasi
Export.image.toDrive({
  image: areaKebakaran,
  description: 'Keparahan_Kebakaran_LosAngeles_2025',
  folder: 'GEE_Kebakaran',
  scale: 10,
  region: batas_wilayah,
  fileFormat: 'GeoTIFF'
});
```

---

## Output

| File | Deskripsi | Format |
|---|---|---|
| `dATBI_LosAngeles_2025.tif` | Nilai dATBI kontinu (float) | GeoTIFF, 10m |
| `Keparahan_Kebakaran_LosAngeles_2025.tif` | Peta keparahan diskret (0–3) | GeoTIFF, 10m |

**Legenda peta keparahan:**

| Nilai | Kelas | Warna |
|---|---|---|
| 0 | Tidak terbakar | Transparan |
| 1 | Keparahan rendah | Kuning |
| 2 | Keparahan sedang | Oranye |
| 3 | Keparahan tinggi | Merah |

---

## Keterbatasan

- **Kalibrasi ambang batas empiris:** Ambang batas keparahan dATBI saat ini diadaptasi dari konvensi dNBR. Kalibrasi terhadap data Composite Burn Index (CBI) lapangan masih diperlukan untuk operasionalisasi penuh di berbagai ekosistem (Bilal, 2025).
- **Koreksi atmosfer:** dATBI sensitif terhadap kualitas data reflektansi permukaan. Produk SREM memberikan hasil yang lebih bersih dibandingkan LaSRC standar; perbedaan produk atmosfer dapat mempengaruhi akurasi (Bilal, 2025).
- **Regrowth cepat:** Di ekosistem dengan regenerasi cepat (misal savana Cerrado), sinyal bakar pada piksel yang sudah tumbuh kembali tetap terdeteksi jika setidaknya satu citra menangkap kondisi pasca-kebakaran segera.
- **Sungai bermuatan sedimen:** Pada skala besar, beberapa sungai bermuatan sedimen tinggi dapat salah terklasifikasi sebagai terbakar karena reflektansi gelap yang menyerupai arang (Bilal, 2025).
- **Adaptasi sensor:** Implementasi ini menggunakan Sentinel-2 (B8/B12), sedangkan paper rujukan menggunakan Landsat. Perbedaan karakteristik sensor perlu diperhatikan dalam interpretasi hasil.

---

## Daftar Pustaka

Bilal, M. (2025). *The automated temporal burn index (ATBI) for accurate and scalable burned area mapping.* International Journal of Applied Earth Observation and Geoinformation, **144**, 104866. https://doi.org/10.1016/j.jag.2025.104866

Bilal, M., Nazeer, M., Nichol, J.E., Bleiweiss, M.P., Qiu, Z., Jäkel, E., ... & Lolli, S. (2019). A Simplified and Robust Surface Reflectance Estimation Method (SREM) for use over Diverse Land Surfaces using Multi-Sensor Data. *Remote Sensing*, **11**.

Boschetti, L., Roy, D.P., Justice, C.O., & Humber, M.L. (2015). MODIS–Landsat fusion for large area 30 m burned area mapping. *Remote Sensing of Environment*, **161**, 27–42.

Bowman, D.M.J.S., Kolden, C.A., Abatzoglou, J.T., Johnston, F.H., van der Werf, G.R., & Flannigan, M. (2020). Vegetation fires in the Anthropocene. *Nature Reviews Earth & Environment*, **1**, 500–515.

Ceccato, P., Flasse, S., Tarantola, S., Jacquemoud, S., & Grégoire, J.M. (2001). Detecting vegetation leaf water content using reflectance in the optical domain. *Remote Sensing of Environment*, **77**, 22–33.

Chuvieco, E., Martín, M.P., & Palacios, A. (2002). Assessment of different spectral indices in the red-near-infrared spectral domain for burned land discrimination. *International Journal of Remote Sensing*, **23**, 5103–5110.

Eidenshink, J., Schwind, B., Brewer, K., Zhu, Z.-L., Quayle, B., & Howard, S. (2007). A Project for monitoring Trends in Burn Severity. *Fire Ecology*, **3**, 3–21.

Goldammer, J.G., Statheropoulos, M., & Andreae, M.O. (2008). Impacts of vegetation fire emissions on the environment, human health, and security: a global perspective. *Developments in Environmental Science*, **8**, 3–36.

Holsinger, L.M., Parks, S.A., Saperstein, L.B., Loehman, R.A., Whitman, E., Barnes, J., ... & Bohlman, S. (2022). Improved fire severity mapping in the North American boreal forest using a hybrid composite method. *Remote Sensing in Ecology and Conservation*, **8**, 222–235.

Key, C.H., & Benson, N.C. (2006). *Landscape Assessment: Ground measure of severity, the Composite Burn Index; and Remote sensing of severity, the Normalized Burn Ratio.* Ogden, UT.

Kloster, S., Mahowald, N.M., Randerson, J.T., & Lawrence, P.J. (2012). The impacts of climate, land use, and demography on fires during the 21st century simulated by CLM-CN. *Biogeosciences*, **9**, 509–525.

Lentile, L.B., Holden, Z.A., Smith, A.M.S., Falkowski, M.J., Hudak, A.T., Morgan, P., ... & Benson, N.C. (2006). Remote sensing techniques to assess active fire characteristics and post-fire effects. *International Journal of Wildland Fire*, **15**.

Liu, Y., Goodrick, S., & Heilman, W. (2014). Wildland fire emissions, carbon, and climate: Wildfire–climate interactions. *Forest Ecology and Management*, **317**, 80–96.

Meddens, A.J.H., Kolden, C.A., & Lutz, J.A. (2016). Detecting unburned areas within wildfire perimeters using Landsat and ancillary data across the northwestern United States. *Remote Sensing of Environment*, **186**, 275–285.

Pleniou, M., & Koutsias, N. (2013). Sensitivity of spectral reflectance values to different burn and vegetation ratios: a multi-scale approach applied in a fire affected area. *ISPRS Journal of Photogrammetry and Remote Sensing*, **79**, 199–210.

Randerson, J.T., Liu, H., Flanner, M.G., Chambers, S.D., Jin, Y., Hess, P.G., ... & Zender, C.S. (2006). The impact of boreal forest fire on climate warming. *Science*, **314**, 1130–1132.

Reid, C.E., Brauer, M., Johnston, F.H., Jerrett, M., Balmes, J.R., & Elliott, C.T. (2016). Critical Review of Health Impacts of Wildfire Smoke Exposure. *Environmental Health Perspectives*, **124**, 1334–1343.

Roy, D.P., Huang, H., Boschetti, L., Giglio, L., Yan, L., Zhang, H.H., & Li, Z. (2019). Landsat-8 and Sentinel-2 burned area mapping — A combined sensor multi-temporal change detection approach. *Remote Sensing of Environment*, **231**.

Sparks, A.M., Smith, A.M.S., Talhelm, A.F., Kolden, C.A., Yedinak, K.M., & Johnson, D.M. (2015). Spectral indices accurately predict forest burn severity in the western USA. *International Journal of Wildland Fire*.

Veraverbeke, S., Harris, S., & Hook, S. (2011). Evaluating spectral indices for burned area discrimination using MODIS/ASTER (MASTER) airborne simulator data. *Remote Sensing of Environment*, **115**, 2702–2709.

Vermote, E., Justice, C., Claverie, M., & Franch, B. (2016). Preliminary analysis of the performance of the Landsat 8/OLI land surface reflectance product. *Remote Sensing of Environment*, **185**, 46–56.

---

*Script GEE: https://code.earthengine.google.com/330ea07830bdf414b5f28e05baa426f6*
