#Generadores 
#yield => iterable 

"""def funcion():
  return 5
print(funcion())


def generador():
  yield 5
print(generador())


def generador():
  yield 5

a = generador()
print(next(a))"""
#=========================
"""def generador():
  n = 2
  yield n

  n += 2
  yield n

  n += 2
  yield n 

g = generador()
print(next(g))
print(next(g))
print(next(g))"""
#=============================
#Iteracion For
"""def generador():
  n = 2
  yield n

  n += 2
  yield n

  n += 2
  yield n 

  n += 2
  yield n 

for i in generador():
  print(i)"""

#=============================
#lista normal
"""lista = [2,4,6,8,10]
#comprension listas 
al_cuadrado = [x**2 for x in lista]
print(al_cuadrado)"""
#=============================
"""#lista normal
lista = [2,4,6,8,10]

#generador
al_cuadrado_generador = (x**2 for x in lista)
print(al_cuadrado_generador)

#ejecucion
for i in al_cuadrado_generador:
  print(i)"""

#=======generator con clases

"""class AlCuadrado:
  
  def __init__(self):
    self.i = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.i > 9:
      raise StopIteration

    result = self.i ** 2
    self.i += 1 
    return result

#creacion nuestro objeto
eleva_al_cuadrado = AlCuadrado()

#iteracion de nuestro clase generador
for i in eleva_al_cuadrado:
  print(i)"""

#=====================================

"""def listaNumeros(n):
  nums = []
  for i in range(n):
    nums.append(i)
  return nums

print(sum(listaNumeros(100)))"""

#======================================

"""def lista2Numeros(n):
  num = 0
  for i in range(n):
    yield num
    num += 1

print(sum(lista2Numeros(100)))"""
