"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos da Matemática.
- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na Matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionarios) em Python:
- Um Dicionario tem chave/valor;
- Um conjunto tem apenas valor;

# Definindo um conjunto:

#Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})    #Repare que temos valores repetidos
print(s)
print(type(s))

#Obs.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que além de nao termos valores duplicados, não temos ordem
# Tuplas aceitam valores duplicados
tupla = 99, 2, 34, 25, 84, 62, 2, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Listas aceitam valores duplicados
lista = [99, 2, 34, 25, 84, 62, 2, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Dicionarios nao aceitam valores duplicados
dicionario = {}.fromkeys([99, 2, 34, 25, 84, 62, 2, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados
conjunto = {99, 2, 34, 25, 84, 62, 2, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')        # NÃO TEMOS ORDEM

# Asssim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

#Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', ' São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos
# O que você faria? Faria um loop na lista??

#Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4)    # Duplicidade não gera erro, simplesmente é ignorado e não é adicionado
print(s)

# Remover elementos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1
s.remove(33)    #NÃO é indice! Informamos o valor a ser removido
print(s)

#Obs.: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2
s.discard(2)
print(s)

#Obs.: Se o valor não for encontrado, nenhum erro é gerado


# Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

#Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso de python e um
# contendo estudantes de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java

#Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# {'Marcos', 'Ana', 'Gustavo', 'Patricia', 'Fernando', 'Pedro', 'Guilherme', 'Ellen', 'Julia'}

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)
# {'Julia', 'Gustavo', 'Guilherme', 'Marcos', 'Ellen', 'Ana', 'Fernando', 'Patricia', 'Pedro'}


# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)
# {'Patricia', 'Pedro', 'Ellen', 'Gustavo', 'Guilherme', 'Ana', 'Julia', 'Marcos', 'Fernando'}


# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma', Valor Máximo', Valor Mínimo', Tamanho
# ' Se os valores forem todos inteiros ou reais

print(sum(s))
print(max(s))
print(min(s))
print(len(s))


"""