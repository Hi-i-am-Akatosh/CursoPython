def cuenta_atras(num):
    aux = num
    if num > 0:
        print(num)
        num -= 1
        cuenta_atras(num)
    else:
        print("Cuenta regresica terminada!\n\n")

print("\n\tCuenta Regresiva")
cuenta_atras(20)
