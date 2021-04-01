"""
Importar random number e somar

"""
from random import randint
corretas = 0
erros = 0
n = 1
while n != 6:
    print(f'Questão número {n}:')
    quest1 = randint(1, 100)
    quest2 = randint(1, 100)
    resp = int(input(f'Quanto é {quest1}+{quest2}? '))
    resp_comp = quest1 + quest2
    if resp != resp_comp:
        erros += 1
    else:
        corretas += 1
    print(f'Resposta correta: {resp_comp}')
    n += 1
print(f'Total de erros: {erros}'
      f'\nTotal de acertos: {corretas}')