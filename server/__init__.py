from flask import Flask
from . import queries

app = Flask(__name__)
queries.init_app(app)