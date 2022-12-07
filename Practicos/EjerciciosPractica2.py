#Ofrecer serie de pares y multiplos de 5
#Este sistema realiza multipos de 5 o pares..
#Pedir limite de la lista.

def Limite(n1):
    while True:
        try:
            if n1 == 1 or n1 == 2:
                n1 = int(input("Ingrese el limite: "))
                return n1
            else:
                print()
            break
        except ValueError:
            print("Error")
            
def Par(n1,n2,list):
    
    if n1 >= 1:
        n1 = n1-1
        list.append(n2)
        n2 = n2 + 2
        Par(n1,n2,list)
        return list
    else:
        return

def Multiplo(n1,n2,list):
    if n1 >= 1:
        n1 = n1-1
        val = 5 * n2
        list.append(val)
        n2 = n2 + 1
        Multiplo(n1,n2,list)
        return list
    else:
        return


print("[1] Pares\n[2] Multiplos de 5")
while True:
    try:
        op = int(input("Ingrese una de las opciones: "))
        num = Limite(op)
        if op == 1:
           pares = []
           paresaux = []
           paresaux = Par(num,2,pares)
           print(paresaux)
        elif op == 2:
           multiplo = []
           multiploaux = []
           multiploaux = Multiplo(num,0,multiplo)
           print(multiploaux)
        else:
           print("Opción no valida.")
        break
    except ValueError:
        print("Ingrese una de las opciones proporcionadas.\n")
#Excepción de limite y op
#Archivos














