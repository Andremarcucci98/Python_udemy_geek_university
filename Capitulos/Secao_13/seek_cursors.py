"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo

arquivo = open('texto.txt')
print(arquivo.read())


# Movimentando o cursor pelo arquivo com a função seek()
# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro
arquivo.seek(0)
print(arquivo.read())


# readline() -> Função que lê o arquivo linha a linha

print(arquivo.readline())       # Imprimiu a primeira linha

print(arquivo.readline())       # Imprimiu a segunda linha

print(arquivo.readline())       # Imprimiu a terceira linha


# readlines()

linhas = arquivo.readlines()

print(len(linhas))



# Obs.: Quando abrimos um arquivo com a função open() é criada uma conexao entre o arquivo no disco
do computador e o nosso programa. Essa conexao é chamada de streaming. Ao finalizar os trabalhos
com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo
arquivo = open('texto.txt')

2 - Trabalhar o arquivo:
print(arquivo.read())

print(arquivo.closed())     # False - Verifica se o arquivo está aberto ou fechado

3 - Fechar o arquivo:
arquivo.close()

print(arquivo.closed)       # True - Verifica se o arquivo está aberto ou fechado

print(arquivo.read())

# Obs.: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError



arquivo = open('texto.txt')
# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))

Eu estou estudando na Geek University e estou apre
"""