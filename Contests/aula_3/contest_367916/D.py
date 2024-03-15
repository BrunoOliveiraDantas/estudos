import math
# Função para obter o último dígito de um número
def ultimo_digito(numero):
    return numero % 10

def sol():

    lista_numeros = [int( input()) for _ in range(0,5)]
    lista_ordenada = sorted(lista_numeros, key=lambda x: (x % 10 == 0, ultimo_digito(x)), reverse=True)
    res = 0

    for num in lista_ordenada[:-1]:
        resto = num % 10 #9
        sobra = 0 if resto == 0 else  10 - resto  
        res += num + sobra

    res += lista_ordenada[4]
    return res
if __name__== "__main__":
    print(sol())