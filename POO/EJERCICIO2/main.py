class Linea():
    #Constructor
    def __init__(self, coor1, coor2):
        #Inicializar atributos
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distancia(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def pendiente(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordenada1 = (3, 2)
coordenada2 = (8 , 10)

#Crear un objeto
obj_linea = Linea(coordenada1,coordenada2)
distancia = obj_linea.distancia()
pendiente = obj_linea.pendiente()
print("\n\t-----Linea-----\n")
print ("La distancia es: ",distancia)
print("\n")
print("La pendiente es: ",pendiente)
print("\n\t-----Final-----\n")




