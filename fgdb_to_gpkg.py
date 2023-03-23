import argparse
import geopandas as gpd
import fiona


def fgdb_to_gpkg(fgdb_path, gpkg_path, quiet=True):
    """Converts all feature classes within a FileGeoDataBase to new layers within a GeoPackage.

    :param fgdb_path: file path of an Esri FileGeoDataBase (.gdb)
    :type fgdb_path: str

    :param gpkg_path: file path of a GeoPackage (.gpkg)
    :type fgdb_path: str

    :param quiet: prints name of each feature class if False, defaults to True
    :type bool, optional
    """

    # List all feature classes within FileGeoDataBase
    fc_list = fiona.listlayers(fgdb_path)

    # Loop through each feature class
    for fc in fc_list:
        if not quiet:
            print(fc)

        # Read the feature class into GeoDataFrame
        gdf = gpd.read_file(fgdb_path, layer=fc)

        # Write the GeoDataFrame to a GeoPackage
        gdf.to_file(gpkg_path, driver="GPKG", layer=fc, index=False, if_exists="append")


if __name__ == '__main__':
    # Set up argparse to parse command line arguments
    parser = argparse.ArgumentParser(description='Convert a File GeoDatabase to a GeoPackage')
    parser.add_argument('fgdb_path', type=str, help='path to the File GeoDatabase')
    parser.add_argument('gpkg_path', type=str, help='path to the GeoPackage to create')
    parser.add_argument('--quiet', action='store_true', help='suppress printing of feature class names')

    # Parse command line arguments
    args = parser.parse_args()

    # Call the fgdb_to_gpkg function with the provided arguments
    fgdb_to_gpkg(args.fgdb_path, args.gpkg_path, args.quiet)