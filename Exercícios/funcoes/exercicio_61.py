"""
Detecção de anagramas
"""


def check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print('As strings são anagramas')
    else:
        print('As strings não são anagramas')


s1 = 'silent'
s2 = 'listen'
check(s1, s2)