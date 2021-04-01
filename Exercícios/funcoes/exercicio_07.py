"""
Converter Fahrenheit para Celsius
"""


def fahrenheit_celsius(num):
    c = (num - 32) * 5/9
    return c


def celsius_fahrenheit(num):
    fah = num * (9.0/5.0) + 32
    return fah


f = float(input('Digite a temperatura em Fahrenheit: '))
print(f'O valor convertido é: {fahrenheit_celsius(f):.1f} graus Celsius ')
cel = float(input('Digite a temperatura em Celsius: '))
print(f'O valor convertido é: {celsius_fahrenheit(cel):.1f} graus Fahrenheit')
