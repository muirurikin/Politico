"""Imports"""
from app.API.v2 import v2


@v2.route('/', methods=['GET'])
def index_v2():
    return '<h1>Welcome To Politico version 2</h1>'
