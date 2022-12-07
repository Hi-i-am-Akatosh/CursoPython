##Menú con submenu..
##Operaciones basicas: Suma resta mult, y division Pedir a y b
##Y factura: Valor unitario, cantidad y total
## Funcion dentro de funcion

def Operadores():
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    return a , b

def Operacion(n1,n2,f):
    return f (n1, n2)

def Suma(n1,n2):
    return n1 + n2

def Resta(n1,n2):
    return n1 - n2

def Multiplicacion(n1,n2):
    return n1 * n2

def Division(n1,n2):
    return n1 / n2

def Control(a):
    while True:
        if (a > 0):
            return
        else:
            print("El valor deber ser mayor a cero")
            break
def Iva(x):
    vt = x * 0.12
    return vt

print("[1] Operaciones básicas\n[2] Facturación")
op1 = int(input("Elija la operación que necesita: "))
if (op1 == 1):
          print("[1] Suma\n[2] Resta\n[3] Multiplicación\n[4] División: ")
          op = int(input("Ingrese la operación que necesita: "))
          if (op == 1):
              n1 , n2 = Operadores()
              result = Operacion(n1 , n2 , Suma)
              print("El resultado es:",result)
          if (op == 2):
              n1 , n2 = Operadores()
              result = Operacion(n1 , n2 , Resta)
              print("El resultado es:",result)
          if (op == 3):
              n1 , n2 = Operadores()
              result = Operacion(n1 , n2 , Multiplicacion)
              print("El resultado es:",result)
          if (op == 4):
             n1 , n2 = Operadores()
             if (n2 > 0):
                 result = Operacion(n1 , n2 , Division)
                 print("El resultado es:",result)
             else:
                 print("No es posible dividir para cero")
elif (op1 == 2):
    d = float(input("Ingrese la cantidad de producto: "))
    Control(d)
    e = float(input("Ingrese el precio unitario: "))
    Control(e)    
    subtotal = Operacion(d , e , Multiplicacion)
    iva = Iva(subtotal)
    total = Operacion(subtotal , iva , Suma)
    print("El valor total de la factura es:",total)
else:
    print("Opción no valida")
