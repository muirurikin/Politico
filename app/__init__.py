# Imports
from flask import Flask
from app.API.v1 import v1 as v1_blueprint
from config import app_config

def create_app():
  app = Flask(__name__)

  app.config.from_object(app_config['development'])
  app.register_blueprint(v1_blueprint)

  return app