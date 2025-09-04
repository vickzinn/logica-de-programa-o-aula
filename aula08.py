import random
import string

def gerar_senha(comprimento = 12, incluir_maiusculo = True, incluir_minusculo = True, incluir_numeros = True, incluir_caracter = True):
    caracter = ''
    if incluir_minusculo:
        caracter += string.ascii_uppercase

    if incluir_minusculo:
        caracter += string.ascii_lowercase
    
    if incluir_numeros:
        caracter += string.digits
    
    if incluir_caracter:
        caracter += string.punctuation
    
    if not caracter:
        return ValueError('deve conter ao menos um caracter...')

    senha = ''.join(random.choice(caracter) for _ in range(comprimento))
    print(f'sua senha é: {senha}')
    return senha
    
def main():
    print ('gerador de senhas fortes:\n')
    comprimento = int(input('digite o comprimento da senha (padrão = 12): ') or 12)
    incluir_maiusculo = input('incluir  maiuscula? (s/n, padrao = sim): ').lower() != 'n'
    incluir_minusculo = input('incluir  minusculo? (s/n, padrao = sim): ').lower() != 'n'
    incluir_numeros = input('incluir  numeros? (s/n, padrao = sim): ').lower() != 'n'
    incluir_caracter_esp = input('incluir  caracter especial? (s/n, padrao = sim): ').lower() != 'n'

    senha = gerar_senha(comprimento, incluir_maiusculo , incluir_minusculo , incluir_numeros , incluir_caracter_esp )

    print (f'a senha gerada foi: {senha}')

    with open('senhas.txt', 'a') as s:
        s.write(f'\n{senha}')


if __name__ == '__main__':
    main()