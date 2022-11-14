#showinfo
"""
from tkinter import *
from tkinter import messagebox as MessageBox

def test():
  MessageBox.showinfo("Hola ", "Hola Mundo")


root = Tk()

Button(root, text="Click", command=test).pack()

root.mainloop()"""
#============================================
#Error
"""from tkinter import *
from tkinter import messagebox as MessageBox

def test():
  MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")


root = Tk()

Button(root, text="Click", command=test).pack()

root.mainloop()"""
#============================================
#askquestion
"""from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

resultado = MessageBox.askquestion("Salir", "¿Estas seguro que desea salir sin guardar?")

if resultado == "yes":
  root.destroy()

root.mainloop()"""
#============================================
#Rentry
"""from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")

if resultado == "yes":
  root.destroy()

root.mainloop()"""
#============================================
#colorchoser
"""from tkinter import *
from tkinter import colorchooser as ColorChooser

root = Tk()

def test():
  color = ColorChooser.askcolor(title="Elige un color")
  print(color)

test()

root.mainloop()"""
#============================================
#fileupload
"""from tkinter import *
from tkinter import filedialog as FileDialog 

root = Tk()

def test():
  archivo = FileDialog.askopenfilename(title="Abrir archivo")
  print(archivo)


test()

root.mainloop()"""
#============================================
