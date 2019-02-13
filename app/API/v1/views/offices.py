"""Imports"""
from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office


# Handle GET POST to /offices
@v1.route('/offices', methods=['GET', 'POST'])
def office_func():
    """Handle requests in the methods list"""
    if request.method == 'POST':
        office_data = request.get_json()
        office_name = office_data['name']
        office_type = office_data['type']

        office_info = Office.create_office(office_name, office_type)

        return make_response(jsonify({
            "Message": "Office Info Added",
            "Status": "Ok",
            "office_id": office_info['id'],
        }), 201)

    return Office.get_offices()


# Handle GET to /offices/office_id
@v1.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    """Handle requests in the methods list"""
    result = Office.get_office(office_id)
    if not result:
        return make_response(jsonify({
            "Message": "Not Found"
        }))
    return make_response(jsonify(result))
