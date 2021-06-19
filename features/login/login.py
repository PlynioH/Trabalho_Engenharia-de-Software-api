from features.login.models.loginModel import LoginModel
from shared.db import db
from flask import request
from flask_restful import Resource

class Login(Resource):
    def post(self):
        data = request.json
        model = LoginModel(data)
        banco = db()
        retorno = banco.login(model)
        return {"status": retorno}