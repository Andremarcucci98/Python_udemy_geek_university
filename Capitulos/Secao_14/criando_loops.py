"""
Criando sua própria versão de loop

# Quando fazemos isso
for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

# O Python está fazendo:

iter([1, 2, 3, 4, 5])

iter('Geek University')

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5, 6]
meu_for(numeros)
"""

