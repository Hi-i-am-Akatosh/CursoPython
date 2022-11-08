#import tkinter as tk
from tkinter import * 

raiz = Tk()
#cambiar el nombre de la ventana
raiz.title("Primera Ventana") 
#configurar tamano
raiz.geometry("520x480")
#cambiar icono
raiz.iconbitmap("temperatura.ico")

def caracteres(saludo,nombre):
    return f"Hola! {saludo} ¿Comó estas {nombre}?"

#Añadir Labels de texto en la ventana
texto = Label(raiz, text = caracteres(saludo = "Bienvenido a mi programa", nombre = "David Navarro"))

texto.config(fg="green",
bg="yellow",
padx=20,
pady=20,
font=("Tahoma",12),
anchor=W,
cursor="dotbox"
)

texto.pack(side = TOP)

def pruebas(apellido, pais):
    return f"{apellido}, veo que eres de {pais}"

texto = Label(raiz, text = pruebas(apellido = "Navarro", pais = "Ecuador"))

texto.config(fg="green",
bg="orange",
padx=40,
pady=40,
font=("Tahoma",12),
anchor=W,
cursor="circle",
justify= "right"
)

texto.pack(side = TOP)


#ejecuta la ventana
raiz.mainloop()


"""def addText(estudiante, universidad):
  return f"{estudiante} de la {universidad}"

texto = Label(raiz, text=addText(estudiante="Informatica", universidad="Universidad de Quito"))
texto.config(
  fg="red",
  bg="cyan",
  padx=20,
  pady=20,
  font=("Tahoma", 15),
  justify=CENTER
)

texto.pack(side=BOTTOM, fill=X, expand=YES)"""