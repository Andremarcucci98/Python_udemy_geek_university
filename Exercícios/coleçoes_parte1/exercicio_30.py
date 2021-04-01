from random import randint
conjunto1 = []
conjunto2 = []
vetor_conjunto1 = vetor_conjunto2 = {}
for i in range(0, 10):
    conjunto1.append(randint(0, 20))
    conjunto2.append(randint(0, 20))
print(conjunto1)
print(conjunto2)
vetor_conjunto1 = set(conjunto1)
print(f'vetor conjunto 1 = {vetor_conjunto1}')
vetor_conjunto2 = set(conjunto2)
print(f'vetor conjunto 2 = {vetor_conjunto2}')
print(f'tamanho vetor_conjunto1 = {len(vetor_conjunto1)} tamanho vetor_conjunto2 = {len(vetor_conjunto2)}')
while len(vetor_conjunto1) < 10 or len(vetor_conjunto2) < 10:
    if len(vetor_conjunto1) < 10:
        vetor_conjunto1.add(randint(0, 20))
    if len(vetor_conjunto2) < 10:
        vetor_conjunto2.add(randint(0, 20))
    print(f'opa: {vetor_conjunto1}')
    print(f'rust: {vetor_conjunto2}')
intersec_conjunto = vetor_conjunto1.intersection(vetor_conjunto2)
print('-----------------------------')
print(f'Interseção de conjuntos : {intersec_conjunto}')

uniao_conjunto = vetor_conjunto1.union(vetor_conjunto2)
print('-'*40)
print(f'Vetor uniao: {uniao_conjunto}')
print('-'*40)