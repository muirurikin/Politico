from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.parties import Party

@v1.route('/parties', methods=['GET'])
def get_parties():
  return Party.get_parties()

@v1.route('/newParty', methods=['POST'])
def new_party():
  party_data = request.get_json()
  party_name = party_data['name']
  party_address = party_data['address']
  party_image = party_data['logo']

  new_party_info = {
    "name": party_name,
    "address": party_address,
    "logo": party_image
  }

  Party.create_party(new_party_info)
  
  return make_response(jsonify({
    "Message": "Party Info Added",
    "Status": "Ok"
  }), 201)