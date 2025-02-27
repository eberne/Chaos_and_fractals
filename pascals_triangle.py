""" Draws an equilateral triangle of hexagons of arbitrary size.
    See figures 2.26 and 2.27 using bokeh"""

from math import comb

import numpy as np
import pyinputplus as pyip
from bokeh.plotting import figure, show
from bokeh.util.hex import axial_to_cartesian

number_of_rows = pyip.inputInt(prompt="How many rows? ", max=65, min=3)
divisor = pyip.inputInt(prompt="What divisor do you want to show? ", min=1, max=15)
background_color = pyip.inputChoice(["Black", "Silver"],
                                    prompt="Do you want the background color to be Silver or Black ? ")
if background_color == "Black":
    fill_color = "Silver"
else:
    fill_color = "Black"

# number_of_rows: int = 64
# divisor: int = 2

q = np.array([])  # set up columns
for i in range(number_of_rows):
    for j in range(-i, 1, 1):
        q = np.append(q, j)

r = np.array([])  # set up rows
for i in range(number_of_rows):
    for j in range(i + 1):
        r = np.append(r, i)

print_color = np.array([])  # set up hexagon colors
for i in range(number_of_rows):
    for j in range(i + 1):
        if comb(i, j) % divisor == 0:
            print_color = np.append(print_color, fill_color)
        else:
            print_color = np.append(print_color, background_color)

p = figure(width=600, height=600, toolbar_location=None, match_aspect=True, title="Pascal's Triangle")
p.grid.visible = False
p.axis.visible = False
p.title.align = "center"

p.hex_tile(q, r,
           line_color="white",
           alpha=0.7,
           line_width=4,
           fill_color=print_color
           )

x, y = axial_to_cartesian(q, r,
                          orientation="pointytop",
                          size=1
                          )

show(p)
