"""
Desenhar linhas
"""


def desenho_exclamacoes(n):
    lista = [n * '!' for n in range(1, n+1)]
    for i in lista:
        print(i)


desenho_exclamacoes(int(input('Digite o numero de linhas: ')))