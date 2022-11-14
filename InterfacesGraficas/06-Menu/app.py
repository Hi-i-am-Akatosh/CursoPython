#Menu

from tkinter import *

root = Tk()

#Base
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)


editemenu = Menu(menubar, tearoff=0)
editemenu.add_command(label="Cortar")
editemenu.add_command(label="Copiar")
editemenu.add_command(label="Pegar")


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de..")

menubar.add_cascade(label="Archivo", menu= filemenu)
menubar.add_cascade(label="Editar", menu= editemenu)
menubar.add_cascade(label="Ayuda", menu= helpmenu)
root.mainloop()