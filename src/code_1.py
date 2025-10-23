import sqlite3
import getpass

conn = sqlite3.connect('controle_usuario.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

conn.commit()

def cadastrar_usuario():
    username = input("Digite o nome de usuário: ")
    senha = getpass.getpass("Digite a senha: ")
    try:
        cursor.execute(
            "INSERT INTO usuarios (username, senha) VALUES (?, ?)",
            (username, senha)
        )
        conn.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Usuário já existe.")

def login():
    username = input("Usuário: ")
    senha = getpass.getpass("Senha: ")
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND senha = ?",
        (username, senha)
    )
    if cursor.fetchone():
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha inválidos.")
        return False

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    try:
        preco = float(input("Preço: ").strip().replace(',', '.'))
        quantidade = int(input("Quantidade: ").strip())
    except ValueError:
        print("Entrada inválida. Preço e quantidade devem ser números.")
        return

    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
        (nome, preco, quantidade)
    )
    conn.commit()
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return
    print("\n--- Lista de Produtos ---")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R${p[2]:.2f} | Quantidade: {p[3]}")
    print("--------------------------\n")

def editar_produto():
    listar_produtos()
    try:
        produto_id = int(input("Digite o ID do produto que deseja editar: "))
    except ValueError:
        print("ID inválido.")
        return
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    if not cursor.fetchone():
        print("Produto não encontrado.")
        return
    novo_nome = input("Novo nome: ")
    try:
        novo_preco = float(input("Novo preço: ").strip().replace(',', '.'))
        nova_qtd = int(input("Nova quantidade: "))
    except ValueError:
        print("Entrada inválida.")
        return
    cursor.execute(
        "UPDATE produtos SET nome=?, preco=?, quantidade=? WHERE id=?",
        (novo_nome, novo_preco, nova_qtd, produto_id)
    )
    conn.commit()
    print("Produto atualizado com sucesso!")

def vender_produto():
    listar_produtos()
    try:
        produto_id = int(input("Digite o ID do produto que deseja vender: "))
        qtd_venda = int(input("Quantidade a vender: "))
    except ValueError:
        print("Entrada inválida.")
        return
    cursor.execute("SELECT quantidade FROM produtos WHERE id=?", (produto_id,))
    resultado = cursor.fetchone()
    if resultado is None:
        print("Produto não encontrado.")
        return
    if resultado[0] < qtd_venda:
        print("Quantidade insuficiente em estoque.")
        return
    nova_qtd = resultado[0] - qtd_venda
    cursor.execute("UPDATE produtos SET quantidade=? WHERE id=?", (nova_qtd, produto_id))
    conn.commit()
    print("Venda realizada com sucesso!")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Editar Produto")
        print("4. Vender Produto")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            editar_produto()
        elif escolha == '4':
            vender_produto()
        elif escolha == '5':
            print("Voltando ao menu principal..")
            break
        else:
            print("Opção inválida.")

def main():
    print("Bem-vindo ao sistema de controle")
    while True:
        print("\n1. Login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")
        opcao = input("Escolha: ")
        if opcao == '1':
            if login():
                menu()
        elif opcao == '2':
            cadastrar_usuario()
        elif opcao == '3':
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
    conn.close()

