class Operations:
    def __init__(self, con):
        self.con = con

    def create(self):
        self.con.conectar()

        query = 'INSERT INTO teste.pessoa VALUES ()'
    
    def read(self):
        self.con.conectar()

        query = 'SELECT * FROM teste.pessoa'
        cursor = self.con.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()
        self.con.desconectar()

    def find_passwd_by_id(self, id):
        self.con.conectar()
        query = f'SELECT senha FROM teste.pessoa WHERE id = {id}'
        cursor = self.con.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        result = result
        self.con.desconectar()
        return str(result)[2:str(result).rfind("'")].strip()
    
    def find_usremail_by_id(self, id):
        self.con.conectar()
        query = f'SELECT email FROM teste.pessoa WHERE id = {id}'
        cursor = self.con.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        result = result
        self.con.desconectar()
        return str(result)[2:str(result).rfind("'")].strip()

    #def authenticate(self):
    #    self.con.conectar()
    #
    #    query = 'SELECT senha FROM teste.pessoa'
    #    cursor = self.con.conn.cursor()
    #    cursor.execute(query)
    #    result = cursor.fetchall()
    #    cursor.close()
    #    self.con.desconectar()