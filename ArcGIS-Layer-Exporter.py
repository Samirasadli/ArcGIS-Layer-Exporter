import arcpy
import os

# Set the path to the folder where you want to save the .lyrx files
output_folder = r"C:\Users\samir\OneDrive\Masaüstü\New folder (2)\Layer"

# Get the current ArcGIS Pro project
project = arcpy.mp.ArcGISProject("CURRENT")

# Get the active map
active_map = project.activeMap

# Make sure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each layer in the active map
for layer in active_map.listLayers():
    # Check if the layer can be exported (it should be a valid feature or raster layer)
    if layer.isFeatureLayer or layer.isRasterLayer:
        # Define the output path for the .lyrx file
        output_path = os.path.join(output_folder, f"{layer.name}.lyrx")

        try:
            # Export the layer's symbology as a .lyrx file
            layer.saveACopy(output_path)
            print(f"Exported {layer.name} to {output_path}")
        except Exception as e:
            print(f"Error exporting {layer.name}: {e}")

print("Layer symbology exported successfully!")
