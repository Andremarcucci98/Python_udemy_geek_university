"""
Data atual
"""
from datetime import datetime


def data_atual():
    dia = datetime.now().day
    mes = datetime.now().month
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
             9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    ano = datetime.now().year
    return f'Data atual: {dia} de {meses[mes]} de {ano}'


print(data_atual())