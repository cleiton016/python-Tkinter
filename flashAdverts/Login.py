from tkinter import *
import Campotext
import Botao
import banco
import Login
import usuario
import Cadastro
class Login:
    def __init__(self, master):
        self.root = master
        master.title('FlashAdverts\Login')
        # master.geometry('300x200+250+50')
        self.conteiner1 = Frame(master)
        # self.conteiner2 = Frame(master)
        # self.conteiner2.grid(column=1,rowspan=3)
        self.conteiner1.grid(column=0, row=0)
        self.email = Campotext.Campotext(self.conteiner1, 'Email ou CPF', 0, 0)
        self.senha = Campotext.Campotext(self.conteiner1, 'Senha', 0, 1, '*')
        self.msg = Label(self.conteiner1, text=' ')
        self.msg.grid(column=1, row=3)
        self.cadastra = Botao.Botao('Cria Conta', self.conteiner1, self.cria, 10, 1, 5)
        self.login = Botao.Botao('Entra', self.conteiner1, self.logar, 5, 1, 4)

    def logar(self, event):
        self.senha.cor()
        dados = banco.cursor.execute('select email,senha,cod_credito from Usuario where email=?',
                                     [self.email.get()]).fetchall()
        if self.email.get() in dados[0]:
            self.email.cor()
        if dados != []:
            if self.senha.get() == dados[0][1]:
                self.msg['text'] = 'Senha Valida'
                self.limpa()
                usuario.Usuario(self.root, dados[0][2])
            else:
                self.msg['text'] = 'Senha Invalida!'
        else:
            pass

    def cria(self, event):
        self.limpa()
        Cadastro.Cadastro(self.root)

    def limpa(self):
        self.conteiner1.destroy()
        # self.conteiner2.destroy()