---
title: 'Exploring Mangrove Mapping with Sentinel-2 and Threshold-Based Classification'
date: 2025-03-29
tags: ['mangrove-indonesia', 'remote-sensing', 'mangrove', 'sentinel']
---

29 March 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/exploring-mangrove-mapping-with-sentinel-2-and-threshold-based-classification-8075288c98dc) · [Semua tulisan](../blog.md)

I am currently learning remote sensing and experimenting with different approaches for land cover analysis. In this exploration, I used Sentinel-2 imagery to distinguish mangroves based on their spectral characteristics.

### Step 1: Acquiring Sentinel-2 Imagery

First, I obtained Sentinel-2 imagery from the Copernicus Open Access Hub. The selected image covers the area of interest during a season with minimal cloud cover to ensure high-quality data.

[Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=5&lat=50.16282&lng=20.78613&demSource3D=%22MAPZEN%22&cloudCoverage=30&dateMode=SINGLE)

### Step 2: Applying Band Composition

To enhance mangrove visibility, I applied an 8–11–4 composite (NIR-SWIR-Red).

![](https://cdn-images-1.medium.com/max/1024/1*ZVSrKcpN0hWrssbpVopVIg.jpeg)

Band 8 (NIR) highlights vegetation. Band 11 (SWIR) differentiates moisture content. Band 4 (Red) helps detect vegetation stress. In this composite, mangroves appear orange, but with varying brightness levels. This spectral difference provided a way to separate mangroves from other vegetation.

### Step 3: Calculating Spectral Indices

To further enhance the distinction of mangroves, I calculated two key indices using the following formulas:

NDMI (Normalized Difference Moisture Index):

The **Normalized Difference Moisture Index (NDMI)** is an extension of NDVI, designed to assess the **water content in vegetation**. It was originally proposed by **Gao (1996)** and utilizes the **Near-Infrared (NIR)** and **Shortwave Infrared (SWIR)** bands

> “NDWI index is often used synonymously with the NDMI index, often using NIR-SWIR combination as one of the two options. Gao, referenced above, also called the index NDWI. NDMI seems to be consistently described using NIR-SWIR combination. As the indices with these two combinations work very differently, with NIR-SWIR highlighting differences in water content of leaves, and GREEN-NIR highlighting differences in water content of water bodies, we have decided to separate the indices on our repository as NDMI using NIR-SWIR, and NDWI using GREEN-NIR” (sentinelhub.com)

![](https://cdn-images-1.medium.com/max/1024/1*Qrzqg0esKXhpCScVrqHNrQ.jpeg)

    NDMI = (B8 - B11) / (B8 + B11)

### NDVI (Normalized Difference Vegetation Index):

The **Normalized Difference Vegetation Index (NDVI)** is a widely used remote sensing index that measures vegetation health and biomass. It was first introduced by **Rouse et al. (1974)** as a way to monitor plant growth and ecosystem dynamics using satellite imagery. NDVI is calculated using the reflectance values of the **Near-Infrared (NIR)** and **Red** bands:

Where: **NIR (Near-Infrared, ~0.76–0.9 µm):** Strongly reflected by healthy vegetation. **Red (~0.63–0.69 µm):** Strongly absorbed by chlorophyll in plants. NDVI values range from **-1 to +1**:

![](https://cdn-images-1.medium.com/max/1024/1*ZYPWu_vuuIMmOpko4JpubQ.jpeg)

    NDVI = (B8 - B4) / (B8 + B4)

### Step 4: Applying Threshold-Based Classification

Using the Raster Calculator in ArcGIS, I classified mangrove areas using the following conditional formula:

    Con((NDMI > 0.2) & (NDVI > 0.3) & ((B8 / B11) > 1.2), 1, 0)

NDMI \> 0.2 identifies moisture-rich vegetation. NDVI \> 0.3 ensures that the area is covered with vegetation. NIR/SWIR Ratio (B8 / B11) \> 1.2 distinguishes mangroves from other vegetation types.

![](https://cdn-images-1.medium.com/max/1024/1*9gQptswKeFhmNhfDDuP80w.jpeg)

### Step 5: Visualizing the Results

After classification, I overlaid the results on the Sentinel-2 imagery to validate the extracted mangrove areas. The classified map effectively separated mangrove and non-mangrove regions.

![](https://cdn-images-1.medium.com/max/1024/1*W-foK5VN3CezBQZ2iWso_g.jpeg)

### References

Gao, B.-C. (1996). “NDWI — A normalized difference water index for remote sensing of vegetation liquid water from space.” *Remote Sensing of Environment, 58(3), 257–266.* <https://doi.org/10.1016/S0034-4257(96)00067-3>

Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1974). “Monitoring vegetation systems in the Great Plains with ERTS.” *Proceedings of the Third Earth Resources Technology Satellite (ERTS) Symposium, Volume 1*, 309–317.

Sentinel Hub Custom Scripts. “NDMI — Normalized Difference Moisture Index.” *Sentinel Hub*, <https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndmi/>

### .
