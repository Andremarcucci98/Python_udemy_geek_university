import time
from threading import Thread

CONTADOR = 5000000


def contagem_regrassiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regrassiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regrassiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')

# Tempo em segundos: 0.4680459499359131
