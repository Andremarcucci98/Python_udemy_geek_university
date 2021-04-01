"""
Recebendo dados do usuário

input() -> Todo dia recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
#- Aspas duplas triplas -> """Angelina Jolie"""

print("Qual seu nome? ")
nome = input()
print('Seja bem-vindo(a) %s' %nome)             #Mais antigo
print('Seja bem-vindo(a) {0}'.format(nome))     #Atual
print(f'Seja bem-vindo(a) {nome}')              #Mais Atual

print("Qual sua idade? ")
idade = input()
print('A %s tem %s anos' % (nome, idade))           #Antiga
print('A {0} tem {1} anos'.format(nome, idade))     #Atual
print(f'A {nome} tem {idade} anos.')                #Mais Atual

"""
#   int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""