class TaxaOcupacaoModel:
    def __init__(self, nleito, nequipamento, npaciente, porcentagemocup, situacao):
        self.nleito = nleito
        self.nequipamento = nequipamento
        self.npaciente = npaciente
        self.porcentagemocup = porcentagemocup
        self.situacao = situacao
    
    def toJson(self):
        json = {'nleito': self.nleito, 'nequipamento': self.nequipamento, 'npaciente': self.npaciente, 'porcentagemocup': self.porcentagemocup, 'situacao': self.situacao}
        return json