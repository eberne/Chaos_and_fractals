import math

from PIL import Image, ImageDraw

edge_length = 40


def hexagon_generator(offset):
    """Generator for coordinates in a hexagon."""
    x, y = offset
    for angle in range(0, 360, 60):
        y += math.cos(math.radians(angle)) * edge_length
        x += math.sin(math.radians(angle)) * edge_length
        yield x, y


def main():
    image = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(image)
    hexagon = hexagon_generator((30, 100))
    draw.polygon(list(hexagon), outline='black')
    hexagon = hexagon_generator((110, 100))
    draw.polygon(list(hexagon), outline='black')
    hexagon = hexagon_generator((70, 30))
    draw.polygon(list(hexagon), outline='black')
    image.show()


if __name__ == '__main__':
    main()
