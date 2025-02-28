import matplotlib.pyplot as plt
import numpy as np

number_of_rows: int = 3
number_of_hexagons: int = int(number_of_rows * (number_of_rows + 1) / 2)
x_offset: int = 18  # controls the horizontal spacing of the hexagons
y_offset: int = 12  # controls the vertical spacing of the hexagons
x_center: int = 10
y_center: int = 8
q = np.array([0, 0, 1, -1, 1, 1])
r = np.array([0, -1, 0, 0, -1, -2])
marker_color = np.full(6, 'w')
marker_size = np.full(6, 1000)
x = np.sqrt(3) * (q + r / 2.0)
y = -3 / 2.0 * r
ax = plt.gca()  # gca = get current axes
# ax.set_xlim([-x_offset + x_center, x.max() + (1 / 2) + x_center])
ax.set_xlim(-10.1, 10.1)
# ax.set_ylim([-y_offset + y_center, y.max() + (1 / 2) + y_center])
ax.set_ylim(-7.75, 7.75)
plt.scatter(x, y, marker_size, marker_color, edgecolor='k', marker='h')
plt.show()
print(x,y)
# TODO figure out the relationship between offset and marker size
# TODO move the picture to the center of the screen
# TODO make q and r dependent on the number of rows
# TODO make the marker color dependent on divisor
