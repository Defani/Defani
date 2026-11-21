---
title: "Water-Body-Extraction-Workflow-Using-R-and-Sentinel-2-Imagery"
---

[Repositori di GitHub](https://github.com/Defani/Water-Body-Extraction-Workflow-Using-R-and-Sentinel-2-Imagery)

This workflow demonstrates the extraction of water bodies from Sentinel-2 imagery using the Normalized Difference Water Index (NDWI). By combining the green band (B3), where water reflects strongly, with the near-infrared band (B8), where water has low reflectance, NDWI enhances aquatic features while suppressing vegetation and soil. The index is calculated as (Green – NIR) / (Green + NIR), and applying a threshold (0.001) produces a binary water mask that clearly delineates hydrological surfaces.


The analysis was conducted in R with the terra package (Hijmans, 2025) for raster processing and RColorBrewer (Neuwirth, 2022) for visualization. NDWI has proven to be an efficient and widely adopted method in remote sensing for water mapping, wetland monitoring, and hydrological studies, with potential applications in turbidity assessment (McFeeters, 1996).


Reference:

McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. International Journal of Remote Sensing, 17(7), 1425–1432. https://lnkd.in/gvZWDHpc

Hijmans R (2025). terra: Spatial Data Analysis. R package version 1.8-62, https://lnkd.in/g9uAMRGW.

Neuwirth, E. (2022). RColorBrewer: ColorBrewer Palettes. R package version 1.1-3. https://lnkd.in/gSfvvGdG
