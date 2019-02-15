from flask import Blueprint

v2 = Blueprint('v2', __name__, url_prefix='/api/v2')

from app.API.v2.views import views
