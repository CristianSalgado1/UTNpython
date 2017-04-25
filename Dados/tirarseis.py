from random import *

def tirarseis(self):
    rta = []
    for a in range(0, int(self.seisE.get())+1):
        rta.append(randint(1, 6))
        resultado = sum(rta)
    seisR = Label(self.myParent,  text = resultado)
    seisR.grid(row = 0,  column = 2)
