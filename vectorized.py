import numpy as np
import time
import math
import matplotlib.pyplot as plt


def mandelbrot(height, width, x=-0.5, y=0.0, zoom=1, max_iterations=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5*height/width
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom

    # Here the actual algorithm starts
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    c = x + 1j * y

    # Initialize z to all zero
    z = np.zeros(c.shape, dtype=np.complex128)
    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)
    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m]

        diverged = np.greater(np.abs(z), 2, out=np.full(c.shape, False), where=m) # Find diverging

        div_time[diverged] = i      # set the value of the diverged iteration number
        m[np.abs(z) > 2] = False    # to remember which have diverged
    return div_time


zoom = 1
file_name = ''
max_iterations = 50
step = 1
print('Processing, this may take a while...')
while step < 100:
    max_iterations = int(max_iterations * math.sqrt(zoom));
    file_name = str(step)
    while len(file_name) < 6:
        file_name = f'0{file_name}'
    plt.imsave(file_name=f'./output/zooms/{file_name}.jpg', arr=mandelbrot(1000, 1000, -0.77568377, 0.13646737, zoom, max_iterations=max_iterations), cmap='magma')
    zoom *= 2
    step += 1
    print(f'step: {step}, zoom level: {zoom}, iter: {max_iterations}')
