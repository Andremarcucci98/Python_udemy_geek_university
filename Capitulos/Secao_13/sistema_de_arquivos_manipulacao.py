"""
Sistema de Arquivos - Manipulação

import os

#Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('frutas.txt'))     # True
print(os.path.exists('arquivo.txt'))    # False

# Diretório
# Paths relativos
print(os.path.exists('geek'))       # True
print(os.path.exists('geek/university'))    #True
print(os.path.exists('geek/university/geek3.py'))    #True
print(os.path.exists('outro'))      # False

# Paths absolutos
print(os.path.exists('/home/geek/university'))  # False
print(os.path.exists('/home/geek/Imagens'))  # False
print(os.path.exisys('/home/geek/Imagens/wallpaper2.png'))  # False


# Criando arquivos

# Forma 1
open('arquivotexte.txt', 'w').close()

# Forma 2
open('arquivoteste2.txt', 'a').close()

# Forma 3
with open('arquivoteste3.txt', 'w') as arquivo:
    pass

os.mknod('arquivoteste4.txt')
os.mknod('/home/geek/university.txt')

# Se você estiver usando no MAC OS, pode haver um erro de PermissionError

# OSB.: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - unicos (um a um)

# Path relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/home/geek/templates')

# OBS.: A função mkdir() cria um diretorio se este nao existir. Caso contrario, teremos FileExistsError

os.mkdir('/etc/templates')
# Obs.: Se não tivermos permissão para criar o diretorio teremos um PermissionError

os.mkdir('templates')
os.mkdir('templates/geek')
os.mkdir('templates/geek/university')

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university')

# Obs.: Se já existir, teremos um FileExistsError

os.makedirs('templates2/bovo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios

os.rename('templates2', 'geek2')

os.rename('geek2/novo2', 'geek2')
# Obs.: Se o diretorio nao existir teremos um FileNotFoundError

#Obs.: Se o diretorio que queremos renomear não estiver vazio, teremos um OSError

# Renomear arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO!! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para
a lixeira, Eles somem.

os.remove('geek.txt')

#Obs.: Se você estiver no Windows e o arquivo que vc for deletar estiver em uso, você terá um erro.

# Obs.: Caso o arquivo não exista, teremos o FileNotFoundError

#Obs.: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError


# Removendo Diretorios varios

os.rmdir('templates')
# Obs.: Se o diretorio tiver qualquer outro conteudo, teremos um OSError

# OBS.: Se o diretório não existir, teremos m FileNotFoundError


# Removendo uma arvore de diretorios
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():


# Podemos remover uma arvore de diretorios vazios

os.removerdirs('geek2/outro/mais')
# Se algum dos diretorios contiver arquivos ou diretorios, o processo para.

# ATENÇÃO! Ao remover arquivos e diretorios eles não vão para a lixeira. Eles vão embora.
sudo apt-get install lsb-core
pip install send2trash

# Importando a biblioteca send2trash    (Envia arquivos e diretórios para a lixeira)

from send2trash import send2trash
os.remove('cesta1.txt')    # Não vai para a lixeira É deletado imediatamente
send2trash('cesta2.txt')    # Vai para a lixeira. Pode ser restaurado

# Se o arquivo não existir, teremos OSError

import os
from send2trash import send2trash

send2trash('teste')

# Trabalhando com arquivos e diretorios temporarios

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretorio temporario, abrindo o mesmo e dentro dele criando
um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
os arquivos temporarios 'vivos' dentro dos blocos with.

# Obs.: possivelmente, o codigo acima não irá funcionar se você estiver utilizando o Windows.
Por conta desse sistema trabalhar de forma diferente com arquivos temporarios.

# Trabalhando com arquivos e diretorios temporarios
import os
import tempfile

# Criando um arquivo temporario

with tempfile.TemporaryFile() as temp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Obs.: Em arquivos temporarios só conseguimos escrever bits. Por isso, utilizamos b''

import os
import tempfile

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'GeekUniversity\n')

print(arquivo.name)
print(arquivo.read())
input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os


"""