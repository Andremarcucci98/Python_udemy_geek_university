arquivo = input('Digite o nome do arquivo de texto a ser aberto: ')
try:
    with open(arquivo) as arq:
        linhas = len(arq.readlines())
        print(f'O arquivo inserido possui {linhas} linhas')
except FileNotFoundError as err:
    print(f'Arquivo inexistente - tipo do erro - {err}')
