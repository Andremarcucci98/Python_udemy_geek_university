"""
Programa deve possuir um vetor A que armazene 6 numeros inteiros
"""

A = [1, 0, 5, -2, -5, 7]
print(type(A))
soma = A[0] + A[1] + A[5]
print(soma)

A.insert(4, 100)
print(A)
A.pop(5)
print(A)

for indice, valor in enumerate(A):
    print(f'indice:{indice} | valor:{valor}')
