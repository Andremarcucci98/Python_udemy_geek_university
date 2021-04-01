"""
Ler matriz 4x4 e contar quantos numeros maiores que 10 ela possui
"""
cont = 0
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para ({l},{c}): '))
        if matriz[l][c] > 10:
            cont += 1
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()

print(f'Quantidade de numeros maiores do que 10: {cont}')
