"""
Funções de Maior Grandeza - Higher Order Functions (HOF)

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado ou mesmo que podemos passar funções como argumentos para outros funções como argumentos para outros funções
, e até mesmo criar variaveis do tipo de funções nos nossos programas.

Obs.: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizen

def somar(a, b):
    return a+b


def diminuir(a, b):
    return a-b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a/b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular((4, 3, diminuir)))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas

# Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions ou também Inner Functions
# Funções Internas

# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de vc '))
    return humor() + pessoa


# Testando
print(cumprimento('Angelina'))

print(cumprimento('Felicity'))


# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkkk', 'jajajajajjaaj'))
    return rir()

# Testando

rindo = faz_me_rir()
print(rindo)
# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahhahahaha', 'lolololololo', 'jajajjaajja'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando
rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
"""
