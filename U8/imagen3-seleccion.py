from tkinter import *
from glob import glob
import random

ruta = 'img/'

def seleccion():
    nombre,  foto =  random.choice(imagen)
    dialogo.config(text = nombre)
    boton.config(image = foto)
    
root = Tk()

dialogo = Label(root,  text  = "aqui va a ir la ruta",  bg = "OrangeRed")
boton = Button(root,  text = "presionar aqui para ver imagen",  command = seleccion)
dialogo.pack(fill = BOTH)
boton.pack()

archivo = glob(ruta +'*.gif')
imagen = [(x,  PhotoImage(file = x)) for x in archivo]
print(archivo)
root.mainloop()
