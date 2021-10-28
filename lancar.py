from tkinter import*
import random
import time
import datetime
import tkinter.messagebox as tkMessageBox
from tkinter import ttk


class lancando():
    Lista=[]

            
    def lancar():
        cadastro = Toplevel()
        cadastro.title("Lançamentos")
        cadastro.geometry("500x600+500+100")
        cadastro['bg'] = '#49A'
        cadastro.resizable(width=False, height=False)
        cadastro.iconbitmap("./Images/logo.ico")
        cadastro.focus_force()
        cadastro.grab_set()
        
        placa = ""
        modelo = ""
        ano = ""
        km = "0"
        valor=""
        

        def cadbanco():
            #tkMessageBox.showinfo("Cadastrou", message= "Cadastrado")
            placa = comboPlaca.get()
            modelo = Txtmodelo.get()
            ano = Txtano.get()
            km = Txtkm.get()
            valor = Txtvalor.get()

            if placa =="" or modelo == "" or ano == "" or km =="":
                tkMessageBox.showinfo("Campo Vazio", message= "Favor verificar todos os campos")
            else:
                result = tkMessageBox.askquestion("Confirma :","Confirma o cadastro?")
                if result == 'yes' :
                    tkMessageBox.showinfo("Cadastrado", message= "Realizado com sucesso!")
                    cadastro.destroy()
                else:
                    Txtplaca.delete(0,END)
                    Txtmodelo.delete(0,END)
                    Txtano.delete(0,END)
                    Txtkm.delete(0,END)
                    #cadastrando.configure(state=DISABLED)

        def sair():
            cadastro.destroy()
                   #Espaços entre labels
        def clicoutipo(event):
            lua=comboTipo.get()
            if (lua=="Receita"):
                comboDesc["values"] = ["Aluguel", "Outros"]
            else:
                comboDesc["values"] = ["Gasolina", "Mecanica"]
            #tkMessageBox.showinfo("Clicado", message= "Foi clicado - "+ lua)


        Lbotoes = Frame (cadastro, relief=RAISED,bg = 'SKyBlue1', borderwidth=4)
        Lbotoes.place(relx=0.05, rely = 0.05, relwidth =0.90, relheight=0.8)

        #label botoes e espaços
        Lblplaca = Label(Lbotoes,fg='white', width=15,text="Placa",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblplaca.place(relx=0.05, rely = 0.04,relheight=0.18)
        #Lblplaca.place(relx=0.5, rely = 0.01, relwidth =0.12, relheight=0.1)


        #Txtplaca = Entry(Lbotoes,fg='black',bg = 'white',bd=3,font=('arial',16,'bold'))
        comboPlaca = ttk.Combobox(Lbotoes,values=["January", "February", "March", "April"],state="readonly",font=('arial',14,'bold'))
        comboPlaca["width"] = 15
        comboPlaca.place(relx=0.05, rely = 0.15,relheight=0.07)
        #Txtplaca.grid(row=2,column=3)
        #Txtplaca.insert(0,"Placa")

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=3,column=2)

        Lblmodelo = Label(Lbotoes, fg='white',width=15,text="Modelo",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblmodelo.place(relx=0.5, rely = 0.04,relheight=0.18)
        #Lblmodelo.grid(row=4,column=2)
        Txtmodelo = Entry(Lbotoes,bd=3,fg='black',bg = 'white', font=('arial',16,'bold'))
        Txtmodelo["width"] = 15
        Txtmodelo.place(relx=0.5, rely = 0.15)
        Txtmodelo.configure(state=DISABLED)
        #Txtmodelo.insert(0,"Modelo")

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=5,column=2)

        Lbltipo = Label(Lbotoes,  fg='white', width=15,text="Tipo",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lbltipo.place(relx=0.05, rely = 0.28,relheight=0.18)
        #Lblano.grid(row=6,column=2)        
        comboTipo = ttk.Combobox(Lbotoes,values=["Receita", "Despesa"],state="readonly",font=('arial',14,'bold'))
        comboTipo["width"] = 15
        comboTipo.place(relx=0.05, rely = 0.39,relheight=0.07)
        comboTipo.bind("<<ComboboxSelected>>", clicoutipo)

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=7,column=2)

        Lblvalor = Label(Lbotoes, fg='white', width=15,text="Valor",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblvalor.place(relx=0.5, rely = 0.28,relheight=0.18)
        #Lblkm.grid(row=8,column=2)
        Txtvalor = Entry(Lbotoes,bd=3,fg='black',bg = 'white', font=('arial',16,'bold'))
        Txtvalor.place(relx=0.5, rely = 0.39)
        Txtvalor["width"] = 15
        Txtvalor.insert(0,"0")
        #Txtkm.grid(row=8,column=3)    

        Lbldescricao = Label(Lbotoes,  fg='white', width=15,text="Descrição",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lbldescricao.place(relx=0.05, rely = 0.52,relheight=0.18)
        #Lblano.grid(row=6,column=2)        
        comboDesc = ttk.Combobox(Lbotoes,state="readonly",font=('arial',14,'bold'))
        comboDesc["width"] = 15
        comboDesc.place(relx=0.05, rely = 0.63,relheight=0.07)

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=9,column=2)

        Lblkm = Label(Lbotoes, fg='white',width=15,text="km",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblkm.place(relx=0.5, rely = 0.52,relheight=0.18)
        #Lblmodelo.grid(row=4,column=2)
        Txtkm = Entry(Lbotoes,bd=3,fg='black',bg = 'white', font=('arial',16,'bold'))
        Txtkm["width"] = 15
        Txtkm.place(relx=0.5, rely = 0.63)


        Btncadastrando=Button(Lbotoes,bd=8,relief=GROOVE,bg= '#49A',fg='white',font=('arial',14,'bold'),width=14,text="Cadastrar",command=cadbanco)
        Btncadastrando.place(relx=0.05, rely = 0.76,relheight=0.15)

        Btnsaindo=Button(Lbotoes,bd=8,relief=GROOVE,bg= '#49A',fg='white',font=('arial',14,'bold'),width=14,text="Sair",command=sair)
        Btnsaindo.place(relx=0.5, rely = 0.76,relheight=0.15)

        #cadastrando.grid(row=10,column=3)
        #cadastrando.configure(state=DISABLED)
        #cadastrando.configure(state=NORMAL)
        

        #tkMessageBox.showinfo("Cadastrou", message= "Cadastrado")