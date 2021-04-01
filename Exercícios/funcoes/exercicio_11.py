"""
Ponderada ou Aritmética?
"""


def nota_aluno(a, b, c, choice):
    if choice == 'A':
        arit = (a + b + c)/3
        return f'Média Aritmética: {arit:.2f}'
    elif choice == 'P':
        pond = (a * 5 + b * 3 + c * 2)/10
        return f'Média Ponderada: {pond:.2f}'
    else:
        return print(f'Valor incoerente com enunciado!')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
letra = str(input('Digite A para saber média aritmética e P para média ponderada: ')).upper()
print('-'*30)
print(nota_aluno(n1, n2, n3, letra))
