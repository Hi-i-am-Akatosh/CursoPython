# Menú de operacion: suma, resta, multiplicación, división y potencia.
def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def potencia(n1, n2):
    return n1 ** n2


while True:
    try:
        a = int(input("Ingrese su primer valor: ")) #Excepciones
        break
    except ValueError:
        print("Ingrese un número.") #Excepciones x2
while True:    
    try:
        b = int(input("Ingrese su segundo valor: "))
        break
    except ValueError:
        print("Ingrese un número.")

print("[1] Suma\n[2] Resta\n[3] Multiplicación\n[4] División\n[5] Potencia\n")
op = int(input("Ingrese la opción que necesita: "))

if (op == 1):
    print("El resultado de de la operación es: ",suma(a,b))
elif (op == 2):
    print("El resultado de de la operación es: ",resta(a,b))
elif (op == 3):
    print("El resultado de de la operación es: ",mult(a,b))
elif (op == 4):
    if b == 0:
        print("\nNo se puede dividir para cero\n")
    else:
        print("El resultado de de la operación es: ",div(a,b))
elif (op == 5):
    print("El resultado de de la operación es: ",potencia(a,b))
else:
    print("Operación no definida, ingrese un valor acorde al menú.")




