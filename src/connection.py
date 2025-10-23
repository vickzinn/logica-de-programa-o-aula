import sqlite3
def get_connect():
    try:
        conexao = sqlite3.connect("controle_usuario.db")
        print("Conexão bem sucedida")
        return conexao
    except sqlite3.Error as e:
        print("Conexão falhou")
        return None
    
get_connect()