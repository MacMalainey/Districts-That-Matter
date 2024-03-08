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
    return geojson.dumps(queries.query_geodata(None), indent=2)

@app.route("/api/units/<unit>/demographics")
def api_units_demographics():
    pass
    