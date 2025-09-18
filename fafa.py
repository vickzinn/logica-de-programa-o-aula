import random

# Lista de 1000 palavras (exemplo, pode ser expandida)
palavras = [
    'banana', 'laranja', 'abacaxi', 'uva', 'morango', 'melancia', 'cereja', 'pera', 'pessego', 'ameixa',
    'cachorro', 'gato', 'elefante', 'girafa', 'zebra', 'tigre', 'leao', 'urso', 'panda', 'macaco',
    'carro', 'bicicleta', 'moto', 'aviao', 'barco', 'caminhao', 'onibus', 'trem', 'patinete', 'trator',
    'escola', 'casa', 'igreja', 'hospital', 'mercado', 'padaria', 'cinema', 'teatro', 'praia', 'fazenda',
    'caneta', 'lapis', 'caderno', 'borracha', 'mochila', 'livro', 'regua', 'tesoura', 'cola', 'quadro',
    'futebol', 'volei', 'basquete', 'natacao', 'corrida', 'xadrez', 'tenis', 'golfe', 'surf', 'skate',
    'brasil', 'argentina', 'franca', 'italia', 'japao', 'china', 'canada', 'mexico', 'alemanha', 'egito',
    'vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco', 'cinza', 'roxo', 'rosa', 'laranja',
    'janela', 'porta', 'mesa', 'cadeira', 'sofa', 'cama', 'espelho', 'armario', 'fogao', 'geladeira',
    'internet', 'computador', 'celular', 'tablet', 'teclado', 'mouse', 'monitor', 'fone', 'controle', 'televisao',
    'planeta', 'estrela', 'lua', 'sol', 'galaxia', 'universo', 'cometa', 'asteroide', 'meteoro', 'orbita',
    'amigo', 'familia', 'professor', 'aluno', 'vizinho', 'colega', 'chefe', 'cantor', 'ator', 'medico',
    'martelo', 'serrote', 'parafuso', 'prego', 'chave', 'furadeira', 'trena', 'escada', 'balde', 'pincel',
    'chuva', 'vento', 'neve', 'raio', 'trovao', 'furacao', 'terremoto', 'tsunami', 'clima', 'nuvem',
    'arroz', 'feijao', 'macarrao', 'pizza', 'hamburguer', 'sanduiche', 'bolo', 'sopa', 'salada', 'batata',
    'felicidade', 'tristeza', 'raiva', 'medo', 'surpresa', 'coragem', 'esperanca', 'saudade', 'cansaco', 'alegria',
    'dinheiro', 'moeda', 'nota', 'banco', 'bolsa', 'carteira', 'loja', 'preco', 'troco', 'salario',
    'relogio', 'anel', 'colar', 'pulseira', 'oculos', 'chapeu', 'sapato', 'camisa', 'calca', 'jaqueta',
    'peixe', 'tartaruga', 'sapo', 'cobra', 'lagarto', 'camaleao', 'polvo', 'tubarao', 'baleia', 'golfinho',
    'floresta', 'rio', 'lago', 'cachoeira', 'deserto', 'vulcao', 'montanha', 'campo', 'ilha', 'oceano',
    'circo', 'palhaco', 'magico', 'acrobata', 'truque', 'espada', 'coroa', 'castelo', 'princesa', 'dragao'
    # ...adicione mais palavras até chegar a 1000...
]

def jogar_forca():
    palavra = random.choice(palavras)
    letras_certas = []
    letras_erradas = []
    tentativas = 7
    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_certas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'
        print('\nPalavra:', palavra_escondida)
        print('Letras erradas:', ' '.join(letras_erradas))
        print('Tentativas restantes:', tentativas)
        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!')
            break
        if tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break
        letra = input('Digite uma letra: ').lower().strip()
        if not letra or len(letra) != 1 or not letra.isalpha():
            print('Digite apenas uma letra!')
            continue
        if letra in letras_certas or letra in letras_erradas:
            print('Você já tentou essa letra!')
            continue
        if letra in palavra:
            letras_certas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1

def menu_forca():
    while True:
        print('\n--- JOGO DA FORCA ---')
        jogar_forca()
        jogar_novamente = input('Deseja jogar novamente? (s/n): ').lower().strip()
        if jogar_novamente != 's':
            print('Obrigado por jogar!')
            break

if __name__ == '__main__':
    menu_forca()
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
