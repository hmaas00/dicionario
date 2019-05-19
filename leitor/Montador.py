# -*- coding: utf-8 -*-


class Montador:
    
    def __init__(self, caminho, sep):
        
        self.caminho_fonte = caminho
        self.separador = sep
        
        
    def montar_dicionario(self):
        f = open(self.caminho_fonte)
        dic = {}
        for i in f:
            s=i.split(sep= self.separador)
            dic[s[0]] = s[1].replace("\n","")
        return dic

