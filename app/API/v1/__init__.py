from flask import Blueprint

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

from app.API.v1.views import offices
from app.API.v1.views import parties
