from tkinter import*
import random
import time
import datetime
import tkinter.messagebox as tkMessageBox


class cadastro():

            
    def cadastrar():
        cadastro = Toplevel()
        cadastro.title("Cadastrar Veículos")
        cadastro.geometry("500x600+500+100")
        cadastro['bg'] = '#49A'
        cadastro.resizable(width=False, height=False)
        cadastro.iconbitmap("./Images/logo.ico")
        cadastro.focus_force()
        cadastro.grab_set()
        
        placa = ""
        modelo = ""
        ano = ""
        km = ""

        def cadbanco():
        	#tkMessageBox.showinfo("Cadastrou", message= "Cadastrado")
            placa = Txtplaca.get()
            modelo = Txtmodelo.get()
            ano = Txtano.get()
            km = Txtkm.get()
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
        Lbotoes = Frame (cadastro, relief=RAISED,bg = 'SKyBlue1', borderwidth=4)
        Lbotoes.place(relx=0.05, rely = 0.20, relwidth =0.90, relheight=0.5)

        #label botoes e espaços
        Lblplaca = Label(Lbotoes,fg='white', width=15,text="Placa",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblplaca.place(relx=0.05, rely = 0.01,relheight=0.3)
        #Lblplaca.place(relx=0.5, rely = 0.01, relwidth =0.12, relheight=0.1)


        Txtplaca = Entry(Lbotoes,fg='black',bg = 'white',bd=3,font=('arial',16,'bold'))
        Txtplaca["width"] = 15
        Txtplaca.place(relx=0.05, rely = 0.19)
        #Txtplaca.grid(row=2,column=3)
        #Txtplaca.insert(0,"Placa")

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=3,column=2)

        Lblmodelo = Label(Lbotoes, fg='white',width=15,text="Modelo",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblmodelo.place(relx=0.5, rely = 0.01,relheight=0.3)
        #Lblmodelo.grid(row=4,column=2)
        Txtmodelo = Entry(Lbotoes,bd=3,fg='black',bg = 'white', font=('arial',16,'bold'))
        Txtmodelo["width"] = 15
        Txtmodelo.place(relx=0.5, rely = 0.19)
        #Txtmodelo.grid(row=4,column=3)
        #Txtmodelo.insert(0,"Modelo")

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=5,column=2)

        Lblano = Label(Lbotoes,  fg='white', width=15,text="Ano",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblano.place(relx=0.05, rely = 0.38,relheight=0.3)
        #Lblano.grid(row=6,column=2)
        Txtano = Entry(Lbotoes,bd=3,fg='black',bg = 'white', font=('arial',16,'bold'))
        Txtano.place(relx=0.05, rely = 0.56)
        Txtano["width"] = 15
        #Txtano.grid(row=6,column=3)    

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=7,column=2)

        Lblkm = Label(Lbotoes, fg='white', width=15,text="Km",bg= '#49A',borderwidth=4,font=('arial',14,'bold'))
        Lblkm.place(relx=0.5, rely = 0.38,relheight=0.3)
        #Lblkm.grid(row=8,column=2)
        Txtkm = Entry(Lbotoes,bd=3,fg='black',bg = 'white', font=('arial',16,'bold'))
        Txtkm.place(relx=0.5, rely = 0.56)
        Txtkm["width"] = 15
        #Txtkm.grid(row=8,column=3)    

        #Lbotoes = Frame (cadastro,width=100, height=50, relief=RAISED,bg = '#49A', borderwidth=0).grid(row=9,column=2)

        Btncadastrando=Button(Lbotoes,bd=8,relief=GROOVE,bg= '#49A',fg='white',font=('arial',14,'bold'),width=14,text="Cadastrar",command=cadbanco)
        Btncadastrando.place(relx=0.05, rely = 0.76,relheight=0.2)

        Btnsaindo=Button(Lbotoes,bd=8,relief=GROOVE,bg= '#49A',fg='white',font=('arial',14,'bold'),width=14,text="Sair",command=sair)
        Btnsaindo.place(relx=0.5, rely = 0.76,relheight=0.2)

        #cadastrando.grid(row=10,column=3)
        #cadastrando.configure(state=DISABLED)
        #cadastrando.configure(state=NORMAL)
        

        #tkMessageBox.showinfo("Cadastrou", message= "Cadastrado")