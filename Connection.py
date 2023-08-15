import mysql.connector

class Connection:
    def __init__(self, user, password, host, database):
        self.db_config = {
            "user" : str(user),
            "password" : str(password),
            "host" : str(host),
            "database" : str(database)
        }
        self.conn = None
    
    def conectar(self):
        try:
            if not self.conn:
                self.conn = mysql.connector.connect(**self.db_config)
                print('Conexao aberta')
            else:
                print('Conexão ja estava aberta.')
        except mysql.connector.Error as error:
            print('Erro ao abrir a conexão: {}.'.format(error))

    def desconectar(self):
        try:
            if self.conn:
                self.conn.close()
                self.conn = None
                print('Conexao fechada')
            else:
                print('Conexao ja estava fechada ou nao foi estabelecida.')
        except mysql.connector.Error as error:
            print('Erro ao fechar a conexao: {}'.format(error))