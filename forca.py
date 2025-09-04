import random
import os

def escolher_palavras():
    j = [
    "banana", "laranja", "abacaxi", "uva", "morango", "melancia", "cereja", "pera", "pessego", "ameixa",
    "cachorro", "gato", "elefante", "girafa", "zebra", "tigre", "leao", "urso", "panda", "macaco",
    "carro", "bicicleta", "moto", "avião", "barco", "caminhao", "onibus", "trem", "patinete", "trator",
    "escola", "casa", "igreja", "hospital", "mercado", "padaria", "cinema", "teatro", "praia", "fazenda",
    "caneta", "lapis", "caderno", "borracha", "mochila", "livro", "régua", "tesoura", "cola", "quadro",
    "futebol", "volei", "basquete", "natacao", "corrida", "xadrez", "tenis", "golfe", "surf", "skate",
    "brasil", "argentina", "franca", "italia", "japao", "china", "canada", "mexico", "alemanha", "egito",
    "vermelho", "azul", "verde", "amarelo", "preto", "branco", "cinza", "roxo", "rosa", "laranja",
    "janela", "porta", "mesa", "cadeira", "sofa", "cama", "espelho", "armario", "fogao", "geladeira",
    "internet", "computador", "celular", "tablet", "teclado", "mouse", "monitor", "fone", "controle", "televisao",
    "planeta", "estrela", "lua", "sol", "galaxia", "universo", "cometa", "asteroide", "meteoro", "orbita",
    "amigo", "familia", "professor", "aluno", "vizinho", "colega", "chefe", "cantor", "ator", "medico",
    "martelo", "serrote", "parafuso", "prego", "chave", "furadeira", "trena", "escada", "balde", "pincel",
    "chuva", "vento", "neve", "raio", "trovão", "furacao", "terremoto", "tsunami", "clima", "nuvem",
    "arroz", "feijao", "macarrao", "pizza", "hamburguer", "sanduiche", "bolo", "sopa", "salada", "batata",
    "felicidade", "tristeza", "raiva", "medo", "surpresa", "coragem", "esperanca", "saudade", "cansaço", "alegria",
    "dinheiro", "moeda", "nota", "banco", "bolsa", "carteira", "loja", "preco", "troco", "salario",
    "relogio", "anel", "colar", "pulseira", "oculos", "chapeu", "sapato", "camisa", "calca", "jaqueta",
    "peixe", "tartaruga", "sapo", "cobra", "lagarto", "camaleao", "polvo", "tubarao", "baleia", "golfinho",
    "floresta", "rio", "lago", "cachoeira", "deserto", "vulcao", "montanha", "campo", "ilha", "oceano",
    "circo", "palhaco", "magico", "acrobata", "truque", "espada", "coroa", "castelo", "princesa", "dragao"
]

    return random.choice(j)

def jogar():
    palavra = escolher_palavras()
    letras_c = []
    letras_e = []
    tentativas = 7

    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_c:
                palavra_escondida += letra

            else:
                palavra_escondida += '_'
        print('palavra: \n',palavra_escondida)
        print('letras erradas: \n',letras_e)
        print(' tentativas restantes: ',tentativas)

        if palavra_escondida == palavra:
            print('parabens...\nvoce ganhou!')
            break
        elif tentativas == 0:
            print('errou, apalavra era: \n', palavra_escondida)
            break

        letras_usuario = input('digite uma letra: ').lower()

        if letras_usuario in palavra:
            letras_c.append(letras_usuario)
        
        else:
            print('letra errada!')
            letras_e.append(letras_usuario)
            tentativas -= 1
if __name__ == '__main__':
    os.system('cls')
    print('bem vindo a forca...')
    jogar()