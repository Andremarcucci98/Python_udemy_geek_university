from time import sleep
from typing import List

from Capitulos.Secao_13.Exercicios_13.exercicio_25_agenda_turbinada.models.contato import Contato

agenda: List[Contato]


def main() -> None:
    menu()


def menu() -> None:
    print('========================')
    print('======== Agenda ========')
    print('========================')

    print('Selecione umas das opções abaixo: ')
    print('---------------------------------')
    print('1 - Criar um contato\n'
          '2 - Remover um contato\n'
          '3 - Pesquisar contato pelo nome\n'
          '4 - Listar todos os contatos\n'
          '5 - Listar contatos cujo nome inicia em dada letra\n'
          '6 - Imprimir os aniversariantes do mês')
    print('---------------------------------')
    opcao: int = int(input('Digite a opção: '))

    if opcao == 1:
        cria_contato()
    elif opcao == 2:
        remove_contato()
    elif opcao == 3:
        pesquisa_contato()
    elif opcao == 4:
        lista_contatos()
    elif opcao == 5:
        lista_contatos_ordem_alfa()
    elif opcao == 6:
        aniversariantes()
    else:
        print('Nenhuma opção solicitada, tenha um bom dia!')
        quit()


def cria_contato():
    print('Opção 1 selecionada! Informe os dados do contato.')

    nome: str = input('Nome do contato: ')
    email: str = input('E-mail do contato: ')
    telefone: str = input('Telefone: ')

    conta: Contato = Contato(nome, email, telefone)

    with open('exercicio_25_agenda_automatizada.txt', 'a', encoding='UTF-8') as arq_escrita:
        #arq_escrita.write(f'Nome: {conta.nome} /E-mail: {conta.email} /Telefone: {conta.telefone}\n')
        arq_escrita.write(f'{conta.nome} /{conta.email} /{conta.telefone}\n')

    print('Conta criada com sucesso')
    sleep(1)
    menu()


def remove_contato():
    contato_remove: str = str(input('Digite o contato a ser removido: '))
    with open('exercicio_25_agenda_automatizada.txt', encoding='UTF-8') as arq_leitura:
        lista = arq_leitura.readlines()
    for line in lista:
        if contato_remove in line:
            lista.remove(line)
            with open('exercicio_25_agenda_automatizada.txt', 'w', encoding='UTF-8') as new_arq_leitura:
                for line in lista:
                    new_arq_leitura.write(line)
        else:
            pass
    sleep(1)
    menu()


def pesquisa_contato():
    contato = str(input('Digite o nome do contato: ')).strip()
    with open('exercicio_25_agenda_automatizada.txt', 'r', encoding='UTF-8') as arq_leitura:
        lista = arq_leitura.readlines()
        for linha in lista:
            if contato in linha:
                print(linha)
                break
            else:
                print('Contato não encontrado! Tente novamente')
    sleep(1)
    menu()


def lista_contatos():
    with open('exercicio_25_agenda_automatizada.txt', 'r', encoding='UTF-8') as arq_leitura:
        lista = arq_leitura.readlines()
        for linha in lista:
            lista_palavras = linha.strip().split('/')
            print(lista_palavras)
    sleep(2)
    menu()


def lista_contatos_ordem_alfa():
    pass

def aniversariantes():
    pass

if __name__ == '__main__':
    main()