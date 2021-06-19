from features.cadastro_leito.models.leito import leito
from shared.db import db
from flask import request
from flask_restful import Resource

class CadastroLeito(Resource):
    def post(self):
        data = request.json
        model = leito(data)
        banco = db()
        banco.cadastroLeito(model)
        return {"status": 200}