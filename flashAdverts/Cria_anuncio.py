from tkinter import *
from tkinter import ttk
from tkinter import tix
import entryPlaceholder
import datetime
class addAnucio:
    def __init__(self, cpf, descricao, faixaI, faixaF):
        self.cpf = cpf
        self.descricao = descricao
        self.faixaI = faixaI
        self.faixaF = faixaF
        self.dataI  = datetime.datetime.now().date()
        self.dataF  = None
    def finalizar(self):
        self.dataF = datetime.datetime.now().date()
class Anuncio:
    def __init__(self, master,cpf):
        p=entryPlaceholder
        self.root = master
        master.geometry('400x300+2000+700')
        self.conteiner1 = Frame(master)
        self.conteiner2 = Frame(master)
        self.conteiner3 = Frame(master)
        self.conteiner4 = Frame(master)
########         INTERFACE           #######
        ###########Numeros#########
        tupla=str()
        for i in range(0, 100):
            tupla=tupla+str(i)+'\n'
        ###########################
        self.titulo = Label(self.conteiner1,text='Titulo:')
        self.tituloText = p.EntryPh(self.conteiner1,'Titulo')
        self.faixa = Label(self.conteiner2,text='Faixa etária de idade', font="-weight bold -size 12")
        self.idadeI_text = Label(self.conteiner2,text='Idade inicial:\n')
        self.idadeI = ttk.Combobox(self.conteiner2, width=5)
        self.idadeI['values'] = tupla
        self.idadeF_text = Label(self.conteiner3,text='Idade final:  \n')
        self.idadeF = ttk.Combobox(self.conteiner3,width=5)
        self.idadeF['values'] = tupla
        self.descriçaoText = Label(self.conteiner4,text='Descrição:')
        self.descriçao = Text(self.conteiner4,height=10, width=40)
        self.descriçao.insert(END,'Descreva seu anúncio')
        self.descriçao['fg']='grey'
        self.descriçao.bind("<FocusIn>",self.deleta)
        #self.descriçao.bind("<FocusOut>",self.insere)

#######    FECHANDO AS INSTANCIAS    ##########
        self.conteiner1.pack(side=TOP, anchor=NW)
        self.conteiner2.pack(side=TOP,anchor=NW)
        self.conteiner3.pack(side=TOP,anchor=NW)
        self.conteiner4.pack(side=TOP,anchor=NW)

        self.titulo.pack(side=LEFT, anchor=NW)
        self.tituloText.pack(side=LEFT, anchor=NW)
        self.faixa.pack()

        self.idadeI_text.pack(side=LEFT,anchor=NW)
        self.idadeI.pack(anchor=NW)

        self.idadeF_text.pack(side=LEFT,anchor=NW)
        self.idadeF.pack(anchor=NW)

        self.descriçaoText.pack(side=LEFT,anchor=NW)
        self.descriçao.pack(anchor=NW)

    def insere(self,*args):

            self.descriçao.insert(END,'Descreva seu anúncio')
            self.descriçao['fg']='grey'
    def deleta(self,*args):
        if self.descriçao.get(1.0, END) == 'Descreva seu anúncio':
            self.descriçao.delete(1.0,END)
            self.descriçao['fg']='black'