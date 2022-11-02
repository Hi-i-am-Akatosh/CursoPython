class Monedero:

  DIVISA = "$"

  VALORES_MONEDAS = {
    "cuarto":0.25,
    "diez":0.10,
    "cinco": 0.05,
    "centavo": 0.01
  }

  def __init__(self):
    self.ganancia = 0
    self.dinero_recibido = 0

  def reporte(self):
    """Imprimir el producto actual"""
    print(f"Dinero: {self.DIVISA}{self.ganancia}")

  def procesar_monedas(self):
    """Devulve el total calculado al ingresar las monedas"""
    print("Por favor inserta moneda.")
    for moneda in self.VALORES_MONEDAS:
      self.dinero_recibido += int(input(f"Cuanto {moneda}?:")) * self.VALORES_MONEDAS[moneda]
    return self.dinero_recibido

  def hacer_pago(self, cost):
    """Devuelve True cuando se acepta el pago, o False si es suficiente"""
    self.procesar_monedas()
    if self.dinero_recibido >= cost:
      cambio = round(self.dinero_recibido - cost, 2)
      print(f"Aqui es {self.DIVISA}{cambio} en cambio.")
      self.ganancia += cost
      self.dinero_recibido = 0
      return True
    else:
      print("Lo siento, no es suficiente dinero. Dinero devuelto")
      self.dinero_recibido = 0
      return False