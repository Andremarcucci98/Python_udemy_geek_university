"""
Ler notas de 10 alunos em 3 provas. Retornar o numero de alunos com piores notas em cada prova.
"""
from random import randint
from collections import Counter


def pior(lista):
    return lista.index(min(lista))


notas_prova = [[randint(0, 10) for _ in range(3)] for _ in range(10)]
print(notas_prova)

pior_prova = [pior(notas_prova[i]) for i in range(10)]

for k in range(3):
    print(f'Qtd de alunos que foi pior na prova {k}: {Counter(pior_prova)[k]}')