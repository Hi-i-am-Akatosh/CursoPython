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
"""
x = 10

def funcion(entrada):
  entrada = 0

funcion(x)
print(x)"""

#pase por referncia

#pase de valor por referencia: 
#hace modificar la variable original
"""
x = [10,20,30]

def funcion(entrada):
  entrada.append(40)


funcion(x)
print(x)"""

#args
#Funciones Args - Kwargs 

# def suma(a,b,c):
#   return a+b+c 

# print(suma(2,4,6,1))

# *args 
"""def suma(*args):
  s = 0
  for arg in args:
    s += arg
  return s 

print(suma(1,2,3,4,5))
print(suma(2,5))"""

#kwargs
#uso kwargs

"""def suma(**kwargs):
  s = 0
  for key, value in kwargs.items():
    print(key, "=", value)
    s += value
  return s 


print(suma(a=3, b=10, c=3))"""

#combinado
#mezcla 
# 1. argumentos normales 
# 2. argumentos *args 
# 3. argumentos **kwargs

"""def funcion(a, b, *args, **kwargs):
  print("a =", a)
  print("b =", b)
  for arg in args:
    print("args =", arg)
  for key, value in kwargs.items():
    print(key, "=", value)

print(funcion(10,20,1,2,3,4,x="Hola", y="Que", z="Tal"))
print(funcion(10,20, *args, **kwargs))"""

#decoradores
#Decoradores 
"""
Modifican el comportamiento de otras funciones
@hola


def mi_decorador(funcion):
  def nueva_funcion(a,b):
    print("Se va a llamar")
    c = funcion(a, b)
    print("Se ha llamado")
    return c

  return nueva_funcion"""

"""@mi_decorador
def suma(a, b):
  print("Entra en la funcion suma")
  return a + b

@mi_decorador
def restar(a,b):
  print("Entra en la funcion resta")
  return a - b 


print(suma(5,8))
print("\n")
print(restar(10,5))
"""