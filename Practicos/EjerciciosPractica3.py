# Archivo vacio.
# Crear archivo y agregar texto.
# Archivo existente y sobreescribir texto.
# Agregar datos a un archivo existente.

from io import open
def vacio(nombre):
    archivo = open(nombre +".txt", "w")
    archivo.close()


def ingresar(nombre, texto):
    archivo = open(nombre +".txt", "w")
    frase = texto
    archivo.write(frase)
    archivo.close()

def leer(nombre):
    archivo = open(nombre +".txt", "r")
    frase = archivo.read()
    archivo.close()
    return frase

def agregar(nombre, texto):
    archivo = open(nombre +".txt", "a")
    frase = texto
    archivo.write("\n"+frase)
    archivo.close()


print("Opciones\n[1] Crear archivo\n[2] Crear archivo con registros\n[3] Leer archivo\n[4] Agregar registros a archivo existente\n")

while True:
    try:
        op = int(input("Ingrese una de las opciones: "))
        if op == 1:
            while True:
                t = str(input("Ingrese el nombre del archivo: "))
                archivo = len(t)
                if archivo >= 1:
                    vacio(t)
                    break
                else:
                    print("Ingrese un nombre al archivo: ")
        elif op == 2:
            while True:
                t = str(input("Ingrese el nombre del archivo: "))
                archivo = len(t)
                if archivo >= 1:
                    texto = str(input("Ingrese el registro: "))
                    ingresar(t,texto)
                    break
                else:
                    print("Ingrese un nombre al archivo: ")
        elif op == 3:
            while True:
                t = str(input("Ingrese el nombre del archivo: "))
                archivo = len(t)
                if archivo >= 1:
                    f = leer(t)
                    print (f)
                    break
                else:
                    print("Ingrese un nombre al archivo: ")
        elif op == 4:
            while True:
                t = str(input("Ingrese el nombre del archivo: "))
                archivo = len(t)
                if archivo >= 1:
                    texto = str(input("Ingrese el registro: "))
                    agregar(t,texto)
                    break
                else:
                    print("Ingrese un nombre al archivo: ")
        break
    except ValueError:
        print("Ingrese una de las opciones proporcionadas.\n")



