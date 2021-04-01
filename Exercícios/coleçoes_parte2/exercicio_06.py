"""
Matriz com maiores valores de duas outras matrizes
"""
from random import randint
maior = 0
matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_final = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('--------- Matriz 1 --------')
for l in range(0, 3):
    for c in range(0, 3):
        matriz1[l][c] = randint(0, 30)
        print(f'[{matriz1[l][c]:^5}]', end=' ')
    print()
print()
print('--------- Matriz 2 --------')
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = randint(0, 30)
        print(f'[{matriz2[l][c]:^5}]', end=' ')
    print()
print('---------------------------')

# Comparando valores
print('---- Matriz Resultante ----')
for l in range(0, 3):
    for c in range(0, 3):
        if matriz1[l][c] > matriz2[l][c]:
            matriz_final[l][c] = matriz1[l][c]
        else:
            matriz_final[l][c] = matriz2[l][c]
        print(f'[{matriz_final[l][c]:^5}]', end=' ')
    print()
print('---------------------------')
