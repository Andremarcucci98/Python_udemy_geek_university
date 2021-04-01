"""
100 primeiros valores multiplos de 7 ou que terminam com 7
"""
cont = 0
i = 1
lista = []
while cont < 100:
    if i % 7 == 0 or i % 10 == 7:
        lista.append(i)
        cont += 1
    i += 1
print(lista)
print(len(lista))