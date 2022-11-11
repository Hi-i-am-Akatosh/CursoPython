from tkinter import *

def borrar():
    n1.set('')
    n2.set('')

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def muti():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def div():
    r.set(float(n1.get()) / float(n2.get()))
    borrar()


root = Tk()

n1 = StringVar()
n2 = StringVar()
r = StringVar()

root.geometry("320x280")

Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", state="disabled", textvariable=r).pack()

Label(root, text="").pack()

Button(root,text="Sumar",command=sumar).pack(side="left")
Button(root,text="Restar",command=resta).pack(side="left")
Button(root,text="Multiplicar",command=muti).pack(side="left")
Button(root,text="Dividir",command=div).pack(side="left")



root,mainloop()