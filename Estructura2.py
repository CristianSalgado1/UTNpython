#Estructura2


from tkinter import *

class miApp:
    def __init__(self, parent = None,  **configs):
        ##Ventana Principal##
        self.myParent = parent
        self.myParent.geometry("300x300")
        ##Agrego Contenedor##
        self.Contenedor = Frame(self.myParent, bg="#444")
        self.Contenedor.pack(expand = YES,  fill = BOTH)
        
        #Agregando Secciones Principales#
        ##CERRAR##
        self.seccion_cerrar = Frame(self.Contenedor, bg ="#FF7F50", height = 22, borderwidth = 2, relief = RAISED)
        self.seccion_cerrar.pack(side = TOP,  expand = NO,  fill = X,  padx = 7)
        
        self.cerrar = Frame(self.seccion_cerrar,  bg = "#222", height = 22)
        self.cerrar.pack(side = TOP,  expand = NO,  fill = X)
        
        ##SECCION CONTROLES##
        
        self.seccion_controles = Frame(self.Contenedor,  bg = "red",  borderwidth= 3,  relief  = RAISED)
        self.seccion_controles.pack(side = TOP,  expand = NO,  fill = BOTH,  padx =7, pady = 7)
        
        titulo_controles= "Controles"
        Label(self.seccion_controles,   text = titulo_controles,  bg ="#222", fg = "OrangeRed", justify = LEFT).pack(side = TOP, expand = NO,   fill = X, anchor = W)
        self.controles = Frame(self.seccion_controles,  bg= "#222")
        self.controles.pack(side = TOP)
        
        #Seccion REPRESENTACION#
        self.seccion_representacion = Frame(self.Contenedor,  bg ="red",  borderwidth = 2,  relief = RAISED)
        self.seccion_representacion.pack(side = BOTTOM,  expand = YES,  fill =BOTH,  padx = 7,  pady = 7)
        
        titulo_grafico = "Representacion Grafica"
        Label(self.seccion_representacion,  text = titulo_grafico,  bg ="#222", fg = "OrangeRed", justify = LEFT).pack(side = TOP, expand = NO, fill = X, anchor = W)
        self.representacion = Frame(self.seccion_representacion,  bg = "OrangeRed")
        self.representacion.pack(side = TOP,  expand = YES,  fill = BOTH)
      
      
if __name__=="__main__":
    root  = Tk()
    miApp(root)
    root.mainloop()
    
