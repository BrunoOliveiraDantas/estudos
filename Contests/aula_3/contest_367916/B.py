def sol():
    lista = [int(n) for n in input().split()]
    lista_ordenada = sorted(lista)

    return lista_ordenada[0] + lista_ordenada[1]

    
if __name__== "__main__":
    print(sol())