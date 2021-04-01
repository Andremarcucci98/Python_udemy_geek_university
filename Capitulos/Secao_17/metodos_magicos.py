"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder

dunder init -> __init__()

Dunder > Double Underscore

dunder repr -> Representação do objeto

def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas
        #return len(self.titulo)2

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória.')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

    
livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Interligencia Artificial', 'Geek University', 350)

print(str(livro1))
print(str(livro2))

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)
print(livro1 * 'Geek')