"""
EXPRESIONES REGUALRES
ES COMO 'REGEX' - 'REGEXP' => que son patrones de busqueda
estan definos con una sintaxis formal.
"""

"""#Metodos basicos 
import re

palabra = "hola"
texto = "En esta cadena se encuentra una palabra magica"

encontrado = re.search(palabra, texto)

if encontrado:
  print("Se ha encontrado la palabra:", palabra)
else:
  print("No se ha encontrado la palabra:", palabra)


#Metodos basicos 
import re

palabra = "hola"
texto = "En esta cadena se encuentra una palabra magica"

encontrado = re.match(palabra, texto)

if encontrado:
  print("Se ha encontrado la palabra:", palabra)
else:
  print("No se ha encontrado la palabra:", palabra)

#rs.split: divide una cadena a partir de un patron

import re 

texto = "Vamos a dividir esta cadena"
print(re.split('', texto))

#re.sub => permite sustituir todas las coincidencias de una cadena

import re 

texto = "Hola amigo"
print(re.sub('amigo', 'amiga', texto))

#re.findall => permite buscar todas las coincidencias en una cadena

import re 

texto = "Hola adios hola hola"
print(re.findall('hola', texto))
print(len(re.findall('hola', texto)))

import re

#Patrones con varios valores
texto = "hola adios hello bye"
print(re.findall('hola | hello', texto))

import re

#Patrones con sintaxis repetida
texto = "hla hola hoola hooola hooooola"

def buscar(patrones, texto):
  for patron in patrones:
    print(re.findall(patron,  texto))

patrones= ['hla', 'hola', 'hoola', 'HOLA']
buscar(patrones, texto)

import re

#Patrones con sintaxis con meta caracter*
texto = "hla hola hoola hooola hooooola"

def buscar(patrones, texto):
  for patron in patrones:
    print(re.findall(patron,  texto))

patrones= ['hla', 'ho*', 'ho*la', 'hu*la']
buscar(patrones, texto)

#Patrones con sintaxis con meta caracter+
texto = "hla hola hoola hooola hooooola"

def buscar(patrones, texto):
  for patron in patrones:
    print(re.findall(patron,  texto))

patrones= ['ho*', 'ho+']
buscar(patrones, texto)

#Patrones con sintaxis con meta caracter ?
texto = "hla hola hoola hooola hooooola"

def buscar(patrones, texto):
  for patron in patrones:
    print(re.findall(patron,  texto))

patrones= ['ho*', 'ho+', 'ho?', 'ho?la']
buscar(patrones, texto)

import re

#Con numero de repeticiones explicito {n}
texto = "hla hola hoola hooola hooooola"

def buscar(patrones, texto):
  for patron in patrones:
    print(re.findall(patron,  texto))

patrones= ['ho{0}la', 'ho{1}la', 'ho{2}la', 'ho{3}la' ]
buscar(patrones, texto)"""

#con un numero de repeticiones en un rango {n, m}
"""import re 

texto = "hla hola hoola hooola hooooola"


def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )

patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']
buscar(patrones, texto)
"""
#conjunto de caracteres 
"""import re 

texto = "hala hela hila hola hula"


def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )


patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
buscar(patrones, texto)"""
#Exclusion de grupos[^]
"""
import re 

texto = "hala hela hila hola hula"


def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )


patrones = ['h[s]la', 'h[^u]la']
buscar(patrones, texto)"""

#RANGOS[-]
"""
.[A-Z] => cualquier caracter alfabetico en mayuscula.
.[a-z] => cualquier caracter alfabetico en minuscula. 
.[A-Za-z] => cualquier caracter alfabetico en minuscula O mayuscula.
.[A-z] => cualquier caracter alfebetico en minuscula o mayuscula
.[0-9] => cualquier caracter numerico  
.[a-zA-Z0-9] => cualquier caracter alfanumerico  
"""
"""import re 

texto = "hola h0la Hola mola M0la"
def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )


patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}']
buscar(patrones, texto)"""

#Codigos escapados \
"""
codigo   | Significado
----------------------------------
  \d     | numerico
  \D     | no numerico
  \s     | espacio en blanco
  \S     | no espacio en blanco
  \w     | alfanumerico
  \W     | no alfanumerico 
"""
"""import re

texto = "Este curso de Python se publico en el year 2022"


def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )


patrones = [r'\d+', r'\D+', r'\s', r'\S+', r'\w'] 
buscar(patrones, texto) """