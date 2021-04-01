"""
Matriz 10 x 10
A[i][j] = 2i + 7j - 2 se i<j
A[i][j] = 3i**2 - 1 se i=j
A[i][j] = 4i**3 - 5j**2 + 1 se i>j
"""
matriz = []
linha = []
l = int(input('Digite o número de linhas da matriz: '))
c = int(input('Digite o número de colunas da matriz: '))
for c1 in range(1, l+1):
    for c2 in range(1, c+1):
        if c1 < c2:
            linha.append(2*c1+7*c2-2)
        elif c1 == c2:
            linha.append((3*c1**2)-1)
        elif c1 > c2:
            linha.append((4*c1**3)-(5*c2**2)+1)
    matriz.append(linha)
    linha = []

print('----------Matriz Resultante--------------')
for c1 in range(0, l):
    for c2 in range(0, c):
        print(f'{matriz[c1][c2]:^5}', end=' ')
    print()
print('--------------------------')