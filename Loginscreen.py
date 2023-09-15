import tkinter as tk
from Operations import Operations
from Mainscreen import Mainscreen
import mysql.connector as sqlerrors

class Loginscreen(tk.Tk):
    def __init__(self, con):
        super().__init__()
        self.op = Operations(con)

        self.geometry('700x500')
        self.title('Login')
        canvas = tk.Frame(self, width=700, height=500)
        canvas.pack()
        canvas.pack_propagate(0)

        frame_login = tk.Frame(canvas, width=300, height=500)
        frame_login.pack()
        frame_login.grid_propagate(0)
        

        username_label = tk.Label(frame_login, text='E-mail: ').grid(column=0, row=0, padx=30, pady = 100)
        username_entry = tk.Entry(frame_login)
        username_entry.grid(column=1, row=0, padx=20)

        password_label = tk.Label(frame_login, text= 'Password: ').grid(column=0, row=1)
        password_entry = tk.Entry(frame_login, show='*')
        password_entry.grid(column=1, row=1)

        button_login = tk.Button(frame_login, width=12, height=1, text='Login', command=lambda: clicked(self)).grid(column=0, row = 2, sticky='E', pady=50)

        def clicked(self):
            user_email = str(username_entry.get())
            user_password = str(password_entry.get())
            try:
                if (user_email != self.op.find_usremail_by_email(str(user_email)) or user_password != self.op.find_passwd_by_email(str(user_email)) or (user_email.strip() == "" or user_password.strip() == "")):
                    create_popup(self, 'Error', 'Incorrect Password or E-mail.')
                else:
                    self.destroy()
                    ms = Mainscreen()
            except sqlerrors.Error as error:
                create_popup(self, 'Error', 'Connection not estabilished: {}'.format(error))

        def create_popup(self, title, aviso):
            top_window = tk.Toplevel(self)
            top_window.title(title)
            top_window.geometry('300x100')
            tk.Label(top_window, text=aviso).pack()
            tk.Button(top_window, text='Ok', command=top_window.destroy).pack()