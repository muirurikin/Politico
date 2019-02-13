'''Imports'''
from flask import make_response, jsonify

OFFICES = []


class Office:
    '''Define Office Class'''
    def __init__(self):
        pass

    @staticmethod
    def get_offices():
        '''Jsonify offices list'''
        return make_response(jsonify(OFFICES))

    @staticmethod
    def create_office(office_name, office_type):
        '''Add new office to offices list'''
        new_office_info = {
            "id": len(OFFICES) + 1,
            "name": office_name,
            "type": office_type
        }
        OFFICES.append(new_office_info)
        return new_office_info

    @staticmethod
    def get_office(office_id):
        '''Check offices list for specific office and return it'''
        office1 = [office for office in OFFICES if office['id'] == office_id]
        return office1
