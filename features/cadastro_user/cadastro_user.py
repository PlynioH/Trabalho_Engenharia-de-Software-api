from shared.db import db
from features.cadastro_user.models.usermodel import User
from flask import request
from flask_restful import Resource

class CadastroUser(Resource):
    def post(self):
        data = request.json
        model = User(data)
        banco = db()
        banco.cadastrouser(model)
        return {"status": 200}