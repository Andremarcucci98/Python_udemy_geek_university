"""
Documentando Funções com Docstrings

Obs.: Podemos ter acesso à documentação de uma função de Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()

# Exemplos
def diz_oi():
    '''Uma função simples que retorna a string 'Oi''''
    return 'Oi'


print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    '''
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    '''
    return numero ** potencia

"""