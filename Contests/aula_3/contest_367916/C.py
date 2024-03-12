import math

def sol():

    lista = []
    
    for i in range(0, 5):
        lista.append(int(input()))
    lista_ordenada = sorted(lista)

    penultimo = lista_ordenada[0]
    ultimo = lista_ordenada[4]
    minsub = ultimo - penultimo

    k = int(input())

    return ':(' if minsub > k else 'Yay!'

if __name__== "__main__":
    print(sol())