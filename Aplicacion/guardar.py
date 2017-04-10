from tkinter import *
from cerrar import Cerrar
campos = ('id', 'nombre', 'edad', 'sueldo', 'trabajo')

def CrearFormGuardar(root, campos):
    formulario = Frame(root)
    div1 = Frame(formulario, width = 10)
    div2 = Frama(formulario, padx = 7, pady = 2)
    formulario.pack(fill = X)
    div1.pack(side = LEFT)
    div2.pack(side = RIGHT, expand = YES, fill = X)

    variables = []
    for field in campos:
        lab = Label(div1, width = 10, text = field)
        ent = Entry(div2, width = 30, relief = SUNKEN)
        lab.pack(side = TOP)
        ent.pack(side = TOP, fill = X)
        var = StringVar()
        ent.config(textvariable= var)
        var.set('---')
        variables.append(var)
    return variables