from turtle import *
"""color('red', 'yellow')
begin_fill()
while True:
  forward(200)
  left(170)
  if abs(pos()) < 1:
    break
end_fill()
done()
"""
"""
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)"""
"""forward(100)
right(45)
forward(-150)
left(50)
forward(200)
setpos(60,30)
setx(80)
sety(150)
heading()"""

# forward(100) distancia
# right(45) #direccion
# forward(-150)
# left(50) #direccion
# forward(200)
# setpos(60,30)
# setx(80) #moviento horizontal
# sety(150) #moviento vertical
# heading()

"""Modo estandar   | Modo logo
0  -  este         | 0  -  norte
90  -  norte       | 90  -  este
180  -  oeste      | 180  -  sur
270  -  sur        | 270  -  oeste
"""
"""setheading(90)
position()
home()"""

#Circulo  -  circle()
#Radius  -  extent  -  steps

"""home()
position()
heading()
circle(50)"""

#===============================

#Dot() # tamnao y un color
"""home()
dot()
fd(50); dot(20, "blue"); fd(50)
position()
dot()
fd(50); dot(20, "red"); fd(50)"""

#===============================

#stamp() => una copia de turtle
"""color("blue")
stamp()
fd(100)"""

#===============================

#undo() => deshace repetidamente
"""for i in range(4):
  fd(50); lt(80)

for i in range(8):
  undo()"""

#===============================

#speed() => la velocidad de la tortuga 

"""speed()
speed('normal')
speed()"""

#===============================

#fillcolor() => permite el formato de cuatro entradas
"""fillcolor("violet")
fillcolor()"""

#color => establecer su color
"""color("red", "green")"""

#===============================

"""import turtle as t 

tim = t.Turtle()

for _ in range(15):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.penup()"""

#===============================

"""import turtle as t 
import random

tim = t.Turtle()

colors = ["cyan","chartreuse","brown","cornflower blue","dark violet"]

def dibujar_forma(num):
  angulo = 360 / num
  for _ in range(num):
    tim.forward(100)
    tim.right(angulo)

for forma in range(3, 11):
  tim.color(random.choice(colors))
  dibujar_forma(forma)"""

#===============================

"""import turtle as t 
import random

tim = t.Turtle()

colors = ["cyan","chartreuse","brown","cornflower blue","dark violet"]

def dibujar_forma(num):
  angulo = 460 / num
  for _ in range(num):
    tim.forward(100)
    tim.right(angulo)

for forma in range(5, 20):
  tim.color(random.choice(colors))
  dibujar_forma(forma)"""

"""import turtle as t 
import random

tim = t.Turtle()
t.colormode(255)


def color_aleatorio():
  r = random.randint(0,255)
  g = random.randint(0, 255)
  b = random.randint(0,255)
  color_aleatorio = (r,g,b)
  return color_aleatorio

direcciones = [0,90,180,270,360]
tim.pensize(20)
tim.speed("slow")


for _ in range(400):
  tim.color(color_aleatorio())
  tim.backward(20)
  tim.setheading(random.choice(direcciones))"""

"""import turtle as t 
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
lista_colores = [(202, 164, 109), (238, 240, 245), 
(150, 75, 49), (223, 201, 135), 
(52, 93, 124), (172, 154, 40), (140, 30, 19), 
(133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), 
(145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), 
(105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), 
(81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), 
(174, 94, 97), (176, 192, 209)]

tim.setheading(255)
tim.forward(30)
tim.setheading(0)
numero_puntos = 100
for puntos in range(1, numero_puntos + 1):
  tim.dot(15, random.choice(lista_colores))
  tim.forward(50)
  tim.left(50)
  
  if puntos % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50)
    tim.heading(0)"""

"""import turtle as t 
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
  r = random.randint(0 , 255)
  g = random.randint(0 , 255)
  b = random.randint(0 , 255)
  color = (r,g,b)
  return color

tim.speed("fastest")

def dibujar_espirografo(size_espacio):
  for _ in range(int(360 / size_espacio)):
    tim.color(random_color())
    tim.forward(100)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    #tim.circle(100)
    tim.setheading(tim.heading() + size_espacio)


dibujar_espirografo(5)

screen = t.Screen()  #Para que no cierre la ejecución
screen.exitonclick() #Para que no cierre la ejecución"""

#import turtle as t 
#import random


#def cuadrado(longitud):
#  for i in range(4):
#    t.forward(longitud)
#    t.right(90)


#def espiral():
#  for i in  range(72):
#    cuadrado(100)
#    t.right(5)

#t.speed(0)
#espiral()


#screen = t.Screen()
#screen.exitonclick()

import turtle as t 
import random


def estrella(longitud):
  for i in range(5):
    t.forward(longitud)
    t.right(180 - 36)

def espiral_estrella():
  for i in range(72):
    estrella(300)
    t.right(5)

t.speed(0)
espiral_estrella()


screen = t.Screen()
screen.exitonclick()