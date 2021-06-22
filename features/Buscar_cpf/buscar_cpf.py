from shared.db import db
from flask import request
from flask_restful import Resource

class BuscarCpf(Resource):
    def post(self):
        data = request.json
        banco = db()
        json = banco.buscarCpf(data)
        return json