"""
Ler número inteiro positivo ímpar e imprimir todos os números ímpares de 1 até N

"""

num = int(input('Digite um numero impar positivo: '))
while num < 0 or num%2 != 1:
    if num%2 != 1 or num < 0:
        num = (int(input('Digite um número ímpar positivo: ')))
    else:
        break
for n in range(num, -1, -2):
    print(n, end=' ')

