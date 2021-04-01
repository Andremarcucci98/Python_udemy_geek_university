"""
Try, Except, Else, Finally

Dica de quando e onde tratar código:
TODA ENTRADA DO USUARIO DEVE SER TRATADA!

OBS.: A função do usuário é DESTRUIR seu sistema

num = 0

# Else -> É executado somente se nao ocorrer o erro.
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')

# Finally ->

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executamos o finally')

# Obs.: O bloco finally é SEMPRE executado. Independente se houver exceção ou não.
# O finally é ,geralmente, utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro numero: '))
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO

# OBS.: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)                                           # Tratamento genérico
    except ValueError:                                                  #except:
        print('Valor incorreto')                                             return 'Ocorreu um problema'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

# Exemplo mais complexo CORRETO - Semi - Genérico

# OBS.: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))


"""
