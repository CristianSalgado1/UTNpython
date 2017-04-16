from tkinter import *
import os
ruta = os.getcwd()
win = Tk()

imagen = PhotoImage(file = "downl.png")
can = Canvas(win)
can.pack(fill = BOTH)
can.create_image(2, 2,  image  = imagen ,  anchor = NW)




win.mainloop()
