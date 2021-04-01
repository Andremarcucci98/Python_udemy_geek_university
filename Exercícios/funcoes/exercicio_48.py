"""
Soma dos elementos acima da diagonal principal da matriz
"""
from random import randint


def soma_diag_superior(matriz):
    acima_diagonal_principal = []
    for l in range(0, 3):
        for c in range(0, 3):
            if l < c:
                acima_diagonal_principal.append(matriz[l][c])
    return f'A soma dos delementos acima da diagonal principal possui valor: {sum(acima_diagonal_principal)}'


matriz1 = []
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(randint(0, 10))
    matriz1.append(linha)
print('-'*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz1[i][j]}]', end='')
    print()
print('-'*20)
print(soma_diag_superior(matriz1))
