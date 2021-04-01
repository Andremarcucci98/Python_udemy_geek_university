"""
Triangulo de Pascal
"""
triangulo = [1]
l = int(input('Digite o numero de linhas: '))
for i in range(l):
    print("Row", i+1, triangulo)
    newlist = []
    newlist.append(triangulo[0])
    for j in range(len(triangulo)-1):
        newlist.append(triangulo[j] + triangulo[j+1])
    newlist.append(triangulo[-1])
    triangulo = newlist

