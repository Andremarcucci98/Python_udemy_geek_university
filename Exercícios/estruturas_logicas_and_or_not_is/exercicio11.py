"""
Ler um número dado pelo usuário e devolver a soma dos algarismos.

"""
num = int(input('Digite um número inteiro positivo: '))
if num <= 0 :
    print('Número inválido, tenha um bom dia.')
else:
    soma = 0
    while num > 0:
        soma += num % 10
        num //=10
    print(soma)
    