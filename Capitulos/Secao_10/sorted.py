"""
Sorted
Obs.: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona em Listas.
Podemos utilizar sorted() em qualquer iterável.
Como o próprio nome diz, sorted() serve para ordenar.

Obs.: O sorted() SEMPRE retorna uma Lista com os elementos do iterável ordenados

# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  #Ordenar do menor para maior
print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))    # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu adoro meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu adoro cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}
]

print(usuarios)
# Ordenando pelo username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

# Último Exemplo
musicas = [
        {'titulo': 'Thunderstruck', 'tocou': 3},
        {'titulo': 'Dead Skin Mask', 'tocou': 2},
        {'titulo': 'Back in Black', 'tocou': 4},
        {'titulo': 'Too old to rock'in'roll, too young to die', 'tocou': 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordenada da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
"""
