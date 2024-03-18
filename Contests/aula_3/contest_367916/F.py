def sol():

    n = int(input())
    lista_numeros = [int(n) for n in input().split()]
    lista_ordenada = sorted(lista_numeros)

    indice_central = (n // 2) - 1
    if n % 2 != 0:
        indice_central = (n // 2)

    lista_anterior = []
    lista_posterior = []
    lista_result = []
   
    for i in range(indice_central, n):
        
        valor_anterior_aux = 0
        valor_posterior_aux = 0
        for j in range(0 , i):
            
            valor_anterior_aux += lista_ordenada[j]
        lista_anterior.append(valor_anterior_aux)

        for k in range(i, n):
            valor_posterior_aux += lista_ordenada[k]
        lista_posterior.append(valor_posterior_aux)

    if n % 2 != 0:
        tamanho = len(lista_anterior)
    else: tamanho = len(lista_anterior)-1
    
    for l in range(0, tamanho):
        print("Lista anterior", lista_anterior)
        print("Lista posterior", lista_posterior)
        if(lista_anterior[l] >= lista_posterior[l]): lista_result.append(lista_anterior[l] - lista_posterior[l])
        else: lista_result.append(lista_posterior[l] - lista_anterior[l])

    return min(lista_result)

    
if __name__== "__main__":
    print(sol())