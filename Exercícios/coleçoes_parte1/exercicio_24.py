"""
Achar alunos mais altos e alunos mais baixos
"""
import random
maior = 0
menor = 2
aluno = {'André': round(random.uniform(1, 2), 2), 'Beatriz': round(random.uniform(1, 2),2 ),
         'Debora': round(random.uniform(1, 2), 2),
         'Daniel': round(random.uniform(1, 2), 2), 'Elisangela': round(random.uniform(1, 2), 2),
         'Fabiano': round(random.uniform(1, 2), 2)}
for nome, altura in aluno.items():
    print(f'nome: {nome} | altura: {altura}')
    if altura > maior:
        maior = altura

    if altura < menor:
        menor = altura

menor_nome = min(aluno, key=aluno.get)
maior_nome = max(aluno, key=aluno.get)
print('=================================================')
print(f'\nMenor aluno:{menor_nome}   Altura: {menor}'
      f'\nMaior aluno:{maior_nome}   Altura: {maior}')

