from collections import Counter


def conta_letras(arquivo):
    """Conta a ocorrência dos caracteres em um arquivo de texto"""
    try:
        with open(arquivo, 'r', encoding='UTF-8') as arq:
            contador = Counter(filter(lambda x: x != '\n', arq.read()))
            for chave, valor in sorted(contador.items()):
                print(f'O caractere {chave} tem {valor} ocorrência(s) no texto.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')


conta_letras(input('Digite o nome do arquivo: '))