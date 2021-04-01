"""
Dicionários

Obs.: Em algumas linguagens de programação, os dicionários Pythn são conhecidos por mapas.

Dicionarios são coleções do tipo chave /valor.

Dicionarios são representados por chaves {}

print(type({}))

Obs.: Sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;
#Criação de dicionários
# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

#Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# Obs.: Caso tentemos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('ru'))     # None

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
russia = paises.get('ru')
if russia:
    print('Encontrei o país)
else:
    print(type(numeros))

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {py}')


# Podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionario, como chaves
de dicionarios.
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesmas
são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan':100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)   #receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# Conclusão 2 : Em dicionarios, NÃO podemos ter chaves repetidas

# Remover dados de um dicionario

# Forma 1 - Mais Comum
ret = receita.pop('mar')
print(ret)

print(receita)
#Obs.: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
#Obs.: Ao removermos um objeto, valor deste objeto é sempre retornado.

#Forma 2
del receita['fev']
print(receita)

# Se a chave não existir, será gerado um KeyError.
# Obs.: Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto1:
        - nome;
        - preço;
        - quantidade;
    Produto2:
        - nome;
        - preço;
        - quantidade;

# 1 - Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla para isso?  Sim
produto1 = ('Playstatio 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

#Teriamos que saber qual é o indice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informação


# Métodos de dicionarios

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario
d.clear()
print(d)

# Copiando um dicionario para outro

#Forma 1 #Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2 #Shallow Copy

novo = d

print(novo)
novo ['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a','b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome','pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#Obs.: O método fromkeys recebe dois parametros: um iteravel e um valor
#Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)


"""