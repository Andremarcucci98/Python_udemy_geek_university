"""
Definindo funções

- Funções são pequenos partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos simlares por repetidas vezes;

Obs.: Se você escrever uma função que realiza várias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada.
Já utilizamos varias funções desde que iniciamos nosso curso:
- print()
- len()
- max()
- min()
- count()
- e muitoas outras;

# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

#Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.appen('roxo')
print(cores)

curso.append('Mais dados...')   #AttributeError
print(curso)

cores.clear()
print(cores)

print(help(print))

# DRY - Don't Repeat Ypurself - Não repita você mesmo/ Não repita seu código

# Mas então, como definir funções?

Em Python, a forma geral de definir uma função é:

def nome_função(parametros_de_entrada):
    bloco_da_função

Onde:

nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underlinem (Snake Case):
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funçao -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Obs.: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos: que é utilizado
em Python para definir blocos.

# Definindo a primeira função
# Definição
def diz_oi():
    print('oi!')

OBS.:
1 - Veja que dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa uma tarefa, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;

# Chamada de execução
diz_oi()

ATENÇÃO : Nunca esqueça de utilizar o parênteses ao executar uma função
Exemplo:
diz_oi      # ERRADO!!
diz_oi ()   # ERRADO!!
diz_oi()    # CERTO!!!

# Exemplo 2
def cantar_parabens():
    print('Parabéns pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variavel

canta = cantar_parabens

canta()



"""