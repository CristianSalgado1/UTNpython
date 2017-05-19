import os
import shelve
from tkinter import *
from random import *


class dados:
    resultados = [] 
    dados = {"Cuatro":0,  "Seis":0,  "Ocho":0,  "Diez":0,  "Doce":0,  "Veinte":0,  "Cien":0}
    guardarA = "default"
    guardados = os.listdir('guardados')
    
     
    def __init__(self,  parent = None,  **configs):
        #Ventana Principal#
        self.myParent = parent
        self.myParent.geometry("600x600")

        
        
       
        
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
        
        ####RESETEAR##
        resetB = Button(self.myParent,  text = "Resetear",  command = self.reset)
        resetB.grid(row = 8,  column = 4)
        
        ## Guardar ##
        
        guardarB= Button(self.myParent,  text = "Guardar Dados",  command = self.guardar)
        guardarB.grid(row = 9,  column = 4)

        self.guardarT = Entry(self.myParent)
        self.guardarT.grid(row = 9,  column = 3)
        
        ##Cargar##
        self.variable = StringVar(self.myParent)
        self.variable.set(self.guardados[0]) # default value

        self.optionList = tuple([tuple(row) for row in self.guardados])
        self.w = OptionMenu(self.myParent, self.variable,  *self.optionList)
        self.w.grid(row = 9,  column = 0)
        
        b = Button(self.myParent,  text = "Cargar Guardados",  command = self.cargar)
        b.grid(row = 9, column = 1)
        
    
        
    def tirarcuatro(self):
        rta = []
        for a in range(0, int(self.cuatroE.get())):
            rta.append(randint(1, 4))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.cuatroR = Label(self.myParent,  text = resultado)
        self.cuatroR.grid(row = 0,  column = 2)
        self.dados['Cuatro'] = rta
    
    
        
    def tirarseis(self):
        rta = []
        for a in range(0, int(self.seisE.get())):
            rta.append(randint(1, 6))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.seisR = Label(self.myParent,  text = resultado)
        self.seisR.grid(row = 1,  column = 2)
        self.dados['Seis'] = rta
        
    def tirarocho(self):
        rta = []
        for a in range(0, int(self.ochoE.get())):
            rta.append(randint(1, 8))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.ochoR = Label(self.myParent,  text = resultado)
        self.ochoR.grid(row = 2,  column = 2)
        self.dados['Ocho'] = rta
    
        
    def tirardiez(self):
        rta = []
        for a in range(0, int(self.doceE.get())):
            rta.append(randint(1, 10))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.diezR = Label(self.myParent,  text = resultado)
        self.diezR.grid(row = 3,  column = 2)
        self.dados['Diez'] = rta
    
    
    def tirardoce(self):
        rta = []
        for a in range(0, int(self.doceE.get())):
            rta.append(randint(1, 12))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.doceR = Label(self.myParent,  text = resultado)
        self.doceR.grid(row = 4,  column = 2)
        self.dados['Doce'] = rta
    
        
    def tirarveinte(self):
        rta = []
        for a in range(0, int(self.veinteE.get())):
            rta.append(randint(1, 20))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.veinteR = Label(self.myParent,  text = resultado)
        self.veinteR.grid(row = 5,  column = 2)
        self.dados['Veinte'] = rta
    
    def tirarcien(self):
        rta = []
        for a in range(0, int(self.cienE.get())):
            rta.append(randint(1, 100))
            resultado = sum(rta)
        self.resultados.append(resultado)
        self.cienR = Label(self.myParent,  text = resultado)
        self.cienR.grid(row = 6,  column = 2)
        self.dados['Cien'] = rta
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
    
    def reset(self):
        self.resultados = []
    def guardar(self):
        os.chdir('guardados')
        self.guardarA = self.guardarT.get()
        archivo = shelve.open(str(self.guardarA))
        archivo['a'] = self.dados
        archivo.close()
        os.chdir('..')
        self.guardados = os.listdir('guardados')
        self.variable = StringVar(self.myParent)
        self.variable.set(self.guardados[0]) # default value
        self.optionList = tuple([tuple(row) for row in self.guardados])
        self.w = OptionMenu(self.myParent, self.variable,  *self.optionList)
        self.w.grid(row = 9,  column = 0)
        
    def cargar(self):
        os.chdir('guardados')
        dbCargada = self.variable.get()
        regex = re.compile('[^a-zA-Z0-9_]')
        archivoD = regex.sub('', dbCargada)
        archivo = shelve.open(archivoD)
        dictArchivo =archivo["a"]
        print(archivo['a'])
        valores = archivo['a'].values()
        print(valores)
        #totalR = Label(self.myParent,  text = todos)
        #totalR.grid(row = 8,  column =2)    
        
        self.cuatroR = Label(self.myParent,  text = str(dictArchivo['Cuatro']))
        self.cuatroR.grid(row = 0,  column = 2)
        self.seisR = Label(self.myParent,  text = str(dictArchivo['Seis']))
        self.seisR.grid(row = 1,  column = 2)
        self.ochoR = Label(self.myParent,  text = str(dictArchivo['Ocho']))
        self.ochoR.grid(row = 2,  column = 2)
        self.diezR = Label(self.myParent,  text = str(dictArchivo['Diez']))
        self.diezR.grid(row = 3,  column = 2)
        self.doceR = Label(self.myParent,  text = str(dictArchivo['Doce']))
        self.doceR.grid(row = 4,  column = 2)
        self.veinteR = Label(self.myParent,  text = str(dictArchivo['Veinte']))
        self.veinteR.grid(row = 5,  column = 2)
        self.cienR = Label(self.myParent,  text = str(dictArchivo['Cien']))
        self.cienR.grid(row = 6,  column = 2)

        archivo.close()
        os.chdir('..')
    
        
if __name__ =="__main__":
    root = Tk()
    dados(root)
    root.configure(background='#1d783a')
    root.mainloop()
    
