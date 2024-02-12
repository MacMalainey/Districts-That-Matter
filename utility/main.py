'''
Utility script for parsing 2021 Canada census data and inserting it into a "Districts that Matter" compatible database
'''
import argparse

import csv
import typing

from k import *

def parse_census_data(data: typing.IO, filter: typing.Container | None):
    '''
    Parses census data from the given file stream, filtering out the 

    File stream is assumed to be a CSV otherwise an error will be thrown if the format is invalid.
    Additionally the header is checked to see if it conforms to the expected column layout.

    Fulfills FR25, FR26
    '''
    reader = csv.reader(data)

    if next(reader) != K_DATA_FIELDS.HEADER_FIELDS:
        raise Exception("Input data header does not match the expected header fields")
    
    subdivision = None
    da = None

    for (i, record) in enumerate(reader):
        # Only interested in DAs
        if record[K_DATA_FIELDS.GEO_LEVEL] != K_GEO_LEVELS.DA:
            # Keep track of the current subdivision we fall under
            if record[K_DATA_FIELDS.GEO_LEVEL] == K_GEO_LEVELS.CSD and subdivision != record[K_DATA_FIELDS.ALT_GEO_CODE]:
                subdivision = record[K_DATA_FIELDS.ALT_GEO_CODE]
            continue

        if filter is not None and subdivision not in filter:
            continue

        if da != record[K_DATA_FIELDS.ALT_GEO_CODE]:
            da = record[K_DATA_FIELDS.ALT_GEO_CODE]
            # print(da)

        # TODO - process data and transform it into data relevant to GIS here

        # TODO - save data to GIS


# Fulfills FR25
if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Convert 2021 Canada census data to DTM database')
    args.add_argument('input', type=argparse.FileType(encoding="latin-1"), help="path to census data file")
    args.add_argument('--filter', type=argparse.FileType(), help="path to filter configuration")
    pargs = args.parse_args()

    filter = None
    if pargs.filter is not None:
        filter = set(pargs.filter.readlines())

    parse_census_data(pargs.input, filter)

    args.input.close()