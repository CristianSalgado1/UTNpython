from tkinter import *

class Hola(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 0
        self.agregarBoton1()
        self.agregarBoton2()
    def agregarBoton1(self):
        widget = Button(self, text  ="Boton1",
                        command = self.valorVariable)
        widget.pack(side = LEFT)
    def agregarBoton2(self):
        widget = Button(self, text  ="Boton2",
                        command = self.valorVariable)
        widget.pack(side = LEFT)
    def valorVariable(self):
        self.data +=1
        print('valor %s!' % self.data)

if __name__== "__main__":
    Hola().mainloop()
