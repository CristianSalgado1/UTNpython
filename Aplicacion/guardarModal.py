from tkinter import *
import shelve
from guardar import *
from PersonaP.PersonaM import Persona
archivo = 'persona'

def guarda(variables, popUpGuardar):
    popUpGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    valor_id = lista[0]
    db =    shelve.open('persona')
    guardoValor = Persona(lista[1], lista[2], lista[3], lista[4])
    db[lista[0]] = guardoValor
    db.close()


def guardar():
    popUpGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popUpGuardar, campos)
    Button(popUpGuardar, text = 'guardar', command = (lambda : guarda(vars_guardar, popUpGuardar))).pack()

    popUpGuardar.grab_set()
    popUpGuardar.focus_set()
    popUpGuardar.wait_window()
    