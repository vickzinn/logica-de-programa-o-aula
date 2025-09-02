'''
aula07
'''
'''
atividade: crie uma aplicação de banco, onde o usuario se cadastra e cria uma conta
corrente que começa com saldo de R$ 0,00. O usuario tera as opções de: criar conta FEITO,
exibir dados da conta FEITO, depositar FEITO, sacar FEITO e sair FEITO .
'''

cadastro = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

print('Cadastro realizado')
def criar_conta():
    global saldo
    saldo = 0.0
    print('Conta criada...')

def mostrar_dados():
    print(f'Nome: {cadastro}')
    print(f'Saldo: R$ {saldo:.2f}')

def depositar():
    global saldo
    valor = float(input('Digite um valor para depositar: R$ '))
    if valor > 0:
        saldo += valor
        print(f'Depósito realizado! Novo saldo: R$ {saldo:.2f}')
    else:
        print('Valor inválido!')
def sacar():
    global saldo
    valor = float(input('Digite o valor para sacar: R$ '))
    if 0 < valor <= saldo:
        saldo -= valor
        print(f'Saque realizado! Novo saldo: R$ {saldo:.2f}')
    else:
        print('Saldo insuficiente ou valor inválido!')
def sair():
    print('Saindo...')
    exit()

while True:
    print('--- MENU DO SEU BANCO ---')
    print('1 - Criar conta bancaria')
    print('2 - Mostrar dados')
    print('3 - Depositar')
    print('4 - Sacar')
    print('5 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        mostrar_dados()
    elif opcao == '3':
        depositar()
    elif opcao == '4':
        sacar()
    elif opcao == '5':
        sair()
    else:
        print('Opção inválida!')

'''
o def funciona para definir funções que podem ser chamadas em diferentes partes do código.
exemplo:
def minha_funcao():
    print('Olá, mundo!')
'''