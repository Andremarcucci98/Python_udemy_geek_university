"""
Mapas
Conhecido em Python como dicionarios
Dicionarios em Python são representado por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

# Acessando as chaves
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios

for chave, valor in receita.itens():
    print(f'chave={chave} e valor={valor}')

# Soma', Valor Máximo', Valor Minimo', Tamanho
# ' Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""