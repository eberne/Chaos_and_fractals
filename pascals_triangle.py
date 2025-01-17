""" Draws an equilateral triangle of hexagons of arbitrary size.
    See figures 2.26 and 2.27"""

from math import comb

import numpy as np
from bokeh.plotting import figure, show
from bokeh.util.hex import axial_to_cartesian

number_of_rows: int = 64
divisor: int = 2

q = np.array([])  # set up columns
for i in range(number_of_rows):
    for j in range(-i, 1, 1):
        q = np.append(q, j)

r = np.array([])  # set up rows
for i in range(number_of_rows):
    for j in range(i + 1):
        r = np.append(r, i)

fill_color = np.array([])  # set up hexagon colors
for i in range(number_of_rows):
    for j in range(i + 1):
        value = comb(i, j)
        if value % divisor == 0:
            fill_color = np.append(fill_color, "black")
        else:
            fill_color = np.append(fill_color, "silver")

p = figure(width=600, height=600, toolbar_location=None, match_aspect=True, title="Pascal's Triangle")
p.grid.visible = False
p.axis.visible = False
p.title.align = "center"

p.hex_tile(q, r,
           line_color="white",
           alpha=0.7,
           line_width=4,
           fill_color=fill_color
           )

x, y = axial_to_cartesian(q, r,
                          orientation="pointytop",
                          size=1
                          )

show(p)
