"""Imports"""
from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.parties import Party as P, PARTIES
from app.API.utils.validator import Validate as V
from app.API.utils.responses import Response


# Handle GET /parties
@v1.route('/parties', methods=['GET'])
def get_parties():
    return P.get_parties()


# Handle POST to /parties
@v1.route('/parties', methods=['POST'])
def add_party():
    party_data = request.get_json()
    party_name = party_data['name']
    party_address = party_data['address']
    party_image = party_data['logo']

    error_handle = V.validate_party(party_name, party_address, party_image)
    if not error_handle:
        party_info = P.create_party(party_name, party_address, party_image)
        if isinstance(party_info, dict):
            res = Response.on_create(party_info['id'])
            return res
        return party_info
    else:
        return error_handle


# Handle GET PUT DELETE to /parties/party_id
@v1.route('/parties/<int:party_id>', methods=['GET'])
def get_party(party_id):
    result = P.get_party(party_id)
    if not result:
        res = Response.on_bad_request(message='Party does not exist')
        return res
    return make_response(jsonify(result))


# Handle GET PUT DELETE to /parties/party_id
@v1.route('/parties/<int:party_id>', methods=['PATCH'])
def update_party(party_id):
    party_info = [party for party in PARTIES if party['id'] == party_id]

    if party_info:
        party_info[0]['name'] = request.json['name']
        party_info[0]['address'] = request.json['address']
        party_info[0]['logo'] = request.json['logo']
        return make_response(jsonify(party_info[0]))
    else:
        res = Response.on_bad_request(message='Party does not exist')
        return res


# Handle DELETE to /parties/party_id
@v1.route('/parties/<int:party_id>', methods=['DELETE'])
def remove_party(party_id):
    result = P.delete_party(party_id)
    return result
