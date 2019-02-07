from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office, offices

@v1.route('/offices', methods=['GET', 'POST'])
def office_func():
  if request.method == 'POST':
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
  else:
    return Office.get_offices()
