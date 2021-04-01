"""
Verificar se o numero é quadrado perfeito
"""


def quadrado_perfeito(n):
    if n == int(n) and n != 0:
        raiz = n ** 0.5
        if raiz == int(raiz) and n > 0:
            return f'O número {n} é um quadrado perfeito'
        else:
            return f'O número {n} não é um quadrado perfeito'


n = int(input('Digite um valor para saber se é quadrado perfeito: '))
print(quadrado_perfeito(n))