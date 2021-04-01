"""
Maior e menor valor
"""


def maior_valor(a, b):
    if a > b:
        return a
    elif a == b:
        return a
    else:
        return b


def menor_valor(a, b):
    if a > b:
        return b
    elif a == b:
        return a
    else:
        return a


num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
print(f'Dentre os valores digitados o maior é {maior_valor(num1, num2)} e o menor valor é '
      f'{menor_valor(num1, num2)}')
