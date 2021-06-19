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
        sql = "INSERT INTO paciente (nome, idade, sexo, tiposanguineo, alergiamedicamento, telefone, cpf, rg, nomemedico, nomepai, nomemae) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (pacienteobject.pnome, pacienteobject.pidade, pacienteobject.psexo, pacienteobject.tiposang, pacienteobject.alergia, pacienteobject.ptelefone, pacienteobject.pcpf, pacienteobject.prg, pacienteobject.pmedico, pacienteobject.ppai, pacienteobject.pmae)
        mycursor.execute(sql, val)
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