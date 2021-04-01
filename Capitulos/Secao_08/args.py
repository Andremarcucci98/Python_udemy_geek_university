"""
Entendendo o *args

- O *args é parametro, com outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que coemçe com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))     # TypeError

print(soma_todos_numeros(4, 6, 9, 5))   # TypeError

# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    total = 0                       # Ou
    for numero in args:                 return sum(args)
        total = total + numero
    return total

print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 4, 5, 6))
print(soma_todos_numeros('Angelina', 'Jolie', 7, 8, 9, 10))


# Outro exemplo de utilização do *args
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(1, 'University', 3.1415))


def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1, 2, 3, 4))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

Obs.: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção
de dados. Desta forma, ele saberá que precisará antes desempacotar estes dados.
# Serve para listas e tuplas, dicionarios é de outra forma (usamos **kwargs)
"""