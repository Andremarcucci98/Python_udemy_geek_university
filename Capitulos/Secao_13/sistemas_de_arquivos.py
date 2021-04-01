"""
Sistemas de arquivos e Sistemas de navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do modulo os.

os -> Operating System - Sistema Operacional

# Fazer o import
import os

# getcwd() -> pega o currente work directory - diretorio de trabalho corrente
print(os.getcwd())          #C:\Users\Usuario\Desktop\Estudar\udemy

# Para mudar o diretorio podemos utilizar o chdir()
os. chdir('..')
print(os.getcwd())          #C:\Users\Usuario\Desktop\Estudar


# Podemos checar se um diretorio é relativou ou absoluto

print(os.path.isabs('/home/geek/'))     #True       # É absoluto??

# Obs. para usuarios WINDOWS: Se você, infelizmente, estiver utilizando um computador Windows
terá que ter cuidado ao verificar diretórios

print(os.path.isabs('C:\\Users\\geek'))

# Fzer o import
import os

# Podemos identificar o sistema operacional com modulo os
print(os.name)      # posix (Linux e Mac) , nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

import sys
print(sys.platform)

import os
#'/home/geek/workspace'

print(os.getcwd())      # /media/sf_Documents/vm/PycharmProjects/guppe
res = os.path.join(os.getcwd(),'geek', 'university')
os.chdir(res)

print(os.getcwd())      # /media/sp_Documents/vm/PycharmProjects/guppe/geek/university

# Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretorio atual e o segundo o
diretório que será juntado ao atual.

# Podemos listar os diretorios e arquivos com a listdir()
print(len(os.listdir()))

import os
print(os.listdir())

import os
print(len(os.listdir('C://')))

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()
import os
scanner = os.scandir()
arquivos = list(scanner)

# print(arquivos)
# print(dir(arquivos[0]))

print(arquivos[0].name)     # Nome do arquivo
print(arquivos[0].inode())  #
print(arquivos[0].is_dir())   # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())   # É um link simbolico?  False
print(arquivos[0].path)     # Caminho até o arquivo
print(arquivos[0].stat())     # Estatisticas sobre o arquivo...

# Obs.: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()
"""
