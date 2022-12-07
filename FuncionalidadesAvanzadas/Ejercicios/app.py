#1 Escribir una funcion que 
# calcule el volumen de una esfera 
# dado su radio. 

#volumen(2) => 33.49333


#V = 4/3 π*r^3
"""import math 


def vol (r):
    return (4/3)*(math.pi)*(r**3)

print (vol(2))"""

#2 Escribir una funcion que verifique 
# si un numero esta en un 
# rango dado (numero - bajo - alto)

#3,2,7

#3 esta en el rango entre 2 y 7


"""def num_check(num,low,high):
    if num in range(low,high+1):
        print('{} esta en el rango entre {} y {}'.format(num,low,high))
    else:
        print('El numero esta fuera del rango.')


num_check(9,2,7)"""

"""def rango(n,n1,n2):
    if n > n1 and n < n2:
        print('{} esta en el rango entre {} y {}'.format(n,n1,n2))
    else:
        print("No esta dentro del rango")

rango(3,2,9)"""

#3 Escribir una funcion que acepte una cadena 
# de string y calcule el numero de letras mayusculas y minisculas

# s = "Hola a todos en Ecuador"
# funcion(s)

# Mayusculas = 2
# Minusculas = 17
"""def cadena(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Cadena original : ", s)
    print("No. Mayusuculas : ", d["upper"])
    print("No. Minusculas : ", d["lower"])

s = "Hola a todos en Ecuador"
cadena(s)"""  #EXAMEN LABORAL

string = input("Ingrese palabra: ")
indice=0
mayusculas=0
minusculas=0
while indice < len(string):
  letra = string[indice]
  if letra.isupper() == True:
    mayusculas +=1
  else:
    minusculas +=1
  indice += 1

print("Total mayusculas: " , mayusculas)
print("Total minusculas: " , minusculas)

