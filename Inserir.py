from interfaceUsuario import *
from conexao import *
import tkinter.messagebox as MessageBox 

def Inserir(nome_entrada, telefone_entrada):

    

    try:

        conexao = conectar()
        

        # id = id_entrada.get()
        nome = nome_entrada.get()
        telefone = telefone_entrada.get()


        if(nome == "" or telefone == ""):
            MessageBox.showinfo("Alerta", "Por favor preencha todos os campos")

        else:
            cursor = conexao.cursor()
            
            cursor.execute("INSERT INTO usuarios(nome, telefone) VALUES('"+ nome +"', '" + telefone +"')")

            cursor.execute("commit")

            MessageBox.showinfo("Status", "Inserido com sucesso")

            conexao.close()

    except(Exception, Error) as error:
        print(error)       