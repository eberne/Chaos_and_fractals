import matplotlib.pyplot as plt

import mplot_1


def plot_hexagon(center):
    """Plot a single hexagon."""
    x_hex, y_hex = mplot_1.hexagon(center)
    # ax.fill(x_hex, y_hex, edgecolor='black', fill=False)


def set_up_hexagon():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')


if __name__ == '__main__':
    size = .8
    # number_of_rows = 6
    # triangle_of_hexagons(number_of_rows)
    set_up_hexagon()
    center = (0, 0)
    plot_hexagon(center)

    plt.show()
