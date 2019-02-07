from flask import make_response, jsonify

offices =[]

class Office:
  def __init__(self):
    pass

  @staticmethod
  def get_offices():
    return make_response(jsonify(offices))
    
  @staticmethod
  def create_office(new_office_info):
    offices.append(new_office_info)

