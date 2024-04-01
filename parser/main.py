'''
Utility script for parsing 2021 Canada census data and inserting it into a "Districts that Matter" compatible database
'''
import argparse
from pathlib import Path
import typing

import csv
import json

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
    COLUMN = 4
    LEVEL = 5

def load_schema(schema_file: typing.IO) -> tuple[dict[str, str], dict[str, list[str]]]:
    '''
    Loads the schema from the file that should be used to create the database

    Fulfills FR27
    '''
    categories: dict[str, list[str]] = {}
    schema: dict[str, str] = {}
    reserved_columns: dict[str, str] = {} # Used for verification

    reader = csv.reader(schema_file)
    next(reader) # Skip header line
    for line in reader:

        column = line[SCHEMA_CFG.COLUMN]
        if line[SCHEMA_CFG.IGNORED] == "TRUE" or column == "":
            continue

        if line[SCHEMA_CFG.CATEGORY] != '':
            if line[SCHEMA_CFG.CATEGORY] not in categories:
                categories[line[SCHEMA_CFG.CATEGORY]] = []
            
            if column == 'rc':
                column = f'rc_{line[SCHEMA_CFG.CATEGORY]}'
            else:
                column = f'{line[SCHEMA_CFG.CATEGORY]}_{column}'
                categories[line[SCHEMA_CFG.CATEGORY]].append(column)

        if column in reserved_columns:
            raise Exception(f"BAD SCHEMA CONFIG: Column {column} cannot be assigned to {line[SCHEMA_CFG.ID]}, it is already assigned to {reserved_columns[column]}")

        schema[line[SCHEMA_CFG.ID]] = column
        reserved_columns[column] = line[SCHEMA_CFG.ID]

    return schema, categories

def create_database_tables(db: spatialite.Connection, schema: list[str]):
    '''
    Initializes the database using the provided schematic

    Fulfills FR27
    '''
    db.execute(f"CREATE TABLE {CENSUS_DATA_TABLE}({DGUID_COLUMN} PRIMARY KEY, {COMMA.join(schema)})")

def save_census_entry(dguid: str, data: dict[str, int], db: spatialite.Connection):
    '''
    Saves a row to the database

    Fulfills FR27
    '''
    schema = list(data.keys())
    placeholders = [":{}".format(k) for k in schema]
    data['dguid'] = dguid
    db.execute(f"INSERT INTO {CENSUS_DATA_TABLE}(dguid, {COMMA.join(schema)}) VALUES(:dguid, {COMMA.join(placeholders)})", data)

def parse_census_data(data: typing.IO, schema: dict[str, str], db: spatialite.Connection, whitelist: set[str] | None) -> int:
    '''
    Parses census data from the given file stream, ignoring DAs that aren't included in the filter

    IO stream is assumed to be a CSV otherwise an error will be thrown if the format is invalid.
    Additionally the header is checked to see if it conforms to the expected column layout.

    Fulfills FR25, FR26, FR27
    '''
    reader = csv.reader(data)

    if next(reader) != K_DATA_FIELDS.HEADER_FIELDS:
        raise Exception("Input data header does not match the expected header fields")

    skip = False
    subdivision = None
    data: dict[str, int] = {}
    dguid: str = None

    saved: set[str] = set()

    count = 0
    for record in reader:
        if record[K_DATA_FIELDS.GEO_LEVEL] != K_GEO_LEVELS.DA:
            if record[K_DATA_FIELDS.GEO_LEVEL] == K_GEO_LEVELS.CSD and record[K_DATA_FIELDS.ALT_GEO_CODE] != subdivision:
                if whitelist is not None:
                    # Exhausted whitelist - break early
                    if len(whitelist) == 0:
                        break
                    skip = record[K_DATA_FIELDS.ALT_GEO_CODE] not in whitelist
                    if not skip:
                        whitelist.remove(record[K_DATA_FIELDS.ALT_GEO_CODE])
                subdivision = record[K_DATA_FIELDS.ALT_GEO_CODE]
            continue

        if skip:
            continue

        if dguid == None or record[K_DATA_FIELDS.DGUID] != dguid:
            if dguid != None:
                if len(data) != len(schema):
                    raise Exception(f"SCHEMA MISMATCH: expected {len(schema)} characteristics, found {len(data)} in region {dguid}")
                save_census_entry(dguid, data, db)
                count += 1
                if count % 300 == 0:
                    print(f"Loaded {count} Dissemination Areas...")

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
    save_census_entry(dguid, data, db)

    return count

# Fulfills FR25
if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Convert 2021 Canada census data to DTM database')
    args.add_argument('data', type=argparse.FileType(encoding="latin-1"), help="path to census data file")
    args.add_argument('--schema', required=True, type=argparse.FileType(), help='path to schema configuration')
    args.add_argument('--filter', type=argparse.FileType(), help="path to filter configuration")
    args.add_argument('--output', type=str, default="regions.db", help="path to output database file")
    pargs = args.parse_args()

    whitelist: set[str] | None = None
    if pargs.filter is not None:
        whitelist = set(pargs.filter.read().splitlines())
        pargs.filter.close()

    schema, categories = load_schema(pargs.schema)
    pargs.schema.close()
    print("Schema load successful!")

    db_path = Path(pargs.output)
    with spatialite.connect(pargs.output) as db:
        print("Creating tables...")
        create_database_tables(db, list(schema.values()))
        print("Tables created!")

        print("Importing data... this takes a while")
        count = parse_census_data(pargs.data, schema, db, whitelist)
        print("Census data imported")
        print(f"Total areas loaded: {count}")
    pargs.data.close()

    db_schema_path = db_path.parent.joinpath(db_path.stem + '_schema.json')
    with open(db_schema_path, 'w') as out:
        json.dump(categories, out, indent=2)
    print(f"Schema saved at: {db_schema_path}")

    print("Census data load successful!")
