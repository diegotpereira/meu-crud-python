from conexao import *
from interfaceUsuario import *
import tkinter.messagebox as MessageBox 

def selecionar(id_entrada, nome_entrada, telefone_entrada):
    # print("botao selecionar")
    
    conexao = conectar()
    if(id_entrada.get() == ""):
        MessageBox.showinfo("Alerta", "ID é necessário para selecionar linha!")

    else:
        cursor = conexao.cursor()
        cursor.execute("select * from usuarios where id= " + id_entrada.get() + "")
        rows = cursor.fetchall()

        for row in rows:
            nome_entrada.insert(0, row[1])
            telefone_entrada.insert(0, row[2])

        

        conexao.close()
        # print(id_entrada, nome_entrada, telefone_entrada)