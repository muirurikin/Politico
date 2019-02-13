'''Imports'''
from flask import Flask
from app.API.v1 import v1 as v1_blueprint
from config import app_config

def create_app(config_name):
    ''' Create app and set up all app configs'''
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app.register_blueprint(v1_blueprint)

    return app
