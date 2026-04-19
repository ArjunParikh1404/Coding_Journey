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
matrix_mult = A @ B
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
if not np.isclose(det_A, 0):
    inverse_A = np.linalg.inv(A)
    print("\nInverse of A:")
    print(inverse_A)
else:
    print("\nMatrix is singular, no inverse.")


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
is_symmetric = np.allclose(A, A.T)
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


# Matrix Norm
norm_A = np.linalg.norm(A)
print("\nNorm of A:")
print(norm_A)


# Condition Number
cond_A = np.linalg.cond(A)
print("\nCondition Number of A:")
print(cond_A)


# Check Orthogonality
is_orthogonal = np.allclose(A.T @ A, np.eye(A.shape[0]))
print("\nIs A orthogonal?")
print(is_orthogonal)


# LU / QR Decomposition
Q, R = np.linalg.qr(A)
print("\nQ matrix:")
print(Q)

print("\nR matrix:")
print(R)


# Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(A)
print("\nSingular Values:")
print(S)


# Check if matrix is invertible
is_invertible = np.linalg.matrix_rank(A) == A.shape[0]
print("\nIs A invertible?")
print(is_invertible)


# Frobenius Inner Product
inner_product = np.sum(A * B)
print("\nFrobenius Inner Product of A and B:")
print(inner_product)


# Matrix Power
power_A = np.linalg.matrix_power(A, 2)
print("\nA squared:")
print(power_A)


# Diagonal Extraction
diag_A = np.diag(A)
print("\nDiagonal elements of A:")
print(diag_A)


# Create Diagonal Matrix
diag_matrix = np.diag([1, 2])
print("\nDiagonal Matrix:")
print(diag_matrix)


# Projection of vector v onto vector u
v = np.array([1, 1])
u = np.array([1, 0])  # you can change u to any vector

projection = (np.dot(v, u) / np.dot(u, u)) * u

print("\nProjection of vector v onto u:")
print(projection)


# Verify Eigen Decomposition
reconstructed_A = eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)

print("\nReconstructed A from eigen decomposition:")
print(reconstructed_A)

# Check if reconstruction is accurate (tolerance check)
is_reconstruction_correct = np.allclose(A, reconstructed_A)

print("\nIs reconstruction accurate?")
print(is_reconstruction_correct)


# Rank-nullity insight
nullity = A.shape[1] - rank_A
print("\nNullity of A:")
print(nullity)


# Check Positive Definiteness 
try:
    np.linalg.cholesky(A)
    is_positive_definite = True
except np.linalg.LinAlgError:
    is_positive_definite = False

print("\nIs A positive definite?")
print(is_positive_definite)


# Pseudo-Inverse
pseudo_inv = np.linalg.pinv(A)
print("\nPseudo-inverse of A:")
print(pseudo_inv)
