
import json
import os
#CLASSE LIVRO
class Livro:
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

    def to_dict(self):
        """Converte o objeto Livro em um dicionário para salvar no JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "isbn": self.isbn
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Livro a partir de um dicionário."""
        return Livro(
            id=data["id"],
            titulo=data["titulo"],
            autor=data["autor"],
            ano=data["ano"],
            isbn=data["isbn"]
        )
    #CLASSE BIBLIOTECA
class Biblioteca:
    def __init__(self, arquivo="livros.json"):
        self.arquivo = arquivo
        self.livros = []
        self.carregar_livros()

    def carregar_livros(self):
        """Carrega os livros salvos no arquivo JSON."""
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                    self.livros = [Livro.from_dict(l) for l in dados]
                except json.JSONDecodeError:
                    self.livros = []
        else:
            self.livros = []

    def salvar_livros(self):
        """Salva a lista de livros no arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([livro.to_dict() for livro in self.livros], f, indent=4)

    def adicionar_livro(self, titulo, autor, ano, isbn):
        """Adiciona um novo livro à biblioteca."""
        novo_id = 1 if not self.livros else self.livros[-1].id + 1
        novo_livro = Livro(novo_id, titulo, autor, ano, isbn)
        self.livros.append(novo_livro)
        self.salvar_livros()

    def listar_livros(self):
        """Retorna a lista de livros."""
        return self.livros

    def atualizar_livro(self, id, novo_titulo, novo_autor, novo_ano, novo_isbn):
        """Atualiza as informações de um livro pelo ID."""
        for livro in self.livros:
            if livro.id == id:
                livro.titulo = novo_titulo
                livro.autor = novo_autor
                livro.ano = novo_ano
                livro.isbn = novo_isbn
                self.salvar_livros()
                return True
        return False

    def excluir_livro(self, id):
        """Exclui um livro da biblioteca pelo ID."""
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                self.salvar_livros()
                return True
        return False
#INTERFACE
def menu():
    print("\n========== MENU BIBLIOTECA ==========")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Atualizar livro")
    print("4. Excluir livro")
    print("5. Sair")
    print("=====================================")

def interface():
    bib = Biblioteca()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            isbn = input("ISBN: ")
            bib.adicionar_livro(titulo, autor, ano, isbn)
            print(" Livro adicionado com sucesso!")

        elif opcao == "2":
            livros = bib.listar_livros()
            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                print("\nLista de Livros:")
                for livro in livros:
                    print(f"[ID: {livro.id}] {livro.titulo} - {livro.autor} ({livro.ano}) | ISBN: {livro.isbn}")

        elif opcao == "3":
            try:
                id = int(input("ID do livro a atualizar: "))
                novo_titulo = input("Novo título: ")
                novo_autor = input("Novo autor: ")
                novo_ano = input("Novo ano: ")
                novo_isbn = input("Novo ISBN: ")
                if bib.atualizar_livro(id, novo_titulo, novo_autor, novo_ano, novo_isbn):
                    print("Livro atualizado com sucesso!")
                else:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id = int(input("ID do livro a excluir: "))
                if bib.excluir_livro(id):
                    print("Livro excluído com sucesso!")
                else:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")
#EXECUTA
interface()