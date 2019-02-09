"""Imports"""
from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.parties import Party

# Handle GET POST to /parties
@v1.route('/parties', methods=['GET', 'POST'])
def party_func():
    '''Handle All methods in methods list'''
    if request.method == 'POST':
        party_data = request.get_json()
        party_name = party_data['name']
        party_address = party_data['address']
        party_image = party_data['logo']


        result = Party.create_party(party_name, party_address, party_image)

        return make_response(jsonify({
            "Message": "Party Info Added",
            "Status": "Ok",
            "party_id": result['id']
        }), 201)
    
    return Party.get_parties()

# Handle GET PUT DELETE to /parties/party_id
@v1.route('/parties/<int:party_id>', methods=['GET', 'PUT', 'DELETE'])
def party_func_id(party_id):
    '''Handle All methods in methods list'''
    if request.method == 'PUT':
        party_info = [party for party in PARTIES if party['id'] == party_id]
        party_info[0]['name'] = request.json['name']
        party_info[0]['address'] = request.json['address']
        party_info[0]['logo'] = request.json['logo']

        return make_response(jsonify(party_info[0]))
    elif request.method == 'DELETE':
        Party.delete_party(party_id)
        return make_response(jsonify({
            "Message": "Party deleted",
            "Status": "ok"
        }), 200)
    else:
        result = Party.get_party(party_id)
        return make_response(jsonify(result))
        