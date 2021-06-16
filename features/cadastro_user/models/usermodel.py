import bcrypt
class User:
    def __init__(self, json):
        self.nome = json['nome']
        self.cpf = json['cpf']
        self.email = json['email']
        self.numregistro = json['numregistro']
        self.localtrab = json['localtrab']
        self.user = json['user']
        self.senha = bcrypt.hashpw(json['senha'].encode('utf-8'),bcrypt.gensalt())