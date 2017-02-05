from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy

def eulers(f, x0, y0, x1, n):
    deltax = (x1 - x0) / (n - 1)
    x = np.linspace(x0, x1 ,n)
    y = np.zeros([n])
    y[0] = y0
    for i in range(1, n):
        y[i] = deltax * f(x[i], y[i - 1]) + y[i - 1]
        return x, y

a = 0.9
k = 7
m = 2
f = lambda x, y: (1 - y ** 2) / ((1 + m) * (x ** 2) + y ** 2 + 1)
x, y = eulers(f, 0, 0, 1, 50)
vx, vy = rk4(f, 0, 0, 1, 50)
plt.plot(vx, vy, 'o')
plt.plot(x, y, 'o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Approximate Solution with Runge Kutta's and Euler's Methods")
plt.show()
