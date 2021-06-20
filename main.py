

from features.taxa_ocupacao.taxaocupacao import TaxaOcupacao
from features.Cadastro_paciente.cadastro_paciente import CadastroPaciente
from features.cadastro_leito.cadastro_leito import CadastroLeito
from features.login.login import Login
from features.cadastro_user.cadastro_user import CadastroUser
from flask import Flask
from flask_restful import Api
from features.on.on import On

app = Flask(__name__)
api = Api(app)

api.add_resource(On, '/')
api.add_resource(CadastroUser, '/cadastro/user')
api.add_resource(Login, '/login')
api.add_resource(CadastroLeito, '/cadastro/leito')
api.add_resource(CadastroPaciente, '/cadastro/paciente')
api.add_resource(TaxaOcupacao, '/taxaocupacao')

if __name__ == '__main__':
    app.run()