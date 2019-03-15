import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = [i for i in range(9)]
    y = [i**2 for i in range(9)]

    plt.plot(x, y)
    plt.show()
