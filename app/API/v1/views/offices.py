from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.offices import Office, offices

# Handle GET POST to /offices
@v1.route('/offices', methods=['GET', 'POST'])
def office_func():
  if request.method == 'POST':
    office_data = request.get_json()
    office_name = office_data['name']
    office_type = office_data['type']

    new_office_info = {
      "id": len(offices) + 1,
      "name": office_name,
      "type": office_type
    }

    Office.create_office(new_office_info)
    
    return make_response(jsonify({
      "Message": "Office Info Added",
      "Status": "Ok",
      "office_id": new_office_info['id'],
    }), 201)
  else:
    return Office.get_offices()

# Handle GET to /offices/office_id
@v1.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
  office1 = [office for office in offices if office['id'] == office_id]
  return make_response(jsonify(office1[0]))