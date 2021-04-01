"""
Função com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pop}')

# Exemplo função

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')

OBS.: Em Python, quando uma função não retorna nenhum valor, o retorno é None

# Vamos refatorar essa função para que ela retorne o valor
# Obs.: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return
# Obs.: Não precisamos necessariamente criar uma variavel para receber  retorno
de uma função. Podemos passa a execução da função para outras funções.

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno {ret}')
print(f'Retorno: {quadrado_de_7() + 1}')

# Refatorando a primeira função

def diz_oi():
    return 'oi'


alguem = 'Pedro'

print(diz_oi() + alguem)

Obs.: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dados e até mesmo múltiplos valores;

# Exemplos 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    return 'oi'
    print('Estou sendo executado após o retorno...')    # Nunca será executado

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns;

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao)

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dados e até mesmo múltiplos valores;

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

print(outra_funcao())   # Tupla
print(type(outra_funcao()))

# Vamos criar uma funçao para jogar a moeda

from random import random

def joga_moeda():
    #Gera um numero pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


# Erros comuns na utilização do retorno,  que na verdade nem é erro, mas sim codificação desnecessaria

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False        # Não foi necessario utilizar um else


print(eh_impar())

"""