from flask import Flask
from . import queries

app = Flask(__name__)
app.teardown_appcontext(queries._on_teardown)