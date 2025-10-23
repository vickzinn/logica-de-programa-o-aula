from connection import get_connect


def criar_usuario():
    try:

        conn = get_connect()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (%s, %s, %s)',
                        (id, nome, email, senha)
        )

        conn.commit()
        print('usuario cadastrado com sucesso!')

        except Exception as e:
        print(f'falha ao criar tabela {e}')

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def listar_usuario():
        try:

        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()

            if usuarios:
                print(f'{30*'-'}Lista de usuarios{30*'-'}')
                for u in usuarios
                print
        except Exception as e:
        print(f'falha ao criar tabela {e}')

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def exlcuir_usuario(id):
    try:

        conn = get_connect()
        cursor = conn.cursor()

    except Exception as e:
        print(f'falha ao criar tabela {e}')

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
def editar_usuario(id):
    try:

        conn = get_connect()
        cursor = conn.cursor()

    except Exception as e:
        print(f'falha ao criar tabela {e}')

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def listar_usuario_email(email):
    try:

        conn = get_connect()
        cursor = conn.cursor()

    except Exception as e:
        print(f'falha ao criar tabela {e}')

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close() 

def criar_tabela():
    try:
        conn = get_connect()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE TB_USUARIO(
        ID INTENGER PRIMARY KEY auto_increment, 
        NOME VARCHAR(120) NOT NULL,
        EMAIL VARCHAR(120) UNIQUE,
        SENHA VARCHAR(255)
);
''')

    except Exception as e:
        print(f'falha ao criar tabela {e}')

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()