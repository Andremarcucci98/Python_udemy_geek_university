"""
Geradores

- Geradores (Generators) são Iterators (Iteradores):
Obs.: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)
---------------------------------------------------------------------------------------------
/ Funções                                            /Generator Functions   /
--------------------------------------------------------------------------------------------
/utilizam return                                     /utilizam yield        /
---------------------------------------------------------------------------------------------
/retorna uma vez                                     /podem utilizar yield multiplas vezes/
---------------------------------------------------------------------------------------------
/quando executada, retorna um valor                  /quando executada, retorna um generator/
---------------------------------------------------------------------------------------------

# Exemplo de Generator Function
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador          # Como se fosse um return, mas não sai da função
        contador = contador + 1

# Obs.: Um Generator Function não é um Generator. Ela gera um generator. ok?

gen = conta_ate(5)

print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))        # StopIteration

gen = conta_ate(10)
print(next(gen))

print('Geek')
for num in gen:
    print(num)

"""


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador          # Como se fosse um return, mas não sai da função
        contador = contador + 1


gen = list(conta_ate(10))
print(gen)
