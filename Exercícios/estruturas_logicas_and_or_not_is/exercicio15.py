"""
Dias da semana
"""
n = int(input('Digite um número entre 1 e 7: '))
while n < 1 or n > 7:
    n = int(input('Digite um número válido: '))
if n == 1:
    print('Domingo')
elif n == 2:
    print('Segunda-feira')
elif n == 3:
    print('Terça-feira')
elif n == 4:
    print('Quarta-feira')
elif n == 5:
    print('Quinta-feira')
elif n == 6:
    print('Sexta-feira')
else:
    print('Sábado')