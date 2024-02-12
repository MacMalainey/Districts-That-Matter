'''
Utility script for parsing 2021 Canada census data and inserting it into a "Districts that Matter" compatible database
'''
import argparse

import csv
import typing

from utility.k import *

def parse_census_data(data: typing.IO, filter):
    '''
    Parses census data from the given file stream, applying the filter settings that are passed in

    File stream is assumed to be a CSV otherwise an error will be thrown if the format is invalid.
    Additionally the header is checked to see if it conforms to the expected column layout.

    Fulfills FR25, FR26
    '''
    reader = csv.reader(data)

    if next(reader) != K_DATA_FIELDS.HEADER_FIELDS:
        raise Exception("Input data header does not match the expected header fields")
    
    subdivision = None

    for (i, record) in enumerate(reader):
        # Only interested in DAs
        if record[K_DATA_FIELDS.GEO_LEVEL] != K_GEO_LEVELS.DA:
            # Keep track of the current subdivision we fall under
            if record[K_DATA_FIELDS.GEO_LEVEL] == K_GEO_LEVELS.CSD and subdivision != record[K_DATA_FIELDS.GEO_NAME]:
                subdivision = record[K_DATA_FIELDS.GEO_NAME]
            continue

        # TODO - put subdivision filter here

        # TODO - process data and transform it into data relevant to GIS here

        # TODO - save data to GIS


# Fulfills FR25
if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Convert 2021 Canada census data to DTM database')
    args.add_argument('input', type=argparse.FileType(encoding="latin-1"), help="path to census data file")
    args.add_argument('--filter', type=argparse.FileType(), help="path to filter configuration")
    args = args.parse_args()

    parse_census_data(args.input, None)

    args.input.close()