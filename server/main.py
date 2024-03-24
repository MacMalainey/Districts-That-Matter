from . import queries
from . import app
from . import schema

from flask import request


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

###################
## API ENDPOINTS ##
###################

@app.route("/api/schema")
def api_schema():
    return schema
    

@app.route("/api/units/totals")
def api_units_totals():
    include = []
    for cols in schema.values():
        include.extend(cols)
    return queries.query_munit_totals(queries.get_db(), include)

@app.route("/api/units/all")
def api_units_all():
    '''
    Returns all of the registered map units boundary info

    Fulfills FR3, FR4
    '''
    other = None
    include = request.args.get('include')
    if include is not None:
        if include not in schema:
            return {'reason': 'unknown category'}, 400
        other = [f"rc_{include}", *(schema[include])]
    return queries.query_munit_geodata(queries.get_db(), other)

@app.route("/api/units/<dguid>/demographics")
def api_units_demographics(dguid):
    return queries.query_munit_demographics_one(queries.get_db(), dguid)

@app.route("/api/districts")
def api_districts():
    return queries.query_districts(queries.get_db())

@app.route("/api/districts/update", methods=["POST"])
def api_districts_update():
    queries.insert_districts(queries.get_db(), request.get_json())
    return {"success": True}