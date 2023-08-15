from Connection import Connection
from Operations import Operations

matricula = int(input('Digite sua matricula: '))
email = str(input('Digite o seu e-mail: ')).strip()
senha = str(input('Digite sua senha: ')).strip()

# Criando a conexão
con = Connection('root', '', '127.0.0.1', 'teste')

# Passando a instância do objeto com a conexão para a instância do objeto de operações usar
op = Operations(con)

if (op.find_usremail_by_id(matricula) != email or op.find_passwd_by_id(matricula) != senha):
    while(op.find_usremail_by_id(matricula) != email or op.find_passwd_by_id(matricula) != senha):
        print('E-mail ou senha incorreta. Por favor, digite novamente: ')
        email = str(input('E-mail: '))
        senha = str(input('Senha:'))
    print('Usuário autenticado.')