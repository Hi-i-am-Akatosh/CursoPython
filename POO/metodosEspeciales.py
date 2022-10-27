"""from ast import AugStore
class Libro:
    def __init__(self, titulo, autor, paginas):
        print("Un libro esta creado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Titulo: %s, autor: %s, paginas: %s"%(self.titulo, self.autor,self.paginas)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Un libro eliminado")

libro = Libro("Libro Python", "David", 200)

#Impresion de los metodos especiales
print(len(libro))
del(libro)"""
class Libro:
    def __init__(self, titulo, autor, paginas):
        print("Un libro esta creado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Titulo: %s, autor: %s, paginas: %s"%(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Un libro eliminado")

libro = Libro("Libro Python", "David", 200)

#Impresion de los metodos especiales
print(len(libro))
del(libro)
