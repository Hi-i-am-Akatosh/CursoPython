class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return self.nombre + 'Wooof!'

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
            return self.nombre + 'Miau!'

p = Perro('Perro -> ')
g = Gato('gato -> ')

print('' + p.sonido())
print('' + g.sonido())