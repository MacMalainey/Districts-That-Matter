import spatialite
import typing
import json
import geojson

from flask import current_app, g

def _get_db():
    if 'db' not in g:
        # TODO fix to use app config
        g.db = spatialite.connect(
            "../.local/dtmTORO.db"
            # current_app.config['DATABASE'],
        )

    return g.db

def _on_teardown(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def query_geodata(limit: int | None) -> list[dict[str, typing.Any]]:
    db = _get_db()

    cur = db.cursor()
    cur.execute("SELECT dguid, AsGeoJson(transform(boundary, 4326)) FROM da_basic_info")

    # Potential optimization here if we load objects on one thread
    # and perform packing into the list on another
    data: list[(str, str)]
    if limit is not None:
        data = cur.fetchmany(limit)
    else:
        data = cur.fetchall()

    collection = list()
    
    for record in data:
        geom = geojson.loads(record[1])
        feature = geojson.Feature(geometry=geom, properties={
            'dguid': record[0]
        })
        collection.append(feature)

    return geojson.FeatureCollection(collection)