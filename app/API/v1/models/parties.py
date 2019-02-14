'''Imports'''
from app.API.utils.responses import Response


PARTIES = []


class Party:
    '''Define Party Class'''
    def __init__(self):
        pass

    @staticmethod
    def get_parties():
        '''Jsonify parties list'''
        res = Response.on_success(PARTIES)
        return res

    @staticmethod
    def create_party(party_name, party_address, party_image):
        '''Add new party to parties list'''
        new_party_info = {
            "id": len(PARTIES) + 1,
            "name": party_name,
            "address": party_address,
            "logo": party_image
        }
        exists = [p for p in PARTIES if p['name'] == new_party_info['name']]
        if not exists:
            PARTIES.append(new_party_info)
            return new_party_info
        else:
            resp = Response.on_bad_request(message='Party already exists')
            return resp

    @staticmethod
    def get_party(party_id):
        '''Get single party from parties list and return it'''
        party1 = [party for party in PARTIES if party['id'] == party_id]
        return party1

    @staticmethod
    def delete_party(party_id):
        '''Get single party from parties list and delete it'''
        delete_party = [party for party in PARTIES if party['id'] == party_id]
        if delete_party:
            deleted = PARTIES.remove(delete_party[0])
            res = Response.on_delete()
            return res
        else:
            res = Response.on_bad_request(message='Party does not exist')
            return res
