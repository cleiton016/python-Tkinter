from tkinter import *
from tkinter import ttk,tix,filedialog

import entryPlaceholder,usuario
import datetime
class addAnuncio:
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
        self.cpf= cpf
        p=entryPlaceholder
        self.root = master
        #master.geometry('450x350+2000+650')
        master.geometry('450x350+250+50')
        self.conteiner1 = Frame(master)
        self.conteiner2 = Frame(master)
        self.conteiner3 = Frame(master)
        self.conteiner4 = Frame(master)
        self.conteinerBotao = Frame(master)
########         INTERFACE           #######
        ###########Numeros#########
        tupla=['']
        for i in range(1, 101):
            tupla.append(i)
        ###########################
        self.titulo = Label(self.conteiner1,text='Titulo:')
        self.tituloText = p.EntryPh(self.conteiner1,'Titulo')

        self.faixa = Label(self.conteiner2,text='Faixa etária de idade', font="-weight bold -size 12")

        self.idadeI_text = Label(self.conteiner2,text='Idade inicial:\n')
        self.idadeI = ttk.Combobox(self.conteiner2, width=5,values=tupla)
        self.idadeF_text = Label(self.conteiner3,text='Idade final:  \n')
        self.idadeF = ttk.Combobox(self.conteiner3,width=5, values=tupla)

        self.arq = Button(self.conteiner4,text='Adicionar arquivo')
        self.arq.bind('<Button-1>',self.abri)
        self.arqConteudo = Listbox(self.conteiner4,width=50,height=1)

        self.descriçaoText = Label(self.conteiner4, text='Descrição:')
        self.descriçao = Text(self.conteiner4, height=10, width=40)
        #self.descriçao.insert(END,'Descreva seu anúncio')
        ##############Botões###################
        self.salvaP = Button(self.conteinerBotao,text='Salvar e publicar',width=13,bg='#00FF00',fg='#fff')
        self.salva = Button(self.conteinerBotao,text='Salvar',bg='#2E64FE',fg='#fff')
        self.cancelar = Button(self.conteinerBotao,text='Cancelar',bg='#FA5858',fg='#fff')
        self.cancelar.bind('<Button-1>',self.Cancelar)
#######    FECHANDO AS INSTANCIAS    ##########
        self.conteiner1.pack(side=TOP, anchor=NW)
        self.conteiner2.pack(side=TOP,anchor=NW)
        self.conteiner3.pack(side=TOP,anchor=NW)
        self.conteiner4.pack(side=TOP,anchor=NW)
        self.conteinerBotao.pack(side=RIGHT)

        self.titulo.pack(side=LEFT, anchor=NW)
        self.tituloText.pack(side=LEFT, anchor=NW)
        self.faixa.pack()

        self.idadeI_text.pack(side=LEFT,anchor=NW)
        self.idadeI.pack(anchor=NW)

        self.idadeF_text.pack(side=LEFT,anchor=NW)
        self.idadeF.pack(anchor=NW)


        self.descriçaoText.pack(side=LEFT,anchor=NW)
        self.descriçao.pack(anchor=NW)

        self.arq.pack(side=LEFT, anchor=NW)
        self.arqConteudo.pack(side=LEFT, anchor=NW)
        ##########botões################
        self.salvaP.pack(side=RIGHT, anchor=SE)
        self.salva.pack(side=RIGHT, anchor=SE)
        self.cancelar.pack(side=RIGHT, anchor=SE)
    def abri(self,event):
        arquivo=filedialog.askopenfilename(initialdir="C:/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print(arquivo)
        self.arqConteudo.delete(END)
        self.arqConteudo.insert(END,arquivo)
        return arquivo
    def Cancelar(self,event):
        self.limpa()
        usuario.Usuario(self.root,self.cpf)
    def limpa(self):
        self.conteiner1.destroy()
        self.conteiner2.destroy()
        self.conteiner3.destroy()
        self.conteiner4.destroy()
        self.conteinerBotao.destroy()