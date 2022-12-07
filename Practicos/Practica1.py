nombre = input("Ingrese por favor su nombre: ")

n = 0
a = float(input(nombre+ " ingrese su nota de Matemáticas: "))
b = float(input(nombre+ " ingrese su nota de Física: "))
c = float(input(nombre+ " ingrese su nota de Quimica: "))
d = float(input(nombre+ " ingrese su nota de Lenguaje: "))
e = float(input(nombre+ " ingrese su nota de Ingles: "))

n = ((a + b + c + d + e)/5)
if n >= 8:
    print("Felicidades, usted aprobo con un promedio de: ", n)
else:
    print("Usted reprobó con un promedio de: ", n)
    
print("Fin del programa")
    
