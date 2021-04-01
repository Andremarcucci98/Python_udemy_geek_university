arq1 = input('Informe o nome do arquivo que deseja abrir: ')
arq2 = input('Agora escreva o nome do arquivo que quer criar a partir do primeiro: ')
extensao = '.txt'

with open(f'{arq1}{extensao}') as arquivo_inicial:
    cont = list(arquivo_inicial)

with open(f'{arq2}{extensao}', 'w') as arquivo_final:
    for i in range(len(cont)):
        arquivo_final.write(cont[i].upper())