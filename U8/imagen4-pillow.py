from tkinter import *
from PIL.ImageTk import PhotoImage
from glob import glob
import random

ruta = 'images/'

def seleccion():
    nombre,  foto = random.choice(imagen)
    dialogo.config(text = nombre)
    boton.config(image = foto)
    
root = Tk()
dialogo = Label(root,  text = "aqui va a ir la ruta",  bg = "green")
dialogo.pack(fill = BOTH)
boton = Button(root,  text = "presionar para ver imagen",  command = seleccion)
boton.pack()

archivo =  glob(ruta + "*.jpg")
imagen = [(x,  PhotoImage(file = x)) for x in archivo]
print(archivo)

root.mainloop()

