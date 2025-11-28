import numpy as np
import matplotlib.pyplot as plt


def a_n(n):
    S = sum(n / 3**k for k in range(n+1))
    return (S * (n - 3) * np.sqrt(n)) / (2*n*n + 5)

N = 200
ns = np.arange(1, N+1)
a_vals = np.array([a_n(int(n)) for n in ns])

plt.figure(figsize=(10,5))
plt.plot(ns, a_vals, marker='o', ms=3)
plt.title("posl (a)")
plt.xlabel("n")
plt.ylabel("a_n")
plt.grid(True)
plt.show()


#/ b

def b_n(n):
    num = (n-1)**4 - (n+2)**4
    den = (2*n+1)**3 + (n-1)**3
    return num / den

N = 200
ns = np.arange(1, N+1)
b_vals = np.array([b_n(int(n)) for n in ns])

print("10 poslednich zna4enii (b):")
print(b_vals[-10:])

b_limit = -4/3
eps = 0.05

k = None
for i in range(len(b_vals)):
    if np.all(np.abs(b_vals[i:] - b_limit) < eps):
        k = i + 1
        break

print(f"k для ε={eps} :", k)

plt.figure(figsize=(10,5))
plt.plot(ns, b_vals, marker='o', ms=3, label="b_n")
plt.axhline(b_limit, color='green', label="limit = -4/3")
plt.axhline(b_limit+eps, color='red', linestyle='--')
plt.axhline(b_limit-eps, color='red', linestyle='--')
plt.title("posl (b)")
plt.xlabel("n")
plt.ylabel("b_n")
plt.grid(True)
plt.legend()
plt.show()