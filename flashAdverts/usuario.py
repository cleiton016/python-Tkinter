from tkinter import *
import banco,Login,Cria_anuncio
class Usuario:
    def __init__(self, master, user=2):
        self.root=master
        self.user= user
        master.geometry('800x450+250+50')
        self.conteiner1 = Frame(master, bg='#FACC2E')
        self.conteiner2 = Frame(master, bg='#848484')
        self.conteiner3 = Frame(master, bg='#FA58F4')
        # self.lista = Listbox(self.conteiner2)
        # self.lista.insert(END, 'teste')
        tm = 15
        self.img = PhotoImage(file='imagens\The-flash.png')
        self.img = self.img.subsample(2,2)
        self.titulo = Label(self.conteiner1, text='FlashAdverts', bg='#FACC2E', fg='#FFF', font="-weight bold -size 15")
        self.menu = Label(self.conteiner2, text='Menu de opçoes\n', bg='#585858', width=tm + 5)
        self.lb3 = Label(self.conteiner2, text='', bg='#848484')
        self.cria = Button(self.conteiner2, text='Cria Anuncio', bg='#FFF', width=tm)
        self.cria.bind('<Button-1>',self.CriaAnuncio)
        self.aplicar = Button(self.conteiner2, text='Aplicar Anuncio', bg='#FFF', width=tm)
        self.editar = Button(self.conteiner2, text='Editar perfil', bg='#fff', width=tm)
        #self.lt1 = Listbox(self.conteiner3)
        #self.img = PhotoImage(file='w.png')
        self.lb4 = Label(self.conteiner3, image=self.img)




        self.sair = Button(self.conteiner2, text='Sair', width=5)
        self.sair.bind('<Button-1>',self.logoff)

        self.conteiner1.pack(side=TOP, fill=X)
        self.conteiner2.pack(side=LEFT, fill=Y)
        self.conteiner3.pack(side=LEFT)

        self.titulo.pack(side=LEFT)
        self.menu.pack()
        self.lb3.pack()
        self.cria.pack()
        self.aplicar.pack()
        self.editar.pack()
        #self.lt1.pack()
        self.lb4.pack()



        self.sair.pack(side=BOTTOM, anchor=SE)
        # self.lista.pack()
        dados = banco.cursor.execute('select saldo from Credito where cod_credito=?', [user]).fetchall()
        self.lb1 = Label(self.conteiner1,text='Saldo:', bg='#FACC2E',fg='#fff')
        self.saldo = Label(self.conteiner1,text=round(dados[0][0],2), bg='#FACC2E',fg='#fff')
        #self.logo = Label(self.conteiner1, text='FlashAdverts', bg='blue',fg='#fff')
        #self.conteiner1.pack(side=TOP, fill=X)
        self.saldo.pack(side=RIGHT,anchor=E)
        self.lb1.pack(side=RIGHT,anchor=E)
        #self.logo.pack(side=LEFT, anchor=W)
        '''
        self.frame =Frame(master)
        self.frame.grid()
        self.menu = Menu(master)
        self.menu['bg'] = 'blue'
        self.arq = Menu(self.menu)
        self.arq.add_command(label='teste')
        self.menu.add_cascade(label='menu',menu=self.arq)
        master.config(menu=self.menu)
        master.mainloop()
        '''
    def CriaAnuncio(self,event):
        self.limpa()
        Cria_anuncio.Anuncio(self.root,self.user)
    def logoff(self,event):
        self.limpa()
        Login.Login(self.root)
    def limpa(self):
        self.conteiner1.destroy()
        self.conteiner2.destroy()
        self.conteiner3.destroy()
