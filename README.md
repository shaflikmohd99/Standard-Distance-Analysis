# Spatial Pattern Analysis (Standard distance, Standard Deviational Ellipse and Mean Center)

# GIS Spatial Statistics: Standard Distance Analysis
One of spatial pattern analysis which is standard distance analysis. This tools measures a spatial dispersion (how spread out your data is around its center).

This repository automates the calculation of **Standard Distance** for Sustainability Initiatives using the ArcGIS Spatial Statistics toolbox. 

While the Mean Center identifies the geographic center of a dataset, the Standard Distance polygon visualizes spatial **dispersion**—showing exactly how clustered or widespread the sustainability projects are around that central point.

## 🛠️ Tool Configuration
The script utilizes the `StandardDistance_stats` tool with the following configurations:
* **Circle Size:** `1_STANDARD_DEVIATION` (Calculates a polygon that encompasses approximately 68% of all spatial features, assuming a normal spatial distribution).
* **Weight Field:** `None` (All sustainability initiatives are treated equally, regardless of budget or size).
* **Case Field:** `None` (Generates a single comprehensive dispersion circle for the entire city/region, rather than grouping by neighborhood).

## 🚀 How to Use
1. Clone this repository to your local machine.
2. Open the script and modify the `INPUT_LAYER` variable to point to your local point dataset.
3. Run the script via your ArcGIS Python environment:
   ```bash
   python 02_standard_distance_analysis.py
