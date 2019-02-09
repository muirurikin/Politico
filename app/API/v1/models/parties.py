'''Imports'''
from flask import make_response, jsonify

PARTIES = []

class Party:
    '''Define Party Class'''
    def __init__(self):
        pass
    @staticmethod
    def get_parties():
        '''Jsonify parties list'''
        return make_response(jsonify(PARTIES))
    @staticmethod
    def create_party(party_name, party_address, party_image):
        '''Add new party to parties list'''
        new_party_info = {
            "id": len(PARTIES) + 1,
            "name": party_name,
            "address": party_address,
            "logo": party_image
        }
        PARTIES.append(new_party_info)
    @staticmethod
    def get_party(party_id):
        party1 = [party for party in PARTIES if party['id'] == party_id]
        return party1
    @staticmethod
    def delete_party(party_id):
        delete_party = [party for party in PARTIES if party['id'] == party_id]
        PARTIES.remove(delete_party[0])
