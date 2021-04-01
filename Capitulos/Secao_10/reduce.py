"""
Reduce

Obs.: A partir do Python versão 3 e acima, a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precise utiliza-la. Em todo caso, 99% das vezes um loop
for é mais legível.

Para entender o reduce()

# Imagine que vc tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E vc tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a funcao reduce() recebe dois paramatros: a função e o iteravel

A função reduce(), funciona da seguinte maneira:
    Passo 1: res1 = f(a1, a2)   #Aplica a funcao nos dois primeiros elementos e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o
    resultado.
    Isso é repetido até o final.
    Passo 3: res3 =(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), ...), an)


# Como funciona na prática?

Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 11, 13, 19, 23, 29]
# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)
"""