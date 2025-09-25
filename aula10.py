'''
aula10
paradigmas
'''  
# classe - espaço onde vou escrever um objeto
# atributos - características do objeto
# métodos - ações do objeto
# nome e vida - atacar
#self - quando quero me referir a algum atributo da classe
#construtor - quando quero criar um novo objeto, chamo o contrutor para acessar os atributos
# __init__ - método construtor

vida = 250

class Personagem:
    #construtor
    def __init__(self, nome, vida):
        #encapsulamento
        self.__nome = nome
        self.__vida = vida
    
    #definindo GET e SET
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    def atacar(self, personagem):
        dano = random.choice(25, 45)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e tirou {dano} pontos de vida')
        print(f'agora {personagem.nome} está com {personagem.vida}')

class Guerreiro(Personagem):
    def __init__(self, nome, vida, escudo=False):
        super().__init__(nome, vida)
        self.__escudo = escudo
    
    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo
    
    #sobrescrevendo o metodo da class pai
    def atacar(self, personagem):
        dano = random.choice(35, 60)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e tirou {dano} pontos de vida')
        print(f'agora {personagem.nome} está com {personagem.vida}')
    
    def protecao(self):
        self.__vida += 20
        self.__escudo += 20


class Arcano(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self, personagem):
        curado = random.choice(25, 35)
        personagem.vida += curado
        print(f'{self.nome} usou poder de cura em {personagem.nome}')
        print(f' a vida de {personagem.nome} agora é {personagem.vida}')

class Arqueiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    @property
    def flecha(self):
        return self.__flecha
    
    @flecha.setter
    def flecha(self, flecha):
        self.__flecha = flecha

    def atacar(self, personagem):
        ataque = [35, 45, 55]
        dano = random.choice(ataque)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e tirou {dano} pontos de vida')
        print(f'agora {personagem.nome} está com {personagem.vida}') 

'''
personagem1(f'noah' 200)
personagem2(f'kaleb' 200)
personagem3(f'mortus' 200)

oponente1(f'michael' 200)
oponente2(f'diego' 200)
oponente3(f'delete' 200 )
'''
print("---PERSONAGENS---")
print('p1 - kaleb\np2 - noah\np3 - mortus\no1 - michael\no2 - diego\no3 - delete')

noah = Arqueiro('noah', vida)
kaleb = Guerreiro('kaleb', vida)
mortus = Arcano('mortus', vida)

michael = Personagem('michael', vida)
diego = Guerreiro('diego', vida)
delete = Arqueiro('delete', vida)

print('---LUTA---')
if vida <= 0:
    print ('morreu 💀')
else:
    print('====continua em batalha====')
noah.atacar(delete)