"""
Maior valor da matriz
"""
from random import randint
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior = 0
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = randint(0, 40)
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
for l in range(0, 4):
    for c in range(0, 4):
        if c == l == 0:
            maior = matriz[l][c]
        else:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print('-'*30)
print(f'O maior valor foi \033[1;36m{maior}\033[m')