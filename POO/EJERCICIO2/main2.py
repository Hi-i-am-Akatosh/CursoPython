class Animal():
    def __init__(self):
        print("Animal Creado")
    
    def quienSoy(self):
        print("Animal")

    def comer(self):
        print("Comiendo")

class Perro(Animal):
    def __init__(self):
        Animal.__init__()
        print("Perro Creado")

    def ladrar(self):
        print("Wooof")

dingo = Perro()
print(dingo)

animal = Animal()

perro = dingo.quienSoy()
print(perro);

animal2 = animal.quienSoy()
print(animal2)