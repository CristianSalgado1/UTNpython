from tkinter import *


class AppDado:
    def __init__(self, parent = None, **configs):
        self.myParent = parent
        self.myParent.geometry("500x500")

        ##Contenedor##
        self.Contenedor = Frame(self.myParent, bg = "#27AE60").pack(expand = YES, fill = BOTH)
        


if __name__ == "__main__":
    root = Tk()
    AppDado(root)
    root.mainloop()
