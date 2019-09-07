from math import sqrt
from matplotlib import pyplot as plt


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def distance(self, p):
        diff = self - p
        distance = sqrt(diff.x**2 + diff.y**2)
        return distance

    @staticmethod
    def draw(x, y):
        # set up range of the plot
        limit = max(x, y) + 1

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect('equal')

        # lines corresponding to x- and y-coordinates
        plt.plot([x, x], [0, y], '-', c='blue', linewidth=3)
        plt.plot([0, x], [y, y], '-', c='blue', linewidth=3)

        plt.scatter(x, y, s=100, marker='o', c='red')  # actual point

        ax.set_xlim((-limit, limit))
        ax.set_ylim((-limit, limit))

        # axis arrows
        left, right = ax.get_xlim()
        bottom, top = ax.get_ylim()
        plt.arrow(left, 0, right - left, 0, length_includes_head=True,
                  head_width=0.15)
        plt.arrow(0, bottom, 0, top - bottom, length_includes_head=True,
                  head_width=0.15)

        plt.grid()
        plt.show()


if __name__ == '__main__':
    p1 = Point(1, 0)
    p2 = Point(5, 3)

    Point.draw(p2.x, p2.y)
