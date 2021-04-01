class Contato:

    contador: int = 0

    def __init__(self: object, nome: str, telefone: int, email: str) -> None:
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        #self._data_nascimento: date = data_nascimento
        #Contato.contador = self.__contador

    @property
    def contador(self: object) -> int:
        return self.__contador

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def telefone(self: object) -> str:
        return self.__telefone

    #@property
    #def data_nascimento(self: object) -> str:
    #    return self.__data_nascimento
