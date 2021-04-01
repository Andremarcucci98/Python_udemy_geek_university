"""
Escrevendo em arquivos

# Obs.: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler, e vice-versa.

# Obs.: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

# Obs.: Para escrevermos um dado em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

# Exemplo de escrita - modo 'w' - write (escrita)
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n)
    arquivo.write('Podemos colocar quantas linhas quisermos.\n)
    arquivo.write('Esta é a ultima linha.')

with open('novo.txt', 'w') as aquivo:
    arquivo.write('Novos dados.\n)
    arquivo.write('Outos podemos colocar quantas linhas quisermos\n)
    arquivo.write('Esta é a ultima linha.')

# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista,
o anterior será apagado e um novo será criado. Dessa forma, todo o conteudo no arquivo anterior é perdido.

# Forma tradicional de escrita em arquivo - NÃO Pythonica
arquivo = open('texto.txt','w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')
arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)



"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
