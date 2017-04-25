from tkinter import *
from random import *

class dados:
    def __init__(self,  parent = None,  **configs):
        #Ventana Principal#
        self.myParent = parent
        self.myParent.geometry("600x600")

        
        
       # dados = ["Seis",  "Ocho",  "Diez",  "Doce",  "Viente",  "Cien"]
        
        
        
        
        #for a in range(len(dados)):
         #   Button(self.myParent,  text = dados[a]).grid(row = a,  column = 0)
         #   Entry(self.myParent). grid(row = a,  column = 1)
        #    Label(self.myParent ,  text = "-").grid(row = a,  column = 2)
        
        seisD = Button(self.myParent,  text = "Seis")
        seisD.grid(row = 0,  column = 0)
        
        self.seisE = Entry(self.myParent)
        self.seisE. grid(row = 0,  column = 1)
        self.seisE.insert(0,  10)
    

        seisT = Button(self.myParent,  text = "Tirar Seises",  command = self.tirarseis)
        seisT.grid(row = 0,  column = 3)
        

    
        

        Button(self.myParent,  text = "Tirar Dados").grid(row = 7,  column = 2)
        
        
    def tirarseis(self):
        rta = []
        for a in range(0, int(self.seisE.get())+1):
            rta.append(randint(1, 6))
            resultado = sum(rta)
        seisR = Label(self.myParent,  text = resultado)
        seisR.grid(row = 0,  column = 2)
            
if __name__ =="__main__":
    root = Tk()
    dados(root)
    root.configure(background='#1d783a')
    root.mainloop()
    
