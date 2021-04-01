"""
Preservando metadatas com wraps

Metadados -> São dados intrinsecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    "Soma dois numeros"
    return a + b

# print(soma(10, 30))

print(soma.__name__)    # soma

print(soma.__doc__)     # Soma dois numeros
"""

# Resolução do problema
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b

print(soma(10, 30))

print(soma.__name__)    # soma

print(soma.__doc__)     # Soma dois numeros

#print(help(soma))

