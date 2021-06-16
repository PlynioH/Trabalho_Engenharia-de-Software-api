from features.cadastro_user.cadastro_user import CadastroUser
from flask import Flask
from flask_restful import Api
from features.on.on import On

app = Flask(__name__)
api = Api(app)

api.add_resource(On, '/')
api.add_resource(CadastroUser, '/cadastro/user')

if __name__ == '__main__':
    app.run()