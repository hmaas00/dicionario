# -*- coding: utf-8 -*-


def traduzir(texto, dicio):
    for k,v in dicio.items():
        texto= texto.replace(k,v)
    return texto
    

if __name__ == "__main__":
    print(soma(2,4))
    