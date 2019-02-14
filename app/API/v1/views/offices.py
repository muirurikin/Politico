"""Imports"""
from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office
from app.API.utils.validator import Validate as V
from app.API.utils.responses import Response


# Handle GET to /offices
@v1.route('/offices', methods=['GET'])
def get_offices():
    return Office.get_offices()


@v1.route('/offices', methods=['POST'])
def add_office():
    office_data = request.get_json()
    office_name = office_data['name']
    office_type = office_data['type']

    error_handle = V.validate_office(office_name, office_type)
    if not error_handle:
        office_info = Office.create_office(office_name, office_type)
        if isinstance(office_info, dict):
            res = Response.on_create(office_info['id'])
            return res
        return office_info
    else:
        return error_handle


# Handle GET to /offices/office_id
@v1.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    """Handle requests in the methods list"""
    result = Office.get_office(office_id)
    if not result:
        res = Response.on_bad_request(message='Office does not exist')
        return res
    return make_response(jsonify(result))
