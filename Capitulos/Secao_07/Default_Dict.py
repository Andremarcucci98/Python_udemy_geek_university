"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionarios
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])      #KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar u, lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

Obs.: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornam valores

# Fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui não
print(dicionario)


"""