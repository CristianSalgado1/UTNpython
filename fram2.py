from sys import exit
from tkinter import *
from frame1 import Hola

root = Tk()
root.geometry("300x300")

parent = Frame(root, bg = "yellow", width = 300, height = 100)

parent.pack(expand = YES, fill = X)

Hola(parent).pack(side = RIGHT)
Button(parent, text = "Agregado", command = exit).pack(side = TOP)

root.mainloop()
