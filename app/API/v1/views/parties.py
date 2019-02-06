from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.parties import Party

@v1.route('/parties', methods=['GET'])
def get_parties():
  return Party.get_parties()