from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office

@v1.route('/offices', methods=['GET'])
def get_offices():
  return Office.get_offices()

@v1.route('/new', methods=['POST'])
def new_office():
  office_data = request.get_json()
  office_name = office_data['name']
  office_type = office_data['type']

  new_office_info = {
    "name": office_name,
    "type": office_type
  }

  Office.create_office(new_office_info)
  
  return make_response(jsonify({
    "Message": "Office Info Added",
    "Status": "Ok"
  }), 201)