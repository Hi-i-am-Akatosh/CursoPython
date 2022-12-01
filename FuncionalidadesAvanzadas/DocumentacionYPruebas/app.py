#Docstrings
#definicion => python cuneta con una variable especial llamda doc y sirve para describir los objetos y esto recibe el nombre de docstrings.

#Funciones
"""def hola(arg):
    #Este es el docstring de la funcion#
  print("Hola", arg, "!")

hola("David")

help(hola)"""



"""def sumar(n1, n2):
    #Esta función realiza sumas
    print(n1 + n2)

sumar(2,4)
help(sumar)
"""
"""def restar(n1,n2):
    #Esta funcion realiza restas
    print(n1-n2)

restar(2,4)
help(restar)"""

#Clases y metodos

"""class Clase:
   #Este es el docstring de la clase

  def __init__(self):
    #Este es el constructor de la clase Clase
    pass

  def metodo(self):
    #Este es el docstring del metodo de clase

o = Clase()
help(o)"""

#Creaer una clase carro 
#crear metodos acelerar, frenar 
#crear la instancia de la clase
#llamar el help


"""class Carro:
    Este es el docstring de la clase

    def __init__(self):
        Este es el constructor de la clase Carro
        pass

    def acelerar(self):
        Permite aumentar la velocidad del carro

    def frenar(self):
        Permite reducir la velocidad del carro

Ins = Carro()

help(Ins)"""


import datetime

#help(datetime)
hora = datetime.datetime.now()
print(hora)
