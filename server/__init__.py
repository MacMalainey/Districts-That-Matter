import json

from flask import Flask
from . import queries
<<<<<<< HEAD
from flask_cors import CORS
=======

schema: dict[str, list[str]]

with open("../.local/dtmTORO_schema.json") as schema_file:
    schema = json.load(schema_file)

>>>>>>> origin/main
app = Flask(__name__)
CORS(app)
queries.init_app(app)