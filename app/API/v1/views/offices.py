from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office, offices

@v1.route('/offices', methods=['GET'])
def get_offices():
  return make_response(jsonify(offices))