from constants.environment import *
from os import getenv
from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API')

ns = api.namespace('api/v1', description='TODO operations')

if getenv("ENV") == PRODUCTION:
    app.config.from_object('config.ProductionConfig')
elif getenv("ENV") == PRE_PRODUCTION:
    app.config.from_object('config.PreProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

