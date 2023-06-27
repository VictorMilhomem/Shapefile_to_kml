import geopandas as gpd
import simplekml
import argparse

def shapefile_to_kml(shapefile_path=None, output_kml_path=None):
    if shapefile_path==None: raise ValueError("None Type as Shapefile path.")
    if output_kml_path==None: output_kml_path = "./output.kml"
    gdf = gpd.read_file(shapefile_path)

    kml = simplekml.Kml()

    for index, row in gdf.iterrows():
        geom = row['geometry']
        kml_geom = geom.__geo_interface__

        geometry_type = kml_geom['type']
        field_name = gdf.columns[0]
        placemark = kml.newmultigeometry(name=row[field_name])
        if geometry_type == 'Point':
            coordinates = kml_geom['coordinates']
            placemark.newpoint(coords=[coordinates])
        elif geometry_type == 'LineString':
            coordinates = kml_geom['coordinates']
            linestring = placemark.newlinestring()
            linestring.coords = coordinates
        elif geometry_type == 'Polygon':
            coordinates = kml_geom['coordinates'][0]
            polygon = placemark.newpolygon()
            polygon.outerboundaryis = coordinates

        for field in gdf.columns:
            if field != 'geometry':
                value = str(row[field])
                placemark.extendeddata.schemadata.newsimpledata(field, value)
    kml.save(output_kml_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert shapefile to KML')
    parser.add_argument('--shapefile', help='Path to the input shapefile')
    parser.add_argument('--kmlfile', help='Path to the output KML file')

    args = parser.parse_args()

    shapefile_path = args.shapefile
    output_kml_path = args.kmlfile
    shapefile_to_kml(shapefile_path=shapefile_path, output_kml_path=output_kml_path)