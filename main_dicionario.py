# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from leitor.Montador import Montador
import leitor.Tradutor as tradutor


#f = open("texto.txt")
#
#dic = {}
#for i in f:
#    s=i.split(sep=":")
#    dic[s[0]] = s[1].replace("\n","")
   
montador = Montador("texto.txt", ":")
dic =montador.montar_dicionario()

t="daeb"

res = tradutor.traduzir(t,dic)

print(res)