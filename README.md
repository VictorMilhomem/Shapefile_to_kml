# Shapefile to KML Converter

This script converts a shapefile to a KML (Keyhole Markup Language) file. It utilizes the `geopandas` and `simplekml` libraries to read the shapefile and create the corresponding KML file.

## Usage

### Option 1: Using the Command Line
1. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```


2. Run the script using the following command:
```
python convert.py --shapefile <path_to_shapefile> --kmlfile <output_kml_path>
```


Replace `<path_to_shapefile>` with the path to the input shapefile you want to convert, and `<output_kml_path>` with the desired path and filename for the output KML file.

## Arguments

- `--shapefile`: Path to the input shapefile (required).
- `--kmlfile`: Path to the output KML file (optional). If not provided, the script will save the output KML file as `output.kml` in the current directory.

## Example

To convert a shapefile named `input.shp` to a KML file named `output.kml`, run the following command:


Replace `<path_to_shapefile>` with the path to the input shapefile you want to convert, and `<output_kml_path>` with the desired path and filename for the output KML file.

## Arguments

- `--shapefile`: Path to the input shapefile (required).
- `--kmlfile`: Path to the output KML file (optional). If not provided, the script will save the output KML file as `output.kml` in the current directory.

## Example

To convert a shapefile named `input.shp` to a KML file named `output.kml` using the command line, run the following command:

### Option 2: Using a Notebook

1. Use (Google Colab)[https://colab.research.google.com/]

2. Open the `Convert_Shapefile_to_Kml.ipynb` notebook file in Colab.

3. Replace the placeholder values with the path to the input shapefile and the desired output KML path.

4. Execute the notebook cells to convert the shapefile to KML. The resulting KML file will be saved at the specified output path.


## License

This script is licensed under the [MIT License](LICENSE).
Feel free to customize the instructions and add any additional information as per your requirements.
