from tkinter import *
import Campotext
import Botao
import banco
import Login
class Cadastro:
    def __init__(self,master):
        self.root=master
        master.geometry('400x300+250+50')
        master.title('FlashAdverts\cadastro')
        c, r = 0, 3
        self.conteiner1 = Frame(master)
        self.conteiner1.grid(column=c, row=r - 3)
        self.conteiner2 = Frame(master)
        # Definindo os Objetos
        self.nome = Campotext.Campotext(self.conteiner1, 'Nome de Usuário', c, r)
        self.email = Campotext.Campotext(self.conteiner1, 'E-mail', c, r + 1)
        self.cpf = Campotext.Campotext(self.conteiner1, 'CPF', c, r + 2)
        self.quadra = Campotext.Campotext(self.conteiner1, 'Quadra', c, r + 3)
        self.lote = Campotext.Campotext(self.conteiner1, 'Lote', c, r + 4)
        self.rua = Campotext.Campotext(self.conteiner1, 'Rua', c, r + 5)
        self.numero = Campotext.Campotext(self.conteiner1, 'Numero', c, r + 6)
        self.comp = Campotext.Campotext(self.conteiner1, 'Complemento', c, r + 7)
        self.senha = Campotext.Campotext(self.conteiner1, 'Senha', c, r + 8, '*')
        ########################   Botões   ###################
        self.conteiner2.grid(column=1, row=0)
        self.msg = Label(self.conteiner1, text='')
        self.msg.grid(column=1, row=14)
        self.cadastra = Botao.Botao('Cadastra', self.conteiner1, self.formulario, 10, 1, 15)
        self.login = Botao.Botao('Fazer Login', self.conteiner1, self.cria, 15, 1, 16)

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
        dados = banco.cursor.execute('select cpf, email from Usuario').fetchall()
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
            banco.cursor.execute('''insert into Usuario values(?,?,?,?,?,?,?,?,?,0)''', lista)
            banco.cursor.commit()
        else:
            self.msg['text'] = 'Dados invalidos!'
            self.msg['fg'] = 'red'
        # cursor.execute("insert into Usuario values(' João', 20)")

    def cria(self, event):
        self.limpa()
        Login.Login(self.root)
    def limpa(self):
        self.conteiner1.destroy()
        self.conteiner2.destroy()