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

def query_munit_demographics_all(db: spatialite.Connection) -> list[dict[str, int]]:
    '''
    Queries map unit demographcs from database

    Fulfills FR4, FR12
    '''

    cur = db.cursor()
    cur.row_factory = _dict_row_factory
    cur.execute(
        """
            SELECT *, AsText(Centroid(transform(bd.geometry, 4326))) AS center
                FROM census_data, boundary_data AS bd USING (dguid)
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

def query_munit_geodata(db: spatialite.Connection) -> geojson.FeatureCollection:
    '''
    Queries map unit boundaries from database

    Fulfills FR3, FR4, FR12
    '''

    cur = db.cursor()
    cur.execute("SELECT dguid, AsGeoJson(geometry), population, landarea FROM census_data JOIN boundary_data USING (dguid)")

    # Potential optimization here if we load objects on one thread
    # and perform packing into the list on another
    data: list[(str, str)] = cur.fetchall()

    collection = list()
    
    for record in data:
        geom = geojson.loads(record[1])
        feature = geojson.Feature(geometry=geom, properties={
            'dguid': record[0],
            'population': record[2],
            'landarea': record[3]
        })
        collection.append(feature)

    return geojson.FeatureCollection(collection)