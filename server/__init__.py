import json
from os import environ

from flask import Flask, g, send_file
from flask_cors import CORS

from .processor import Processor
from . import queries

import spatialite


schema: dict[str, list[str]]

_SCHEMA_PATH = environ["DTM_SERVER_SCHEMA"]
_DATABASE_PATH = environ["DTM_SERVER_DATABASE"]
_STATIC_PATH = environ["DTM_SERVER_STATIC_DIR"]

with open(_SCHEMA_PATH) as schema_file:
    schema = json.load(schema_file)

def get_db():
    '''
    Initiatlizes a database context for request

    If a context for the given request already exists it will return it

    Note: this ONLY works for an instance of a request - nothing else

    Fulfills FR4, FR12
    '''
    if 'db' not in g:
        # TODO fix to use app config
        g.db = spatialite.connect(_DATABASE_PATH)

    return g.db

def _on_teardown(e=None):
    '''
    Closes the database context for the given request

    Fulfills FR4, FR12
    '''
    db = g.pop('db', None)

    if db is not None:
        db.close()

def _init_processor():
    db = spatialite.connect(_DATABASE_PATH)
    data = queries.query_munits(db)
    p = Processor(data, schema)
    p._districts = queries.query_districts_dataframe(db)
    db.close()
    return p

app = Flask(
    __name__,
    static_url_path='',
    static_folder=_STATIC_PATH
)
CORS(app)
processor = _init_processor()
app.teardown_appcontext(_on_teardown)

@app.route("/")
def hello_world():
    return send_file(_STATIC_PATH+"/index.html")