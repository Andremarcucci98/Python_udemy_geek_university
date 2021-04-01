"""Programa lê 10 numero inteiros, descarta numeros negativos e calcula média"""
media = soma = num = cont = cont2 =0
while cont < 10:
    num = int(input('Digite um numero: '))
    if num < 0:
        soma = soma
    else:
        soma += num
        cont2 += 1
    cont += 1
media = soma/cont2
print(f'A média obtida de {cont2} numeros validos será de: {media} ')
