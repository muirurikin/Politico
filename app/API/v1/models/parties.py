from flask import make_response, jsonify

parties = []

class Party:
  def __init__(self):
    pass

  @staticmethod
  def get_parties():
    return make_response(jsonify(parties))
    