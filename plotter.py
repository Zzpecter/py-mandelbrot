"""Plotter module"""
from collections import defaultdict

from constants import START_X, START_Y, END_X, END_Y
from PIL import Image, ImageDraw
from mandelbrot import Mandelbrot
from datetime import datetime
from math import floor, ceil


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

        histogram = defaultdict(lambda: 0)
        values = {}

        for x in range(0, self.width):
            for y in range(0, self.height):

                c = complex(START_X + (x / self.width) * (END_X - START_X),
                            START_Y + (y / self.height) * (END_Y - START_Y))

                iterations = self.my_mandel.perform_calculation(c)
                values[(x, y)] = iterations
                if iterations < self.my_mandel.max_iterations:
                    histogram[floor(iterations)] += 1

        total = sum(histogram.values())
        hues = []
        h = 0
        for i in range(self.my_mandel.max_iterations):
            h += histogram[i] / total
            hues.append(h)
        hues.append(h)

        im = Image.new('HSV', (self.width, self.height), (0, 0, 0))
        draw = ImageDraw.Draw(im)

        for x in range(0, self.width):
            for y in range(0, self.height):
                m = values[(x, y)]

                hue = 255 - int(255 * self.linear_interpolation(hues[floor(m)], hues[ceil(m)], m % 1))
                saturation = 255
                value = 255 if m < self.my_mandel.max_iterations else 0

                draw.point([x, y], (hue, saturation, value))

        im.convert('RGB').save(f'./output/IMG-{datetime.now():%Y%m%d_%H%M%S%z}.png', 'PNG')

    @staticmethod
    def linear_interpolation(color1, color2, t):
        return color1 * (1 - t) + color2 * t


    def plot_with_GPU():