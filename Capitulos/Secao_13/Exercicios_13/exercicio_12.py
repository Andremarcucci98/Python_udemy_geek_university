"""
Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras
neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento)
"""
import string

arquivo = input('Digite o nome do arquivo seguido de ".txt": ')
extensao = '.txt'
dicionario = dict()

with open(f'{arquivo}{extensao}', 'r', encoding='UTF-8') as arq:
    character = str(arq.read())
    arq.seek(0)
    word = arq.read().split()
    arq.seek(0)
    print(f'A quantidade de caracteres: {len(character)}')
    print(f'A quantidade de linhas: {len(arq.readlines())}')
    print(f'A quantidade de palavras: {len(word)}')
    print(f'A quantidade de cada letra do alfabeto no texto (caracteres acentuados serão ignorados): ')
    [dicionario.update({letra: character.lower().count(letra)}) for letra in character.lower() if letra in string.ascii_letters]
    for key, value in sorted(dicionario.items()):
        print(f'{key} - {value}')