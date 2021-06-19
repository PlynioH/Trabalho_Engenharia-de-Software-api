from features.Cadastro_paciente.models.paciente import paciente
from shared.db import db
from flask import request
from flask_restful import Resource

class CadastroPaciente(Resource):
    def post(self):
        data = request.json
        model = paciente(data)
        banco = db()
        banco.cadastroPaciente(model)
        return {"status": 200}