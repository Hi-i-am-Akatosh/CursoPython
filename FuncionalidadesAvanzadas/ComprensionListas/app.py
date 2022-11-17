#declaracion de lista normal 
"""lista = []
for letra in 'casa':
  lista.append(letra)
print(lista)"""

#comprension de listas
"""lista = [letra for letra in 'casa']
print(lista)"""

#metodo tradicional
"""lista = []
for numero in range(0,11):
  lista.append(numero**2)
print(lista)"""

#Comprension de lista
"""lista = [n**2 for n in range(0,11)]
print(lista)"""

#Tradicional
"""lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)"""

#Comprension

#[expresion for variable in collections if condicion]

"""lista = [n for n in range (0,11) if n % 2 == 0]
print(lista)"""

"""lista = []
for numero in range(0,11):
  lista.append(numero**2)

pares = []
for numero in lista:
  if numero % 2 == 0:
    pares.append(numero)

print(pares)"""

#Comprension

lista = [n ** 2 for n in range (0,11) if n % 2 == 0]
print(lista)
