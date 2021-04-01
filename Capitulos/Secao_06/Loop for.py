"""
_Loop for_

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

#Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'Geek University'
- String
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)

nome = 'Geek University'
lista = [1,,3, 5, 7, 9]
números = range(1,10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1,10):
    print(numero)
Obs.: range(valor_inicial, valor_final) #Vai do 1 ao 9!!!

"""

"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'),...)
for indice, letra in enumerate(nome):
    print(nome[indice])
    
for _, letra in enumerate(nome):        Obs.: Quando não precisamos de um valor, podemos descartá-lo
     print(letra)                                                   utilizando um underline (_)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?' ))
soma = 0
for n in range(1, qtd):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += soma + num
print(f'A soma é {soma}')

nome = 'Geek university'
for letra in nome:
    print(letra, end='')
    
Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode 
"""