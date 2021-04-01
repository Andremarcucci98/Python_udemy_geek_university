"""
Modos de abertura de arquivos

r -> Abre para leitura - padrão.
w -> Abre para escrita - sobrescreve caso o arquivo ja exista.
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError.
a -> Abre para escrita, adicionando o conteudo ao final do arquivo SEMPRE.Com o modo 'a', não controlamos os cursor
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

# Obs.: Abrindo com 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo será
adicionado ao final.

http://docs.python.org/3/library/functions.html#open

# Exemplo com 'x'
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2.\n')
except FileExistsError:
    print('Arquivo já existe')


# Exemplo com 'a'
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Mais um linha.\n')
    arquivo.write('Outra linha.\n')

# Exemplos com 'r+'
with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Novo topo!\n')
    arquivo.write('Mais uma nova linha.\n')
    arquivo.write('Outra linha.\n')

with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Novo topo!\n')
    arquivo.seek(11)
    arquivo.write('Mais uma nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Outra linha.\n')
"""
