"""def par_impar(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

par_impar(6)
par_impar(6)"""


print("---------")
      
def fib(num):
    a = 0
    b = 1
    cont = 2

    print(f'{a}\n{b}')
    
    while(num > cont):
        t = a + b
        print (t)
        a = b
        b = t
        cont += 1

fib(10)

