'''
Utility script for parsing 2021 Canada census data and inserting it into a "Districts that Matter" compatible database
'''
import argparse
import typing

import csv
import pygml

from lxml import etree

from k import *

class CharacteristicHandler:
    uids: set

    def __init__(self):
        self.uids = set()

    def __call__(self, data: list[str]):
        self.uids.add(data[K_DATA_FIELDS.DGUID])

    def build_uid_filter(self) -> typing.Callable[[str], bool]:
        return lambda x: x not in self.uids

def parse_census_data(data: typing.IO, on_event: typing.Callable[[typing.Any], None], ignore: typing.Callable[[str], bool] | None):
    '''
    Parses census data from the given file stream, ignoring DAs that aren't included in the filter

    IO stream is assumed to be a CSV otherwise an error will be thrown if the format is invalid.
    Additionally the header is checked to see if it conforms to the expected column layout.

    Fulfills FR25, FR26
    '''
    reader = csv.reader(data)

    if next(reader) != K_DATA_FIELDS.HEADER_FIELDS:
        raise Exception("Input data header does not match the expected header fields")

    skip = False
    subdivision = None

    for (i, record) in enumerate(reader):
        if record[K_DATA_FIELDS.GEO_LEVEL] != K_GEO_LEVELS.DA:
            if record[K_DATA_FIELDS.GEO_LEVEL] == K_GEO_LEVELS.CSD and subdivision != record[K_DATA_FIELDS.ALT_GEO_CODE]:
                subdivision = record[K_DATA_FIELDS.ALT_GEO_CODE]
                skip = ignore is not None and ignore(subdivision)
            continue

        if skip:
            return # TODO - REMOVE
            continue

        on_event(record)

        # TODO - save data to GIS
            
def parse_boundary_data(data: typing.IO, ignore: typing.Callable[[str], bool]) -> etree._Element:
    """
    Parses boundary data from the given file stream, ignoring DAs that aren't included in the filter

    IO stream is assumed to contain Geographical Markup Language (GML) content. The GML is assumed to have
    certain extra fields that correspond to identifiable DA info, in accordance to the Government of Canada
    2021 census boundary data GML format.

    Fulfills 29, 30
    """

    context = etree.iterparse(data, events=('end',))

    delete = []
    remove = False

    elem: etree._Element
    for action, elem in context:
        tag = elem.tag.split('}')[1]

        if elem.prefix == 'gml' and tag == 'featureMember' and remove:
            remove = False
            elem.clear()
            delete.append(elem)
        elif elem.prefix == 'fme' and tag == 'DGUID':
            remove = ignore(elem.text)
    
    root = context.root
    for elem in delete:
        root.remove(elem)

    return root

def init_database():
    pass


# Fulfills FR25
if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Convert 2021 Canada census data to DTM database')
    args.add_argument('census_data', type=argparse.FileType(encoding="latin-1"), help="path to census data file")
    args.add_argument('boundary_data', type=argparse.FileType(mode='rb'), help='path to boundary data file')
    args.add_argument('--filter', type=argparse.FileType(), help="path to filter configuration")
    pargs = args.parse_args()

    filter: typing.Callable[[str], bool] | None = None
    if pargs.filter is not None:
        whitelist = set(pargs.filter.read().splitlines())
        filter = lambda a: a not in whitelist

    handler = CharacteristicHandler()
    parse_census_data(pargs.census_data, handler, filter)
    root = parse_boundary_data(pargs.boundary_data, handler.build_uid_filter())

    pargs.census_data.close()
    pargs.boundary_data.close()
