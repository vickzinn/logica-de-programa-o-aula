
import json
import os

usuarios = []
new_file = ''

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('1 - cadastrar novo usuario:  ')
    print('2 - salvar arquivo json: ')
    print('3 - ler json: ')
    print('4 - sair...')

    opcao = input('digite uma opcao: ')
    limpar()

    match opcao:
        case '1':
            usuario = {}
            usuario['nome'] = input('informe o nome: ').strip().title()
            usuario['idade'] = input('informe a idade: ')
            usuario['email'] = input('digite o email: ').strip().lower()
            usuarios.append(usuario)
            limpar()
            print('usuario cadastrado com sucesso...')
            continue
        case '2':
            new_file = input('informe o novo arquivo: ').strip().lower()
            with open(f'{new_file}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('arquivo salvo com sucesso...')
            continue
        case '3':
            if not new_file:
                new_file = input('digite o nome do arquivo: ').strip().lower()
            try:
                with open(f'{new_file}.json', 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                print(f'{"_"*30} USUARIOS {"_"*30}')
                for usuario in dados:
                    for chave in usuario:
                        print(f'{chave.capitalize()}: {usuario.get(chave)}')
                    print('_'*60)  
            except FileNotFoundError:
                print('Arquivo não encontrado!')
            continue
        case '4':
            print('saindo...')
            break
        case _:
            print('opcao invalida...')
