class paciente:
    def __init__(self,json):
        self.pnome = json['nome']
        self.pidade = json['idade']
        self.psexo = json['sexo']
        self.tiposang = json['tiposanguineo']
        self.alergia = json['alergiamedicamento']
        self.ptelefone = json['telefone']
        self.pcpf = json['cpf']
        self.prg = json['rg']
        self.pmedico = json['nomemedico']
        self.ppai = json['nomepai']
        self.pmae = json['nomemae']