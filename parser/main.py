'''
Utility script for parsing 2021 Canada census data and inserting it into a "Districts that Matter" compatible database
'''
import argparse
import typing

import csv
from lxml import etree

import spatialite

from k import *


BOUNDARY_TABLE_COLUMN = (
    "da_basic_info", "boundary", 3347
)

GEOMETRY_TABLE_COLUMNS = [
    ("da_basic_info", "boundary", 3347, "POLYGON", "XY", 0),
]

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

class CharacteristicGroup:
    '''
    Used to help define the schema of the database

    Characteristics that can be categorically grouped together into one table are done so in the schema.
    This helps optimize queries while simultaneously helps make the data more readable.

    A characteristic group is by definition the schema for a specific table and is used for saving data and verification.

    Fulfills FR27
    '''
    table: str
    columns: list[str]
    
    id_column_map: dict[str, int]

    def __init__(self, table: str) -> None:
        self.table = table
        self.columns = []
        self.id_column_map = {}

    def add_column(self, id: str, column: str):
        if column in self.id_column_map:
            raise Exception("BAD SCHEMA_CFG_CFG: Column ({}) already exists in group {}".format(column, self.table))
        self.id_column_map[id] = len(self.columns)
        self.columns.append(column)

class Schema:
    '''
    Used to store the schema for the database

    Fulfills FR27
    '''
    groups: dict[str, CharacteristicGroup]
    groups_by_id: dict[str, CharacteristicGroup]

class Region:
    '''
    Used for keeping track of data for a specific region.

    Performs active verification of expected data format and can save the data to the database

    Fulfills FR27, FR28
    '''
    dguid: str
    _schema: Schema
    _data: dict[str, dict[str, int]]

    def from_schema(dguid: str, schema: Schema):
        region = Region()
        region.dguid = dguid
        region._schema = schema
        region._data = {}

        for name in schema.groups.keys():
            region._data[name] = {}

        return region

    def register(self, id: str, value: int):
        if id not in self._schema.groups_by_id:
            raise Exception("Bad id ({}) used to register data to region {}".format(id, self.dguid))
        
        group = self._schema.groups_by_id[id]
        column = group.id_column_map[id]

        if column in self._data[group.table]:
            raise Exception("Duplicate registration of id ({}) in region {}".format(id, self.dguid))
        
        self._data[group.table][group.columns[column]] = value
    
    def _validate(self):
        for group in self._schema.groups.values():
            if group.table not in self._data:
                raise Exception("Missing table ({}) in region {}".format(group.table, self.dguid))
            
            if len(self._data[group.table]) != len(group.columns):
                raise Exception("Column mismatch in region {} for group {}: expected {}, found {}".format(self.dguid, group.table, len(self._data[group.table]), len(group.columns)))
    
    def save(self, db: spatialite.Connection):
        self._validate()

        for (table, data) in self._data.items():
            columns = data.keys()
            placeholders = [":{}".format(k) for k in columns]
            stmt = "INSERT INTO {}(dguid, {}) VALUES(:dguid, {})".format(table, ", ".join(columns), ", ".join(placeholders))
            data["dguid"] = self.dguid
            db.execute(stmt, data)


def load_schema(schema_file: typing.IO) -> Schema:
    '''
    Loads the schema from the file that should be used to create the database

    Fulfills FR27
    '''
    groups_by_table: dict[str, CharacteristicGroup] = {}
    groups_by_id: dict[str, CharacteristicGroup] = {}

    reader = csv.reader(schema_file)
    next(reader) # Skip header line
    for line in reader:

        if line[SCHEMA_CFG.IGNORED] == "TRUE" or line[SCHEMA_CFG.TABLE] == "":
            continue

        if line[SCHEMA_CFG.TABLE] not in groups_by_table:
            groups_by_table[line[SCHEMA_CFG.TABLE]] = CharacteristicGroup(line[SCHEMA_CFG.TABLE])

        groups_by_table[line[SCHEMA_CFG.TABLE]].add_column(line[SCHEMA_CFG.ID], line[SCHEMA_CFG.COLUMN])
        
        if line[SCHEMA_CFG.ID] in groups_by_id:
            raise Exception("BAD SCHEMA_CFG: Characteristic ({}) already assigned to {}".format(line[SCHEMA_CFG.ID], groups_by_id[line[SCHEMA_CFG.ID]].table))
        
        groups_by_id[line[SCHEMA_CFG.ID]] = groups_by_table[line[SCHEMA_CFG.TABLE]]

    schema = Schema()
    schema.groups = groups_by_table
    schema.groups_by_id = groups_by_id

    return schema

def init_database(db: spatialite.Connection, groups: list[CharacteristicGroup], geometries: dict[str, list[str]]):
    '''
    Initializes the database using the provided schematic

    Fulfills FR27, FR31
    '''
    db.execute("SELECT InitSpatialMetaData()")

    for group in groups:
        db.execute("CREATE TABLE {}(dguid PRIMARY KEY, {})".format(group.table, ", ".join(group.columns)))
    
    for entry in geometries:
        db.execute("SELECT AddGeometryColumn(?, ?, ?, ?, ?, ?)", entry)

def parse_census_data(data: typing.IO, schema: Schema, db: spatialite.Connection, ignore: typing.Callable[[str], bool] | None) -> set[str]:
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
    region: Region = None

    dauids: set[str] = set()

    for record in reader:
        if record[K_DATA_FIELDS.GEO_LEVEL] != K_GEO_LEVELS.DA:
            if record[K_DATA_FIELDS.GEO_LEVEL] == K_GEO_LEVELS.CSD and record[K_DATA_FIELDS.ALT_GEO_CODE] != subdivision:
                skip = ignore is not None and ignore(record[K_DATA_FIELDS.ALT_GEO_CODE])
                subdivision = record[K_DATA_FIELDS.ALT_GEO_CODE]
            continue

        if skip:
            continue

        if region == None or record[K_DATA_FIELDS.DGUID] != region.dguid:
            if region != None:
                region.save(db)
            dauids.add(record[K_DATA_FIELDS.DGUID])
            region = Region.from_schema(record[K_DATA_FIELDS.DGUID], schema)
        
        if record[K_DATA_FIELDS.CHARACTERISTIC_ID] not in schema.groups_by_id:
            continue

        value = None
        if '.' in record[K_DATA_FIELDS.C1_COUNT_TOTAL]:
            value = float(record[K_DATA_FIELDS.C1_COUNT_TOTAL])
        elif record[K_DATA_FIELDS.C1_COUNT_TOTAL] != "":
            value = int(record[K_DATA_FIELDS.C1_COUNT_TOTAL])
        region.register(record[K_DATA_FIELDS.CHARACTERISTIC_ID], value)

    region.save(db)
    return dauids
            
def parse_boundary_data(data: typing.IO, schema: tuple[str, str], db: spatialite.Connection, ignore: typing.Callable[[str], bool]) -> etree._Element:
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
    dguid = None

    elem: etree._Element
    for _, elem in context:
        tag = elem.tag.split('}')[1]

        if elem.prefix == 'gml':
            if tag == 'featureMember':
                dguid = None
                if remove:
                    remove = False
                    elem.clear()
                    delete.append(elem)
            elif tag == 'posList' and not remove:
                # Thankfully we can get lazy with parsing as every element uses the same format of a single LinearRing with a single posList
                raw: list[str] = elem.text.split(' ')
                coords = list(zip(raw[::2], raw[1::2]))
                for i in range(len(coords)):
                    coords[i] = ' '.join(coords[i])
                value = 'POLYGON(({}))'.format(', '.join(coords))
                # print('UPDATE {} SET {} = GeomFromText("{}", {}) WHERE dguid = "{}"'.format(schema[0], schema[1], schema[2], value, dguid,))
                db.execute('UPDATE {} SET {} = GeomFromText(?, ?) WHERE dguid = ?'.format(schema[0], schema[1],), (value, schema[2], dguid,))

        elif elem.prefix == 'fme' and tag == 'DGUID':
            dguid = elem.text
            remove = ignore(dguid)

# Fulfills FR25
if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Convert 2021 Canada census data to DTM database')
    args.add_argument('census_data', type=argparse.FileType(encoding="latin-1"), help="path to census data file")
    args.add_argument('boundary_data', type=argparse.FileType(mode='rb'), help='path to boundary data file')
    args.add_argument('--schema', type=argparse.FileType(), default='characteristics.csv', help='path to schema configuration')
    args.add_argument('--filter', type=argparse.FileType(), help="path to filter configuration")
    args.add_argument('--output', type=str, default="dtm_census_data.db", help="path to output database file")
    pargs = args.parse_args()

    filter: typing.Callable[[str], bool] | None = None
    if pargs.filter is not None:
        whitelist = set(pargs.filter.read().splitlines())
        filter = lambda a: a not in whitelist

    schema = load_schema(pargs.schema)
    with spatialite.connect(pargs.output) as db:
        init_database(db, schema.groups.values(), GEOMETRY_TABLE_COLUMNS)

        dauids = parse_census_data(pargs.census_data, schema, db, filter)
        parse_boundary_data(pargs.boundary_data, BOUNDARY_TABLE_COLUMN, db, lambda x: x not in dauids)

    pargs.census_data.close()
    pargs.boundary_data.close()
