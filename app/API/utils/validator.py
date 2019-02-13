'''Imports'''
from flask import make_response, jsonify


class Validate:
    '''Define Validate Class'''
    @staticmethod
    def validate_party(party_name, party_address, party_image):
        '''Check If party input data is valid'''
        def len_checker(info):
            return len(info.strip())
        if len_checker(party_name) == 0:
            message = "Party Name cannot be empty"
            return make_response(jsonify({
                "Message": message,
                "Status": 404
            }), 404)
        if len_checker(party_address) == 0:
            message = "Address value cannot be empty"
            return make_response(jsonify({
                "Message": message,
                "Status": 404
            }), 404)
        if len_checker(party_image) == 0:
            message = 'Image link cannot be empty'
            return make_response(jsonify({
                "Message": message,
                "Status": 404
            }), 404)
