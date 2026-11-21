---
title: "RasterViz-StandAlone-dekstop-app-for-Windows"
---

[Repositori di GitHub](https://github.com/Defani/RasterViz-StandAlone-dekstop-app-for-Windows)

> 💡 **Background:** This application is developed as a direct evolution and standalone port of the **RasterViz QGIS Python Plugin**. While the original plugin required users to have QGIS installed, this Standalone Edition frees the user from any heavy GIS software dependencies, packing powerful spatial visualization tools into a fast, dedicated desktop environment.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-41CD52?logo=qt&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?logo=python&logoColor=white)
![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?logo=pandas&logoColor=white)
![Rasterio](https://img.shields.io/badge/Rasterio-0052CC?logo=osgeo&logoColor=white)
![Contextily](https://img.shields.io/badge/Contextily-Basemaps-orange)
![Fiona](https://img.shields.io/badge/Fiona-Vector_I%2FO-yellow)
![QtAwesome](https://img.shields.io/badge/QtAwesome-Icons-EA4335)

**RasterViz standalone** Designed for simplicity and speed, it allows users to effortlessly load, style, and compose beautiful, publication-ready maps involving both raster imagery and vector boundaries without the overhead of heavy desktop GIS software.
<img width="1920" alt="Screenshot 2026-07-16 033129" src="https://github.com/user-attachments/assets/700d178c-47ea-484b-a7be-5b57b89a040b" />

## ✨ Key Features

* **🗂️ Interactive Layer Manager:** Drag and drop to reorder raster and vector layers in real-time.
* **🛰️ Raster Rendering:** Support for single-band (continuous & discrete) and RGB composite imagery.
* **🗺️ Vector Symbology:** Render shapefiles, KML, and GeoPackages with customizable fill, stroke, and categorized colors.
* **🌐 Dynamic Basemaps:** Instantly overlay your data on top of Esri, OpenStreetMap, or CartoDB basemaps.
* **📐 Cartographic Tools:** Built-in coordinate grid, scale bars (simple & alternating), and dynamic north arrows.
* **🌙 Dark / Light Mode:** Eye-friendly UI themes tailored for long hours of spatial analysis.
* **📸 High-Quality Export:** Save your map compositions as high-resolution PNG, TIFF, SVG, or PDF files.

---

## 🚀 How to Run from Source

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Defani/RasterViz.git](https://github.com/Defani/RasterViz.git)
   cd RasterViz

```

2. **Create and activate a virtual environment (optional but recommended):**
```bash
python -m venv build_venv
# Windows
build_venv\Scripts\activate
# Linux/Mac
source build_venv/bin/activate

```


3. **Install the dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the application:**
```bash
cd app
python main.py

```



---

## 📦 Compiling into a Permanent App (.exe)

You can compile RasterViz into a permanent, standalone Windows executable using **PyInstaller**. This allows you to run the application on any computer without needing to install Python or the required libraries.

1. Ensure you have PyInstaller and the necessary hooks installed in your environment:
```bash
pip install pyinstaller pyinstaller-hooks-contrib

```


2. Navigate to the root directory of the project and run the following command:
```bash
pyinstaller --noconsole --name="RasterViz" --windowed --icon="app/icon.png" --add-data="app/icon.png;." app/main.py

```


*Note: Because geospatial libraries (like `rasterio`, `fiona`, and `pyproj`) require extensive underlying C-libraries and PROJ data dictionaries, compiling them might require specific `.spec` file modifications to ensure all coordinate system data is bundled correctly.*
3. Once compiled, your executable will be located in the newly created `dist/RasterViz` folder. You can create a shortcut of `RasterViz.exe` to your desktop!

---

## 🙏 Acknowledgments & Credits

This application exists because of the monumental efforts of the open-source GIS and Python community. A massive thank you to the developers and maintainers of the following libraries:

* **[PyQt5](https://riverbankcomputing.com/software/pyqt/)**: For providing a rock-solid, cross-platform GUI framework.
* **[Matplotlib](https://matplotlib.org/)**: The backbone of our map rendering, turning raw arrays into beautiful cartography.
* **[Rasterio](https://rasterio.readthedocs.io/)** & **[GDAL](https://gdal.org/)**: For fast, efficient, and Pythonic reading of geospatial raster data.
* **[GeoPandas](https://geopandas.org/)** & **[Fiona](https://fiona.readthedocs.io/)**: For making vector data manipulation and rendering incredibly intuitive.
* **[Contextily](https://contextily.readthedocs.io/)**: For seamlessly retrieving and plotting web map tiles (basemaps).
* **[NumPy](https://numpy.org/)**: For the blazingly fast array operations required in image processing.
* **[QtAwesome](https://github.com/spyder-ide/qtawesome)**: For providing beautiful, scalable UI icons.

*Special thanks to the global open-source community for continuing to democratize geospatial technology.*

---

**Author:** Defani Arman Alfitriansyah

**License:** MIT License
