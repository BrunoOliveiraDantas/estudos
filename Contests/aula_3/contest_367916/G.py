def solucao_correta():
    str = input()

    sample = '10' * 50001

    print(min(sub(str, sample), sub(str, sample[1:])))

def sub(s, t):
    c = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            c += 1
    return c

def sol():
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
        else:
            posicao_anterior = digito

    return qtd_tiles


if __name__== "__main__":
    print(sol())