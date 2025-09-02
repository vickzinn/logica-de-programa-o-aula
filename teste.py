'''
aula07
'''
'''
atividade: crie uma aplicação de banco, onde o usuario se cadastra e cria uma conta
corrente que começa com saldo de R$ 0,00. O usuario tera as opções de: criar conta,
exibir dados da conta, depositar, sacar e sair.
'''

cadastro = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

print('Cadastro realizado com sucesso!')

# Conta corrente
saldo = 0.0

def exibir_dados():
    print(f'Nome: {cadastro}')
    print(f'Saldo: R$ {saldo:.2f}')

def depositar():
    global saldo
    valor = float(input('Digite o valor para depositar: R$ '))
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

while True:
    print('\n--- MENU BANCO ---')
    print('1 - Exibir dados da conta')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        exibir_dados()
    elif opcao == '2':
        depositar()
    elif opcao == '3':
        sacar()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
