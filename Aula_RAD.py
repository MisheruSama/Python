from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        self.janela_principal=Tk()
        self.botao=Button(self.janela_principal, text='Clique Aqui', command=self.hello_world)
        self.botao_sair=Button(self.janela_principal, text='Sair', command=self.quit)
        self.botao.pack()
        self.botao_sair.pack()
        self.janela_principal.mainloop()
    def quit(self):
        self.janela_principal.destroy()
    def hello_world(self):
        messagebox.showinfo('Aula de RAD!', 'Olá Mundo!')
gui=MinhaGUI()
