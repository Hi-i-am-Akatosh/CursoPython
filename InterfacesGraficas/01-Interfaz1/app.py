"""import tkinter as tk
raiz = tk.Tk()

raiz.mainloop()"""

from tkinter import *
raiz=Tk()
#Cambiar el nombre de la ventana.
raiz.title("Primera Ventana")
#Configuracion de tamaño
raiz.geometry("520x480")
#Cambiar icono
raiz.iconbitmap("carpeta.ico")
#Cambiar el color de fondo
raiz.config(bg="skyblue")
#No permite reajustar el tamaño del aplicativo
raiz.resizable(0,0)

#Ejecuta la ventana
raiz.mainloop()

