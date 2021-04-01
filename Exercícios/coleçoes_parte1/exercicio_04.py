"""
Ler um vetor de 8 posições, Ler dois valores X e Y quaisquer correspondentes a duas posições no vetor.
Ao final escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""
from random import randint
soma = 0
lista = []
for i in range(0, 8):
    lista.append(randint(0, 9))
x = randint(0, 8)
print(lista)
print(x)
soma += lista[x]
print(soma)
lista.pop(x)
y = randint(0, 7)
print(lista)
print(y)
soma += lista[y]
print(soma)
