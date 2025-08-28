primeiro_numero = input('coloque o primeiro numero: ')
segundo_numero = input('coloque o segundo numero: ')
terceiro_numero = input('coloque o terceiro numero: ')

if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
    print('o primeiro numero é o menor')
    menor = primeiro_numero

elif segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
    print('o segundo numero é o menor')
    menor = segundo_numero
else:
    print('o terceiro numero é o menor')
    menor = terceiro_numero

print(f'o menor numero é {menor}')
