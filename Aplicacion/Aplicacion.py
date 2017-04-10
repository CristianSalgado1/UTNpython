from tkinter import *
#from guardarModal import *
#from leerModal import *
#from cerrar import Cerrar

class MiApp:
    def __init__(self, parent = None,  **configs):
        ##Ventana Principal##
        
        self.myParent = parent
        self.myParent.geometry("400x300")
        
        
        ##Agrego Contenedor ##
        self.Contenedor = Frame(self.myParent,  bg = "#444")
        self.Contenedor.pack(expand = YES,  fill = BOTH)
        
        ##Agrego Secciones Principales ##
        
        ##CERRAR##
        self.seccion_cerrar = Frame(self.Contenedor,  bg = "#FF7F50", height = 22, 
        borderwidth = 2,  relief = RAISED)
        self.seccion_cerrar.pack(side = TOP,  expand = NO,  fill = X,  padx =   7)
        
        self.cerrar = Frame(self.seccion_cerrar,  bg ="#222", height = 22)
        self.cerrar.pack(side = TOP,  expand = NO,  fill = X)
        
        ##Seccion Controles##
        self.seccion_controles = Frame(self.Contenedor,  bg = "red",  borderwidth = 2,  relief = RAISED)
        self.seccion_controles.pack(side = TOP,  expand = NO,  fill = BOTH,  padx = 7,  pady = 7)
        titulo_controles = "Controles"
        Label(self.seccion_controles,  text = titulo_controles,  bg = "#222", fg = "OrangeRed",
        justify = LEFT
        ).pack(side = TOP,  expand = NO,  fill = X, anchor = W)
        
        self.controles = Frame(self.seccion_controles,  bg = "#222", )
        self.controles.pack(side = TOP,  expand = NO,  fill = X)
        
        boton1 = Button(self.seccion_controles,  text = "Guardar",  command = guardar)
        boton1.pack()
        boton2 = Button(self.seccion_controles,  text = "Ver",  command = leer)
        boton2.pack()

if __name__ == "__main__":
    root = Tk()
    MiApp(root)
    root.mainloop()
