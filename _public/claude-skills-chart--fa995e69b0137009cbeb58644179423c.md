---
title: "claude-skills-chart-generator"
---

Skill untuk Claude (Claude.ai / Claude Code) yang membantu membuat grafik ilmiah (bar chart, line chart, scatter, box plot, heatmap, dan lainnya) menggunakan Python/matplotlib, cocok untuk paper, laporan lab, atau publikasi akademik.

[Repositori di GitHub](https://github.com/Defani/claude-skills-chart-generator)

[![Made for Claude](https://img.shields.io/badge/made%20for-Claude-CC785C?style=flat-square)](https://claude.ai)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![Matplotlib](https://img.shields.io/badge/matplotlib-charts-11557C?style=flat-square)](https://matplotlib.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-informational?style=flat-square)](#lisensi)

Skill untuk Claude (Claude.ai / Claude Code) yang membantu membuat grafik ilmiah (bar chart, line chart, scatter, box plot, heatmap, dan lainnya) menggunakan Python/matplotlib, cocok untuk paper, laporan lab, atau publikasi akademik.

Skill ini dirancang minim ketik, maksimal klik — Claude akan bertanya lewat tombol pilihan, mendeteksi otomatis kolom dari file data yang diupload, dan dapat menyamakan gaya grafik dengan paper referensi (PDF) yang diberikan. Output akhirnya berupa kode Python siap jalan di Google Colab.

## Fitur

- Interaksi lewat tombol pilihan, bukan mengetik jawaban panjang
- Auto-baca CSV/Excel yang diupload: deteksi kolom, tipe data, kandidat sumbu X/Y, dan error bar
- Bisa menyamakan gaya visual dengan paper referensi (PDF) yang diupload
- 50 palet warna siap pilih, dengan preview visual dan klik langsung
- 8 pola hatch untuk grafik hitam-putih, cocok untuk syarat cetak jurnal
- Preset cepat: Nature style, ggplot, seaborn, classic matplotlib, print-friendly (B/W), presentasi
- Output kode Python (`.py`) lengkap dengan blok konfigurasi, siap dijalankan di Google Colab
- File hasil (PNG/SVG/JPG) ikut digenerate dan disajikan bersama kodenya

## Cara download

1. Klik tombol **Code → Download ZIP** di halaman repo ini, atau
2. Download langsung file `sci-chart-generator.skill` dari bagian [Releases](https://github.com/Defani/claude-skills-chart-generator/blob/main/releases) / folder repo ini.

## Cara pakai di Claude.ai

1. Buka **Settings → Capabilities → Skills**.
2. Upload file `sci-chart-generator.skill`.
3. Mulai chat baru, upload data (CSV/Excel) dan/atau PDF referensi, lalu minta Claude membuatkan grafik ilmiah — skill akan aktif otomatis.

### Alur singkat

<p align="center">
  <img width="900" alt="Pilih engine bahasa" src="https://github.com/user-attachments/assets/31b1e0fe-deaa-4398-b326-dcea3c1bcd43"><br>
  <sub>1. Pilih engine bahasa (Python/R)</sub>
</p>

<p align="center">
  <img width="900" alt="Pilih tipe chart" src="https://github.com/user-attachments/assets/824f6db6-5e06-4efb-ae56-fcfd4237e246"><br>
  <sub>2. Pilih tipe chart atau custom</sub>
</p>

<p align="center">
  <img width="900" alt="Pilih palet warna" src="https://github.com/user-attachments/assets/074a7679-dc72-426c-888f-cbac126faa61"><br>
  <sub>3. Klik salah satu palet warna dari preview</sub>
</p>

<p align="center">
  <img width="900" alt="Pilih style theme" src="https://github.com/user-attachments/assets/0a00f308-f370-458f-8da6-e076867be4f4"><br>
  <sub>4. Pilih style theme</sub>
</p>

<p align="center">
  <img width="900" alt="Pengaturan warna" src="https://github.com/user-attachments/assets/970fb271-00ed-4c75-aac5-0e8a92a222c6"><br>
  <sub>5. Pengaturan warna tambahan</sub>
</p>

<p align="center">
  <img width="900" alt="Pengaturan axis" src="https://github.com/user-attachments/assets/4cf8cece-0d13-4768-bbb6-63ea70bca897"><br>
  <sub>6. Konfirmasi mapping axis</sub>
</p>

<p align="center">
  <img width="900" alt="Posisi legend" src="https://github.com/user-attachments/assets/8cde6fd1-1c91-49bb-a890-013b0dc0ee5a"><br>
  <sub>7. Pilih posisi legend</sub>
</p>

<p align="center">
  <img width="900" alt="Pengaturan label" src="https://github.com/user-attachments/assets/9d7ab1a7-2191-4e91-9400-1de4041c7ebb"><br>
  <sub>8. Pengaturan label data</sub>
</p>

<p align="center">
  <img width="900" alt="Pilih pattern" src="https://github.com/user-attachments/assets/e360da39-92ba-4f64-a9de-9d7d83da4190"><br>
  <sub>9. Pilih mode polos atau pattern</sub>
</p>

<p align="center">
  <img width="900" alt="Ukuran gambar" src="https://github.com/user-attachments/assets/ab7da85c-2653-4b15-b649-73ee1c830d53"><br>
  <sub>10. Atur ukuran gambar</sub>
</p>

<p align="center">
  <img width="900" alt="Resolusi export" src="https://github.com/user-attachments/assets/8b03717d-01e8-4fbb-9dbd-b7a3ad5b11ae"><br>
  <sub>11. Atur resolusi export</sub>
</p>

<p align="center">
  <img width="900" alt="Format export" src="https://github.com/user-attachments/assets/a29b4b90-e11e-4562-bd28-6b367921812e"><br>
  <sub>12. Pilih format export</sub>
</p>

<p align="center">
  <img width="900" alt="Pilih bahasa" src="https://github.com/user-attachments/assets/724c211d-dc5c-426f-8426-0d09b5ae5f70"><br>
  <sub>13. Pilih bahasa label</sub>
</p>

<p align="center">
  <img width="900" alt="Judul chart" src="https://github.com/user-attachments/assets/523d6403-037d-45ff-b738-a956b31ec029"><br>
  <sub>14. Tentukan judul chart</sub>
</p>

<p align="center">
  <img width="900" alt="Hasil akhir" src="https://github.com/user-attachments/assets/e57f063d-5643-415e-a16b-0260bdd25f9f"><br>
  <sub>15. Kode siap Colab dihasilkan</sub>
</p>

<p align="center">
  <img width="900" alt="Contoh output chart" src="https://github.com/user-attachments/assets/c86a360a-a889-467a-a408-8f8e686ae362"><br>
  <sub>Contoh output: distribusi genus</sub>
</p>

## Isi skill

```text
sci-chart-generator/
├── SKILL.md                  # instruksi utama skill
└── data/
    ├── palettes.json         # 50 palet warna
    └── hatch_legend.json     # 8 pola hatch + 8 posisi legend
```

## Lisensi
MIT
