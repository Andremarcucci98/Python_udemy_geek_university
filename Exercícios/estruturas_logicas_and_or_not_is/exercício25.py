"""
Equação de 2°grau
"""
import math
a = int(input('Digite os coeficiente de a: '))
while a == 0:
    a = int(input('Digite um valor válido para a : '))
b = int(input('Digite o coeficiente de b: '))
c = int(input('Digite o coeficiente de c: '))
print(f'Equação digitada {a}x^2 + {b}x + {c}')
delta = b**2 - 4*a*c
if delta < 0:
    print('Não existe raiz real')
elif delta == 0:
    x = (-b+math.sqrt((b**2-4*a*c))/2*a)
    print(f'Existe apenas uma raíz real, sendo ela {x}')
else:
    x1 = (-b+math.sqrt(((b**2)-(4*(a*c))))/(2*a))
    x2 = (-b-math.sqrt(((b**2)-(4*(a*c))))/(2*a))
    print(f'A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}')