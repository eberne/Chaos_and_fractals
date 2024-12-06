import numpy as np
import matplotlib.pyplot as plt


def hexagon(center):
    """Generate the vertices of a hexagon centered at `center` with a given `size`."""
    angle = np.linspace(0, 2 * np.pi, 7) + np.pi / 6
    x_hex = center[0] + size * np.cos(angle)
    y_hex = center[1] + size * np.sin(angle)
    # y_hex = center[1] + np.sqrt(3) * size
    return x_hex, y_hex


def plot_hexagon(ax, center):
    """Plot a single hexagon."""
    x_hex, y_hex = hexagon(center)
    ax.fill(x_hex, y_hex, edgecolor='black', fill=False)


def triangle_of_hexagons(rows: int) -> None:
    """Plot a triangle of hexagons."""
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    for row in range(rows):
        for col in range(row + 1):
            if row % 2 == 0:
                x_offset = (row - col) * size * 2
            else:
                x_offset = (row - col) * size + 1
            y_offset = col * np.sqrt(3) * size
            plot_hexagon(ax, (x_offset, -y_offset))
    plt.show()


if __name__ == '__main__':
    size = .8
    number_of_rows = 1
    triangle_of_hexagons(number_of_rows)
