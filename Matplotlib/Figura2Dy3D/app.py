import matplotlib.pyplot as plt 
import random

"""def main():
    X = list(range(50))
    Y1 = [1/(x+5) for x in X]
    Y2 = [x**2 for x in X]

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot(X, Y1)
    ax2 = fig.add_subplot(122)
    C2 = ax2.plot(X, Y2)
    C2[0].set_color("green")
    plt.show()

if __name__ == '__main__':
    main()"""



"""def main():
    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['font.size'] = '10'
    X = list(range(1,11))
    Y1 = [x**0.5 for x in X]
    Y2 = [x**1.5 for x in X]
    fig = plt.figure(figsize=(12,5), frameon= False, facecolor="yellow")
    #fig.canvas.set_window_title("Ventana con dos tipos de graficos distintos")
    fig.suptitle("Titulo superior", fontsize= 15, color='red')
    ax1 = fig.add_subplot(121)
    ax1.set_xlim(0.5,10.5)
    ax1.set_ylim(0, max(Y1) * 1.05)
    ax1.grid(True, axis="y", ls = "-", color='0.3')
    ax1.set_xticks([i for i in range(1, 11)])
    ax1.set_xlabel("Eje x primer grafico", color="magenta")
    ax1.set_ylabel("Eje y primer grafico", color="magenta")
    ax1.set_title("Primer grafico", color="blue")
    ax1.bar(X,Y1, width= 1, color ="green", align="center")
    ax2 = fig.add_subplot(122)
    ax2.set_xlim(0.5,10.5)
    ax2.set_ylim(0, max(Y2) * 1.05)
    ax2.grid(True, axis="x", ls="-", color='0.3')
    ax2.set_xticks([i for i in range(1, 11)])
    ax2.set_xticklabels(['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez',], fontsize=9, color="b")
    ax2.set_xlabel("Eje x segundo grafico", color="r")
    ax2.set_ylabel("Eje y segundo grafico", color="r")
    ax2.set_title("Segundo grafico", color="green")
    ax2.scatter(X, Y2)
    plt.show()

if __name__ == '__main__':
    main()"""

#Grafica de interseccion

"""def main():
    X = list(range(50))
    Y1 = [1/(x+5) for x in X]
    Y2 = [x**2 for x in X]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(X, Y1, color="magenta")
    ax1.set_xlabel("Eje x")
    ax1.set_ylabel("Curva magenta")
    ax2 = ax1.twinx()
    c2, = ax2.plot(X,Y2)
    c2.set_color("green")
    ax2.set_ylabel("Curva verde")
    plt.show()

if __name__ == '__main__':
    main()"""

#Grafica parabolica

"""def main():
    X = list(range(50))
    Y1 = [1/(x+5) for x in X]
    Y2 = [x**2 for x in X]

    plt.rcParams['toolbar'] = 'None'
    fig = plt.figure(frameon=True, facecolor='1')

    ax1 = fig.add_subplot(121)
    ax1.tick_params(width=0)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_title("primer funcion", loc="left", color="b")
    ax1.plot(X, Y1)

    ax2 = fig.add_subplot(122)
    ax2.tick_params(width = 0)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_title("Segunda funcion", loc="right", color="g")
    ax2.grid(True, axis="both", ls="-", color='0.3')

    c2, = ax2.plot(X, Y2)
    c2.set_color("green")
    propiedades = dict(arrowstyle='->', linewidth=2, connectionstyle='angle3', color=(0.5,0.5,0.5))
    ax1.annotate('y - 1/(x+5)', xytext=(25,0.10), xy=(15,0.05), ha='left', va='top', arrowprops=propiedades)

    propiedades = dict(arrowstyle='<->', linewidth=2, connectionstyle='angle', color="blue")
    ax2.annotate('y = x**2', xytext=(20, 1200), xy=(30,890), ha='right', va='bottom', color="blue", arrowprops=propiedades)


    plt.show()

if __name__ == '__main__':
    main()"""

#Grafico pastel

def main():
    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['font.size'] = '10'

    X = list(range(10))
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    for y in range(10):
        Y1.append(10)
        Y2.append(random.randint(1, 50))
        Y3.append(random.randint(1, 50))
        Y4.append(random.randint(1, 50))

    nombres = ['Ajos','Patatas','Lechuga','Fresas','Puerros','Tomates','Pimientos','Coles','Perejil','Rabano']
    colores = ['b','g','r','0.65','c','m','0.85','y','w',(0.7,0.1,0.3)]
    fig = plt.figure(figsize=(12,10), frameon=False)
    fig.suptitle("Numero de productos pedidos", fontsize=15, color="blue")

    ax1 = fig.add_subplot(221)
    ax1.set_title("Colores por producto", color='b')
    ax1.pie(Y1, autopct='%d', labels=nombres, shadow=True, colors=colores,explode=[0.1]*10)

    ax2 = fig.add_subplot(222)
    ax2.set_title("Cliente David", color='r')
    ax2.pie(Y2, autopct='%d', labels=nombres, shadow=True, colors=colores,explode=[0.1]*10)

    ax3 = fig.add_subplot(223)
    ax3.set_title("Cliente Jose", color='b')
    ax3.pie(Y3, autopct='%d', labels=nombres, shadow=True, colors=colores,explode=[0.1]*10)

    ax4 = fig.add_subplot(224)
    ax4.set_title("Cliente Maria", color='m')
    ax4.pie(Y4, autopct='%d', labels=nombres, shadow=True, colors=colores,explode=[0.1]*10)
    plt.show()

if __name__ == '__main__':
    main()







