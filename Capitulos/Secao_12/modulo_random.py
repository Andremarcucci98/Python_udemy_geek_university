"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python

Módulo Random -> Possui varias funções para geração de numeros pseudo-aleatórios (pode ter repetição).

# Obs.: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado)

import random

# random() -> Gera um numero pseudo-aleatorio entre 0 e 1.

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
#dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiva quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())
# Veja que para utilizar a função random() do pacote, nós colocamos o nome do pacote e o nome da função.
# separados por ponto.

# Obs.: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo

from random import random

#  No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() -> gerar um numero pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))    # 7 Não é incluído


# randint() -> Gera valores pseudo-aleatorios entre os valores estabelecidos.
from random import randint
# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')     # começa em 1 e vai até 60



# choice() -> Mostra um valor aleatorio entre um iteravel
from random import choice
jogadas = ['Pedra', 'Papel', 'Tesoura']
print(choice(jogadas))

print(choice('Geek University'))



# shuffle() -> Tem a função de embaralhar dados
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas.pop())


"""