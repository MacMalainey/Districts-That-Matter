import json

import geojson

from . import queries
from . import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

###################
## API ENDPOINTS ##
###################

@app.route("/api/units/all")
def api_units_all():
    '''
    Returns all of the registered map units boundary info

    Fulfills FR3, FR4
    '''
    return geojson.dumps(queries.query_munit_geodata(queries.get_db()))

@app.route("/api/units/<dguid>/demographics")
def api_units_demographics(dguid):
    return json.dumps(queries.query_munit_demographics_one(queries.get_db(), dguid))
    