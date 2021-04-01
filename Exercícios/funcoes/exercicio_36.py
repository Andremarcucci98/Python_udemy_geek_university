"""
Superfatorial
"""


def superfatorial(n):
    fatorial = 1
    superfat = 1
    for i in range(n, 0, -1):
        for j in range(i, 1, -1):
            fatorial = j * fatorial
        print(f'{i}!', end=' * ')
    return fatorial


num = int(input('Digite um numero para saber seu superfatorial: '))
print(f'\nO super fatorial de {num} é {superfatorial(num)}')