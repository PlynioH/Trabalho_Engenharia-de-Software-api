class LoginModel:
    def __init__(self, json):
        self.user = json['user']
        self.senha = json['pass']