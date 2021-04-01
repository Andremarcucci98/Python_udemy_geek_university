"""
Somar elementos acima da diagonal principal
"""
from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 30)
        if l != c:
            if c > l:
                if l == 0:
                    soma += matriz[0][c]
                if l == 1:
                    soma += matriz[1][c]
                if l == 2:
                    soma += matriz[2][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma acima da diagonal principla foi de {soma}')