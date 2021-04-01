"""
POO - MRO (Method Resolution Order)

Method Resolution Ordem (Resolução de Ordem de Métodos) é a ordem de execução dos métodos
Quem será executado primeiro.

Em Python podemos conferir a ordem de execução dos métodos de tres formas:
     - Via Propriedade da classe __mro__
     - Via método mro()
     - Via help
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra.'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Pinguim'           # Vai debaixo para cima


tux = Pinguim('Tux')
print(tux.cumprimentar())

"""
Pinguim(Aquatico, Terrestre)
Eu sou Tux do mar!

Pinguim(Terrestre, Aquatico)
Eusou Tux da terra!
"""