#Clase productos metodo(Precio de venta; oferta de stock[2x1]; descripcion) : Nombre prod. Precio de distribuidor
#3 productos. (heredado por nombre prod.)

class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
        
    
    def Precio(self):
        pass
    
    def Oferta(self):
        pass

    def Descripcion(self):
        print("El producto ", type(self).__name__," estará disponible en nuestra tienda durante todo el año.")

class Gaseosas(Producto):
    def Precio(self):
        print("$3")

    def Oferta(self):
        print("$2.5")

class Frituras(Producto):
    def Precio(self):
        print("$1")
        
    def Oferta(self):
        print("$0.75")

class Dulces(Producto):
    def Precio(self):
        print("$0.35")
        
    def Oferta(self):
        print("$0.15")

obj_cocacola = Gaseosas('Coca Cola', 2)
obj_doritos = Frituras('Doritos', 0.5)
obj_jet = Dulces('Jet', 0.10)

print("\nProducto Coca Cola")
print('\nNombre del producto: ', obj_cocacola.nombre)
print('Precio de distribuidor: ', obj_cocacola.precio)
print("Precio de venta:")
obj_cocacola.Precio()
print("El precio de oferta es:")
obj_cocacola.Oferta()

print("\nProducto Doritos")
print('\nNombre del producto: ', obj_doritos.nombre)
print('Precio de distribuidor: ', obj_doritos.precio)
print("Precio de venta:")
obj_doritos.Precio()
print("El precio de oferta es:")
obj_doritos.Oferta()

print("\nProducto Jet")
print('\nNombre del producto: ', obj_jet.nombre)
print('Precio de distribuidor: ', obj_jet.precio)
print("Precio de venta:")
obj_jet.Precio()
print("El precio de oferta es:")
obj_jet.Oferta()