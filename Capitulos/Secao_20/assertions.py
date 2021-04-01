"""
Testes - Assertions (Afirmações/Checagens/Questionamentos)

Em Python utilizamos a palavra 'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos verificar se é válida ou não.

Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

#Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizado;
# Obs: A palvra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser
exclusivamente nos testes.

# Alerta: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion
será validado. Ou seja, todas as suas validações já eram.
"""

"""
def soma_numero_positivos(a,b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


ret = soma_numero_positivos(2, 4)    # 6
ret = soma_numero_positivos(-2, 4)   # AssertionError
print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# Alerta: Cuidado ao utilizar 'assert'

def faca_algo_ruim(usuario):
    assert usuario.eh.admin, 'Somente administradores podem fazer coisas ruins!'
    destroi_todo_o_sistema()
    return 'Adeus'

"""