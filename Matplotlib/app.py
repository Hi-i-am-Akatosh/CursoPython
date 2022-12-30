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


def main():
    eje_x = list(range(1,11))
    eje_y = [23,4,32,77,8,43,45,90,12,68]
    eje_y2 = [45,10,3,7,65,4,32,21,38,6]
    plt.xlim(0,11)
    plt.ylim(0,120)
    plt.bar(eje_x, eje_y, color="green", align="center")
    plt.bar(eje_x, eje_y2, color="blue", align="center", bottom=eje_y)
    plt.show()


if __name__ == '__main__':
    main()