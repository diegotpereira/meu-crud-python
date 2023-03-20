from tkinter import *
import tkinter.messagebox as MessageBox 
import traceback
from Inserir import *
from selecionar import *
from atualizarTabela import *
from deletarUsuario import *



root  = Tk()
root.geometry("500x300")
root.title("Operações Crud com Postgresql")

id = Label(root, text="Digite id:", font=("verdana 15"))
id.place(x=50, y=30)
id_entrada = Entry(root, font=("verdana 15"))
id_entrada.place(x=150, y=30)

nome = Label(root, text="Nome: ", font=("verdana 15"))
nome.place(x=50, y=80)
nome_entrada = Entry(root, font=("verdana 15"))
nome_entrada.place(x=150, y=80)

telefone = Label(root, text="Telefone: ", font=("verdana 15"))
telefone.place(x=50, y=130)
telefone_entrada = Entry(root, font=("verdana 15"))
telefone_entrada.place(x=150, y=130)




def Selecione():
    selecionar(id_entrada, nome_entrada, telefone_entrada)

def Insere():
    Inserir(nome_entrada, telefone_entrada)

def Delete():
    deletar(id_entrada, nome_entrada, telefone_entrada)

def Atualize():
    atualizarTabela(id_entrada, nome_entrada, telefone_entrada)



btnInserir = Button(root, text="Inserir", command=Insere, font=('verdana 15')).place(x=100, y=190)
btnDeletar = Button(root, text="Deletar", command=Delete, font=("verdana 15")).place(x=200, y=190)
btnAtualizar = Button(root, text="Atualizar", command=Atualize, font=("verdana 15")).place(x=320, y=190)
btnSelecionar = Button(root, text="Selecionar", command=Selecione, font=("verdana")).place(x=200, y=240)

root.mainloop()