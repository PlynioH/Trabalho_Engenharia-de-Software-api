from shared.db import db
from flask import request
from flask_restful import Resource

class DeletarPaciente(Resource):
    def post(self):
        data = request.json
        banco = db()
        banco.deletarPaciente(data)
        return {'status': 'ok'}