# ArcGIS-Layer-Exporter
# ArcGIS Pro Layer Symbology Exporter

This repository contains a Python script that automates the export of symbology for all layers in an ArcGIS Pro map to `.lyrx` files. This tool is particularly useful when managing or sharing layer symbology between projects or team members.

## Project Overview

The script iterates through all the layers in a specified map from an ArcGIS Pro project and exports their symbology to individual `.lyrx` files. It works for both feature and raster layers, making it a flexible solution for various mapping projects.

### Key Features:
- Exports symbology for all feature and raster layers in the map.
- Saves symbology in the `.lyrx` format for easy reuse.
- Supports ArcGIS Pro projects.

## How to Use

1. Clone this repository or download the Python script.
2. Make sure you have **ArcGIS Pro** installed, as well as access to **ArcPy**.
3. Update the file paths in the script:
   - Set the path to your ArcGIS Pro project (`.aprx`).
   - Specify the output folder where the `.lyrx` files should be saved.
4. Run the script from ArcGIS Pro’s Python window or your Python environment that has ArcGIS Pro and ArcPy installed.


## Purpose of this Script

This script was created as part of my work with ArcGIS Pro to streamline the process of exporting layer symbology. The main goal was to simplify symbology management for projects that involve multiple layers or need consistent symbology across various projects.

## Acknowledgments

I developed this script with the help of AI tools, which provided guidance and assisted me in streamlining the workflow.

## License

Feel free to use and modify the script according to your needs. If you find it useful, a star on this repository would be appreciated!
