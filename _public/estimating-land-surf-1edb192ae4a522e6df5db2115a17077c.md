---
title: "ESTIMATING-LAND-SURFACE-TEMPERATURE-FROM-LANDSAT-8-SURFACE-REFLECTANCE-USING-R"
---

[Repositori di GitHub](https://github.com/Defani/ESTIMATING-LAND-SURFACE-TEMPERATURE-FROM-LANDSAT-8-SURFACE-REFLECTANCE-USING-R)

This study estimates Land Surface Temperature (LST)  using Landsat 8 Collection 2 Level-2 Surface Reflectance (SR) data, particularly Thermal Infrared Sensor (TIRS) Band 10. Unlike Top of Atmosphere (TOA) products, which require multiple preprocessing steps—including conversion to radiance, brightness temperature, and often emissivity correction using NDVI—the SR product provides a Surface Temperature band (ST_B10) that is already atmospherically corrected. Therefore, the LST can be directly derived without involving NDVI.
The conversion from digital numbers to temperature in Celsius was performed using the calibration formula:

LST(∘C)=(DN×0.00341802+149.0)−273.15

To ensure physical consistency, values outside the realistic thermal range (–50 °C to 80 °C) were masked. The data processing was conducted in R programming language with the terra package, which enables efficient handling of raster data.

By utilizing SR-based LST, this analysis highlights spatial temperature variation at the local scale, offering valuable insights into land–atmosphere interactions, microclimate assessment, and environmental monitoring. The approach demonstrates the advantage of SR products in simplifying the LST workflow compared to TOA imagery, while still ensuring scientifically robust results.
