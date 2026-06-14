"""
Script Name: 02_standard_distance_analysis.py
Description: Calculates the spatial dispersion (Standard Distance) of 
             sustainability initiatives to measure their geographic spread.
"""

import os
import arcpy

def run_standard_distance(input_features, output_shapefile, circle_size):
    """Executes the Standard Distance spatial statistics tool."""
    try:
        # Standard Distance is a core Spatial Statistics tool.
        # Note: No 'Spatial' extension checkout is required here!
        arcpy.env.overwriteOutput = True

        arcpy.AddMessage(f"Calculating spatial dispersion for: {input_features}...")

        # Core Geoprocessing Execution mapped exactly to original parameters
        arcpy.StandardDistance_stats(
            Input_Feature_Class=input_features,
            Output_Standard_Distance_Feature_Class=output_shapefile,
            Circle_Size=circle_size,
            Weight_Field="",  # Unweighted: treats all initiatives equally
            Case_Field=""     # No grouping: calculates one circle for the entire dataset
        )

        arcpy.AddMessage(f"SUCCESS: Standard distance polygon saved to {output_shapefile}")

    except arcpy.ExecuteError:
        # Log specific ArcGIS geoprocessing errors
        arcpy.AddError("ArcPy Geoprocessing Error: " + arcpy.GetMessages(2))
    except Exception as e:
        # Log unexpected Python system/logic errors
        arcpy.AddError(f"Unexpected Script Error: {str(e)}")

if __name__ == "__main__":
    # 1. Standardizing paths dynamically for GitHub reproducibility
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(current_directory, "Outputs", "Spatial_Mean_Center")

    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 2. Map parameters from the original ArcMap export
    # Targeting the SQL view created in Step 1
    INPUT_LAYER = "sustainability_initiatives" 
    
    # Outputting to a .shp as requested in the original script
    OUTPUT_SHP = os.path.join(output_folder, "standard_sustainability.shp")
    
    # 1 Standard Deviation captures approx ~68% of features (if normally distributed)
    CIRCLE_SIZE = "1_STANDARD_DEVIATION"

    # Execute main workflow
    run_standard_distance(INPUT_LAYER, OUTPUT_SHP, CIRCLE_SIZE)
