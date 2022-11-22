#FUNCIONES LAMBDA
#funciones anonimas
"""

#Funcion tradicional
def doblar(num):
  return num **2
print(doblar(4))

#mas simplificada
def doblar(num): return num**2
print(doblar(2))

#notacion lambda
doblar = lambda num: num**2
print(doblar(5))"""

#sintaxis
#lambda args: expresion
"""
impar = lambda num: num % 2 != 0
print(impar(5))"""

"""sumar = lambda num, num2 : num + num2
print(sumar(4,4))"""
#slicing ['h','o','l','a']  
#labda   ['aloH']   

"""revertir = lambda cadena: cadena[::-1]
print("Palabra original: David")
print("Palabra invertida: ", revertir("David"))

===========
suma = (lambda *args: sum(args))(1, 2, 3, 4, 9)
print(suma)

====================
#suma kwargs y uso labda 
suma = (lambda **kwargs : sum(kwargs.values()))(a=1, b=2, c=3, d=5, g=9)
print(suma)"""
