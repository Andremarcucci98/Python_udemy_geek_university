"""
Triangulo de Floyd
"""
num = int(input('Digite um numero de linhas: '))
m = 1
for c in range(1, num+1):
    for i in range(1, c+1):
        print(f'{m:<4}', end= '')
        m += 1
    print()
