from tkinter import *

class dados:
    def __init__(self,  parent = None,  **configs):
        #Ventana Principal#
        self.myParent = parent
        self.myParent.geometry("400x400")

        
        dados = ["Seis",  "Ocho",  "Diez",  "Doce",  "Viente",  "Cien"]
        for a in range(len(dados)):
            Button(self.myParent,  text = dados[a]).grid(row = a,  column = 0)
            Entry(self.myParent). grid(row = a,  column = 1)
            Label(self.myParent ,  text = "15").grid(row = a,  column = 2)



        


     
if __name__ =="__main__":
    root = Tk()
    dados(root)
    root.configure(background='#1d783a')
    root.mainloop()
    
