# Program to create a matrix and calculate the sum of its diagonal elements using NumPy.

import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("\nEnter matrix elements row by row:")


for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

matrix = np.array(matrix)

print("\nMatrix:")
print(matrix)


if rows != cols:
    print("\nDiagonal sum is only possible for square matrices.")
else:
    diagonal_sum = np.trace(matrix)

    print("\nDiagonal Elements:")
    print(np.diag(matrix))

    print("\nDiagonal Sum:")
    print(diagonal_sum)
