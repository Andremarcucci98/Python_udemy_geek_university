"""
Digitar um numero inteiro nao negativo e imprimir a soma dos n primeiros numeros primos
"""
soma = 0
n = int(input('Digite um numero inteiro positivo: '))
while n < 0:
    n = int(input('Digite um numero inteiro positivo: '))
for c in range(1, n + 1):
    div = 0
    for i in range(1, c+1):
        if c % i == 0:
            div += 1
    if div == 2:
        print(c, end='+')
        soma += c
print(f'= {soma}')