"""
Generators

Em aulas anteriores, nós estudamos:
 - List Comprehension;
 - Dict Comprehension;
 - Set Comprehension;

Não vimos:
 - Tuple Comprehension... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes])

# Poderiamos ter feito utilizando Generators
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))


# Qual é a utilidade de getsizeof
from sys import getsizeof

# Mostra quantos bytes a string Geek está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(6541911))
print(getsizeof(True))


from sys import getsizeof

# Gerando uma lista de parametros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de parametros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de parametros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de parametros com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set COmprehension: {set_comp} bytes')
print(f'Dictionary COmprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

"""