import spatialite
import geojson
import pandas as pd

from flask import current_app, g, Flask

def _dict_row_factory(cursor, row):
    '''
    Transforms rows into dictionaries by the database

    Fulfills FR4, FR12
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def _geojson_row_factory(cursor, row):
    '''
    Transforms rows into geojson by the database

    Fulfills FR4, FR12
    '''
    properties = {}
    geom_index = None
    for idx, col in enumerate(cursor.description):
        if col[0] == 'geometry':
            geom_index = idx
            continue
        properties[col[0]] = row[idx]

    assert(geom_index is not None)

    geom = geojson.loads(row[geom_index])
    feature = geojson.Feature(geometry=geom, properties=properties)

    return feature

# TODO this should be replaced by the OLAP
def query_munit_totals(db: spatialite.Connection, other=None) -> list[dict[str, int]]:
    '''
    Queries demographics totals from the database

    Fulfills FR4, FR12
    '''

    cur = db.cursor()
    cur.row_factory = _dict_row_factory

    other_str = ""
    if other is not None and len(other) > 0:
        other_str = ", {}".format(", ".join([f"MAX({col}) as {col}" for col in other]))

    cur.execute(
        f"""
            SELECT SUM(population) as population {other_str}
                FROM census_data, boundary_data AS bd USING (dguid)
        """
    )
    return cur.fetchone()

def query_munit_as_dataframe(db: spatialite.Connection) -> pd.DataFrame:
    '''
    Queries map unit demographcs from database

    Fulfills FR4, FR12
    '''

    return pd.read_sql(
        "SELECT cd.*, AsText(bd.geometry) AS geometry_wkt FROM census_data AS cd, boundary_data AS bd USING (dguid);",
        db
    )

def query_munit_demographics_one(db: spatialite.Connection, dguid: str) -> list[dict[str, int]]:
    '''
    Queries map unit demographcs from database

    Fulfills FR4, FR12
    '''

    cur = db.cursor()
    cur.row_factory = _dict_row_factory
    cur.execute(
        """
            SELECT * FROM census_data
                WHERE dguid = ?
        """,
        (dguid, )
    )
    return cur.fetchone()

def query_munit_geodata(db: spatialite.Connection, other=None) -> geojson.FeatureCollection:
    '''
    Queries map unit boundaries from database

    Fulfills FR3, FR4, FR12
    '''

    cur = db.cursor()
    cur.row_factory = _geojson_row_factory

    other_str = ""
    if other is not None and len(other) > 0:
        other_str = ", {}".format(", ".join(other))

    cur.execute(f"SELECT dguid, AsGeoJSON(geometry) as geometry, population, landarea {other_str} FROM census_data JOIN boundary_data USING (dguid)")

    # Potential optimization here if we load objects on one thread
    # and perform packing into the list on another
    data: list[(str, str)] = cur.fetchall()

    collection = list()
    
    for record in data:
        collection.append(record)

    return geojson.FeatureCollection(features=collection)

def query_districts(db: spatialite.Connection):
    """
    Queries all defined districts from the database

    Fulfills FR21
    """

    cur = db.cursor()
    cur.execute("SELECT dguid, id FROM districts")

    res = {}
    for line in cur.fetchall():
        if line[0] is not None:
            res[line[0]] = line[1]

    return res

def insert_districts(db: spatialite.Connection, districts: list[tuple[str, int]]):
    cur = db.cursor()
    cur.executemany("INSERT OR REPLACE INTO districts(dguid, id) VALUES (?, ?)", districts)
    db.commit()
