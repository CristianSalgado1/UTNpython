#Estructura1


from tkinter import *

class miApp:
    def __init__(self, parent = None,  **configs):
        ##Ventana Principal##
        self.myParent = parent
        self.myParent.geometry("300x300")
        
if __name__=="__main__":
    root  = Tk()
    miApp(root)
    root.mainloop()
    
