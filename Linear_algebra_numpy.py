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


# Transpose
transpose_A = A.T
print("\nTranspose of A:")
print(transpose_A)


# Determinant
det_A = np.linalg.det(A)
print("\nDeterminant of A:")
print(det_A)


# Inverse
inverse_A = np.linalg.inv(A)
print("\nInverse of A:")
print(inverse_A)


# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of A:")
print(eigenvalues)

print("\nEigenvectors of A:")
print(eigenvectors)


# Rank
rank_A = np.linalg.matrix_rank(A)
print("\nRank of A:")
print(rank_A)


# Linear System
b = np.array([1, 2])

solution = np.linalg.solve(A, b)
print("\nSolution to Ax = b:")
print(solution)


# Trace (Sum of Diagonal)
trace_A = np.trace(A)
print("\nTrace of A:")
print(trace_A)


# Symmetric Check 
is_symmetric = np.array_equal(A, A.T)
print("\nIs A symmetric?")
print(is_symmetric)


# Identity Matrix
I = np.eye(2)
print("\nIdentity Matrix:")
print(I)


# Zero & Ones Matrix
print("\nZero Matrix:")
print(np.zeros((2,2)))

print("\nOnes Matrix:")
print(np.ones((2,2)))
