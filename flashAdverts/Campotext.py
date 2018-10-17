from tkinter import *
from entryPlaceholder import *
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