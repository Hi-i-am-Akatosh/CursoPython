class Vehiculo():
    def __init__(self, nombre, color):
        self.__nombre = nombre
        self.__color = color
    #self.__ es una clase privada
    def getColor(self):
        return self.__color

    def serColor(self, color):
        self.__color = color

    def getNombre(self):
        return self.__nombre

class Auto(Vehiculo):
    def __init__(self, nombre, color, modelo):
        super().__init__(nombre, color)
        self.__modelo = modelo

    def getDescrpcion(self):
        return self.getNombre() + " - " + self.__modelo + " - " + self.getColor()

carro = Auto("Ford" , "Azul" , "GT350")
print(carro.getDescrpcion())
print(carro.getColor())