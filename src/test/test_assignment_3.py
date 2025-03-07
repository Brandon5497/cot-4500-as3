import numpy as np

iterations = 10
a = 0.0
b = 2.0
initial = 1
prev = initial
y = 0

step_size = (b-a) / iterations

for i in np.arange(a, b, step_size):
    y = i - prev ** 2
    prev = prev + step_size * y

print(f"Euler Method: {prev}")

k1 = 0
k2 = 0
k3 = 0
k4 = 0

for i in np.arange(a, b, step_size):
    k1 = step_size * (i - prev ** 2)
    k2 = step_size * ((i + step_size / 2) - ((prev + (k1 / 2)) ** 2))
    k3 = step_size * ((i + step_size / 2) - ((prev + (k2 / 2)) ** 2))
    k4 = step_size * ((i + step_size) - ((prev + k3) ** 2))

    prev = prev + ((k1 + 2 * k2 + 2 * k3 + k4) / 6)

print(f"Runge-Kutta: {prev}")
