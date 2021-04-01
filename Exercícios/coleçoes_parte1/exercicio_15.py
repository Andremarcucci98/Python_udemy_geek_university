"""
Ler 20 números inteiros e escrever vetor eliminando elementos repetidos
"""
from random import randint
lista = []
for i in range(0, 20):
    lista.append(randint(0, 10))
print('-'*5,'VALORES ORIGINAIS', '-'*5)
print(lista)
unicos = list(set(lista))
print('-'*5,'VALORES ÚNICOS', '-'*5)
print(unicos)
print('-'*5,'VALORES DUPLICADOS', '-'*5)
duplicados = list(set([x for x in lista if lista.count(x) > 1]))
print(duplicados)