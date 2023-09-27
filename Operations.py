import mysql.connector
from cryptography.fernet import Fernet

class Operations:
    def __init__(self, con):
        self.con = con

    def create(self, name, bornyear, gender, email, password):

        encrypted = bytes(password, encoding='utf-8')
        encrypted = self.encrypt(encrypted)

        try:
            self.con.conectar()

            query = "INSERT INTO pessoa (nome, idade, sexo, email, senha, crypt_key) VALUES (%s, %s, %s, %s, %s, %s)"
            data_person = (name, bornyear, gender, email, encrypted[0], encrypted[1])
            print(query)
            cursor = self.con.conn.cursor()
            cursor.execute(query, data_person)
            self.con.conn.commit()

            self.con.desconectar()
        except mysql.connector.Error as error:
            print('Ocorreu um erro na persistência de dados: {}'.format(error))
        else:
            print('Persistência realizada com sucesso.')
    
    #in development
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

    def find_usremail_by_email(self, email):
        self.con.conectar()

        query = f"SELECT email FROM teste.pessoa WHERE email = '{email}'"
        cursor = self.con.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        result = result

        self.con.desconectar()
        return str(result)[3:str(result).rfind("'")].strip()
    
    def find_passwd_by_email(self, email):
        self.con.conectar()

        query = f"SELECT senha FROM teste.pessoa WHERE email = '{email}'"
        cursor = self.con.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        result = result

        self.con.desconectar()
        return str(result)[3:str(result).rfind("'")].strip()

    def encrypt(self, password):
        key = Fernet.generate_key()

        # for while, i kept the key to decrypt the password
        # on the "main" db because the purpose of this project is to study
        list = [str(Fernet(key).encrypt(password))[2:str(Fernet(key).encrypt(password)).rfind("'")], key]
        return list
    
    def decrypt(self, token, key) -> bytes:
        return Fernet(key).decrypt(token)