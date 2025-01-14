import numpy as np
from bokeh.plotting import figure, show
from bokeh.util.hex import axial_to_cartesian

max_row = 32

q = np.array([])
for i in range(max_row):
    for j in range(-i, 1, 1):
        q = np.append(q, j)

r = np.array([])
for i in range(max_row):
    for j in range(i + 1):
        r = np.append(r, i)

p = figure(width=600, height=600, toolbar_location=None, match_aspect=True)
p.grid.visible = False
p.axis.visible = False

p.hex_tile(q, r,
           line_color="white",
           alpha=0.7,
           line_width=4)

x, y = axial_to_cartesian(q, r,
                          orientation="pointytop",
                          size=1)

show(p)
