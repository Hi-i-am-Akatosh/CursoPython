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

"""
import datetime

#help(datetime)
hora = datetime.datetime.now()
print(hora)"""

#================================================

#DOCTEST 
"""def suma(a,b):
  #Esta funcion recibe dos parametros y devuelve la suma de ambos

  >>> suma(5, 4)
 
  return a+b

if __name__ == "__main__":
  import doctest
  doctest.testmod()"""

  
  
#DOCTEST 
def resta(a,b):
  """Esta funcion recibe dos parametros y devuelve la resta de ambos

  >>> resta(5, 4)
  1
  """
  return a-b

if __name__ == "__main__":
  import doctest
  doctest.testmod()


def doblar(lista):
  """Duplica el valor de los elementos de una lista
  
  >>> l = [1,2,3,4,5]
  >>> doblar(l)
  [2, 4, 6, 8, 10]
  """
  return [n*2 for n in lista]

if __name__ == "__main__":
  import doctest
  doctest.testmod()