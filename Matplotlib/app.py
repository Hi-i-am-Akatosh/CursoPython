import matplotlib.pyplot as plt 

"""def main():
    x = [1, 2, 3, 4, 5]
    y = [77.77, 34.56, 89.32, 90.21, 29.12]
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()"""


"""def main():
    X = list(range(50))
    Y1 = [1/(x+5) for x in X]
    Y2 = [x**2 for x in X]
    Y3 = [((x-2)/(x+1))**0.5 for x in X]

    plt.subplot2grid((2,2),(0,0), rowspan=1)
    plt.plot(X, Y1)

    plt.subplot2grid((2,2),(0,1), rowspan=1)
    plt.plot(X, Y2)

    plt.subplot2grid((2,2),(1,0), colspan=2)
    plt.plot(X, Y3)

    plt.show()


if __name__ == '__main__':
  main()"""

"""def main():
    X = list(range(10))
    Y1 = [x**0.5 for x in X]
    Y2 = [x for x in X]
    Y3 = [x**1.5 for x in X]
    Y4 = [x**2 for x in X]
    
    plt.suptitle("Ejemplo de funciones simultaneas", fontsize=10)

    plt.subplot2grid((2,2),(0,0), colspan=2)
    plt.title("Dos funciones representadas simultaneamente", fontsize=10)
    plt.plot(X, Y1)
    plt.plot(X, Y2)
    plt.plot(X, Y3)
    plt.plot(X, Y4)

    plt.subplot2grid((2,2),(0,0), colspan=2)
    plt.title("Dos funciones representadas simultaneamente", fontsize=10)
    plt.plot(X, Y1)
    plt.plot(X, Y2)
    plt.show()

if __name__ == '__main__':
    main()"""


"""def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,60]
    plt.xlim(0,11)
    plt.ylim(0,100)
    #plt.title("Grafico de dispercion")
    plt.suptitle("Grafico de dispercion")
    plt.scatter(eje_x,eje_y)
    plt.show()

if __name__ == "__main__":
    main()
"""
"""
def main():
    eje_x = list(range(1, 11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    
    plt.xlim(0 , 100)
    plt.ylim(0,11)
    plt.barh(eje_x, eje_y)
    plt.suptitle("Grafico de barras")
    plt.show()

if __name__ == "__main__":
    main()"""

"""def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    plt.subplot2grid((1,2),(0,1), colspan=1, rowspan=1)
    plt.xlim(0,11)
    plt.ylim(0,100)
    plt.bar(eje_x,eje_y, width=1, color='green', align='center')
    plt.subplot2grid((1,2),(0,1),colspan=1, rowspan=1)
    plt.xlim(0, 100)
    plt.ylim(0,11)
    plt.barh(eje_x, eje_y, height=1, color='red', align='center')
    plt.show()


if __name__ == '__main__':
    main()"""


"""def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    eje_y2 = [45,10,3,7,65,4,32,21,38,6]
    plt.xlim(0,11)
    plt.ylim(0,120)
    plt.bar(eje_x, eje_y, color="green", align="center")
    #plt.bar(eje_x, eje_y2, color="blue", align="center")
    plt.show()


if __name__ == '__main__':
    main()"""


"""def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    plt.subplot2grid((1,2),(0,0), colspan=1, rowspan=1)
    plt.xlim(0,11)
    plt.ylim(0,100)
    plt.bar(eje_x,eje_y, width=1, color='green', align='center')
    plt.subplot2grid((1,2),(0,1),colspan=1, rowspan=1)
    plt.xlim(0, 100)
    plt.ylim(0,11)
    plt.barh(eje_x, eje_y, height=1, color='red', align='center')
    plt.show()


if __name__ == '__main__':
    main()"""


"""def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    eje_y2 = [45,10,3,7,65,4,32,21,38,6]
    plt.xlim(0,11)
    plt.ylim(0,120)
    plt.bar(eje_x, eje_y, color="green", align="center")
    plt.bar(eje_x, eje_y2, color="blue", align="center", bottom=eje_y)
    plt.show()


if __name__ == '__main__':
    main()"""

"""def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    eje_y2 = [45,10,3,7,65,4,32,21,38,6]
    eje_y3 = [80,50,7,10,95,10,22,31,58,12]
    plt.xlim(0,11)
    plt.ylim(0,240)
    plt.bar(eje_x, eje_y, color="green", align="center")
    plt.bar(eje_x, eje_y2, color="blue", align="center", bottom=eje_y)
    #plt.bar(eje_x, eje_y3, color="cyan", align="center", bottom=eje_y2)
    plt.bar(eje_x, eje_y3, color="cyan", align="center", bottom=[eje_y[i] + eje_y2[i] for i in range(len(eje_x))])
    plt.show()

 
if __name__ == '__main__':
    main()
"""

#Barras sobre puesta x2
"""def main():
    eje_y = list(range(10,20))
    eje_x = [23,4,7,77,81,43,45,90,12,68]
    eje_x2 = [45,10,3,67,65,24,32,21,38,56]

    plt.ylim(9,20)
    plt.barh(eje_y, eje_x, color='red', align='center')
    plt.barh(eje_y,[-eje_x2[i] for i in range(len(eje_x2))], color='y', align='center')
    plt.show()

if __name__ == '__main__':
    main()
"""

#Barras sobre puesta x3
"""def main():
    eje_x = list(range(1,11))
    for i in range(len(eje_x)):
        eje_x_2 = [x + 1/3 for x in eje_x ]
    for i in range(len(eje_x)):
        eje_x_3 = [x + 2/3 for x in eje_x]

    eje_y = [23,4,32,77,8,43,45,90,12,68]
    eje_y2 = [45,10,3,7,65,4,32,21,38,6]
    eje_y3 = [11,98,42,71,12,67,4,9,2,52]
    plt.xlim(1-1/6, 11-1/6)
    plt.ylim(0, 100)
    plt.grid(linestyle='--', axis='y')
    plt.bar(eje_x,eje_y, width=1/3, color='green', align='center')
    plt.bar(eje_x_2,eje_y, width=1/3, color='blue', align='center')
    plt.bar(eje_x_3,eje_y, width=1/3, color='y', align='center')
    plt.show()

if __name__ == '__main__':
    main()"""


#Pastel
"""def main():
    datos = [23,12,32,77,38]
    plt.pie(datos)
    plt.show()

if __name__ == '__main__':
    main()"""


#Pastel con datos
"""def main():
    calificaciones = [23,12,32,77,38]
    plt.pie(calificaciones)
    plt.pie(calificaciones, labels=['Ana','Eva','David','Jose','Marta'], shadow=True, labeldistance=0.7)
    plt.show()

if __name__ == '__main__':
    main()"""

#Histograma
"""def main():
    eje_x = list(range(1,13))
    eje_y = [23,4,32,77,48,93,75,90,32,28,21,18]
    plt.xlim(0.5, 12.5)
    plt.ylim(0, 100)
    plt.bar(eje_x, eje_y, color='cyan', align='center', width=1)
    plt.show()

if __name__ == '__main__':
    main()"""

"""def main():
    eje_x = list(range(1,13))
    eje_y = [23,4,32,77,48,93,75,90,32,28,21,18]
    plt.xlim(0.5, 12.5)
    plt.ylim(0, 100)
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto", "Septiembre","Octubre","Noviembre","Diciembre"]
    plt.xticks([x for x in range(1,13)], meses, fontsize=7, rotation=25)
    plt.yticks([10*x for x in range(11)])
    plt.bar(eje_x, eje_y, color='cyan', align='center', width=1)
    plt.show()

if __name__ == '__main__':
    main()"""

#Ejercicios

"""def main():
    plt.figure(figsize=(14,8))
    eje_x = list(range(1,13))
    eje_y = [9,4,10,7,8,9,7,9,3,5,7,0]
    plt.xlim(0.5, 12.5)
    plt.ylim(0, 100)
    meses = ["David", "Tómas", "Mateo", "Alejandro", "Gisell", "Carla", "Javier", "Ariel", "Fernando", "Alegría", "Ruth", "Joaquin"]
    plt.xticks([x for x in range(1,13)], meses, fontsize=7, rotation=25)
    plt.yticks([10*x for x in range(11)])
    plt.bar(eje_x, eje_y, color='green', align='center', width=1)
    plt.show()

if __name__ == '__main__':
    main()"""