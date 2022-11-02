#Crear una maquina de cafe
from menu import Menu
from cafetera import Cafetera
from monedero import Monedero

monedero = Monedero()
cafetera = Cafetera()
menu = Menu()

encendido = True 

while encendido:
  opciones = menu.obtener_items()
  eleccion = input(f"Que le gustaria? ({opciones}): ")
  if eleccion == "off":
    encendido = False
  elif eleccion == "reporte":
    cafetera.reporte()
    monedero.reporte()
  else:
    tomar = menu.encontrar_bebida(eleccion)

    if cafetera.es_recurso_suficiente(tomar) and monedero.hacer_pago(tomar.cost):
      cafetera.hacer_cafe(tomar)