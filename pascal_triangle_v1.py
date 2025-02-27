"""
Duplicates the images on pages 84 and 85 of "Chaos and Fractals" by Peitgan, etal
"""

from math import sin, cos, radians
from typing import Generator
from bokeh.plotting import figure, show
from PIL import Image, ImageDraw


def hexagon_generator(edge_length: int, location) -> Generator:
    """Generator for coordinates of a hexagon."""
    x, y = location
    for angle in range(0, 360, 60):
        y += cos(radians(angle)) * edge_length
        x += sin(radians(angle)) * edge_length
        yield x, y


def main():
    canvas = (800, 600)
    image = Image.new('L', canvas, 'white')
    image.draft("L",(100,100))
    print(f"Format = {image.format}  Size = {image.size}  Mode = {image.mode}")
    image.save('pascal_triangle_v1.png')
    draw = ImageDraw.Draw(image)
    hexagon = hexagon_generator(40, location=(400, 20))
    draw.polygon(list(hexagon), outline='black')
    hexagon = hexagon_generator(40, location=(400, 400))
    draw.polygon(list(hexagon), outline='black', fill='black')
    # this doesn't work because it prints the hexagon as an picture. Need to use bokeh or equal
    # image.show(title="Pascal Triangle")
    fig = figure(width=canvas[0],
                 height=canvas[1],
                 toolbar_location=None,
                 title = "Pascal Triangle"
                )
    fig.title.align = "center"
    fig.scatter([2,2], [3,3], marker='hex', size= 80)
    show(fig)

if __name__ == "__main__":
    main()
