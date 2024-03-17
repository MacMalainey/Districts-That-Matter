import json

from flask import Flask
from . import queries

schema: dict[str, list[str]]

with open("../.local/dtmTORO_schema.json") as schema_file:
    schema = json.load(schema_file)

app = Flask(__name__)
queries.init_app(app)