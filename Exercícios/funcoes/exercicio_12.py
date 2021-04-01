"""
Soma de algarismos
"""


def soma(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


n = int(input('Digite um numero para saber a soma de algarismos: '))
print(f'A soma dos algarismos de "{n}" é {soma(n)} ')
