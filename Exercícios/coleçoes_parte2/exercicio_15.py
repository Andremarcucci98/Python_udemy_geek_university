"""
Comparando com gabarito
"""
import random
gabarito = ('b', 'd', 'd', 'a', 'c', 'c', 'd', 'b', 'b', 'a')
matriz = list()
respostas = list()
resultado = list()
for l in range(5):
    linha = []
    for c in range(10):
        linha.append(random.choice('abcd'))
    matriz.append(linha)
print('Gabarito:')
print('b,   d,   d,   a,   c,   c,   d,   b,   b,   a')
print('-x'*30)
print('Matriz das notas. Aluno x Resposta')
for l in range(5):
    for c in range(10):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()
for l in range(len(matriz)):
    for c in range(10):
        if matriz [l][c] == gabarito[c]:
            respostas.append(1)
        else:
            respostas.append(0)
    resultado.append(list(respostas))
    respostas.clear()
for i in range(5):
    nota = resultado[i].count(1)
    print(f'O aluno {i+1} acertou {nota} e errou {10 - nota} questões')


