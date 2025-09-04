import random
import os

def animais():
    animais = [
        "cachorro", "gato", "elefante", "girafa", "zebra", "tigre", "leao", "urso", "panda", "macaco",
        "cavalo", "boi", "vaca", "ovelha", "cabra", "camelo", "golfinho", "baleia", "tubarao", "polvo",
        "sapo", "cobra", "lagarto", "camaleao", "jacare", "crocodilo", "pato", "galinha", "galo", "pavao",
        "aguia", "falcao", "coruja", "pombo", "pardal", "beija-flor", "pinguim", "foca", "morsa", "lontra",
        "tartaruga", "caracol", "abelha", "formiga", "aranha", "escorpiao", "cavalo-marinho", "estrela-do-mar", "lagosta", "crustaceo"
]
    return random.choice(animais)

def objetos():
    objetos = [
        "mesa", "cadeira", "sofa", "cama", "armario", "prateleira", "fogao", "geladeira", "microondas", "televisao",
        "computador", "notebook", "tablet", "celular", "teclado", "mouse", "fone", "controle", "camera", "impressora",
        "caneta", "lapis", "borracha", "caderno", "mochila", "livro", "régua", "tesoura", "cola", "estojo",
        "bola", "raquete", "patins", "skate", "bicicleta", "patinete", "trampolim", "copo", "garrafa", "prato",
        "colher", "garfo", "faca", "panela", "frigideira", "balde", "martelo", "serrote", "prego", "chave"
]
    return random.choice(objetos)

def paises():

    paises = [
        "brasil", "argentina", "chile", "uruguai", "paraguai", "bolivia", "peru", "colombia", "venezuela", "equador",
        "estados unidos", "canada", "mexico", "cuba", "haiti", "panama", "costa rica", "honduras", "guatemala", "jamaica",
        "portugal", "espanha", "franca", "italia", "alemanha", "inglaterra", "irlanda", "suica", "austria", "grecia",
        "russia", "china", "japao", "coreia do sul", "coreia do norte", "india", "tailandia", "vietna", "filipinas", "indonesia",
        "australia", "nova zelandia", "egito", "marrocos", "argelia", "africa do sul", "nigeria", "congo", "quenia", "tanzania"
    ]
    return random.choice(paises)

def jogar():
    while True:
        print('_______MENU FORCA_______')
        print('1 - ANIMAL')
        print('2 - PAIS')
        print('3 - OBJETOS')
        print('4 - Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            palavra = animais()
        elif opcao == '2':
            palavra = paises()
        elif opcao == '3':
            palavra = objetos()
        elif opcao == '4':
            print('Saindo do jogo...')
            break
        else:
            print('Opção inválida!')
            continue

        tentativas = 7
        letras_certas = []
        letras_erradas = []

        while True:
            progresso = ''
            for letra in palavra:
                if letra in letras_certas or not letra.isalpha():
                    progresso += letra + ' '
                else:
                    progresso += '_ '
            print('\nPalavra:', progresso.strip())
            print('Letras certas:', ' '.join(letras_certas))
            print('Letras erradas:', ' '.join(letras_erradas))
            print('Tentativas restantes:', tentativas)

            if tentativas == 0:
                print('Você perdeu! A palavra era:', palavra)
                break
            if all((letra in letras_certas) or not letra.isalpha() for letra in palavra):
                print('Parabéns, você acertou! A palavra era:', palavra)
                break

            chute = input('Digite uma letra: ').lower()
            if len(chute) != 1 or not chute.isalpha():
                print('Digite apenas uma letra!')
                continue
            if chute in letras_certas or chute in letras_erradas:
                print('Você já tentou essa letra!')
                continue
            if chute in palavra:
                letras_certas.append(chute)
                print('Você acertou uma letra!')
            else:
                letras_erradas.append(chute)
                tentativas -= 1
                print('Letra errada!')

if __name__ == '__main__':
    jogar()