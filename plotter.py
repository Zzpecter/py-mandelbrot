"""Plotter module"""
from constants import START_X, START_Y, END_X, END_Y
from PIL import Image, ImageDraw
from mandelbrot import Mandelbrot
from datetime import datetime


class Plotter:
    """
    Class for defining the necessary attributes and methods to plot figures and
    save images.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.my_mandel = Mandelbrot()

    def plot(self):
        """
        method that plots and saves an image with the predefined mandelbrot
        object.

        """
        im = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        draw = ImageDraw.Draw(im)

        for x in range(0, self.width):
            for y in range(0, self.height):

                c = complex(START_X + (x / self.width) * (END_X - START_X),
                            START_Y + (y / self.height) * (END_Y - START_Y))

                iterations = self.my_mandel.perform_calculation(c)
                color = 255 - int(iterations * 255 / self.my_mandel.max_iterations)

                draw.point([x, y], (color, color, color))

        im.save(f'./output/IMG-{datetime.now():%Y%m%d_%H%M%S%z}.png', 'PNG')
