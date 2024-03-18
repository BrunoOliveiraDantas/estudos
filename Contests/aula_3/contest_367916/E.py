def sol():

    n = int(input())
    lista_h = [int(n) for n in input().split()]
    qtd_inns = 0

    for i in range(1, n):
        if(lista_h[0] <= lista_h[i]):
            if(lista_h[i-1] <= lista_h[i]):
                qtd_inns += 1
    return qtd_inns +1

    
if __name__== "__main__":
    print(sol())