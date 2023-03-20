from conexao import *
from interfaceUsuario import *
import tkinter.messagebox as MessageBox 

def atualizarTabela(id_entrada, nome_entrada, telefone_entrada):

    conexao = conectar()


    id = id_entrada.get()
    nome = nome_entrada.get()
    telefone = telefone_entrada.get()

    if(nome == "" or telefone == ""):

        MessageBox.showinfo("Alerta", "Por favor, insira os campos que deseja atualizar!")

    else:

        cursor = conexao.cursor()
        cursor.execute("UPDATE USUARIOS SET NOME = '" + nome + "', telefone ='" + telefone +"' WHERE id='" + id + "'")
        cursor.execute("commit")

        MessageBox.showinfo("Status", "Atualização realizada")
        conexao.close()

