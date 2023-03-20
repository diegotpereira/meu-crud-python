from conexao import *
from interfaceUsuario import *
import tkinter.messagebox as MessageBox 

def deletar(id_entrada, nome_entrada, telefone_entrada):

    conexao = conectar()

    if(id_entrada.get() == ""):

        MessageBox.showinfo("Alerta", "Insira o ID para excluir a linha")

    else:

        sql = "DELETE FROM USUARIOS WHERE ID =" + id_entrada.get() + ""
        cursor = conexao.cursor()
        cursor.execute(sql)
        cursor.execute("commit")

        id_entrada.delete(0, 'end')
        nome_entrada.delete(0, 'end')
        telefone_entrada.delete(0, 'end')

        MessageBox.showinfo("Status", "Deletar com sucesso")
        conexao.close()
