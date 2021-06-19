class leito:
    def __init__(self,json):
        self.nleito = json['numeroleito']
        self.nequipamento = json['numeroequipamento']
        self.nquarto = json['quarto']
        self.ocup = json['ocupacao']