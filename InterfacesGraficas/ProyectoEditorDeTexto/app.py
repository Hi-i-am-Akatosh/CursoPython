from tkinter import *
from tkinter import filedialog as FileDialog 
from io import open 


ruta = "" #almacenar la ruta del fichero

root = Tk()
root.title("Mi Editor")

#Menu Superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Guardar como")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)
#Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(padx=6,  pady=4, bd=0, font=("Consolas", 12))

#Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='right')
monitor.pack(side='left')

root.config(menu= menubar)

root.mainloop()

