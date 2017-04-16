from tkinter import *
from tkinter.messagebox import *


def mensaje_error():
    showerror("Titulo del mensaje de error",  "Contenido del mensaje de error")
    
def verificar():
    if askyesno('Titulo de la consulta de verificacion',  "Contenido de la verificacion"):
        showinfo('Si',  'Mensaje de Información')
    else:
        showinfo('No',  'Está a punto de salir')

Button(text = 'Error',  command = mensaje_error).pack(fill = X)
Button(text = 'Verificar',  command = verificar).pack(fill = X)

mainloop()
