print('vamos brincar')
print('voce quer brincar?')
resposta = input('Sim ou Nao ---> S/N: ').lower()
if resposta == 's':
    print('Vamos brincar!')
else:
    print('nao tem outra opcao, vamos brincar, AGORA!')
while True:
    print('\nEscolha um brinquedo:')
    print('1 - Carro')
    print('2 - Boneca')
    print('3 - Quebra-cabeça')
    print('4 - Jogo de videogame')
    print('5 - Ursinhos')
    brinquedo = input('Digite o número do brinquedo que você quer: ')
    match brinquedo:
        case '1':
            print('Você escolheu um carro!')
        case '2':
            print('Você escolheu uma boneca!')
        case '3':
            print('Você escolheu um quebra-cabeça!')
        case '4':
            print('Você escolheu um jogo de videogame!')
        case '5':
            print('Você escolheu um ursinhos!')
        case '6':
            print('Você escolheu uma bola!')
            break
        case _:
            print('Brinquedo não reconhecido!')
    continuar = input('Você quer escolher outro brinquedo? (s/n) ').lower()
    if continuar != 's':
        print('Ok, obrigado por brincar!')
        break
print('Obrigado por brincar!')