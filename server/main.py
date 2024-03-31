from . import queries, get_db, app, schema, processor

from flask import request

###################
## API ENDPOINTS ##
###################

@app.route("/api/schema")
def api_schema():
    return schema
    

@app.route("/api/units/totals")
def api_units_totals():
    return processor.map_units_totals().to_json()

@app.route("/api/units/all")
def api_units_all():
    '''
    Returns all of the registered map units boundary info

    Fulfills FR3, FR4
    '''
    fields = ["population", "landarea", "geometry"]
    include = request.args.get('include')
    if include is not None:
        if include not in schema:
            return {'reason': 'unknown category'}, 400
        fields.append(f"rc_{include}")
        for field in schema[include]:
            fields.append(field)

    return processor.all_map_units(fields).to_json()

@app.route("/api/units/<dguid>/demographics")
def api_units_demographics(dguid):
    return processor.single_map_unit(dguid).to_json()

@app.route("/api/cois/all")
def api_cois_all():
    seed = request.args.get('seed', 0, int)
    return processor.cluster(seed, n=100).to_json()

@app.route("/api/districts/demographics")
def api_districts_demographics():
    return processor.districts_demographics().to_json()

@app.route("/api/districts")
def api_districts():
    return processor.districts().to_json()

@app.route("/api/districts/update", methods=["POST"])
def api_districts_update():
    queries.insert_districts(get_db(), request.get_json())
    processor._districts = queries.query_districts_dataframe(get_db())

    return {"success": True}