'''Imports'''
from app.API.utils.responses import Response


class Validate:
    '''Define Validate Class'''
    @staticmethod
    def validate_party(party_name, party_address, party_image):
        '''Check If party input data is valid'''
        def len_checker(info):
            return len(info.strip())
        if len_checker(party_name) == 0 or len_checker(party_address) == 0 or len_checker(party_image) == 0:
            message = "Fill all the required fields and try again."
            res = Response.on_bad_request(message)
            return res
        elif not party_name.isalpha():
            message = 'Fill in a valid party details'
            res = Response.on_bad_request(message)
            return res
