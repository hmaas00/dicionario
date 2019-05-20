# -*- coding: utf-8 -*-
	

import tkinter as tk
from leitor.Montador import Montador
import leitor.Tradutor as tradutor


window = tk.Tk()
 
window.title("Tradutor")
 
window.geometry('700x600')

def clicked():
    montador = Montador( fonte_dic_input.get(), sep_input.get())
    dic =montador.montar_dicionario()
    x = txt.get('1.0', tk.END)
    res = tradutor.traduzir(x,dic)
    
    txt2.delete('1.0', tk.END)
    txt2.insert('1.0', res)

label_fonte = tk.Label(window, text="arquivo fonte do dicionário")
fonte_dic_input = tk.Entry(window)
fonte_dic_input.insert(0, "fonte.txt")

label_sep = tk.Label(window, text="separador do dicionário")
sep_input = tk.Entry(window)
sep_input.insert(0, ":")

#e.delete(0, END)
#e.insert(0, "a default value")

txt = tk.scrolledtext.ScrolledText(window,width=80,height=15)
txt2 = tk.scrolledtext.ScrolledText(window,width=80,height=15)
 
btn = tk.Button(window, text="traduzir", command=clicked)

label_fonte.grid(column=0,row=0,  sticky = tk.E)
fonte_dic_input.grid(column=1,row=0,  sticky = tk.W)

label_sep.grid(column=0,row=1,  sticky = tk.E)
sep_input.grid(column=1,row=1,  sticky = tk.W)

                     
txt.grid(column=0,row=2, columnspan=2)

btn.grid(column=0,row=3, columnspan=2)

txt2.grid(column=0,row=4, columnspan=2)
 
window.mainloop()