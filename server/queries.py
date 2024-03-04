import spatialite
import typing
import json

db: spatialite.Connection = None

def _conguard():
    if db is None:
        raise Exception("query_api: database not initialized")

def database_connect(path):
    global db
    db = spatialite.connect(path)

def database_close():
    global db
    _conguard()
    db.close()
    db = None

def query_geodata(limit: int | None) -> list[dict[str, typing.Any]]:
    _conguard()

    cur = db.cursor()
    cur.execute("SELECT dguid, AsGeoJson(transform(boundary, 4326)) FROM da_basic_info")

    data: list[(str, str)]
    if limit is not None:
        data = cur.fetchmany(limit)
    else:
        data = cur.fetchall()
    
    for i in range(len(data)):
        record = data[i]
        geodata = json.loads(record[1])
        data[i] = {
            'type': 'Feature',
            'properties': {
                'dguid': record[0]
            },
            'geometry': geodata,
        }

    return {
        'type': 'FeatureCollection',
        'features': data
    }