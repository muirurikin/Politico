'''Imports'''
from app.API.utils.responses import Response

OFFICES = []


class Office:
    '''Define Office Class'''
    def __init__(self):
        pass

    @staticmethod
    def get_offices():
        res = Response.on_success(OFFICES)
        return res

    @staticmethod
    def create_office(office_name, office_type):
        '''Add new office to offices list'''
        new_office_info = {
            "id": len(OFFICES) + 1,
            "name": office_name,
            "type": office_type
        }
        exists = [o for o in OFFICES if o['name'] == new_office_info['name']]
        if not exists:
            OFFICES.append(new_office_info)
            return new_office_info
        else:
            resp = Response.on_bad_request(message='Office already exists')
            return resp

    @staticmethod
    def get_office(office_id):
        '''Check offices list for specific office and return it'''
        office1 = [office for office in OFFICES if office['id'] == office_id]
        return office1
