"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Ordem Functions;
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar/ Açúcar Sintático)

# Decorators como funções (Sintaxe mão recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você ')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem vindo a Geek Unviersity')

# Testando 1

teste = seja_educado(saudacao)

teste()

# Testando 2
def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com Syntax Sugar (Açúcar Sintatico)
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo()


@seja_educado_mesmo
def apresentando():
    print('Meu nome é André')

# Testando
apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

# Obs.: Não é código funcional, é apenas um exemplo

def checa_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')

def home(request):
    return 'Pode acessar home'

def servicos(request):
    return 'Pode acessar produtos'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'


# Obs.: Não confunda Decorator com Decorator Function


"""
