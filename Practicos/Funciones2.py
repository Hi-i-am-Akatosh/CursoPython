def tablas(num):
    result = []
    for i in range(10):
        result.append(num * (i+1))
    return result
v = 3
res = tablas(v)
print(res,'\n')

cont = 1
for k in res:
    print(f'{v} x {cont} = {k}')
    cont += 1
