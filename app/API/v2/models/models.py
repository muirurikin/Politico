"""Imports"""
from app.API.v1 import v1


@v1.route('/', methods=['GET'])
def index():
    return '<h1>Welcome To Politico version 2</h1>'
