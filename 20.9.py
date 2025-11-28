import numpy as np

n = int(input("порядок матрицi для n: "))

A = np.array([[float(input(f"A[{i}][{j}] = ")) for j in range(n)] for i in range(n)])

norm_A1 = np.max(np.sum(np.abs(A), axis=1))

print("\nМатриця A:")
print(A)
print("\nНорма ||A||_1 =", norm_A1)
