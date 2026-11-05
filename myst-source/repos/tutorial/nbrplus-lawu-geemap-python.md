---
title: "NBRplus-Lawu-Geemap-Python"
---

This project maps and analyzes burned areas resulting from the Mount Lawu forest fire (August 30 – September 29, 2023) using the Normalized Burn Ratio Plus (NBR+) index applied to Sentinel-2 Surface Reflectance imagery via Google Earth Engine.

[Repositori di GitHub](https://github.com/Defani/NBRplus-Lawu-Geemap-Python)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1y6rEKWDKBnWwJGgrs-ScnkHeLUryxZTY?usp=sharing)
[![Open in Earth Engine](https://img.shields.io/badge/Open%20in-Earth%20Engine-4285F4?style=flat-square&logo=google&logoColor=white)](https://code.earthengine.google.com/457addfc0dcb9d8e840be1ac7d5e2c4d?hl=id)
[![GitHub](https://img.shields.io/badge/GitHub-NBRplus--Lawu-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/Defani/NBRplus-Lawu-Geemap-Python)

<div align="left">
  <a href="https://linkedin.com/in/defaniarmanalfitriansyah"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://medium.com/@defaniarman"><img src="https://img.shields.io/badge/Medium-12100E?style=flat-square&logo=medium&logoColor=white" alt="Medium" /></a>
  <a href="https://tiktok.com/@defaniarman"><img src="https://img.shields.io/badge/TikTok-000000?style=flat-square&logo=tiktok&logoColor=white" alt="TikTok" /></a>
  <a href="https://www.instagram.com/de.fanii"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="https://www.kaggle.com/defani123"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white" alt="Kaggle" /></a>
  <a href="https://rpubs.com/defanii"><img src="https://img.shields.io/badge/RPubs-75AADB?style=flat-square&logo=r&logoColor=white" alt="RPubs" /></a>
  <a href="https://www.behance.net/defaniarman"><img src="https://img.shields.io/badge/Behance-1769FF?style=flat-square&logo=behance&logoColor=white" alt="Behance" /></a>
  <a href="mailto:defaniarman@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
</div>

---
<img width="1677" height="1069" alt="download (57)" src="https://github.com/user-attachments/assets/d299096b-2f4e-4f8e-9098-77d65608beda" />

## Overview

This project maps and analyzes burned areas resulting from the Mount Lawu forest fire (August 30 – September 29, 2023) using the **Normalized Burn Ratio Plus (NBR+)** index applied to **Sentinel-2 Surface Reflectance** imagery via Google Earth Engine. The bi-temporal approach computes the difference between pre-fire and post-fire NBR+ composites (dNBR+) to classify burn severity across the affected area.

NBR+ was proposed by Alcaras et al. (2022) as an enhancement over the classical NBR. By incorporating Sentinel-2 Blue (B2) and Green (B3) bands alongside NIR (B8A) and SWIR2 (B12), NBR+ inherently suppresses false positives from water bodies and clouds without requiring external masking layers.

---

## Study Area

| Parameter | Description |
|---|---|
| Location | Mount Lawu, Central Java / East Java border, Indonesia |
| Coordinates | 111°11'39" E, 7°37'37" S |
| Fire period | August 30 – September 29, 2023 |
| Satellite | Sentinel-2A SR Harmonized |
| Pre-fire composite | August 1–29, 2023 (median) |
| Post-fire composite | October 1–31, 2023 (median) |
| Spatial resolution | 20 m |

---

## Spectral Index

### NBR+ (Normalized Burn Ratio Plus)

NBR+ extends the classical NBR by incorporating the Blue (B2) and Green (B3) bands of Sentinel-2 in addition to NIR (B8A) and SWIR2 (B12) (Alcaras et al., 2022):

```
NBR+ = (B12 - B8A - B3 - B2) / (B12 + B8A + B3 + B2)
```

The spectral rationale is as follows. Water bodies exhibit strong reflectance in blue-green wavelengths, so including B2 and B3 in the subtraction drives NBR+ values for water pixels toward negative. Clouds also yield strongly negative NBR+ due to their low SWIR2 (B12) reflectance relative to the other three bands. Burned areas, characterized by high SWIR reflectance and low NIR and visible reflectance, produce distinctively high positive NBR+ values. This spectral separation allows burned areas to be identified without reliance on external water or cloud masks.

### Bi-temporal Delta Index (dNBR+)

The bi-temporal approach isolates fire-induced spectral change by differencing pre- and post-fire composites:

```
dNBR+ = NBR+_postfire - NBR+_prefire
```

Positive dNBR+ values indicate pixels where NBR+ decreased after the fire, consistent with vegetation loss and increased bare ground exposure.

---


---

## Project Structure

```
NBRplus-Lawu-Geemap-Python/
├── notebook.ipynb      # Main analysis notebook (GEE + geemap + cartoee)
└── README.md
```

---

## Workflow

```
1. Authenticate and initialize Google Earth Engine
        |
2. Define AOI — Mount Lawu polygon
        |
3. Load Sentinel-2 SR Harmonized collection
   - Cloud masking via Cloud Score+ (cs_cdf >= 0.6)
   - Filter by CLOUDY_PIXEL_PERCENTAGE < 20
        |
4. Build pre-fire and post-fire median composites
        |
5. Compute NBR+ for pre-fire and post-fire images
        |
6. Compute dNBR+ = NBR+_post - NBR+_pre
        |
7. Apply burn threshold (dNBR+ >= 0.3) to extract burned area mask
        |
8. Generate 2x3 visualization panel:
   A. Pre-fire false color composite  (B11 / B8 / B4)
   B. Post-fire false color composite (B11 / B8 / B4)
   C. Post-fire composite with burned area overlay
   D. Pre-fire NBR+ raster
   E. Post-fire NBR+ raster
   F. Burned area mask
```

---

## Requirements

```bash
pip install geemap cartopy earthengine-api
```

| Package         | Purpose                                          |
|-----------------|--------------------------------------------------|
| earthengine-api | Google Earth Engine Python client                |
| geemap          | EE image processing and cartoee map export       |
| cartopy         | Cartographic projections and coordinate systems  |
| matplotlib      | Figure layout, colorbar, and export              |
| numpy           | Numerical operations                             |

---

## Quick Start

```python
import ee
import geemap

ee.Authenticate()
ee.Initialize(project='your-project-id')

# Define AOI
lawu = ee.Geometry.Polygon([[
    [111.17372873826915, -7.647583870310043],
    [111.24342325731212, -7.647583870310043],
    [111.24342325731212, -7.55587155368799],
    [111.17372873826915, -7.55587155368799],
    [111.17372873826915, -7.647583870310043]
]])

# Cloud masking via Cloud Score+
def mask_s2(image):
    cs = image.select('cs_cdf')
    return image.updateMask(cs.gte(0.6))

# Load Sentinel-2 SR and build composites
s2 = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterBounds(lawu)
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
    .linkCollection(ee.ImageCollection('GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED'), ['cs_cdf'])
    .map(mask_s2))

pre_fire  = s2.filterDate('2023-08-01', '2023-08-29').median().clip(lawu)
post_fire = s2.filterDate('2023-10-01', '2023-10-31').median().clip(lawu)

# NBR+ calculation
def calc_nbr_plus(image):
    num = (image.select('B12').subtract(image.select('B8A'))
                              .subtract(image.select('B3'))
                              .subtract(image.select('B2')))
    den = (image.select('B12').add(image.select('B8A'))
                              .add(image.select('B3'))
                              .add(image.select('B2')))
    return num.divide(den).rename('nbr_plus')

nbr_plus_pre  = calc_nbr_plus(pre_fire)
nbr_plus_post = calc_nbr_plus(post_fire)

# Bi-temporal delta and burned area mask
d_nbr_plus = nbr_plus_post.subtract(nbr_plus_pre).rename('d_nbr_plus')
burn_mask  = d_nbr_plus.gte(0.3).selfMask()
```

---

## References

- Alcaras, E., Costantino, D., Guastaferro, F., Parente, C., & Pepe, M. (2022). Normalized Burn Ratio Plus (NBR+): A New Index for Sentinel-2 Imagery. *Remote Sensing*, 14, 1727. https://doi.org/10.3390/rs14071727
- Garcia, M. J. L., & Caselles, V. (1991). Mapping burns and natural reforestation using thematic mapper data. *Geocarto International*, 6(1), 31–37. https://doi.org/10.1080/10106049109354290
- Salsabella, R. I., & Arrofiqoh, E. N. (2024). Mapping the Severity Level of Forest Fire Area in Mount Lawu Using Landsat 9 Imagery. *Journal of Geospatial Information Science and Engineering (JGISE)*, 7(2), 151–160. https://doi.org/10.22146/jgise.100721
- USGS. (2022). *Landsat 9 Data Users Handbook Version 1.0*. NASA.
- Wu, Q. (2020). geemap: A Python package for interactive mapping with Google Earth Engine. *Journal of Open Source Software*, 5(51), 2305. https://doi.org/10.21105/joss.02305
- European Space Agency (ESA). Sentinel-2 Level-2A Surface Reflectance. Copernicus Programme. https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED

---

## License

This project is for academic and research purposes. Sentinel-2 imagery is provided by ESA through the Copernicus programme and is freely available for scientific use.

---

*Last updated: June 2026*
