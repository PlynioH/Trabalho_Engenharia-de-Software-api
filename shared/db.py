from features.taxa_ocupacao.models.taxamodel import TaxaOcupacaoModel
import mysql.connector
import bcrypt
import os
class db:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host= os.environ['host'],
            user= os.environ['user'],
            password= os.environ['password'],
            database= os.environ['database']
        )
    def limpar(self, texto):
        ovo = texto.replace('(', '')
        ovo = ovo.replace(',', '')
        ovo = ovo.replace(')', '')
        return ovo

    def taxaocupacao(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT count(numcadastro) as t FROM paciente"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        numeroClientes = self.limpar(str(myresult))
        sql = "SELECT count(numeroleito) as t FROM leito"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        numeroLeito = self.limpar(str(myresult))
        sql = "SELECT count(numeroequipamento) as t FROM leito"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        numeroEquipamento = self.limpar(str(myresult))
        sql = "SELECT count(ocupacao) as t FROM leito WHERE ocupacao = 'ocupado'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        qtdocupado = str(int(((int(self.limpar(str(myresult))) * 100)/int(numeroLeito)))) + '%'
        situacao = ''
        if(int(((int(self.limpar(str(myresult))) * 100)/int(numeroLeito))) <= 50):
            situacao = 'Ok'
        elif(int(((int(self.limpar(str(myresult))) * 100)/int(numeroLeito))) > 50 and int(((int(self.limpar(str(myresult))) * 100)/int(numeroLeito))) < 80):
            situacao = 'Alerta'
        else:
            situacao = 'Crítico'
        model = TaxaOcupacaoModel(numeroLeito,numeroEquipamento,numeroClientes,qtdocupado,situacao)
        return model
    
    def deletarPaciente(self, json):
        mycursor = self.mydb.cursor()
        sql = "DELETE FROM pacientes WHERE cpf = '"+ json['cpf'] +"'"
        mycursor.execute(sql)
        self.mydb.commit()
        sql = "UPDATE leito SET ocupacao = 'Livre' WHERE quarto = '"+ json['quarto'] +"'"
        mycursor.execute(sql)
        self.mydb.commit()
    
    def buscarCpf(self, json):
        mycursor = self.mydb.cursor()
        sql = "SELECT cpf FROM paciente WHERE cpf = '"+ json['cpf'] +"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        cpf = self.limpar(str(myresult))
        sql = "SELECT nome FROM paciente WHERE cpf = '"+ json['cpf'] +"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        nome = self.limpar(str(myresult))
        sql = "SELECT nquarto FROM paciente WHERE cpf = '"+ json['cpf'] +"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        quarto = self.limpar(str(myresult))
        return {"cpf": cpf, "nome": nome, "quarto": quarto}
                    
    def cadastrouser(self, userobject):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO usuario (nome, cpf, email, numregistro, localtrabalho, nomeusuario, senhausuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (userobject.nome, userobject.cpf, userobject.email, userobject.numregistro, userobject.localtrab, userobject.user, userobject.senha)
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def cadastroLeito(self, leitoobject):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO leito (numeroleito, numeroequipamento, quarto, ocupacao) VALUES (%s, %s, %s, %s)"
        val = (leitoobject.nleito, leitoobject.nequipamento, leitoobject.nquarto, leitoobject.ocup)
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def cadastroPaciente(self, pacienteobject):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO paciente (nome, idade, sexo, tiposanguineo, alergiamedicamento, gravidade, telefone, cpf, rg, nquarto, nomemedico, nomepai, nomemae) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (pacienteobject.pnome, pacienteobject.pidade, pacienteobject.psexo, pacienteobject.tiposang, pacienteobject.alergia, pacienteobject.pgravidade, pacienteobject.ptelefone, pacienteobject.pcpf, pacienteobject.prg, pacienteobject.pquarto, pacienteobject.pmedico, pacienteobject.ppai, pacienteobject.pmae)
        mycursor.execute(sql, val)
        self.mydb.commit()
        sql = "UPDATE leito SET ocupacao = 'Ocupado' WHERE quarto = '"+ pacienteobject.pquarto +"'"
        mycursor.execute(sql)
        self.mydb.commit()
        
    
    def login(self, loginobject):
        mycursor = self.mydb.cursor()
        sql = "SELECT nomeusuario FROM usuario WHERE nomeusuario = '"+ loginobject.user +"'" 
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        loginUsuario = ''
        senhaUsuario = ''
        try:
            for x in myresult:
                loginUsuario = x
            print(loginUsuario)
        except:
            pass
        sql2 = "SELECT senhausuario FROM usuario WHERE nomeusuario = '"+ loginobject.user +"'" 
        mycursor.execute(sql2)
        myresult = mycursor.fetchone()
        try:
            for y in myresult:
                senhaUsuario = y
            print(senhaUsuario)
        except:
            pass
        try:
            if bcrypt.hashpw(loginobject.senha.encode('utf-8'), senhaUsuario) == senhaUsuario and loginUsuario == loginobject.user:
                print("match")
                return True
            else:
                print("does not match")
                return False
        except:
            print("does not match")
            return False