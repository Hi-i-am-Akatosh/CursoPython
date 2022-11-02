class Cafetera:
  def __init__(self):
    #diccionario
    self.recursos = {
      "agua":300,
      "leche": 200,
      "cafe": 100
    }

  def reporte(self):
    """Imprimir un reporte de todos los recursos"""
    print(f"Agua: {self.recursos['agua']}ml")
    print(f"Leche: {self.recursos['leche']}ml")
    print(f"Cafe: {self.recursos['cafe']}g")

  def es_recurso_suficiente(self, tomar):
    """Devolver True cuando se puede hacer un pedido
    False si los ingredientes son suficientes """
    poder_hacer = True
    for item in tomar.ingredientes:
      if(tomar.ingredientes[item] > self.recursos[item]):
        print(f"Lo siento, no hay sufiente {item}.")
        poder_hacer = False
      return poder_hacer


  def hacer_cafe(self, orden):
    """Solicitar los ingredientes necesarios de los recursos"""
    for item in orden.ingredientes:
      self.recursos[item] -= orden.ingredientes[item]
    print(f"Aqui esta tu {orden.nombre} . Difurta!")