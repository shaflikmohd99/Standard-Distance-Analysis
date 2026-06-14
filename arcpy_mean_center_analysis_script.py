"""
Script Name: 02_mean_center_analysis.py
Description: Automates the calculation of the spatial Mean Center (center of gravity) 
             for sustainability initiatives using the core Spatial Statistics toolbox.
"""

import os
import arcpy

def calculate_mean_center(input_features, output_feature_class):
    """Executes the Mean Center spatial statistics tool."""
    try:
        # Overwrite outputs if they already exist from a previous run
        arcpy.env.overwriteOutput = True

        arcpy.AddMessage(f"Calculating spatial center of gravity for: {input_features}...")

        # Core Geoprocessing Execution (Mapped exactly to original parameters)
        # Note: No 'Spatial' extension checkout is required for this toolbox!
        arcpy.MeanCenter_stats(
            Input_Feature_Class=input_features,
            Output_Feature_Class=output_feature_class,
            Weight_Field="",    # Unweighted: Calculates purely based on geographic location
            Case_Field="",      # Global: Calculates one central point for all data
            Dimension_Field=""  # 2D analysis (ignores Z-values/elevation)
        )

        arcpy.AddMessage(f"SUCCESS: Mean Center point saved to {output_feature_class}")

    except arcpy.ExecuteError:
        # Catch and log specific ArcGIS geoprocessing faults
        arcpy.AddError("ArcPy Geoprocessing Error: " + arcpy.GetMessages(2))
    except Exception as e:
        # Catch regular Python system/syntax faults
        arcpy.AddError(f"Unexpected Script Error: {str(e)}")

if __name__ == "__main__":
    # Standardizing paths dynamically for GitHub repository cloning
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_directory, "Outputs", "Spatial_Mean_Center")

    # Safely create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Variables mapped from original environment setup
    INPUT_LAYER = "sustainability_initiatives_mc"  # Matches the enterprise SQL view
    OUTPUT_SHP = os.path.join(output_dir, "mean_center_sustainability.shp")

    # Execute main workflow
    calculate_mean_center(INPUT_LAYER, OUTPUT_SHP)
