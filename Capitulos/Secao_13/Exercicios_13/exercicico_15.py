import datetime
ano = datetime.date.today().year
entrada = input('Digite o nome do arquivo que deseja abrir, juntamente com sua extensão: ')
saida = input('Digite o nome da saída: ')
lista1 = list()
lista2 = list()
with open(f'{entrada}', 'w') as arq:
    for r in range(2):
        nome = input('Digite seu nome: ')
        lista1.append(nome)
        nascimento = int(input('Digite o ano de seu nascimento: '))
        lista2.append(nascimento)
        arq.write(nome)
        arq.write(' ')
        arq.write(str(nascimento))
        arq.write('\n')
with open(f'{saida}', 'w') as pasta:
    for i in range(2):
        idade = ano - lista2[i]
        pasta.write(lista1[i])
        pasta.write(' ')
        if idade < 18:
            pasta.write('Menor de idade\n')
        elif idade == 18:
            pasta.write('Entrando na maioridade\n')
        else:
            pasta.write('Maior de idade\n')
