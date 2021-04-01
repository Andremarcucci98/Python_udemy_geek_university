# math.prod - retorna o produto de um container numerico

import math

num_v1 = [2, 4, 6, 8]
num_v2 = (2, 3, 6, 8)
num_v3 = {2, 3, 6, 8}

print(math.prod(num_v1))
print(math.prod(num_v2))
print(math.prod(num_v3))

# math.isqrt - retorna a parte inteira da raiz quadrada de um numero

print(math.isqrt(9))    # valor inteiro
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))

# math.dist - retorna distanca euclidiana entre dois pontos, 3D ou 2D
#Pontos 3D
p3d1 = (12, 58, 48)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 58]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# math.hypot - retorna a hipotenusa ou a norma euclidiana

print(math.hypot(*p3d1))    # Descompactando os elementos da lista
print(math.hypot(*p2d1))

# Estatística
import statistics
# statistics.fmean - Calcula a média de numeros reais

valores_reais = [1.45, 6.87, 89.89, 14.65]
valores_inteiros = [1, 6, 89, 14]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean - calcula a media geometrica de numeros reais

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

# statistics.multimode - retorna o valor mais frequente em uma sequencia

seq1 = 'Geek University'
seq2 = [3, 5, 2, 8, 9, 7, 3]
seq3 = [1, 2, 3, 4, 6, 3, 4]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
