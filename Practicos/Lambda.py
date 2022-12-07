def operar (n1,n2,f):
    return f (n1,n2)
def suma(n1,n2):
    return n1 + n2
def resta(n1, n2):
    return n1 - n2

suma = lambda n1, n2: n1+ n2
resta = lambda n1, n2: n1 - n2
operar = lambda n1, n2, f: f(n1,n2)


result = operar(5,4,)
print("El resultado es: ",result)
