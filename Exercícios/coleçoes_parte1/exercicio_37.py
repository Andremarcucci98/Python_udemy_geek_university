"""
Ordenar lista com numeros (crescente até sexto elemento e depois decrescente até décimo primeiro elemento)
"""
lista = list()
for tamanho1 in range(0, 6):
    numero = int(input('Digite um numero: '))
    if tamanho1 == 0:
        lista.append(numero)
    elif numero > lista[len(lista)-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(lista)
for tamanho2 in range(0, 5):
    numero2 = int(input('Digite um numero: '))
    pos = 5
    if tamanho2 == 0:
        if numero2 < lista[len(lista)-1]:
            lista.append(numero2)
        elif numero2 > lista[len(lista)-1]:
            lista.insert(pos, numero2)
    elif numero2 < lista[len(lista)-1]:
        lista.append(numero2)
    else:
        while pos < len(lista):
            if numero2 >= lista[pos]:
                lista.insert(pos, numero2)
                break
            pos += 1
print(lista)

