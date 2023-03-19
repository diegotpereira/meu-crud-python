import psycopg2
import config

def conectar():
    try:
        conexao = psycopg2.connect(
            user = config.usuario,
            password = config.senha,
            database = config.database,
            host = config.host,
            port = config.port
        )
        return conexao
    except Exception as err:
        print("Ocorreu um erro ao fazer a conexão…")
        traceback.print_exc()


def imprimir_versao(conexao):
    cursor = conectar().cursor()
    cursor.execute('select version()')
    db_versao = cursor.fetchone()
    print(db_versao)
    cursor.close()
    conexao.close()

if __name__ == '__main__':

    imprimir_versao(conectar())
