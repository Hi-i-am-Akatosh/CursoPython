#funciones decoradoras
#fuincion valores locales 
"""lista = [1,2,3]

def hola():

  numero = 50

  def bienvenido():
    return "Hola"

  print(locals()) #muestra el ambito local
  #print(globals()) #muestra el ambito global

hola()"""

#decoradores
"""def monitorizar(funcion):

  def decorar():
    print("\t* Se esta apunto de ejecutar la funcion", funcion.__name__)
    funcion()
    print("\t* Se ha finalizado la ejecucion:", funcion.__name__)

  return decorar()

@monitorizar
def adios():
  print('adios')

@monitorizar
def hola():
    print("Hola")
hola()
print()
adios()"""

#paso por valor => no cambia en python 

x = 10

def funcion(entrada):
  entrada = 0

funcion(x)
print(x)
