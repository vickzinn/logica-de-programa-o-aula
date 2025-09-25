'''
atividade biblioteca com POO

# classe - espaço onde vou escrever um objeto
# atributos - características do objeto
# métodos - ações do objeto
# nome e vida - atacar
#self - quando quero me referir a algum atributo da classe
#construtor - quando quero criar um novo objeto, chamo o contrutor para acessar os atributos
# __init__ - método construtor
'''
import json 
import os

livro = []

class Livro:
    def __init__(self, nomelivro):
        self.__nomelivro = novo_livro
    
    @property
    def nomelivro(self):
        return self.__livro
    
    @nomelivro.setter
    def livro(self, novo_livro):
        self.__nome = novo_livro

    def adicionar_livro(self, livro):
        adicionar.livro += 1
        print(f'agora temos {adicionar.Livro} livros')

class Cliente(Livro):
    def __init__(self, nomelivro):
        super().__init__(novo_livro)
    
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente_pegar(self, cliente_pegar):
        self.__cliente = cliente_pegar

    def cliente_pegar(self, livro):
        cliente.pegar -= 1
        print(f'agora {cliente.pegar} está com {adicionar.livro} livros')
