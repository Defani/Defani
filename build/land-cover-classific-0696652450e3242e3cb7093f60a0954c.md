---
title: "Land-Cover-Classification-Using-Random-Forest"
---

[Repositori di GitHub](https://github.com/Defani/Land-Cover-Classification-Using-Random-Forest)

This study demonstrates a Random Forest (RF) workflow implemented in R to map land cover from multispectral satellite imagery. The analysis combines spectral bands (NIR, SWIR, RED) and NDVI (Rouse et al., 1973) as predictors with polygon training samples to produce a detailed, spatially explicit land cover map. Raster layers in GeoTIFF (.tif) format were aligned and resampled using terra (Hijmans, 2025), while training polygons from ESRI Shapefile (.shp) were transformed and centroids extracted with sf (Pebesma & Bivand, 2023). A Random Forest model with 500 trees (randomForest, Liaw & Wiener, 2002) was trained to classify the raster stack. 

The output was visualized with a custom color palette, north arrow, scale bar, and gridlines using ggplot2 (Wickham, 2016), tidyterra (Hernangómez, 2023), ggspatial (Dunnington, 2025), and scales (Wickham et al., 2025), and exported as a high-resolution PNG. This workflow demonstrates a reproducible, machine learning-driven approach to land cover mapping, integrating spectral indices, geospatial processing, and visualization entirely within R.

References:
Dunnington, D. (2025). ggspatial: Spatial data framework for ggplot2 (R package version 1.1.10). https://lnkd.in/dCMEcQDW

Hernangómez, D. (2023). Using the tidyverse with terra objects: the tidyterra package. Journal of Open Source Software, 8(91), 5751. https://lnkd.in/dYiXTpRe

Hijmans, R. J. (2025). terra: Spatial data analysis (R package version 1.8-62). https://lnkd.in/g9uAMRGW

Liaw, A., & Wiener, M. (2002). Classification and regression by randomForest. R News, 2(3), 18–22. https://lnkd.in/da5eey5f

Pebesma, E., & Bivand, R. (2023). Spatial data science: With applications in R. Chapman and Hall/CRC. https://lnkd.in/dtX8x6_e

R Core Team (2024). R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria.

Rouse, J.W., Haas, R.H., Schell, J.A., & Deering, D.W. (1973). Monitoring Vegetation Systems in the Great Plains with ERTS (Earth Resources 
Technology Satellite). Proceedings of 3rd Earth Resources Technology Satellite Symposium, Greenbelt, 10–14 December, SP-351, 309–317.

Wickham, H. (2016). ggplot2: Elegant graphics for data analysis. Springer-Verlag New York. ISBN 978-3-319-24277-4. https://lnkd.in/d_NJ4zNx

Wickham, H., Pedersen, T. L., & Seidel, D. (2025). scales: Scale functions for visualization (R package version 1.4.0). https://scales.r-lib.org
