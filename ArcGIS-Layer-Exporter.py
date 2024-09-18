import arcpy
import os

# Set the project and map variables
project_path = r"C:\path\to\your\ArcGISProject.aprx"  # Update with the actual path to your ArcGIS Pro project
output_folder = r"C:\path\to\output\folder"  # Update with the folder where you want to save the .lyrx files

# Load the ArcGIS Pro project
aprx = arcpy.mp.ArcGISProject(project_path)

# Access the map (replace 'Map' with your map's actual name)
map_name = 'Map'  # Change this to the name of your map in the project
map_obj = aprx.listMaps(map_name)[0]

# Loop through each layer in the map
for layer in map_obj.listLayers():
    if layer.isFeatureLayer or layer.isRasterLayer:  # Ensure it works for feature and raster layers
        # Set the output path for the layer's .lyrx file
        output_path = os.path.join(output_folder, f"{layer.name}.lyrx")
        
        # Export the layer symbology to a .lyrx file
        layer.saveACopy(output_path)
        print(f"Saved {layer.name} symbology to {output_path}")

# Clean up
del aprx
