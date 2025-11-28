import numpy as np
import matplotlib.pyplot as plt
from math import factorial

a, b = -3, 3
m = 10

def f(x):
    return np.sinh(x)

def taylor_sinh(x, n):
    s = 0
    for k in range(n):
        s += x**(2*k+1) / factorial(2*k+1)
    return s

x = np.linspace(a, b, 400)

plt.figure(figsize=(10,5))
plt.plot(x, f(x), label="sinh(x)", linewidth=2)

for n in range(1, m+1):
    plt.plot(x, taylor_sinh(x, n), label=f"n={n}")

plt.title("Taylor sinh(x)")
plt.legend()
plt.grid()
plt.show()
