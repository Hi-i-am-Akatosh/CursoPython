from tkinter import *
from tkinter import filedialog as FileDialog 
from io import open 


ruta = "" #almacenar la ruta del fichero


#Agregar metodos
def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Fichero de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    if ruta != "":
            fichero = open(ruta, 'r')
            contenido = fichero.read()
            texto.delete(1.0, 'end')
            texto.insert('insert', contenido)
            fichero.close()
            root.title(ruta + " - Mi editor")        
        
def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        print("Guardar como ...")

def guardar_como():
    global ruta
    mensaje.set("Guardar como ...")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode = "w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0 , 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Guardado cancelado")
        ruta = ""

root = Tk()
root.title("Mi Editor")

#Menu Superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar )
filemenu.add_command(label="Guardar como", command=guardar_como)
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

