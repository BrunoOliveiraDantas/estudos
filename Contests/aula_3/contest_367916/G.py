def sol():

    #tiles = input()
    #tiles.replace("00", "01").replace("11", "10")
    digitos = [int(n) for n in input()]
    qtd_tiles = 0
    posicao_anterior = digitos[-1]

    for digito in reversed(digitos[:-1]):
   
        if posicao_anterior == digito:
            qtd_tiles += 1
            if digito == 1:
                posicao_anterior = 0
            if digito == 0:
                posicao_anterior = 1

    return qtd_tiles

   
    
if __name__== "__main__":
    print(sol())