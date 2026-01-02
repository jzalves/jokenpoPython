import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def escolheu_pedra():
    jokenpo('pedra')


def escolheu_papel():
    jokenpo('papel')


def escolheu_tesoura():
    jokenpo('tesoura')

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(["pedra", "papel", "tesoura"])

    if escolha_usuario == escolha_computador:
        mensagem=f'''
                Você: {escolha_usuario.upper()}
                EU: {escolha_computador.upper()}

                Resultado: Empate!!!
        '''
    elif(escolha_usuario == 'pedra' and escolha_computador=='tesoura') or (escolha_usuario == 'papel' and escolha_computador == 'pedra') or (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        mensagem=f'''
                Você: {escolha_usuario.upper()}
                EU: {escolha_computador.upper()}

                Resultado: Você Ganhou!!!
        '''
    else:
        mensagem=f'''
                Você: {escolha_usuario.upper()}
                EU: {escolha_computador.upper()}

                Resultado: Você Perdeu!!!


        '''
    resultado.config(text=mensagem)   





janela = tk.Tk()
janela.resizable(False, False)


frame = LabelFrame(janela, text = "Qual você escolhe?", padx=10, pady = 10)
frame.pack()

icone_pedra = PhotoImage(file='png/pedra.png')
icone_papel = PhotoImage(file='png/papel.png')
icone_tesoura = PhotoImage(file='png/tesoura.png')

Button(frame, text="Pedra", command=escolheu_pedra, image=icone_pedra,compound=tk.LEFT).grid(column=0, row=1)
Button(frame, text="Papel", command=escolheu_papel, image=icone_papel,compound=tk.LEFT).grid(column=2, row=1)
Button(frame, text="Tesoura", command=escolheu_tesoura, image=icone_tesoura,compound=tk.LEFT).grid(column=3, row=1)

resultado= Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=
3)

janela.title("Pedra, Papel e Tesoura")
janela.geometry("500x200+700+200")
janela.mainloop()

