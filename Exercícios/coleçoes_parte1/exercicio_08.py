"""
Lê 6 valores inteiros e mostra na tela os valores lidos na ordem inversa
"""
from random import randint
lista = []
for i in range(0, 6):
    lista.append(randint(0, 8))
print(lista)
lista.reverse()
print(lista)