"""
Script Name: 02_directional_distribution.py
Description: Automates the calculation of a Standard Deviational Ellipse (SDE)
             to measure the geographic trend and orientation of features.
"""

import os
import arcpy

def calculate_directional_trend(input_features, output_ellipse, ellipse_size):
    """Executes the Directional Distribution spatial statistics tool."""
    try:
        # Overwrite outputs if they already exist
        arcpy.env.overwriteOutput = True

        arcpy.AddMessage(f"Analyzing directional distribution for: {input_features}")

        # Core Geoprocessing Execution mapped to your original parameters
        arcpy.StandardDistance_stats(
            Input_Feature_Class=input_features,
            Output_Standard_Distance_Feature_Class=output_ellipse, # Generates the .shp geometry
            Circle_Size=ellipse_size,                              # 1 Standard Deviation
            Weight_Field="",                                       # Unweighted analysis
            Case_Field=""                                          # Single global ellipse
        )

        # Alternative alias call based on your exact script preference:
        # arcpy.DirectionalDistribution_stats(input_features, output_ellipse, ellipse_size, "", "")

        arcpy.AddMessage(f"SUCCESS: Standard Deviational Ellipse saved to {output_ellipse}")

    except arcpy.ExecuteError:
        # Catch and surface ArcGIS geoprocessing faults
        arcpy.AddError("ArcPy Geoprocessing Error: " + arcpy.GetMessages(2))
    except Exception as e:
        # Catch regular Python system/syntax faults
        arcpy.AddError(f"Unexpected Script Error: {str(e)}")

if __name__ == "__main__":
    # Standardizing paths dynamically for effortless repository deployment
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_directory, "Outputs", "Spatial_Statistics")

    # Safeguard directory creation
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Variables mapped from your original environment setup
    INPUT_LAYER = "sustainability_initiatives_sde" # Matches the enterprise SQL view
    OUTPUT_SHP = os.path.join(output_dir, "ellipse_sustainability.shp")
    ELLIPSE_SIZE = "1_STANDARD_DEVIATION"

    # Execute main workflow
    calculate_directional_trend(INPUT_LAYER, OUTPUT_SHP, ELLIPSE_SIZE)
