#FUNCIONES MAP()
#DEFINIICON => DEVULVE UN ITERABLE DE TIPO MAP

"""def doblar(numero):
  return numero**2

numeros = [2,5,10,23,50,33]

print(list(map(doblar, numeros)))"""

#Con lambda
"""numeros = [2,5,10,23,50,33]
print(list(map(lambda numero: numero ** 2, numeros)))"""

#Tradicional
"""a = [1,2,3,4,5,9]
b = [6,7,8,9,10]

print(list(map(lambda x,y: x + y, a, b)))"""

#Con lambda

"""a = [1,2,3,4,5,9]
b = [6,7,8,9,10,15]
c = [2,5,10,23,50,33]

print(list(map(lambda x,y,z: x + y + z, a, b, c)))"""

#mapeos de objetos 

"""class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __str__(self):
    return "{} de {} years".format(self.nombre, self.edad)

personas = [
  Persona("David", 20),
  Persona("Maria", 30),
  Persona("Jose", 40),
  Persona("Andrea", 50),
  Persona("Elena", 60),
]

personas = map(lambda p: Persona(p.nombre, p.edad + 1), personas)

#mostrarlos 
for persona in personas:
  print(persona)"""

#ejercio base
elementos = ['casa', 'arbol', 'patio']

resultado = list(map(list, elementos))
print(resultado)

#resultado
# [['c','a','s','a'],['a','r','b','o','l'],['p','a','t','i','o']]

#resultado
#[['c','a','s','a'],['a','r','b','o','l'],['p','a','t','i','o']]