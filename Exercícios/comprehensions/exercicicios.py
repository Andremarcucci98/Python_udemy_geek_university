"""
Usando lambda
"""
"""
dobro = lambda x: x * 2
print(dobro(2))
"""

"Usuario"
"""
usuario = lambda name, age: print(name.strip().title(), 'possui', age, 'anos')
nome = str(input('Qual seu nome?: '))
idade = int(input('Idade?: '))
usuario(nome, idade)
"""
"""
# Solicite dois numeros ao usuario e exiba a multiplicação deles
multiplicacao = lambda num1, num2: print(f'A multiplicação {num1} x {num2} é: ', num1 * num2)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
multiplicacao(n1, n2)
"""

# Dez numeros usando list comprehensions e lambda para achar pares
"""
def escrever_array(array):
    for valor in array:
        print(valor, end=' ')
"""
"""
numeros = [int(input('Digite um numero: ')) for num in range(5)]
pares = filter(lambda par: par % 2 == 0, numeros)
impares = list(filter(lambda par: par % 2 == 1, numeros))
print(impares)
print(pares)
"""


