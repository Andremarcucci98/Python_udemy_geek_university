from datetime import date


def agenda(opcao, nome='', telefone='', aniversario=''):

    if opcao == 'a':
        with open('exercicio_08/agenda.txt', 'a') as arq_escrita:
            if not isinstance(telefone, str):
                telefone = str(telefone)
            if not isinstance(aniversario, str):
                aniversario = str(aniversario)
            arq_escrita.write(nome.ljust(60, ' ') + telefone.ljust(9,' ') + aniversario + '\n')

    elif opcao == 'b':
        with open('exercicio_08/agenda.txt', 'r') as arq_leitura:
            lista = arq_leitura.readlines()
            with open('exercicio_08/agenda.txt', 'w') as arq_remove:
                for linha in lista:
                    contato = linha[0:60:].strip()
                    if contato == nome:
                        pass
                    else:
                        arq_remove.write(linha)

    elif opcao == 'c':
        with open('exercicio_08/agenda.txt', 'r') as arq_leitura:
            for contato in arq_leitura.readlines():
                if nome in contato:
                    print(f'{contato[0:60:].strip()} {contato[60:69:]}')

    elif opcao == 'd':
        with open('exercicio_08/agenda.txt', 'r') as arq_leitura:
            for contato in arq_leitura.readlines():
                print(f'{contato[0:60:].strip()} {contato[60:69:]}')

    elif opcao == 'e':
        with open('exercicio_08/agenda.txt', 'r') as arq_leitura:
            for contato in arq_leitura.readlines():
                if contato[0:len(nome)] == nome:
                    print(f'{contato[0:60:].strip()} {contato[60:69:]}')

    elif opcao == 'f':
        with open('exercicio_08/agenda.txt', 'r') as arq_leitura:
            for contato in arq_leitura.readlines():
                if int(contato[71:73]) == date.today().month:
                    print(f'{contato[0:60:].strip()}')

agenda(opcao='a', nome='Nome Contato', telefone=964484452, aniversario=2807)