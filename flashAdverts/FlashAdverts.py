from tkinter import *
from entryPlaceholder import *
import pyodbc

cursor = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-DVVEP7S\CLEITON_LUIZ;DATABASE=FlashAdverts').cursor()
# cursor = pyodbc.connect('DRIVER={SQL Server};SERVER=PC-CPD-2;DATABASE=FlashAdverts').cursor()
class Campotext:
    def __init__(self, frame, nome, col, linha, show=None, x=None, y=None):
        self.n = nome
        self.nome = Label(frame, text=nome)
        self.text = EntryPh(frame, nome)
        self.text['show'] = show
        self.text['width'] = 30
        self.valido = Label(frame, text='*')
        self.valido.grid(column=col + 2, row=linha)
        self.nome.grid(column=col, row=linha)
        self.text.grid(column=col + 1, row=linha)

    def cor(self):
        if self.text.get() == self.n or len(self.text.get()) == 0:
            self.valido['fg'] = 'red'
        else:
            if self.n == 'CPF':
                if len(self.text.get()) == 14:
                    self.valido['fg'] = 'green'
                else:
                    self.valido['fg'] = 'red'
            elif self.n == 'Senha':
                if len(self.text.get()) >= 8:
                    self.valido['fg'] = 'green'
                else:
                    self.valido['fg'] = 'red'
            else:
                self.valido['fg'] = 'green'

    def corrigi_cpf(self):
        self.text.insert(3, '.')
        self.text.insert(7, '.')
        self.text.insert(11, '-')

    def destroy(self):
        self.nome.destroy()
        self.text.destroy()

    def get(self):
        return self.text.get()
class Botao:
    def __init__(self, nome, frame, comando, tamanho=None, x=None, y=None):
        self.botao = Button(frame, text=nome)
        self.botao.bind('<Button-1>', comando)
        self.botao['bg'] = 'grey'
        self.botao['fg'] = '#fff'
        self.botao['width'] = tamanho
        self.botao.grid(column=x, row=y)
class Cadastro:
    def __init__(self, master):
        master.geometry('400x300+250+50')
        master.title('FlashAdverts\cadastro')
        c, r = 0, 3
        self.conteiner1 = Frame(master)
        self.conteiner1.grid(column=c, row=r - 3)
        self.conteiner2 = Frame(master)
        # Definindo os Objetos
        self.nome = Campotext(self.conteiner1, 'Nome de Usuário', c, r)
        self.email = Campotext(self.conteiner1, 'E-mail', c, r + 1)
        self.cpf = Campotext(self.conteiner1, 'CPF', c, r + 2)
        self.quadra = Campotext(self.conteiner1, 'Quadra', c, r + 3)
        self.lote = Campotext(self.conteiner1, 'Lote', c, r + 4)
        self.rua = Campotext(self.conteiner1, 'Rua', c, r + 5)
        self.numero = Campotext(self.conteiner1, 'Numero', c, r + 6)
        self.comp = Campotext(self.conteiner1, 'Complemento', c, r + 7)
        self.senha = Campotext(self.conteiner1, 'Senha', c, r + 8, '*')
        ########################   Botões   ###################
        self.conteiner2.grid(column=1, row=0)
        self.msg = Label(self.conteiner1, text='')
        self.msg.grid(column=1, row=14)
        self.cadastra = Botao('Cadastra', self.conteiner1, self.formulario, 10, 1, 15)
        self.login = Botao('Fazer Login', self.conteiner1, self.cria, 15, 1, 16)

    def formulario(self, event):
        self.nome.cor()
        self.email.cor()
        self.cpf.cor()
        self.quadra.cor()
        self.lote.cor()
        self.rua.cor()
        self.numero.cor()
        self.senha.cor()
        if len(self.cpf.get()) == 11:
            self.cpf.corrigi_cpf()
        dados = cursor.execute('select cpf, email from Usuario').fetchall()
        if dados == []:
            dados = [(None, None)]
        if self.cpf.get() not in dados[0] and self.email.get() not in dados[0] and self.cpf.get() != 'CPF' \
                and self.email.get() != 'E-mail' and self.nome.get() != 'Nome de Usuário' and self.quadra.get() != 'Quadra' \
                and self.lote.get() != 'Lote' and self.rua.get() != 'Rua' \
                and self.numero.get() != 'Numero' and self.senha.get() != 'Senha' and len(self.senha.get()) >= 8:

            self.msg['text'] = 'cadastro realizado com suscesso!'
            self.msg['fg'] = 'green'
            lista = [self.nome.get(), self.email.get(), str(self.cpf.get()), self.quadra.get(), self.lote.get()
                , self.rua.get(), self.numero.get(), self.comp.get(), self.senha.get()]
            cursor.execute('''insert into Usuario values(?,?,?,?,?,?,?,?,?,0)''', lista)
            cursor.commit()
        else:
            self.msg['text'] = 'Dados invalidos!'
            self.msg['fg'] = 'red'
        # cursor.execute("insert into Usuario values(' João', 20)")

    def cria(self, event):
        self.limpa()
        Login(root)
    def limpa(self):
        self.conteiner1.destroy()
        self.conteiner2.destroy()
class Login:
    def __init__(self, master):
        self.master = master
        master.title('FlashAdverts\Login')
        # master.geometry('300x200+250+50')
        self.conteiner1 = Frame(master)
        # self.conteiner2 = Frame(master)
        # self.conteiner2.grid(column=1,rowspan=3)
        self.conteiner1.grid(column=0, row=0)
        self.email = Campotext(self.conteiner1, 'Email ou CPF', 0, 0)
        self.senha = Campotext(self.conteiner1, 'Senha', 0, 1, '*')
        self.msg = Label(self.conteiner1, text=' ')
        self.msg.grid(column=1, row=3)
        self.cadastra = Botao('Cria Conta', self.conteiner1, self.cria, 10, 1, 5)
        self.login = Botao('Entra', self.conteiner1, self.logar, 5, 1, 4)

    def logar(self, event):
        self.senha.cor()
        dados = cursor.execute('select email,senha,cod_credito from Usuario where email=?',
                               [self.email.get()]).fetchall()
        if self.email.get() in dados[0]:
            self.email.cor()
        if dados != []:
            if self.senha.get() == dados[0][1]:
                self.msg['text'] = 'Senha Valida'
                self.limpa()
                Usuario(self.master, dados[0][2])
            else:
                self.msg['text'] = 'Senha Invalida!'
        else:
            pass

    def cria(self, event):
        self.limpa()
        Cadastro(root)

    def limpa(self):
        self.conteiner1.destroy()
        # self.conteiner2.destroy()
class Usuario:
    def __init__(self, master, user):
        master.geometry('400x300+250+50')
        self.conteiner1 = Frame(master, bg='#FACC2E')
        self.conteiner2 = Frame(master, bg='#848484')
        self.conteiner3 = Frame(master, bg='#FA58F4')
        # self.lista = Listbox(self.conteiner2)
        # self.lista.insert(END, 'teste')
        tm = 15
        self.img = PhotoImage(file='w.png')
        self.img = self.img.subsample(10,10)
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
        dados = cursor.execute('select saldo from Credito where cod_credito=?', [user]).fetchall()
        self.lb1 = Label(self.conteiner1,text='Saldo:', bg='blue',fg='#fff')
        self.saldo = Label(self.conteiner1,text=round(dados[0][0],2), bg='blue',fg='#fff')
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
        Login(root)
    def limpa(self):
        self.conteiner1.destroy()
        self.conteiner2.destroy()
        self.conteiner3.destroy()

root = Tk()
Cadastro(root)
#Usuario(root, None)
root.mainloop()
