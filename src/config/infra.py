import os
from constants import environment
from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API')

ns = api.namespace('api/v1', description='TODO operations')

if app.config['ENV'] == environment.DEVELOPMENT:
    app.config.from_pyfile('../development.cfg', silent=True)
