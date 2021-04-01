"""
Transposta da matriz
"""
from random import randint


def transposta(matriz):
    for l in range(0, n):
        for c in range(0, n):
            print(f'[{matriz[c][l]}]', end='')
        print()
    return


n = int(input('Digite o a ordem da matriz: '))
matriz = []
for i in range(0, n):
    linha = []
    for j in range(0, n):
        linha.append(randint(0, 30))
    matriz.append(linha)
print('-'*20)
print('--------- Matriz Original -----------')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end='')
    print()
print('-'*20)
print('-------- Matriz Transposta ----------')
print(transposta(matriz))


