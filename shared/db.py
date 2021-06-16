import mysql.connector
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