import spatialite
import geojson

from flask import current_app, g, Flask

def init_app(app: Flask):
    '''
    Initializes the flask app to support the application's database

    Fulfills FR4, FR12
    '''
    app.teardown_appcontext(_on_teardown)

def get_db():
    '''
    Initiatlizes a database context for request

    If a context for the given request already exists it will return it

    Note: this ONLY works for an instance of a request - nothing else

    Fulfills FR4, FR12
    '''
    if 'db' not in g:
        # TODO fix to use app config
        g.db = spatialite.connect(
            "../.local/dtmTORO.db"
            # current_app.config['DATABASE'],
        )

    return g.db

def _on_teardown(e=None):
    '''
    Closes the database context for the given request

    Fulfills FR4, FR12
    '''
    db = g.pop('db', None)

    if db is not None:
        db.close()

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

def query_munit_demographics_all(db: spatialite.Connection) -> list[dict[str, int]]:
    '''
    Queries map unit demographcs from database

    Fulfills FR4, FR12
    '''

    cur = db.cursor()
    cur.row_factory = _dict_row_factory
    cur.execute(
        """
            SELECT cd.*, AsGeoJSON(bd.geometry) AS center
                FROM census_data as cd, boundary_data AS bd USING (dguid)
        """
    )
    return cur.fetchall()

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
        res[line[0]] = line[1]

    return res

def insert_districts(db: spatialite.Connection, districts: list[tuple[str, int]]):
    cur = db.cursor()
    cur.executemany("INSERT OR REPLACE INTO districts(dguid, id) VALUES (?, ?)", districts)
    db.commit()
