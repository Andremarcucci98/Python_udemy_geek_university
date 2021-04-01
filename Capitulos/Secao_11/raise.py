"""
Levantando os próprios erros com o raise

raise -> Lança exceções

Obs.: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.
Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

# Exemplo real
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 7)



def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('testo precisa ser string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'verde')
"""