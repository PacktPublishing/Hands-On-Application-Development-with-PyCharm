from math import sqrt


def tuple_distance(tuple1, tuple2):
    return sqrt((tuple1[0]-tuple2[0])**2 +(tuple1[1]-tuple2[1])**2)


if __name__ == '__main__':
    x = (1, 0)
    y = (5, 3)
    print(f'Distance between {x} and {y} is {tuple_distance(x, y)}')
