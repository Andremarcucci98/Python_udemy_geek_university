cont = 0
lista_dicionario = []
while True:
    variavel = 'variavel_' + str(cont)
    # valor pode ser substituido por pegar valor automaticamente
    valor = input('Digite valor: ')
    if valor:
        lista_dicionario.append({variavel: valor})
        cont += 1
    else:
        break
# Verificando se está tudo certo
print('---------------------------')
for i in lista_dicionario:
    for chave, valor in i.items():
        print(f'{chave} = {valor}')
print('--------------------------')

