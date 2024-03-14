from flask import Flask
from . import queries
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
queries.init_app(app)