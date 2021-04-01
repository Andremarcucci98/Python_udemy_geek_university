"""
Multiplicação de matrizes
"""
from random import randint


def multiplicacao_de_matrizes(matriz1, matriz2):
    m3 = []
    if n1 == n2:
        for l in range(n1):
            m3.append([])
            for co in range(n2):
                val = 0
                for k in range(n1):
                    val += matriz1[l][k] * matriz2[k][co]
                m3[l].append(val)
        return m3
    else:
        return f'Não é possivel efetuar a multiplicação da matrizes quadradas.'


def printamatriz(matriz):
    for m in range(len(matriz)):
        for n in range(len(matriz[m])):
            print(f'[{matriz[m][n]:^5}]', end=' ')
        print()
    return "FIM"


m1 = []
m2 = []
n1 = int(input('Digite a ordem da primeira matriz: '))
for i in range(0, n1):
    linha = []
    for j in range(0, n1):
        linha.append(randint(0, 5))
    m1.append(linha)

print('--------- Matriz 1 -----------')
for i in range(0, n1):
    for j in range(0, n1):
        print(f'[{m1[i][j]}]', end='')
    print()
print('-'*20)
print()

n2 = int(input('Digite a ordem da segunda matriz: '))
for i in range(0, n2):
    linha = []
    for j in range(0, n2):
        linha.append(randint(0, 5))
    m2.append(linha)

print('--------- Matriz 2 -----------')
for i in range(0, n2):
    for j in range(0, n2):
        print(f'[{m2[i][j]}]', end='')
    print()
print('-'*20)

print(f'{printamatriz(multiplicacao_de_matrizes(m1, m2))}')
