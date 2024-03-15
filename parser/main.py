'''
Utility script for parsing 2021 Canada census data and inserting it into a "Districts that Matter" compatible database
'''
import argparse
import typing
import os

import csv
from lxml import etree

import spatialite

from k import *

CENSUS_DATA_TABLE = "census_data"
BOUNDARY_DATA_TABLE = "boundary_data"

DGUID_COLUMN = "dguid"
BOUNDARY_DATA_COLUMN = "boundary"

SOURCE_WKID = 3347
TARGET_WKID = 4326

COMMA = ", " # Cause f-strings aren't fool proof

class SCHEMA_CFG:
    '''
    Constants for parsing the schema config file

    Fulfills FR27
    '''
    ID = 0
    DESCRIPTION = 1
    IGNORED = 2
    CATEGORY = 3
    TABLE = 4
    COLUMN = 5
    LEVEL = 6

def load_schema(schema_file: typing.IO) -> dict[str, str]:
    '''
    Loads the schema from the file that should be used to create the database

    Fulfills FR27
    '''
    schema: dict[str, str] = {}
    reserved_columns: dict[str, str] = {} # Used for veri

    reader = csv.reader(schema_file)
    next(reader) # Skip header line
    for line in reader:

        if line[SCHEMA_CFG.IGNORED] == "TRUE" or line[SCHEMA_CFG.COLUMN] == "":
            continue

        if line[SCHEMA_CFG.COLUMN] in reserved_columns:
            raise Exception(f"BAD SCHEMA_CFG: Column {line[SCHEMA_CFG.COLUMN]} cannot be assigned to {line[SCHEMA_CFG.ID]}, it is already assigned to {reserved_columns[line[SCHEMA_CFG.COLUMN]]}")

        schema[line[SCHEMA_CFG.ID]] = line[SCHEMA_CFG.COLUMN]
        reserved_columns[line[SCHEMA_CFG.COLUMN]] = line[SCHEMA_CFG.ID]

    return schema

def init_database(db: spatialite.Connection, schema: list[str]):
    '''
    Initializes the database using the provided schematic

    Fulfills FR27, FR31
    '''
    db.execute("SELECT InitSpatialMetaData()")
    db.execute(f"CREATE TABLE {CENSUS_DATA_TABLE}({DGUID_COLUMN} PRIMARY KEY, {COMMA.join(schema)})")
    # db.execute(f"CREATE TABLE {BOUNDARY_DATA_TABLE}({DGUID_COLUMN} PRIMARY KEY)")
    # db.execute("SELECT AddGeometryColumn(?, ?, ?, ?, ?, ?)", (BOUNDARY_DATA_TABLE, BOUNDARY_DATA_COLUMN, TARGET_WKID, "POLYGON", "XY", 0))

def save_census_data(dguid: str, data: dict[str, int], db: spatialite.Connection):
    schema = list(data.keys())
    placeholders = [":{}".format(k) for k in schema]
    data['dguid'] = dguid
    db.execute(f"INSERT INTO {CENSUS_DATA_TABLE}(dguid, {COMMA.join(schema)}) VALUES(:dguid, {COMMA.join(placeholders)})", data)

def parse_census_data(data: typing.IO, schema: dict[str, str], db: spatialite.Connection, ignore: typing.Callable[[str], bool] | None) -> set[str]:
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
    data: dict[str, int] = {}
    dguid: str = None

    saved: set[str] = set()

    for record in reader:
        if record[K_DATA_FIELDS.GEO_LEVEL] != K_GEO_LEVELS.DA:
            if record[K_DATA_FIELDS.GEO_LEVEL] == K_GEO_LEVELS.CSD and record[K_DATA_FIELDS.ALT_GEO_CODE] != subdivision:
                skip = ignore is not None and ignore(record[K_DATA_FIELDS.ALT_GEO_CODE])
                subdivision = record[K_DATA_FIELDS.ALT_GEO_CODE]
            continue

        if skip:
            continue

        if dguid == None or record[K_DATA_FIELDS.DGUID] != dguid:
            if dguid != None:
                if len(data) != len(schema):
                    raise Exception(f"SCHEMA MISMATCH: expected {len(schema)} characteristics, found {len(data)} in region {dguid}")
                save_census_data(dguid, data, db)
                data = {}
            dguid = record[K_DATA_FIELDS.DGUID]
            saved.add(dguid)
        
        if record[K_DATA_FIELDS.CHARACTERISTIC_ID] not in schema:
            continue

        field = schema[record[K_DATA_FIELDS.CHARACTERISTIC_ID]]

        if field in data:
            raise Exception(f"DUPLICATE CHARACTERISTIC: ID ({id}) in region {dguid}")

        value = None
        if '.' in record[K_DATA_FIELDS.C1_COUNT_TOTAL]:
            value = float(record[K_DATA_FIELDS.C1_COUNT_TOTAL])
        elif record[K_DATA_FIELDS.C1_COUNT_TOTAL] != "":
            value = int(record[K_DATA_FIELDS.C1_COUNT_TOTAL])
        data[field] = value

    if len(data) != len(schema):
        raise Exception(f"SCHEMA MISMATCH: expected {len(schema)} characteristics, found {len(data)} in region {dguid}")
    save_census_data(dguid, data, db)

    return saved

def parse_boundary_data(data: typing.IO, db: spatialite.Connection, ignore: typing.Callable[[str], bool]) -> etree._Element:
    """
    Parses boundary data from the given file stream, ignoring DAs that aren't included in the filter

    IO stream is assumed to contain Geographical Markup Language (GML) content. The GML is assumed to have
    certain extra fields that correspond to identifiable DA info, in accordance to the Government of Canada
    2021 census boundary data GML format.

    Fulfills 29, 30
    """

    context = etree.iterparse(data, events=('end',))

    remove = False
    dguid = None
    collide = set()

    elem: etree._Element
    for _, elem in context:
        tag = elem.tag.split('}')[1]

        if elem.prefix == 'gml':
            if tag == 'featureMember':
                dguid = None
                if remove:
                    remove = False
                    elem.clear()
            elif tag == 'posList' and not remove:
                # Thankfully we can get lazy with parsing as every element uses the same format of a single LinearRing with a single posList
                raw: list[str] = elem.text.split(' ')
                coords = list(zip(raw[::2], raw[1::2]))
                for i in range(len(coords)):
                    coords[i] = ' '.join(coords[i])
                value = f'POLYGON(({COMMA.join(coords)}))'
                if dguid in collide:
                    print(f"Found duplicate dguid ({dguid}) among {len(collide)}")
                    continue
                collide.add(dguid)
                db.execute(f'INSERT INTO {BOUNDARY_DATA_TABLE}({DGUID_COLUMN}, {BOUNDARY_DATA_COLUMN}) VALUES(?, Transform(GeomFromText(?, ?), ?))', (dguid, value, SOURCE_WKID, TARGET_WKID))
        elif elem.prefix == 'fme' and tag == 'DGUID':
            dguid = elem.text
            remove = ignore(dguid)

# Fulfills FR25
if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Convert 2021 Canada census data to DTM database')
    args.add_argument('census_data', type=argparse.FileType(encoding="latin-1"), help="path to census data file")
    # args.add_argument('boundary_data', type=argparse.FileType(mode='rb'), help='path to boundary data file')
    args.add_argument('--schema', type=argparse.FileType(), default='characteristics.csv', help='path to schema configuration')
    args.add_argument('--filter', type=argparse.FileType(), help="path to filter configuration")
    args.add_argument('--output', type=str, default="dtm_census_data.db", help="path to output database file")
    pargs = args.parse_args()

    if os.path.exists(pargs.output):
        print(f"FATAL: {pargs.output} already exists - cannot overwrite")
        exit(1)

    filter: typing.Callable[[str], bool] | None = None
    if pargs.filter is not None:
        whitelist = set(pargs.filter.read().splitlines())
        filter = lambda a: a not in whitelist

    schema = load_schema(pargs.schema)
    print("Schema load successful!")

    with spatialite.connect(pargs.output) as db:
        init_database(db, list(schema.values()))
        print("Database initialized - importing data")

        dauids = parse_census_data(pargs.census_data, schema, db, filter)
        print("Census data imported")

        # parse_boundary_data(pargs.boundary_data, db, lambda x: x not in dauids)
        print("Boundary data imported")

    pargs.census_data.close()
    # pargs.boundary_data.close()

    print("Database setup successful!")
