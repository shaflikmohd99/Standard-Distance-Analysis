# Spatial Pattern Analysis (Standard Distance, Standard Deviational Ellipse and Mean Center)

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

# GIS Spatial Statistics: Standard Deviational Ellipse Analysis

Directional Distribution (Standard Deviational Ellipse) builds an ellipse that shows both the dispersion and the geographic orientation/trend of your data (e.g., whether sustainability initiatives are stretching along a specific transit corridor or river basin).

This repository contains an automated script using the ArcGIS Spatial Statistics toolbox to calculate the **Directional Distribution (Standard Deviational Ellipse)** of spatial features. 

While basic spatial statistics identify central points or generic dispersion distances, Directional Distribution calculates the exact rotation angle, elongation, and orientation of features. This allows analysts to determine if a spatial pattern is pulling along a specific geographic axis (e.g., following highways, coastlines, or urban expansion trends).

## 🛠️ Tool Configuration
The script utilizes the `DirectionalDistribution_stats` geoprocessing tool with the following specific configurations:
* **Ellipse Size:** `1_STANDARD_DEVIATION` (The resulting ellipse encompasses approximately 68% of the input data points, mapping the primary core area of spatial orientation).
* **Weight Field:** `None` (Spatial coordinates are evaluated purely on location density without financial or size bias).
* **Case Field:** `None` (Calculates a single dominant regional axis rather than breaking it down into sub-groups).

## 🚀 How to Use
1. Clone this repository to your local machine.
2. Open the script and modify the `INPUT_LAYER` variable to target your point data view.
3. Run the script via your ArcGIS Python environment:
   ```bash
   python 02_directional_distribution.py
