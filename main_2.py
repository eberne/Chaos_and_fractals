import matplotlib.pyplot as plt
import numpy as np

x_padding = 18
y_padding = 12
q = np.array([0, 0, 1, -1, 1, 1])
r = np.array([0, -1, 0, 0, -1, -2])
size = np.full(6, 1)
marker_color = np.full(6, 'k')
marker_size = np.full(6, 1000)
edge_color = np.full(6, 'k')
x = size * np.sqrt(3) * (q + r / 2.0)
y = -size * 3 / 2.0 * r
ax = plt.gca()  # get current axes
ax.set_xlim([-x_padding + 10, 10 + x.max() + size[0] / 2])
ax.set_ylim([-y_padding + 8, 8 + y.max() + size[0] / 2])

plt.scatter(x, y, marker_size, marker_color, marker='h')
plt.show()
