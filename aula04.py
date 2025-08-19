'''
aula 04
'''
'''
nome_1 = input('Digite o primeiro nome: ')
nome_2 = input('Digite o segundo nome: ')
nome_3 = input('Digite o terceiro nome: ')
nome_4 = input('Digite o quarto nome: ')
nome_5 = input('Digite o quinto nome: ')
'''
'''
importando bibliotecas
'''
'''
sorteio 1

import random 

lista = []

sair = False

while sair == False:
    nome_candidato = input('digite os nomes: ')
    if nome_candidato != '':
        lista.append(nome_candidato)
    else:
        sair = True
        escolhido = random.choice(lista)
        print(f'o nome escolhido foi: {escolhido}')
print(90*'_')
'''
'''
lista_nome = []
lista_sorteados = []
'''
'''
pop - funcao que remove pelo indice
    lista_nome.pop(indice)

del - funcao que remove pelo valor
    lista_nome.remove(valor)

remove - funcao que remove pelo valor
    lista_nome.remove(valor)
'''
'''
while True:
    if lista_nome:
        os.system('cls')
        escolhido = random.choice(lista_nome)
        lista_sorteados.append(escolhido)

        print(f'O nome sorteado foi: {escolhido}')

        opcao = input('deseja sortear outro nome? S - sim\n / N - não\n: ').lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print('Não há mais nomes para sortear.')
        break
print('programa finalizado...')
'''
#import lib
from random import randint

print('tente adivinhar o numero!')
num1 = int(input('digite um numero: '))

num_secreto = randint(1, 10)

if num1 == num_secreto:
    print('parabens! voce acertou!')
else:
    print(f'o numero secreto era {num_secreto}')
print('fim de jogo')
print(100*'_')

from random import randint

print('tente adivinhar o numero!')
num1 = int(input('digite um numero: '))

num_secreto = randint(1, 10)

h = 'hello world!'

if num1 == num_secreto:
    print('parabens! voce acertou!')
else:
    print(f'o numero secreto era {h}')
print('fim de jogo')
print(100*'-')

import random 

secret_number = random.randint(1, 100)
tentativas = 0
max_tentativas = 15
acertou = False

print(40*'_', 'bem vindo ao jogo', 40*'_')
print(100*'_')

import random 

secret_number = random.randint(1, 100)
tentativas = 0
max_tentativas = 15
acertou = False


print(f'voce tem {max_tentativas} tentativas para acertar o numero secreto entre 1 e 100')
print('vamos comecar?')

while tentativas < max_tentativas:
    try:
        palpite = int(input('Digite seu palpite: '))
        tentativas += 1

        if palpite == secret_number:
            acertou = True
            break
        elif palpite < secret_number:
            print('Muito baixo!')
        else:
            print('Muito alto!')
    except ValueError:
        print('Por favor, digite um número válido.')

if acertou:
    print(f'Parabéns! Você acertou o número secreto {secret_number} em {tentativas} tentativas.')
else:
    print(f'Você não acertou o número secreto {secret_number} em {max_tentativas} tentativas.')