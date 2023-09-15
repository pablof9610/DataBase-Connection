from tkinter import Tk, Frame, Button

class Mainscreen:
    def __init__(self):
        mainscreen = Tk()

        mainscreen.geometry('700x500')

        frame_operations = Frame(mainscreen, width=700, height=50, background='black')
        frame_operations.pack_propagate(0)


        button_create = Button(frame_operations, text='Create', width=50).pack(side='left')
        button_read = Button(frame_operations, text='Read').pack(side='left')
        button_update = Button(frame_operations, text='Update').pack(side='left')
        button_delete = Button(frame_operations, text='Delete').pack(side='left')

        frame_operations.pack(side='top')

        mainscreen.mainloop