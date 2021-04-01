"""
Módulos customizados

Como modulos Python nada mais são do que arquivos Python, então todos os programas, ou todos os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.

# Importando uma função especifica do nosso modulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Importando todo o modulo
import funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.tupla)
print(fcp.soma_impares(fcp.lista))


# Exemplo 2
from map import cidades, c_para_f
print(list(map(c_para_f, cidades)))

"""