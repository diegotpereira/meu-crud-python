from conexao import *

def criar_tabela(conexao):
    cursor = conexao.cursor()

    sql = '''
    CREATE TABLE usuarios(id serial not null, 
    nome varchar(60),
    telefone varchar(60));
    '''

    try:
        cursor.execute(sql)
        conexao.commit()
        print('Tabela criada com sucesso')

    except(Exception, Error) as error:
        print(error)

    finally:
        if conexao is not None:
            cursor.close()
            conexao.close()
            print('\nBanco de dados fechado')

if __name__ == '__main__':

    criar_tabela(conectar())