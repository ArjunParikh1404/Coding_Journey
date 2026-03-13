# Matrix Operations using NumPy

import numpy as np

# Create matrices
A = np.array([[2, 4],
              [1, 3]])

B = np.array([[5, 7],
              [6, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


# Matrix Addition
addition = A + B
print("\nA + B:")
print(addition)


# Matrix Subtraction
subtraction = A - B
print("\nA - B:")
print(subtraction)


# Element-wise Multiplication
element_mult = A * B
print("\nElement-wise Multiplication (A * B):")
print(element_mult)


# Matrix Multiplication
matrix_mult = np.dot(A, B)
print("\nMatrix Multiplication (A @ B):")
print(matrix_mult)

print(rank_A)
