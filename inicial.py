from tkinter import*
import random
import time
import datetime
import tkinter.messagebox as tkMessageBox
from cadastrar import cadastro
from lancar import lancando
from excluir import excluindo
from relatorio import gerando


tinicial = Tk()
tinicial.geometry("1350x750+100+100")
tinicial.title("LOCADORA - SIS")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = '#49A'
tinicial.iconbitmap("./Images/logo.ico")
imgcad=PhotoImage(file='./Images/cad.png')
imglan=PhotoImage(file='./Images/lan.png')
imgrel=PhotoImage(file='./Images/rel.png')
imgexc=PhotoImage(file='./Images/exc.png')

def cadastrar():
	#cadastrar = cadastro()
	cad= cadastro.cadastrar()




def lancar():
	lac= lancando.lancar()


def relatorio():
	rel= gerando.gerar()
    
    
def excluir():
	#janela filha
    exc=excluindo.excluir()

    
    




Tops = Frame (tinicial,width=1350, height=325, relief=RAISED,bg='SKyBlue1', borderwidth=4)
Tops.pack(side=RIGHT)

Lbotoes = Frame (Tops,width=25, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=1)


cmdCadastrar=Button(Tops,image=imgcad,bd=0,relief=GROOVE,bg = 'SKyBlue1',fg='white',font=('arial',18,'bold'),width=300,height=300,
                                                          command = cadastrar).grid(row=0,column=2)

Lbotoes = Frame (Tops,width=25, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=3)
 
cmdLancar=Button(Tops,image=imglan,bd=0,relief=GROOVE,bg = 'SKyBlue1',fg='white',font=('arial',18,'bold'),width=300,height=300,
                                                          command = lancar).grid(row=0,column=4)

Lbotoes = Frame (Tops,width=25, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=5)
 
cmdRelatorio=Button(Tops,image=imgrel,bd=0,relief=GROOVE,bg = 'SKyBlue1',fg='white',font=('arial',18,'bold'),width=300,height=300,
                                                          command = relatorio).grid(row=0,column=6)

Lbotoes = Frame (Tops,width=25, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=7)
 
cmdExcluir=Button(Tops,image=imgexc,bd=0,relief=GROOVE,bg = 'SKyBlue1',fg='white',font=('arial',18,'bold'),width=300,height=300,
                                                          command = excluir).grid(row=0,column=8)

Lbotoes = Frame (Tops,width=200, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=9)

Lbotoes = Frame (Tops,width=200, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=10)
#Lbotoes = Frame (Tops,width=200, height=400, relief=RAISED,bg='SKyBlue1', borderwidth=0).grid(row=0,column=10)

tinicial.mainloop()



