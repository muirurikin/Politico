"""Imports"""
from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.parties import Party as P, PARTIES
from app.API.utils.validator import Validate as V


# Handle GET POST to /parties
@v1.route('/parties', methods=['GET', 'POST'])
def party_func():
    '''Handle All methods in methods list'''
    if request.method == 'POST':
        party_data = request.get_json()
        party_name = party_data['name']
        party_address = party_data['address']
        party_image = party_data['logo']

        error_handle = V.validate_party(party_name, party_address, party_image)
        if error_handle:
            return error_handle
        else:
            party_info = P.create_party(party_name, party_address, party_image)
            return make_response(jsonify({
                "Message": "Party Info Added",
                "Status": 201,
                "party_id": party_info['id']
            }), 201)

    return P.get_parties()


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
        P.delete_party(party_id)
        return make_response(jsonify({
            "Message": "Party deleted",
            "Status": "ok"
        }), 200)
    else:
        result = P.get_party(party_id)
        if not result:
            return make_response(jsonify({
                "Message": "Not Found"
            }))

        return make_response(jsonify(result))
