from tkinter import *
import tkinter.messagebox as MessageBox 
import traceback
from selecionar import *



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

def Inserir():
    print("Inserir")

def DEL():
    print("Deletar")

def Atualizar():
    print("Atualizar")



# btnInserir = Button(root, text="Inserir", command=Inserir, font=('verdana 15'))
# btnDeletar = Button(root, text="Deletar", command=DEL, font=("verdana 15"))
# btnAtualizar = Button(root, text="Atualizar", command=Atualizar, font=("verdana 15"))
btnSelecionar = Button(root, text="Selecionar", command=Selecione, font=("verdana")).place(x=200, y=240)

root.mainloop()