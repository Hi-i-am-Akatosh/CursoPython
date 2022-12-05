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

import turtle as t 
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
  dibujar_forma(forma)