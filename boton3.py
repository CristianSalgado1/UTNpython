#boton3.py

from tkinter import *
from boton1 import HolaButton

class TemadeButton():
    def __init__(self, parent = None, **config):
        self.myParent = parent
        self.myParent.geometry("1000x120")
        button = Button(self.myParent, **config)
        button.pack()
        button.config(fg = "red", bg = 'yellow', font =('courier', 12), relief = RAISED, bd = 5)

def callback2():
    print('callback2')


if __name__ == "__main__":
    root = Tk()
    B1 = TemadeButton(root, text = 'Boton con tema y con callback', command = callback2)
    B1 = TemadeButton(root, text = 'Boton con tema y sin callback')
    B3 = HolaButton(root, text = 'Boton sin tema')
    root.mainloop()
    
