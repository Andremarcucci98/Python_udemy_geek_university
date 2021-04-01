"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
Dinâmicos e também de podermos colocar QUALQUER tipo de dado.

Já em Python:
- Dinâmico: Não possui tamanho fixo; Ou seja podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: As listas possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis

type([])
lista1 = [1, 99, 4, 27, 15, 44, 22, 27]
lista2 = ['G', 'e', 'k', 'j', 'u', 't']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Podemos facilmente checar se determinado valor está contido em determinada lista
num = 18
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

#Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

Obs.: Com append, nós só conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

# Obs.:Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) Erro!!

lista1.append([8, 3, 1])        #Coloca a lista com elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])       # Coloca cada elemento da lista como valor adicionar à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Obs.: Isso não substitui o valor inicial . O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
#lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista
#Forma1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
#Forma2
print(lista1[::-1])
print(lista2[::-1])
print(lista1)
print(lista2)

#Podemos facilmente conseguir o numero de elementos dentro da lista
print(len(lista3))

#Podemos remover facilmente remover o ultimo elemento de uma lista
Obs.: O pop não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# Obs.: Os elementos á direita deste índice serão deslocados para esquerda
# Obs.: Se não houver elemento no índice informado, teremos erro IndexError
lista5.pop(2)
print(lista5)

# Não podemos remover todos os elementos (zerar os elementos)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo1
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#Obs.:Por padrão, o split separa os elemtnso da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#Exemplo 3
# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)
# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

#Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 46148]

# Iterando sobre listas
# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair'
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizar variáveis em listas
numeros [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

#Fazemos acesso aos elementos de forma indexada
#           0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista com um círculo, onde
o final de um elemento está ligado ao início da lista

print(cores[-1])    #branco
print(cores[-2])    #azul
print(cores[-3])    #amarelo
print(cores[-4])    #verde
print(cores[-5])    # Erro, pois não existe índice -5

# Exemplo
cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

#Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(32)
lista.append(32)
lista.append(42)
print(lista)

#Outros métodos não tão importantes mas também úteis
# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]
#Em qual índice da lista está o valor 6?
print(numeros.index(6))
#Em qual índice da lista está o valor 9?
print(numeros.index(6))

#Obs.: Caso não tenha este elemento na lista, será apresentado erro ValueError

print(numeros.index(5)) # Retorna o índice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual índice começa a buscar
print(numeros.index(5, 1))  #buscando a partir do índice 1
print(numeros.index(5, 2))  #buscando a partir do índice 2
print(numeros.index(5, 3))  #buscando a partir do índice 3
print(numeros.index(5, 4))  #buscando a partir do índice 4
# Obs.: Caso não tenha este elemento na lista, será apresentado erro ValueError

#Podemos fazer busca dentro de um range, início/fim
print(numeros.index(8, 3, 6)    #Buscar o índice do valor8, entre os índices 3 a 6

# Revisão de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

#Trabalhando com slice de lista com o parâmetro 'início'
lista = [1, 2, 3, 4]
print(lista[1:])     #Iniciando no índice 1 e pegando todos os elementos restantes

#Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2])    #Começa em 0, pega até o índice 2 - 1

print(lista[:4])    #Começa em 0, pega até o índice 4 - 1

print(lista[1:3])    #Começa em 1, pega até o índice 3 - 1

# Trabalho com slice de lista com o parâmetro 'passo'
print(lista[1::2]) #Começa em 1, vai até o final, de 2 em 2
print(lista[::2]) #Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nome = ['Geek', 'University']

nomes[0] , nomes[1] = nomes[1], nomes[0]
print(nomes)
nome = ['Geek', 'University']
nome.reverse()
print(nome)

# Soma", "Valor Máximo", "Valor mínimo", Tamanho
# " Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))   #soma
print(max(lista))   #máximo valor
print(min(lista))   #mínimo valor
print(len(lista))   #tamanho da lista

# Transformar uma lista em uma tupla

lista = [1, 2, 3, 4, 5]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#Desempacotamento de listas

lista = [1, 2, 3, 4, 5]
num1 = num2 = num3 = lista
print(num1)
print(num2)
print(num3)

#Obs.: Se tivermos um número diferente de elementos na lista ou variaveis para receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

#Veja que ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
é chamado Deep Copy (cópia profunda)

Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

niva = lista    #copia
print(nova)
nova.append(4)

print(lista)
print(nova)
#Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas
após realizar modificações em uma das listas, essa modificação se refletiu em ambas as listas.
Isso em Python é chamado de Shallow Copy.
"""
