#Funcion Filter()

#definicion => filtrar elementos de una collections

#multiplos de 5

"""def multiplos(numero):
  if numero % 5 ==0:
    return True

numeros = [2,5,10,23,50,33]

print(filter(multiplos, numeros))

print(list(filter(multiplos, numeros)))"""

"""#creacion con lambda
print(list(filter(lambda numero: numero %5 == 0, numeros)))"""

class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad


  def __str__(self):
    return "{} de {} years".format(self.nombre, self.edad)


personas = [
  Persona("David", 20),
  Persona("Jose", 29),
  Persona("Manuel", 78),
  Persona("Eduardo", 12)
]

#personas menores de edad < 18

#personas menores de edad < 18 lambda y filter | for 
#eduado = 12 years 
#david  = 16 years 
menores = filter(lambda personas: personas.edad < 18, personas)

for menor in menores:
  print(menor)