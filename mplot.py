import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def hexagon(x_center, y_center):
    angle = np.linspace(0, 2 * np.pi, 7)
    x_hex = x_center + size * np.cos(angle)
    y_hex = y_center + size * np.sin(angle)
    return x_hex, y_hex


size = 1
"""Generate the vertices of a hexagon centered at (x_center, y_center) with a given size."""

x_centers = np.arange(0, 10, 2 * size)
y_centers = np.arange(0, 10, np.sqrt(3) * size)

fig, ax = plt.subplots()
for x in x_centers:
    for y in y_centers:
        hex_x, hex_y = hexagon(x, y)
        hexagon_patch = patches.Polygon(np.column_stack([hex_x, hex_y]), closed=True, edgecolor='black')
        ax.add_patch(hexagon_patch)

ax.set_aspect('equal')
plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.show()
