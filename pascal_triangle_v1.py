"""
Duplicates the images on pages 84 and 85 of "Chaos and Fractals" by Peitgan, etal
"""

from math import sin, cos, radians
from typing import Generator
from PIL import Image, ImageDraw

def hexagon_generator(edge_length:int, location) -> Generator:
    """Generator for coordinates of a hexagon."""
    x, y = location
    for angle in range(0, 360, 60):
        y += cos(radians(angle)) * edge_length
        x += sin(radians(angle)) * edge_length
        yield x, y


def main():
    canvas = (800, 600)
    image = Image.new('RGB', canvas, 'white')
    draw = ImageDraw.Draw(image)
    hexagon = hexagon_generator(40, location=(400, 20))
    draw.polygon(list(hexagon), outline='black')
    hexagon = hexagon_generator(40, location=(400, 400))
    draw.polygon(list(hexagon), outline='black', fill='black')
    image.show()


if __name__ == "__main__":
    main()
