from features.taxa_ocupacao.models.taxamodel import TaxaOcupacaoModel
from shared.db import db
from flask import request
from flask_restful import Resource

class TaxaOcupacao(Resource):
    def get(self):
        data = request.json
        banco = db()
        model = banco.taxaocupacao()
        return model.toJson()