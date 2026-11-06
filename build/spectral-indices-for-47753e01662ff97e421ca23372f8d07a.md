---
title: "Spectral-Indices-For-Vegetation"
---

[Repositori di GitHub](https://github.com/Defani/Spectral-Indices-For-Vegetation)

The Normalized Difference Vegetation Index (NDVI) is one of the most fundamental tools in remote sensing for analyzing vegetation health and distribution. First introduced by Rouse et al. (1974), NDVI has been widely applied to monitor vegetation dynamics by leveraging spectral differences between the red and near-infrared bands. Its simplicity, effectiveness, and scalability make it highly valuable for ecological monitoring and forest management. In the context of forestry, NDVI provides essential insights into canopy density, forest degradation, and ecosystem health, supporting evidence-based decision-making in conservation and sustainable land use.

In this project, NDVI analysis was implemented using Google Earth Engine (GEE), a cloud-based geospatial processing platform that allows rapid analysis of large-scale Earth observation data. Sentinel-2 imagery was selected as the primary dataset, offering high-resolution multispectral information suitable for vegetation studies. Data preprocessing included filtering for low cloud coverage, applying scene classification (SCL) masks to remove unwanted pixels such as clouds and shadows, and mosaicking imagery across the study period to produce a clean composite. This approach ensured reliable input data for NDVI calculation.

The NDVI computation followed the classical equation proposed by Rouse et al. (1974):


	​


where the near-infrared (Band 8) and red (Band 4) bands of Sentinel-2 were utilized. Vegetation typically exhibits strong reflectance in the NIR spectrum while absorbing in the red spectrum, making NDVI a robust measure of vegetation vigor. The resulting index was mapped with a color gradient ranging from brownish tones for sparse or stressed vegetation to vibrant green shades for dense and healthy forest cover. Such visualization is highly useful for identifying critical areas in need of restoration or conservation interventions.

Beyond the computation itself, GEE enabled the integration of multiple processing steps, including raster clipping, thresholding, and exporting analysis outputs directly to Google Drive for further interpretation. Binary classification was also performed by applying threshold values to NDVI results, following principles of digital image processing described by Gonzalez & Woods (2018). This classification approach allowed the distinction between vegetation and non-vegetation classes, a necessary step for quantifying forest cover or monitoring land cover changes.

The analysis demonstrated that NDVI derived from GEE provides powerful insights into mangrove distribution and general vegetation health within the study area. Mangroves, in particular, exhibited distinct spectral responses that allowed them to be differentiated in false-color composites. Such outputs are not only beneficial for ecological research but also have practical implications in supporting sustainable forestry programs, coastal ecosystem management, and climate change adaptation strategies.

From a broader perspective, this project reflects the growing significance of cloud-based geospatial platforms in forestry research and practice. Traditional desktop-based GIS tools often face challenges when handling large datasets, whereas GEE provides scalability, accessibility, and computational efficiency. For a forestry student specializing in GIS and remote sensing, the integration of NDVI analysis with GEE highlights the ability to combine ecological theory with cutting-edge technological approaches. This ensures that monitoring and management efforts are not only scientifically rigorous but also practical and reproducible across different regions and timeframes.

Ultimately, this project illustrates how NDVI, as one of the earliest and most widely applied vegetation indices, continues to play a central role in modern forest monitoring. By combining the foundational methods established by Rouse et al. (1974) with advanced digital image processing principles (Gonzalez & Woods, 2018) and the computational power of GEE, vegetation analysis becomes more accurate, efficient, and impactful for conservation and sustainable land management.

📖 References

Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1974). Monitoring vegetation systems in the Great Plains with ERTS. NASA SP-351, 309–317.
