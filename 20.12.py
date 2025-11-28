import numpy as np

n = int(input("Введіть розмір матриці  "))

# ввод матрицы
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i}][{j}] = "))

print("\nМатриця A:\n", A)

upper = True
for i in range(1, n):
    for j in range(0, i):
        if A[i][j] != 0:
            upper = False

lower = True
for i in range(n-1):
    for j in range(i+1, n):
        if A[i][j] != 0:
            lower = False

if upper:
    print("\nМатриця верхня треугольна")
else:
    print("\nМатриця не верхня треугольна")

if lower:
    print("Матриця нижня треугольна")
else:
    print("Матриця не нижня треугольна")
