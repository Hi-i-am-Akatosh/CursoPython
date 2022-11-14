"""#Radiobutton 

from tkinter import *

def selecionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()

opcion = IntVar()

Radiobutton(root, text="Opcion 1", variable=opcion, value=1, command=selecionar).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2, command=selecionar).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3, command=selecionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()
root.mainloop()"""

"""#CheckButton (Seleccionar)

from tkinter import *

def selec():
    cadena= ""

    if(leche.get()): cadena += "Con leche"
    else: cadena += "Sin leche"

    if(azucar.get()): cadena += "Con azucar"
    else: cadena += " y sin azucar"

    monitor.config(text=cadena)



root = Tk()
root.title("Cafeteria")

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file="image.gif")
Label(root,image=imagen).pack(side="left")

frame = Frame(root).pack(side="left")

Label(frame, text="¿Como quieres el cafe?\n").pack(anchor="w")

Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=selec).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=selec).pack(anchor="w")


monitor = Label(frame)
monitor.pack()

root.mainloop()"""


from tkinter import *

def selec():
  cadena = ""

  if(leche.get()): cadena += "Con leche"
  else: cadena += "Sin leche"

  if(azucar.get()): cadena += "y con azucar"
  else: cadena += "y sin azucar"

  monitor.config(text=cadena)
root = Tk()
root.title("Cafeteria")

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿Como quieres el cafe?\n").pack(anchor="w")

Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=selec).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=selec).pack(anchor="w")


monitor = Label(frame)
monitor.pack()

root.mainloop()