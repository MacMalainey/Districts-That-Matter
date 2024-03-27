import json

from flask import Flask, g
from flask_cors import CORS

import spatialite

from .processor import Processor
from . import queries

import matplotlib.pyplot as plt

schema: dict[str, list[str]]

with open("../.local/dtmTORO_schema.json") as schema_file:
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

def _load_data(app: Flask):
    db = spatialite.connect("../.local/dtmTORO.db")
    data = queries.query_munit_as_dataframe(db)
    db.close()
    return data

app = Flask(__name__)
CORS(app)
processor = Processor(_load_data(app), schema)
app.teardown_appcontext(_on_teardown)