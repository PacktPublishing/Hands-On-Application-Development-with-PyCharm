from matplotlib import pyplot as plt
from matplotlib.pyplot import plot, scatter, arrow, grid, show


def draw(xs, ys):
    limit = max(xs + ys) + 1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    for x, y in zip(xs, ys):
        plot([x, x], [0, y], '-', c='blue', linewidth=3)
        plot([0, x], [y, y], '-', c='blue', linewidth=3)

        scatter(x, y, s=100, marker='o', c='red')

    ax.set_xlim((-limit, limit))
    ax.set_ylim((-limit, limit))

    left, right = ax.get_xlim()
    bottom, top = ax.get_ylim()
    arrow(left, 0, right - left, 0, length_includes_head=True,
          head_width=0.15)
    arrow(0, bottom, 0, top - bottom, length_includes_head=True,
          head_width=0.15)

    grid()
    show()