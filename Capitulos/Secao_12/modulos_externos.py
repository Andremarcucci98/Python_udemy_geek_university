"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em:  https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'Geek University')
print(Fore.GREEN + 'Geek University')
print(Fore.YELLOW + 'Geek University')
print(Style.Din + 'Geek University')
print(Style.RESET_ALL)

# Instalando o pacote colorama
pip install colorama

# Utilizando p pacote instalado
from colorama import init, Fore
init()
print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')


import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')
with open('test_doc_pdf', 'wb') as f:
    f.write(pdf)
"""