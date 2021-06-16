from flask import Flask
from flask_restful import Resource

class On(Resource):
    def get(self):
        return {"status": 200}