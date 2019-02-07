from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office, offices

@v1.route('/offices', methods=['GET'])
def get_offices():
  return Office.get_offices()

@v1.route('/new', methods=['POST'])
def new_office():
  office_data = request.get_json()
  office_id = office_data['id']
  office_name = office_data['name']
  office_type = office_data['type']

  new_office_info = {
    "id": office_id,
    "name": office_name,
    "type": office_type
  }

  Office.create_office(new_office_info)
  
  return make_response(jsonify({
    "Message": "Office Info Added",
    "Status": "Ok"
  }), 201)

@v1.route('/office/<int:office_id>', methods=['GET'])
def get_office(office_id):
  for office in offices:
    if office['id'] == office_id:
      return make_response(jsonify(office))
    else:
      return None