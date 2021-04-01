"""
Maior número palíndromo feito a partir do produto de dois numeros de 3 digitos
"""
i = 0
j = 0
pol = 0
while i < 999:
    j = i
    while j < 999:
        temp = str(i * j)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            polTemp = int(temp)
            if polTemp > pol:
                pol = polTemp
                valor1 = i
                valor2 = j
        j += 1
    i += 1
print(f'O maior palíndromo é {i}x{j}={pol}')