from mimetypes import init


class Estudiante():
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre


class Institucion():
    def presentarInstituto(self):
        print("Estudio en el Instituto de Informatica")

class Informatica(Estudiante, Institucion):
    def presentarse(self):
        print(f"Soy {self.nombre} tengo {self.edad} años y estudio Informatica")

Estudiante = Informatica(29, 'Jose Diaz')
print(Estudiante.presentarse())
print(Estudiante.presentarInstituto())