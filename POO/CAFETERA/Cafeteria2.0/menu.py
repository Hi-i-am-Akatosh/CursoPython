class MenuItem:
  def __init__(self, nombre, agua, leche, cafe, cost):
    self.nombre = nombre
    self.cost = cost
    self.ingredientes = {
      "agua": agua,
      "leche": leche,
      "cafe": cafe
    }

class Menu:
  """ Molde del menu con bebidas """
  def __init__(self):
    self.menu = [
      MenuItem(nombre="latte", agua=200, leche=150, cafe=24, cost=2.5),
      MenuItem(nombre="expreso", agua=50, leche=0, cafe=18, cost=1.5),
      MenuItem(nombre="cappuccino", agua=250, leche=50, cafe=24, cost=3),
    ]

  def obtener_items(self):
    "Mostrar los nombres de productos disponibles"
    opciones = ""
    for item in self.menu:
      opciones += f"{item.nombre}/"
    return opciones

  def encontrar_bebida(self, nombre_pedido):
    """Buscar alguna bebida en particular"""
    for item in self.menu:
      if item.nombre == nombre_pedido:
        return item 
    print("Lo sentimos, ese producto no esta disponible")