'''iMPORTS'''
from flask import make_response, jsonify


class Response:
    '''Declare Response class'''
    @staticmethod
    def on_success(data):
        return make_response(jsonify({
            "status": 200,
            "message": "success",
            "data": data
        }), 200)

    @staticmethod
    def on_error():
        return make_response(jsonify({
            "status": 404,
            "message": "error"
        }), 404)

    @staticmethod
    def on_create(data):
        return make_response(jsonify({
            "status": 201,
            "message": "created",
            "id": data
        }), 201)

    @staticmethod
    def on_update(data):
        return make_response(jsonify({
            "status": 202,
            "message": "updated",
            "data": data
        }), 202)

    @staticmethod
    def on_delete():
        return make_response(jsonify({
            "status": 202,
            "message": "Deleted"
        }), 202)

    @staticmethod
    def on_no_content():
        return make_response(jsonify({
            "status": 204,
            "message": "Content not available"
        }), 204)

    @staticmethod
    def on_bad_request(message):
        return make_response(jsonify({
            "status": 400,
            "response": "Bad Request",
            "message": message
        }), 400)
