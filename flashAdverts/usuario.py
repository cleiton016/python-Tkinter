from tkinter import *
import banco
import Login
class Usuario:
    def __init__(self, master, user=2):
        self.root=master
        master.geometry('400x300+250+50')
        self.conteiner1 = Frame(master, bg='#FACC2E')
        self.conteiner2 = Frame(master, bg='#848484')
        self.conteiner3 = Frame(master, bg='#FA58F4')
        # self.lista = Listbox(self.conteiner2)
        # self.lista.insert(END, 'teste')
        tm = 15
        self.img = PhotoImage(file='imagens\The-flash.png')
        self.img = self.img.subsample(2,2)
        self.lb1 = Label(self.conteiner1, text='FlashAdverts', bg='#FACC2E', fg='#FFF', font="-weight bold -size 15")
        self.lb2 = Label(self.conteiner2, text='Menu de opçoes\n', bg='#585858', width=tm + 5)
        self.lb3 = Label(self.conteiner2, text='', bg='#848484')
        self.bt1 = Button(self.conteiner2, text='Cria Anuncio', bg='#FFF', width=tm)
        self.bt2 = Button(self.conteiner2, text='Aplicar Anuncio', bg='#FFF', width=tm)
        self.bt3 = Button(self.conteiner2, text='Editar perfil', bg='#fff', width=tm)
        #self.lt1 = Listbox(self.conteiner3)
        #self.img = PhotoImage(file='w.png')
        self.lb4 = Label(self.conteiner3, image=self.img)




        self.sair = Button(self.conteiner2, text='Sair', width=5)
        self.sair.bind('<Button-1>',self.logoff)

        self.conteiner1.pack(side=TOP, fill=X)
        self.conteiner2.pack(side=LEFT, fill=Y)
        self.conteiner3.pack(side=LEFT)

        self.lb1.pack(side=LEFT)
        self.lb2.pack()
        self.lb3.pack()
        self.bt1.pack()
        self.bt2.pack()
        self.bt3.pack()
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
    def logoff(self,event):
        self.limpa()
        Login.Login(self.root)
    def limpa(self):
        self.conteiner1.destroy()
        self.conteiner2.destroy()
        self.conteiner3.destroy()
