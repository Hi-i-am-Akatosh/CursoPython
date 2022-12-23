import matplotlib.pyplot as plt 

"""def main():
    x = [1, 2, 3, 4, 5]
    y = [77.77, 34.56, 89.32, 90.21, 29.12]
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()"""


def main():
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
  main()