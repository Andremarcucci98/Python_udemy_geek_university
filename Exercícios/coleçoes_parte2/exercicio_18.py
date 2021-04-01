"""
Array com colunas da matriz
"""
array = []
soma = 0
from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('--------------------------')
for c in range(0, 3):
    for l in range(0, 3):
        soma += matriz[l][c]
    array.append(soma)
    soma = 0
print(array)