"""
Funções para determinar se é triangulo
"""


def forma_triangulo(a, b, c):
    print()
    if a < b + c and b < a + c and c < b + a:
        if a == b == c:
            tipo = 'Equilátero'
        elif a == b or a == c or b == c:
            tipo = 'Isósceles'
        elif a != b != c:
            tipo = 'Escaleno'
        return f'Forma um triângulo do tipo \033[1;7;31m{tipo}\033[m'
    else:
        return f'\033[1;31mNão forma um triângulo\033[m'



lado1 = float(input('Digite lado 1: '))
lado2 = float(input('Digite lado 2: '))
lado3 = float(input('Digite lado 3: '))
while lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    if lado1 <= 0:
        lado1 = float(input('Digite um valor maior do que "0" para o lado 1: '))
    elif lado2 <= 0:
        lado2 = float(input('Digite um valor maior do que "0" para o lado 2: '))
    elif lado3 <= 0:
        lado3 = float(input('Digite um valor maior do que "0" para o lado 3: '))
print(f'Pelos valores digitados sabemos que:'
      f'\n{forma_triangulo(lado1, lado2, lado3)}')