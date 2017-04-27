from tkinter import *
from random import *

class dados:
    resultados = []    
    def __init__(self,  parent = None,  **configs):
        #Ventana Principal#
        self.myParent = parent
        self.myParent.geometry("600x600")

        
        
       # dados = ["Seis",  "Ocho",  "Diez",  "Doce",  "Viente",  "Cien"]
        
        ###########TIRA TODOS LOS DADOS##################
        Button(self.myParent,  text = "Tirar Dados",  command = self.tirartodos).grid(row = 7,  column = 2)
        
        
        #for a in range(len(dados)):
         #   Button(self.myParent,  text = dados[a]).grid(row = a,  column = 0)
         #   Entry(self.myParent). grid(row = a,  column = 1)
        #    Label(self.myParent ,  text = "-").grid(row = a,  column = 2)
        
        ##Cuatro####################################################
        cuatroD = Button(self.myParent,  text = "Cuatro")
        cuatroD.grid(row = 0,  column = 0)
        
        self.cuatroE = Entry(self.myParent)
        self.cuatroE. grid(row = 0,  column = 1)
        self.cuatroE.insert(0,  1)
        
        
        cuatroT = Button(self.myParent,  text = "Tirar Cuatro",  command = self.tirarcuatro)
        cuatroT.grid(row = 0,  column = 3)
        
     
        ##SEISES####################################################
        seisD = Button(self.myParent,  text = "Seis")
        seisD.grid(row = 1,  column = 0)
        
        self.seisE = Entry(self.myParent)
        self.seisE. grid(row = 1,  column = 1)
        self.seisE.insert(0,  1)
    
        
        seisT = Button(self.myParent,  text = "Tirar Seises",  command = self.tirarseis)
        seisT.grid(row = 1,  column = 3)
        
        
        ##OCHO####################################################
        
        ochoD = Button(self.myParent,  text = "Ocho")
        ochoD.grid(row = 2,  column = 0)
        
        self.ochoE = Entry(self.myParent)
        self.ochoE. grid(row = 2,  column = 1)
        self.ochoE.insert(0,  1)
    

        ochoT = Button(self.myParent,  text = "Tirar Ochos",  command = self.tirarocho)
        ochoT.grid(row = 2,  column = 3)
        ####Diez###
        
        diezD = Button(self.myParent,  text = "Diez")
        diezD.grid(row = 3,  column = 0)
        
        self.diezE = Entry(self.myParent)
        self.diezE. grid(row = 3,  column = 1)
        self.diezE.insert(0,  1)
    

        diezT = Button(self.myParent,  text = "Tirar Dieces",  command = self.tirardiez)
        diezT.grid(row = 3,  column = 3)
        
        
        ############ DOCE##################
        
        doceD = Button(self.myParent,  text = "Doce")
        doceD.grid(row = 4,  column = 0)
        
        self.doceE = Entry(self.myParent)
        self.doceE. grid(row = 4,  column = 1)
        self.doceE.insert(0,  1)
    

        doceT = Button(self.myParent,  text = "Tirar Doces",  command = self.tirardoce)
        doceT.grid(row = 4,  column = 3)
        
        ############ Veinte##################
        
        veinteD = Button(self.myParent,  text = "Veinte")
        veinteD.grid(row = 5,  column = 0)
        
        self.veinteE = Entry(self.myParent)
        self.veinteE. grid(row = 5,  column = 1)
        self.veinteE.insert(0,  1)
    

        veinteT = Button(self.myParent,  text = "Tirar Veintes",  command = self.tirarveinte)
        veinteT.grid(row = 5,  column = 3)
        
    
        
        ############ Cien##################
        
        cienD = Button(self.myParent,  text = "Cien")
        cienD.grid(row = 6,  column = 0)
        
        self.cienE = Entry(self.myParent)
        self.cienE. grid(row = 6,  column = 1)
        self.cienE.insert(0,  1)
    

        cienT = Button(self.myParent,  text = "Tirar Cienes",  command = self.tirarcien)
        cienT.grid(row = 6,  column = 3)
        
    
        
    def tirarcuatro(self):
        rta = []
        for a in range(0, int(self.cuatroE.get())):
            rta.append(randint(1, 4))
            resultado = sum(rta)
            self.resultados.append(resultado)
        cuatroR = Label(self.myParent,  text = resultado)
        cuatroR.grid(row = 0,  column = 2)
    
    
        
    def tirarseis(self):
        rta = []
        for a in range(0, int(self.seisE.get())):
            rta.append(randint(1, 6))
            resultado = sum(rta)
            self.resultados.append(resultado)
        seisR = Label(self.myParent,  text = resultado)
        seisR.grid(row = 1,  column = 2)
            
    def tirarocho(self):
        rta = []
        for a in range(0, int(self.ochoE.get())):
            rta.append(randint(1, 8))
            resultado = sum(rta)
            self.resultados.append(resultado)
        ochoR = Label(self.myParent,  text = resultado)
        ochoR.grid(row = 2,  column = 2)
            
    
        
    def tirardiez(self):
        rta = []
        for a in range(0, int(self.doceE.get())):
            rta.append(randint(1, 10))
            resultado = sum(rta)
            self.resultados.append(resultado)
        doceR = Label(self.myParent,  text = resultado)
        doceR.grid(row = 3,  column = 2)
    
    
    def tirardoce(self):
        rta = []
        for a in range(0, int(self.doceE.get())):
            rta.append(randint(1, 12))
            resultado = sum(rta)
            self.resultados.append(resultado)
        doceR = Label(self.myParent,  text = resultado)
        doceR.grid(row = 4,  column = 2)
    
        
    def tirarveinte(self):
        rta = []
        for a in range(0, int(self.veinteE.get())):
            rta.append(randint(1, 20))
            resultado = sum(rta)
            self.resultados.append(resultado)
        veinteR = Label(self.myParent,  text = resultado)
        veinteR.grid(row = 5,  column = 2)
    
    def tirarcien(self):
        rta = []
        for a in range(0, int(self.cienE.get())):
            rta.append(randint(1, 100))
            resultado = sum(rta)
            self.resultados.append(resultado)
        cienR = Label(self.myParent,  text = resultado)
        cienR.grid(row = 6,  column = 2)
    def tirartodos(self):
        self.tirarcuatro()
        self.tirarseis()
        self.tirarocho()
        self.tirardoce()
        self.tirardiez()
        self.tirarveinte()
        self.tirarcien()
        total = sum(self.resultados)
        totalR = Label(self.myParent,  text = total)
        totalR.grid(row = 8,  column =2)
        self.reset()
    def reset(self):
        self.resultados = []
        
        
if __name__ =="__main__":
    root = Tk()
    dados(root)
    root.configure(background='#1d783a')
    root.mainloop()
    
