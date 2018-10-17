from tkinter import *
class Botao:
    def __init__(self, nome, frame, comando, tamanho=None, x=None, y=None):
        self.botao = Button(frame, text=nome)
        self.botao.bind('<Button-1>', comando)
        self.botao['bg'] = 'grey'
        self.botao['fg'] = '#fff'
        self.botao['width'] = tamanho
        self.botao.grid(column=x, row=y)