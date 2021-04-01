"""
Min e Max

max() -> Retorna o maior valor em um iteravel ou o maior de dois ou mais elementos

# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))       # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))       # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))       # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))       # f

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))       # 129

# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))
print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'g'))
print(max(3.1415, 5.789))
print(max('Geek University'))

min() -> Retorna o menor valor em um iteravel ou o menor de dois ou mais elementos

# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))       # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))       # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))       # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))       # a

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))       # 1

# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))


print(min(4, 67, 54))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'g'))
print(min(3.1415, 5.789))
print(min('Geek University'))   # Espaço conta como menor valor


# Outros exemplos
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))       # Tim   -> Ordem alfabética
print(min(nomes))       # Arya  -> Ordem alfabética

print(max(nomes, key=lambda nome: len(nome)))   # Ollivander
print(min(nomes, key=lambda nome: len(nome)))   # Tim
# Exemplo

musicas = [
        {'titulo': 'Thunderstruck', 'tocou': 3},
        {'titulo': 'Dead Skin Mask', 'tocou': 2},
        {'titulo': 'Back in Black', 'tocou': 4},
        {'titulo': 'Too old ro rock'in'roll, too young to die', 'tocou': 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


# DESAFIO!! Imprima somente o título da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO!! Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['tocou'])

min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
for musica in musicas:
    if musica['tocou'] == min:
        print(musica['tocou'])

"""