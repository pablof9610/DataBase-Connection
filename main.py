from Connection import Connection
from window.Loginscreen import Loginscreen

user = 'root'
password = ''
host = '127.0.0.1'
database = 'teste'

con = Connection(user, password, host, database)
app = Loginscreen(con).mainloop()