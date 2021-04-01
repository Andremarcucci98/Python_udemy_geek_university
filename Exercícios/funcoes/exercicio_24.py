"""
Função que gera um triangulo de altura e lados n e base 2 * n - 1
"""


def triangulo(n=6):
    list(print(' ' * (n - i) + ('*' * (2 * i - 1))) for i in range(1, n+1))


a = int(input('Digite um valor para a altura: '))
triangulo(a)
