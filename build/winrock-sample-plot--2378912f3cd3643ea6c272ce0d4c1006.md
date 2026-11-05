---
title: "winrock-sample-plot-calculator-web"
---

[Repositori di GitHub](https://github.com/Defani/winrock-sample-plot-calculator-web) · [Halaman web](https://defani.github.io/winrock-sample-plot-calculator-web/)

Kalkulator jumlah plot sampel untuk cadangan karbon (biomassa & tanah), diadaptasi dari
**Winrock International CDM A/R Sample Plot Calculator (2014)**, berdasarkan rumus resmi
CDM A/R Methodological Tool *"Calculation of the number of sample plots for measurements
within A/R CDM project activities"* v2.1.0.

Dibuat oleh **Defaniarman Alfitriansyah**.

## Cara pakai (lokal)
Cukup buka `index.html` di browser — tidak butuh server atau build step apa pun (murni HTML/CSS/JS).

## Deploy ke GitHub Pages

1. Buat repository baru di GitHub (bisa public), misal: `plot-calculator`.
2. Upload/push file `index.html` ini ke branch `main` (root repo).
   ```bash
   git init
   git add index.html
   git commit -m "Winrock sample plot calculator"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo>.git
   git push -u origin main
   ```
3. Di GitHub: buka repo → **Settings** → **Pages**.
4. Pada **Source**, pilih branch `main` dan folder `/ (root)` → **Save**.
5. Tunggu 1-2 menit, situs akan aktif di:
   `https://<username>.github.io/<repo>/`

Tidak ada dependency eksternal, jadi cukup 1 file `index.html` saja yang perlu di-deploy.

## Fitur
- Tab **Biomass Stocks** dan **Soil Carbon Stocks** (rumus sama, label unit berbeda)
- Tab **Metode** — penjelasan Equation 1, 2, 3 dan alokasi plot per strata
- Input dinamis per strata (tambah/hapus baris)
- Parameter: level error, tingkat kepercayaan (80/90/95/98/99%), buffer plot tambahan
- Output otomatis: N, luas total, rata-rata tertimbang, t-value, sampling fraction,
  jumlah plot total & per strata (dengan/tanpa buffer)

Rumus asli © Winrock International — https://www.winrock.org
