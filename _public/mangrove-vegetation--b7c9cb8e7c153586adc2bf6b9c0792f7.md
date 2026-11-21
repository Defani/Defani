---
title: "Mangrove-Vegetation-Index-Using-Terra-Package"
---

This repository provides a complete workflow for mapping mangrove forests using  MVI and Sentinel-2A imagery in R.

[Repositori di GitHub](https://github.com/Defani/Mangrove-Vegetation-Index-Using-Terra-Package)

This repository provides a complete workflow for mapping mangrove forests using Sentinel-2A imagery in R. The analysis applies the Mangrove Vegetation Index (MVI), a spectral index specifically developed to improve mangrove detection compared to general vegetation indices such as NDVI (Baloloy et al., 2020). In addition, the classification process follows the principle of global thresholding, a fundamental image segmentation technique as described by Gonzalez and Woods (2018).


The workflow includes the following steps:

Loading Sentinel-2 Bands
The key bands required for MVI are Band 8 (NIR), Band 3 (Green), and Band 11 (SWIR). These files are stored in GeoTIFF format and read into R using the terra::rast() function.

False-Color Composite Visualization
A false-color composite (NIR–SWIR–Green) is generated to visualize mangrove vegetation, which typically appears in orange to brown tones. This provides a quick way to inspect potential mangrove areas before index calculation.

Calculation of Mangrove Vegetation Index (MVI)
The index is computed using the formula:

$$
MVI = \frac{NIR - Green}{SWIR - Green}
$$


This highlights the spectral contrast between mangroves and other vegetation.

Threshold Classification
Following Baloloy et al. (2020), a threshold value of 3.5 is applied to the MVI layer. Pixels with MVI ≥ 3.5 are classified as Mangrove, while those below the threshold are classified as Non-Mangrove. This approach is based on the global thresholding method, which separates objects from background using a single cut-off value (Gonzalez & Woods, 2018).
According to **Gonzalez and Woods (2018)**, the binary classification process can be represented mathematically as:

According to **Gonzalez and Woods (2018)**, the binary classification process can be represented mathematically as:

$$
g(x,y) =
\begin{cases}
1 & \text{if } I(x,y) \geq T \\
0 & \text{if } I(x,y) < T
\end{cases}
$$


Final Mapping and Area Calculation
The classified raster is visualized with clear labels and colors (green = mangrove, white = non-mangrove). Pixel counts are converted to hectares (1 pixel = 0.01 ha for Sentinel-2 at 10 m resolution), producing a summary of mangrove extent.

All processing steps are carried out with the terra
 package, which provides fast and efficient handling of raster data. The scripts included in this repository are reproducible and can be easily adapted for different regions or datasets.

References

Baloloy, A. B., Blanco, A. C., Sta. Ana, R. R. C., & Nadaoka, K. (2020). Development and Application of a New Mangrove Vegetation Index (MVI) for Rapid and Accurate Mangrove Mapping. ISPRS Journal of Photogrammetry and Remote Sensing, 166, 95–117. https://doi.org/10.1016/j.isprsjprs.2020.06.001

Gonzalez, R. C., & Woods, R. E. (2018). Digital Image Processing. New York, NY: Pearson.
