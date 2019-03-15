from math import sqrt

from point_util import draw


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance(self, other):
        diff = self - other
        distance = sqrt(diff.x**2 + diff.y**2)
        return distance


if __name__ == '__main__':
    p1 = Point(1, 0)
    p2 = Point(5, 3)
    print(f'Distance between {p1} and {p2} is {p1.distance(p2)}')

    draw([p1.x, p2.x], [p1.y, p2.y])
