'''
aula 04
'''
age = int(input('coloque sua idade: '))

sala_1 = 'aventuras de dock'
min_1 = 1

sala_2 = 'os incriveis'
min_2 = 10

sala_3 = 'jumanji: bem vindo a selva'
min_3 = 12

sala_4 = 'bad boys'
min_4 = 16

sala_5 = 'deadpool e wolverine'
min_5 = 18

sala_6 = 'sair'

while True:
    print(40*'_', 'bem vindo ao cinema', 40*'_')

    print ('escolha um filme: ')

    print(f'1 - {sala_1} (idade minima: {min_1})')

    print(f'2 - {sala_2} (idade minima: {min_2})')

    print(f'3 - {sala_3} (idade minima: {min_3})')

    print(f'4 - {sala_4} (idade minima: {min_4})')

    print(f'5 - {sala_5} (idade minima: {min_5})')

    print(f'para sair do cinema, digite \'{sala_6}\'')

    opcao = input('Digite o número do filme ou \"sair\": ')

    if opcao == '1':
        if age >= min_1:
            print(f'voce pode ver {sala_1}')
            print('aproveite o filme...')
            break
        else:
            print('voce nao pode ver este filme, pois é muito novo')
            ...

    elif opcao == '2':
        if age >= min_2:
            print(f'voce pode ver {sala_2}')
            print('aproveite o filme...')
            break
        else:
            print('voce nao pode ver este filme, pois é muito novo')
            ...

    elif opcao == '3':
        if age >= min_3:
            print(f'voce pode ver {sala_3}')
            print('aproveite o filme...')
            break
        else:
            print('voce nao pode ver este filme, pois é muito novo')
            ...

    elif opcao == '4':
        if age >= min_4:
            print(f'voce pode ver {sala_4}')
            print('aproveite o filme...')
            break
        else:
            print('voce nao pode ver este filme, pois é muito novo')
            ...

    elif opcao == '5':
        if age >= min_5:
            print(f'voce pode ver {sala_5}')
            print('aproveite o filme...')
            break
        else:
            print('voce nao pode ver este filme')
            ...

    elif opcao == '6':
        print(f'{sala_6}')
        break
    else:
        print('opcao invalida')