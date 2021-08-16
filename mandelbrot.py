"""Mandelbrot module"""
class Mandelbrot:
    """
    Class for performing the necessary calculations  and variables to generate
    a mandelbrot set.
    """
    def __init__(self, max_iterations=200, threshold_value=2):
        self.max_iterations = max_iterations
        self.threshold_value = threshold_value

    def perform_calculation(self, complex_num):
        """
        iteratively calculates 'z=z^2 + c' until it either surpasses
        the max_iterations value (bounded result) or the result becomes bigger
        than two (unbounded result), where c is the parameter
        'complex_num' .

        :param
            complex_num: (complex) the complex number to run the calculation.
        :return:
            count: (int) the number of iterations performed.
        """
        result, count = 0, 0
        while abs(result) <= self.threshold_value and count < self.max_iterations:
            result = result**2 + complex_num
            count += 1
        return count
