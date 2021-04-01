""""""
"""
Doctests

Doctests são testes que colocamos nas docstrings das funções/métodos Python
""""""
def soma(a, b):
    '''soma os numeros a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    '''
    return a + b

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py

(guppe) C:\Users\Usuario\Desktop\Estudar\udemy>python -m doctest -v doctestes.py
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctestes
1 items passed all tests:
   1 tests in doctestes.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Outro Exemplo, aplicando o TDD

def duplicar(valores):
    #"""#duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
      '''...'''
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    """
    return [2 * elemento for elemento in valores]

# Erro inesperado...

# Obs.: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.
def fala_oi():
    #"""#Fala oi

    '''# >>> fala_oi() 
    #'oi'
    '''"""
    return "oi"

# Último caso estranho...

def verdade():
   # """#Retorna verdade

   # >>> verdade()
   # True
    """
    return True

"""