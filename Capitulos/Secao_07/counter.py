"""
Módulo Collections - Counter(Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-Performance Container Datetypes

Counter -> Recebe um iteravel como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionario, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

# Utilizando o Counter

from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6 ]

# Utilizando o Counter

res = Counter(lista)

print(type(res))    # <class 'collections.Counter'>
print(res)          #Counter({4: 7, 5: 6, 1: 3, 3: 3, 2: 2, 6: 2})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias.

# Exemplo 2
from collections import Counter
 print(Counter('Geek University'))
 #Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
from collections import Counter
texto = '''Dromaius novaehollandiae minor é uma subespécie extinta de emu que era endêmica da ilha King, localizada
no estreito de Bass entre a Austrália continental e a Tasmânia. Seu "primo" mais próximo é a também extinta subespécie
de emu da Tasmânia (D. n. diemenensis), pois eles pertenciam a uma única população até menos de 14 mil anos atrás,
quando as duas ilhas ainda estavam conectadas. O pequeno tamanho do emu da ilha King pode ser um exemplo de nanismo
insular. A ave era o menor de todos os emus conhecidos e possuía plumagem mais escura que o emu do continente.
Era preto e marrom e tinha pele nua de cor azul no pescoço; seus filhotes eram listrados como os do continente.'''

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)
#''' Counter({'de': 7, 'emu': 4, 'a': 4, 'e': 4, 'da': 3, 'do': 3, 'é': 2, 'uma': 2, 'subespécie': 2, 'extinta': 2,
'que': 2, 'era': 2, 'ilha': 2, 'no': 2, 'mais': 2, 'o': 2, 'os': 2, 'continente.': 2, 'Dromaius': 1,
 'novaehollandiae': 1, 'minor': 1, 'endêmica': 1, 'King,': 1, 'localizada': 1, 'estreito': 1, 'Bass': 1, 'entre': 1,
  'Austrália': 1, 'continental': 1, 'Tasmânia.': 1, 'Seu': 1, '"primo"': 1, 'próximo': 1, 'também': 1, 'Tasmânia': 1,
   '(D.': 1, 'n.': 1, 'diemenensis),': 1, 'pois': 1, 'eles': 1, 'pertenciam': 1, 'única': 1, 'população': 1, 'até': 1,
    'menos': 1, '14': 1, 'mil': 1, 'anos': 1, 'atrás,': 1, 'quando': 1, 'as': 1, 'duas': 1, 'ilhas': 1, 'ainda': 1,
     'estavam': 1, 'conectadas.': 1, 'O': 1, 'pequeno': 1, 'tamanho': 1, 'King': 1, 'pode': 1, 'ser': 1, 'um': 1,
      'exemplo': 1, 'nanismo': 1, 'insular.': 1, 'A': 1, 'ave': 1, 'menor': 1, 'todos': 1, 'emus': 1, 'conhecidos': 1,
       'possuía': 1, 'plumagem': 1, 'escura': 1, 'Era': 1, 'preto': 1, 'marrom': 1, 'tinha': 1, 'pele': 1, 'nua': 1,
        'cor': 1, 'azul': 1, 'pescoço;': 1, 'seus': 1, 'filhotes': 1, 'eram': 1, 'listrados': 1, 'como': 1})'''

"""