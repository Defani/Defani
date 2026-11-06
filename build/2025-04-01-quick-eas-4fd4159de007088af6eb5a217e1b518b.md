---
title: 'Quick & Easy DEM Download in QGIS with OpenTopography Plugin'
date: 2025-04-01
tags: ['topographic-maps', 'qgis', 'gis', 'dem']
---

01 April 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/quick-easy-dem-download-in-qgis-with-opentopography-plugin-a87194614103) · [Semua tulisan](../blog.md)

Need Digital Elevation Model data for your GIS projects? Stop searching endlessly! The **OpenTopography DEM Downloader** plugin in QGIS makes downloading Digital Elevation Models (DEMs) quick, easy, and hassle-free. Whether you’re analyzing terrain, modeling watersheds, or working on remote sensing applications, this plugin streamlines the entire process — letting you focus on your analysis instead of wrestling with data sources.

Follow this step-by-step guide and start accessing top-tier elevation data in just a few clicks!

### Prerequisites

Before you begin, make sure you have: **QGIS installed** (latest version recommended), **active internet connection, and OpenTopography API Key** (required for downloading DEMs)

### Request API Key

Before using the plugin, you need to obtain an API key from OpenTopography. This step is only required the first time you install and set up the plugin — after that, your API key will be saved for future use.

1.  Go to [**OpenTopography API Key Request**](https://portal.opentopography.org/login?redirect=%2FrequestService%3Fservice%3Dapi).
2.  Log in or create a free account.
3.  Generate your API key and copy it for later use.

![](https://cdn-images-1.medium.com/max/1024/1*oSTZPRW_27Uv7tELw9rssQ.png)

Visit link : <https://portal.opentopography.org/login?redirect=%2FrequestService%3Fservice%3Dapi>

![](https://cdn-images-1.medium.com/max/1024/1*gx30vYNQ2JVwrr8OIqg5XA.png)

Create free account for request API Key

### Install the OpenTopography DEM Downloader Plugin

1.  Open **QGIS**.
2.  Navigate to **Plugins** \> **Manage and Install Plugins**.
3.  In the search bar, type [**OpenTopography DEM Downloader**.](https://portal.opentopography.org/login?redirect=%2FrequestService%3Fservice%3Dapi)

![](https://cdn-images-1.medium.com/max/1024/1*i9d_VhJSpJXADgiPUxRSTw.png)

### Launch the Plugin

1.  Once installed, open the plugin from the **menu bar** at the top of QGIS.
2.  Alternatively, click on **Raster** \> **OpenTopography DEM Downloader**.
3.  A user-friendly window will appear, allowing you to select your area of interest (AOI) and DEM dataset.
4.  Enter your **OpenTopography API Key** to activate downloads.

![](https://cdn-images-1.medium.com/max/1024/1*r9PJ0-38eB0A9GQBikSDEg.png)

### Define Your Area of Interest

1.  Choose your AOI using one of these methods:

- Manually input **latitude and longitude** coordinates.
- Use the **Select on Map** tool to define your desired area visually.
- If you have an uploaded shapefile of your study area, use **Calculate from Layer** for precise selection.

![](https://cdn-images-1.medium.com/max/1024/1*HGuFOrP0JdF8bxvJ_zsDiQ.png)

2\. Pick from a variety of high-quality DEM datasets, including

![](https://cdn-images-1.medium.com/max/1024/1*IP_92t3UBnAWqn73SCFEsg.png)

Including SRTM (90m & 30m), ALOS World 3D (30m), SRTM GL1 Ellipsoidal (30m), Global Bathymetry SRTM15+ V2.1, Copernicus Global DSM (30m & 90m), NASADEM Global DEM, Europe DTM (30m), GEDI L3 Grid (1km), GEBCOIceTopo Bathymetry (500m), and GEBCOSubIceTopo Bathymetry (500m).

3\. Select your preferred **output format**

4\. Click “Run” and let the magic happen!

### Load and Visualize Your DEM in QGIS

![](https://cdn-images-1.medium.com/max/1024/1*EK7QCQpSIIkX1KdzexrPpg.png)

![](https://cdn-images-1.medium.com/max/1024/1*NDph4XsNQ0XDV7SJ_U2n9w.png)

![](https://cdn-images-1.medium.com/max/1024/1*VepiQaotqK08eyKXVMqsdw.jpeg)

### References

[opentopography.org](https://opentopography.org/)

[QGIS Plugin](https://plugins.qgis.org/plugins/OpenTopography-DEM-Downloader/)
